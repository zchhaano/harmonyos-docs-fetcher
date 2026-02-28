# 建立应用侧与前端页面数据通道(C/C++)

前端页面和应用侧之间可以使用Native方法实现两端通信（以下简称Native PostWebMessage），可解决ArkTS环境的冗余切换，同时允许发送消息、回调在非UI线程上运行，避免造成UI阻塞。当前只支持string和buffer数据类型。

## 适用的应用架构

应用使用ArkTS、C++语言混合开发，或本身应用架构较贴近于小程序架构，自带C++侧环境，推荐使用ArkWeb在Native侧提供的[ArkWeb_ControllerAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-controllerapi)、[ArkWeb_WebMessageAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageapi)、[ArkWeb_WebMessagePortAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageportapi)实现PostWebMessage功能。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165746.39480867368713238585936165841180:50001231000000:2800:823E9861FF7BC015D11CC0C4D2FE3ED293DF8716D3203BBA3FA0569FA48F2912.png)

上图展示了具有普遍适用性的小程序的通用架构。在这一架构中，逻辑层依赖于应用程序自带的JavaScript运行时，该运行时在一个已有的C++环境中运行。通过Native接口，逻辑层能够直接在C++环境中与视图层（其中ArkWeb充当渲染器）进行通信，无需回退至ArkTS环境使用ArkTS PostWebMessage接口。

左图是使用ArkTS PostWebMessage接口构建小程序的方案，如红框所示，应用需要先调用到ArkTS环境，再调用到C++环境。右图是使用Native PostWebMessage接口构建小程序的方案，不需要ArkTS环境和C++环境的切换，执行效率更高。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165746.75461223131034377206632870785334:50001231000000:2800:CE49AFBCFF980E3958097A8AA0917D51F557ABFFEDB3B34682676AB08390CBF7.png)

## 使用Native接口实现PostWebMessage通信

### 使用Native接口绑定ArkWeb

- ArkWeb组件声明在ArkTS侧，需要用户自定义一个标识webTag，并将webTag通过Node-API传至应用C++侧。后续ArkWeb Native接口使用时，均需webTag作为对应组件的唯一标识。
- ArkTS侧

 收起自动换行深色代码主题复制

```
import { webview } from '@kit.ArkWeb' ; // 自定义webTag，在WebviewController创建时作为入参传入，建立controller与webTag的映射关系 webTag : string = 'ArkWeb1' ; controller : webview. WebviewController = new webview. WebviewController ( this . webTag ); // ... // aboutToAppear中将webTag通过Node-API接口传入C++侧，作为C++侧ArkWeb组件的唯一标识 aboutToAppear ( ) { console . info ( "aboutToAppear" ) // 初始化web ndk testNapi. nativeWebInit ( this . webTag ); } // ...
```

### 使用Native接口获取API结构体

ArkWeb Native侧需先获取API结构体，才能调用结构体里的Native API。ArkWeb Native侧API通过函数[OH_ArkWeb_GetNativeAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-interface-h#oh_arkweb_getnativeapi)获取，根据入参type不同，可获取对应的函数指针结构体。其中本指导涉及[ArkWeb_ControllerAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-controllerapi)、[ArkWeb_WebMessageAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageapi)、[ArkWeb_WebMessagePortAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageportapi)。

 收起自动换行深色代码主题复制

```
static ArkWeb_ControllerAPI *controller = nullptr ; static ArkWeb_WebMessagePortAPI *webMessagePort = nullptr ; static ArkWeb_WebMessageAPI *webMessage = nullptr ; // ... controller = reinterpret_cast <ArkWeb_ControllerAPI *>( OH_ArkWeb_GetNativeAPI (ARKWEB_NATIVE_CONTROLLER)); webMessagePort = reinterpret_cast <ArkWeb_WebMessagePortAPI *>( OH_ArkWeb_GetNativeAPI (ARKWEB_NATIVE_WEB_MESSAGE_PORT)); webMessage = reinterpret_cast <ArkWeb_WebMessageAPI *>( OH_ArkWeb_GetNativeAPI (ARKWEB_NATIVE_WEB_MESSAGE));
```

### 完整示例

在调用API前建议通过[ARKWEB_MEMBER_MISSING](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h#宏定义)校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。[createWebMessagePorts](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-controllerapi#createwebmessageports)、[postWebMessage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-controllerapi#postwebmessage)、[close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageportapi#close)需运行在UI线程。

- 前端页面代码

 收起自动换行深色代码主题复制

```
<!-- entry/src/main/resources/rawfile/index.html --> <!-- index.html --> <!DOCTYPE html > < html lang = "en-gb" > < body > < h1 > etsRunJavaScriptExt测试demo </ h1 > < h1 id = "h1" > </ h1 > < h3 id = "msg" > Receive string: </ h3 > < h3 id = "msg2" > Receive arraybuffer: </ h3 > </ body > < script type = "text/javascript" > var h5Port; window . addEventListener ( 'message' , function ( event ) { if (event. data == 'init_web_messageport' ) { const port = event. ports [ 0 ]; // 1. 保存从应用侧发送过来的端口。 if (port) { console . info ( "hwd In html got message" ); h5Port = port; port. onmessage = function ( event ) { console . info ( "hwd In html got message" ); // 2. 接收应用侧发送过来的消息. var result = event. data ; var type_s = typeof (result) switch (type_s) { case "object" : if (result instanceof ArrayBuffer ) { type_s = "ArrayBuffer" ; var view = new Uint8Array (result); const decoder = new TextDecoder ( 'utf-8' ); result = decoder. decode (result); } else if (result instanceof Error ) { type_s = "Error" ; } else if (result instanceof Array ) { type_s = "Array" ; } break ; default : break ; } console . info ( "H5 recv type: " + type_s + "\nH5 recv result: " + result) document . getElementById ( "msg" ). innerHTML = "recv type: " + type_s; document . getElementById ( "msg2" ). innerHTML = "recv value: " + result; } h5Port. onmessageerror = ( event ) => { console . error ( `hwd In html Error receiving message: ${event} ` ); }; } } }) window . onerror = function ( message, url, line, column, error ) { console . info ( "JavaScript Error: " + message + " on line " + line + " in " + url); document . getElementById ( "h1" ). innerHTML = "执行函数失败" }; // 3. 使用h5Port向应用侧发送消息。 function postStringToApp ( ) { if (h5Port) { h5Port. postMessage ( "send string from H5" ); } else { console . error ( "In html h5port is null, please init first" ); } } function postBufferToApp ( ) { if (h5Port) { const str = "Hello, World!" ; const encoder = new TextEncoder (); const uint8Array = encoder. encode (str); h5Port. postMessage (uint8Array. buffer ); } else { console . error ( "In html h5port is null, please init first" ); } } function postJsonToApp ( ) { if (h5Port) { var e = { "json" : "json" }; h5Port. postMessage (e); } else { console . error ( "In html h5port is null, please init first" ); } } function postArrayStringToApp ( ) { if (h5Port) { h5Port. postMessage ([ "1" , "2" , "3" ]); } else { console . error ( "In html h5port is null, please init first" ); } } function postNumberToApp ( ) { if (h5Port) { h5Port. postMessage ( 123 ); } else { console . error ( "In html h5port is null, please init first" ); } } class MyClass { constructor ( ) { // 构造器 this . myProperty = 'Hello, World!' ; } myMethod ( ) { // 实例方法 console . info ( this . myProperty ); } static myStaticMethod ( ) { // 静态方法 console . info ( 'This is a static method.' ); } } function postObjectToApp ( ) { if (h5Port) { h5Port. postMessage ( new MyClass ()); } else { console . error ( "In html h5port is null, please init first" ); } } </ script > </ html >
```
- ArkTS侧代码

 收起自动换行深色代码主题复制

```
import testNapi from 'libentry.so' ; import { webview } from '@kit.ArkWeb' ; import { BusinessError } from '@kit.BasicServicesKit' ; @Entry @Component struct Index { @State webTag : string = 'postMessage' ; controller : webview. WebviewController = new webview. WebviewController ( this . webTag ); @State h5Log : string = 'Display received message send from HTML' ; aboutToAppear ( ) { webview. WebviewController . setWebDebuggingAccess ( true ); // 初始化web Native Development Kit testNapi. nativeWebInit ( this . webTag ); } aboutToDisAppear ( ) { console . error ( 'aboutToDisAppear' ); } build ( ) { Scroll () { Column ({ space : 10 }) { // 展示H5接收到的内容 Text ( 'H5_Side_Message_Display_From_App' ) TextArea ({ text : this . h5Log }) . id ( 'log_area' ) . width ( '100%' ) . height ( 100 ) . border ({ width : 1 }) Text ( 'App_Side_Button' ) Row () { Button ( 'createNoControllerTagPort' ) . id ( 'create_no_tag_btn' ) . onClick ( () => { try { testNapi. createWebMessagePorts ( 'noTag' ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) Button ( 'createPort' ) . id ( 'create_port_btn' ) . onClick ( () => { try { testNapi. createWebMessagePorts ( this . webTag ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) } Row ({ space : 10 }) { Button ( 'setHandler' ) . id ( 'set_handler_btn' ) . onClick ( () => { try { testNapi. setMessageEventHandler ( this . webTag ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) Button ( 'setHandlerThread' ) . id ( 'set_handler_thread_btn' ) . onClick ( () => { try { testNapi. setMessageEventHandlerThread ( this . webTag ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) } Row ({ space : 10 }) { Button ( 'SendString' ) . id ( 'send_string_btn' ) . onClick ( () => { try { this . h5Log = '' testNapi. postMessage ( this . webTag ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) Button ( 'SendStringThread' ) . id ( 'send_string_thread_btn' ) . onClick ( () => { try { this . h5Log = '' testNapi. postMessageThread ( this . webTag ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) } Row ({ space : 10 }) { Button ( 'SendBuffer' ) . id ( 'send_buffer_btn' ) . onClick ( () => { try { this . h5Log = '' testNapi. postBufferMessage ( this . webTag ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) Button ( 'SendNone' ) . id ( 'send_none_btn' ) . onClick ( () => { try { this . h5Log = '' testNapi. postNoneMessage ( this . webTag ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) } Row ({ space : 10 }) { Button ( 'closePort' ) . id ( 'close_port_btn' ) . onClick ( () => { try { testNapi. closeMessagePort ( this . webTag ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) Button ( 'destroyNullPort' ) . id ( 'destroy_null_btn' ) . onClick ( () => { try { testNapi. destroyNullMessagePort ( this . webTag ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) Button ( 'destroyPort' ) . id ( 'destroy_port_btn' ) . onClick ( () => { try { testNapi. destroyMessagePort ( this . webTag ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) } . width ( '100%' ) . padding ( 10 ) . border ({ width : 1 }) Column ({ space : 10 }) { Text ( 'H5_Side_Send_Button' ) Row ({ space : 10 }) { Button ( 'H5String' ) . id ( 'h5_send_string_btn' ) . onClick ( () => { try { this . controller . runJavaScript ( 'for(var i = 0; i < 2000; i++) postStringToApp()' ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) Button ( 'H5Buffer' ) . id ( 'h5_send_buffer_btn' ) . onClick ( () => { try { this . controller . runJavaScript ( 'postBufferToApp()' ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) Button ( 'H5Number' ) . id ( 'h5_send_number_btn' ) . onClick ( () => { try { this . controller . runJavaScript ( 'postNumberToApp()' ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) } Row ({ space : 10 }) { Button ( 'H5Json' ) . id ( 'h5_send_json_btn' ) . onClick ( () => { try { this . controller . runJavaScript ( 'postJsonToApp()' ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) Button ( 'H5Array' ) . id ( 'h5_send_array_btn' ) . onClick ( () => { try { this . controller . runJavaScript ( 'postArrayStringToApp()' ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) Button ( 'H5Object' ) . id ( 'h5_send_object_btn' ) . onClick ( () => { try { this . controller . runJavaScript ( 'postObjectToApp()' ); } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) } } . width ( '100%' ) . margin ( 10 ) . padding ( 10 ) . border ({ width : 1 }) Web ({ src : $rawfile( 'index.html' ), controller : this . controller }) . onConsole ( ( event ) => { if (event) { let msg = event. message . getMessage (); if (msg. startsWith ( 'H5' )) { this . h5Log = event. message . getMessage () + '\n' + this . h5Log ; } } return false ; }) } }. height ( '100%' ) . scrollable ( ScrollDirection . Vertical ) . scrollBar ( BarState . Off ) . edgeEffect ( EdgeEffect . Spring ) } }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkWeb/UseFrontendJSApp/entry5/src/main/ets/pages/Index.ets#L16-L274)
- Node-API侧暴露ArkTS接口

 收起自动换行深色代码主题复制

```
// entry5/src/main/cpp/types/libentry5/index.d.ts export const nativeWebInit : ( webName: string ) => void ; export const createWebMessagePorts : ( webName: string ) => void ; export const postMessage : ( webName: string ) => void ; export const postNoneMessage : ( webName: string ) => void ; export const setMessageEventHandler : ( webName: string ) => void ; export const closeMessagePort : ( webName: string ) => void ; export const destroyMessagePort : ( webName: string ) => void ; export const postBufferMessage : ( webName: string ) => void ; export const destroyNullMessagePort : ( webName: string ) => void ; export const setMessageEventHandlerThread : ( webName: string ) => void ; export const postMessageThread : ( webName: string ) => void ;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkWeb/UseFrontendJSApp/entry5/src/main/cpp/types/libentry5/Index.d.ts#L16-L29)
- Node-API侧编译配置

 收起自动换行深色代码主题复制

```
# entry/src/main/cpp/CMakeLists.txt # the minimum version of CMake. cmake_minimum_required(VERSION 3.4.1) project(NDKPostMessage) set (NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR} ) if (DEFINED PACKAGE_FIND_FILE) include( ${PACKAGE_FIND_FILE} ) endif() include_directories( ${NATIVERENDER_ROOT_PATH} ${NATIVERENDER_ROOT_PATH} /include) add_library(entry SHARED hello.cpp) find_library( # Sets the name of the path variable. hilog-lib # Specifies the name of the NDK library that # you want CMake to locate. hilog_ndk.z ) target_link_libraries(entry PUBLIC libace_napi.z.so ${hilog-lib} libohweb.so)
```
- Node-API层代码

 收起自动换行深色代码主题复制

```
```

[hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkWeb/UseFrontendJSApp/entry5/src/main/cpp/hello.cpp#L16-L479)
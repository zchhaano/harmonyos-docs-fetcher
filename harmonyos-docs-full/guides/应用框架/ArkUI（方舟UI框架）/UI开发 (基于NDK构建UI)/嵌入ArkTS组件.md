# 嵌入ArkTS组件

ArkUI在Native侧提供的能力作为ArkTS的子集，部分能力不会在Native侧提供，如声明式UI语法，自定义struct组件，UI高级组件。

针对需要使用ArkTS侧独立能力的场景，ArkUI开发框架提供了Native侧嵌入ArkTS组件的能力，该能力依赖[ComponentContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent)机制，通过ComponentContent完成对ArkTS组件的封装，然后将封装对象传递到Native侧，通过Native侧的[OH_ArkUI_GetNodeHandleFromNapiValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-napi-h#oh_arkui_getnodehandlefromnapivalue)接口转化为ArkUI_NodeHandle对象用于Native侧组件挂载使用。

 说明 

- 通过OH_ArkUI_GetNodeHandleFromNapiValue接口获得的ArkUI_NodeHandle对象只能作为子组件参数使用，如[addChild](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addchild)接口的第二个参数，将该对象使用在其他场景下，如[setAttribute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#setattribute)设置属性将不生效并返回错误码。
- 针对Native侧修改ArkTS组件的场景，需要在Native侧通过Node-API方式构建ArkTS侧的更新数据，再通过ComponentContent的[update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent#update)接口更新。
- [构建自定义组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-build-custom-components)时，相关函数如measureNode等无法对ArkTS模块内部的组件进行调用。

以下示例代码在[接入ArkTS页面](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-access-the-arkts-page)章节基础上引入ArkTS的Refresh组件。

**图1** Refresh组件挂载文本列表

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165751.68677496789691767375092394833395:50001231000000:2800:88AD5C90C7458E393FD5FF568394CC4ABC97C366FE45EF784F0E36ACC9343D50.gif)

1. 注册ArkTS组件创建函数给Native侧，以便Native侧调用，创建函数使用ComponentContent能力进行封装。

 收起自动换行深色代码主题复制

```
// 使用ComponentContent能力创建ArkTS组件 import { NodeContent , UIContext , RefreshModifier , ComponentContent } from '@kit.ArkUI' ; import { hilog } from '@kit.PerformanceAnalysisKit' ; const DOMAIN = 0x0000 ; // 定义Native侧和ArkTS进行交互的数据对象。 interface NativeRefreshAttribute { isRefreshing : boolean ; width?: number ; height?: number ; backgroundColor?: number ; refreshOffset?: number ; pullToRefresh?: boolean ; onRefreshing?: () => void ; onOffsetChange?: ( offset: number ) => void ; } // 定义@Builder函数的入参格式。 interface RefreshAttribute { isRefreshing : boolean ; // 属性设置通过Modifier优化性能 modifier?: RefreshModifier ; slot?: NodeContent ; onRefreshing?: () => void ; onOffsetChange?: ( offset: number ) => void ; } // ComponentContent封装ArkTS组件依赖全局@Builder函数，涉及复杂自定义组件场景，可以在@Builder函数中嵌套@Component自定义组件。 // @Builder函数提供入参方式，方便后续通过ComponentContent的update接口进行参数更新。 @Builder function mixedRefresh ( attribute: RefreshAttribute ) { Refresh ({ refreshing : attribute. isRefreshing }) { // Refresh作为容器组件，需要使用ContentSlot机制预留子组件占位 ContentSlot (attribute. slot ); }. attributeModifier (attribute. modifier ) . onRefreshing ( () => { hilog. info ( DOMAIN , 'testTag' , 'on onRefreshing' ); if (attribute. onRefreshing ) { hilog. info ( DOMAIN , 'testTag' , 'on native onRefreshing' ); attribute. onRefreshing (); } }) . onOffsetChange ( ( value: number ) => { hilog. info ( DOMAIN , 'testTag' , 'on offset change: ' + value); if (attribute. onOffsetChange ) { hilog. info ( DOMAIN , 'testTag' , 'on native onOffsetChange' ); attribute. onOffsetChange (value); } }); } // 定义创建函数的返回值，用于ArkTS侧和Native侧的交互。 interface MixedModuleResult { // 定义针对Refresh构建函数的封装对象，用于Native侧转化为ArkUI_NodeHandle对象。 content?: ComponentContent < RefreshAttribute >; // Refresh作为容器组件，需要使用ContentSlot机制挂载Native侧的子组件。 childSlot?: NodeContent ; } // 提供创建ArkTS组件的入口函数。 export function createMixedRefresh ( value: NativeRefreshAttribute ): MixedModuleResult { hilog. info ( DOMAIN , 'testTag' , 'createMixedRefresh' ); // 通过AppStorage对象在Ability启动的时候保持UI上下文对象。 let uiContent = AppStorage . get < UIContext >( 'context' ); let modifier = new RefreshModifier (); if (value. width ) { modifier. width (value. width ); } if (value. height ) { modifier. height (value. height ); } if (value. backgroundColor ) { modifier. backgroundColor (value. backgroundColor ); } if (value. pullToRefresh ) { modifier. pullToRefresh (value. pullToRefresh ); } if (value. refreshOffset ) { modifier. refreshOffset (value. refreshOffset ); } // 创建NodeContent插槽对象用于Refresh子组件挂载。 let nodeSlot = new NodeContent (); // 通过ComponentContent创建Refresh组件并将它封装起来。 let content = new ComponentContent < RefreshAttribute >(uiContent!, wrapBuilder<[ RefreshAttribute ]>(mixedRefresh), { isRefreshing : value. isRefreshing , modifier : modifier, slot : nodeSlot, onRefreshing : value. onRefreshing , onOffsetChange : value. onOffsetChange }); // 将Refresh组件的封装对象及其子组件插槽对象传递给Native侧。 return { content : content, childSlot : nodeSlot }; } // 定义Refresh组件的更新函数，用于Native侧更新。 // 在更新场景下，需要将Refresh组件的封装对象及其子组件插槽对象返回，防止组件重新创建。 export function updateMixedRefresh ( refresh: ComponentContent<RefreshAttribute>, childSlot: NodeContent, value: NativeRefreshAttribute ): void { let modifier = new RefreshModifier (); if (value. width ) { modifier. width (value. width ); } if (value. height ) { modifier. height (value. height ); } if (value. backgroundColor ) { modifier. backgroundColor (value. backgroundColor ); } if (value. pullToRefresh ) { modifier. pullToRefresh (value. pullToRefresh ); } if (value. refreshOffset ) { modifier. refreshOffset (value. refreshOffset ); } // 调用ComponentContent的update接口进行更新。 refresh. update ({ isRefreshing : value. isRefreshing , modifier : modifier, slot : childSlot, onRefreshing : value. onRefreshing , onOffsetChange : value. onOffsetChange }); }
```

[MixedModule.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/ets/pages/MixedModule.ets#L15-L144)
2. 将创建和更新函数注册给Native侧。

 收起自动换行深色代码主题复制

```
//  Index.ets import nativeNode from 'libentry.so' ; import { NodeContent } from '@kit.ArkUI' ; import { createMixedRefresh, updateMixedRefresh } from './MixedModule' ; @Entry @Component struct Index { private rootSlot = new NodeContent (); @State @Watch ( 'changeNativeFlag' ) showNative : boolean = false ; aboutToAppear (): void { // 设置uiContext; AppStorage . setOrCreate < UIContext >( 'context' , this . getUIContext ()); // 设置混合模式下的builder函数。 nativeNode. registerCreateMixedRefreshNode (createMixedRefresh); nativeNode. registerUpdateMixedRefreshNode (updateMixedRefresh); } changeNativeFlag (): void { if ( this . showNative ) { // 创建NativeModule组件挂载 nativeNode. createNativeRoot ( this . rootSlot ); } else { // 销毁NativeModule组件 nativeNode. destroyNativeRoot (); } } build ( ) { Column () { Button ( this . showNative ? 'HideNativeUI' : 'ShowNativeUI' ). onClick ( () => { this . showNative = ! this . showNative ; }); Row () { // ArkTS插入Native组件。 ContentSlot ( this . rootSlot ); }. layoutWeight ( 1 ) . id ( 'row_' ); } . width ( '100%' ) . height ( '100%' ); } }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/ets/pages/Index.ets#L15-L61) 收起自动换行深色代码主题复制

```
// native_init.cpp # include "napi/native_api.h" # include "ArkUIMixedRefresh.h" # include "NativeEntry.h" EXTERN_C_START static napi_value Init (napi_env env, napi_value exports) { napi_property_descriptor desc[] = { { "createNativeRoot" , nullptr , NativeModule::CreateNativeRoot, nullptr , nullptr , nullptr , napi_default, nullptr }, { "registerCreateMixedRefreshNode" , nullptr , NativeModule::ArkUIMixedRefresh::RegisterCreateRefresh, nullptr , nullptr , nullptr , napi_default, nullptr }, { "registerUpdateMixedRefreshNode" , nullptr , NativeModule::ArkUIMixedRefresh::RegisterUpdateRefresh, nullptr , nullptr , nullptr , napi_default, nullptr }, { "destroyNativeRoot" , nullptr , NativeModule::DestroyNativeRoot, nullptr , nullptr , nullptr , napi_default, nullptr }}; napi_define_properties (env, exports, sizeof (desc) / sizeof (desc[ 0 ]), desc); return exports; } EXTERN_C_END static napi_module demoModule = { .nm_version = 1 , .nm_flags = 0 , .nm_filename = nullptr , .nm_register_func = Init, .nm_modname = "entry" , .nm_priv = (( void *) 0 ), .reserved = { 0 }, }; extern "C" __attribute__((constructor)) void RegisterEntryModule ( void ) { napi_module_register (&demoModule); }
```

[NapiInit.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/NapiInit.cpp#L15-L48)
3. Native侧通过Node-API保存创建和更新函数，用于后续调用。

 收起自动换行深色代码主题复制

```
// 混合模式交互类。 # ifndef MYAPPLICATION_ARKUIMIXEDREFRESHTEMPLATE_H # define MYAPPLICATION_ARKUIMIXEDREFRESHTEMPLATE_H # include "ArkUIMixedNode.h" # include <optional> # include <arkui/native_node_napi.h> # include <js_native_api_types.h> namespace NativeModule { class ArkUIMixedRefresh : public ArkUIMixedNode { public: static napi_value RegisterCreateAndUpdateRefresh (napi_env env, napi_callback_info info) ; }; } // namespace NativeModule # endif // MYAPPLICATION_ARKUIMIXEDREFRESHTEMPLATE_H
```

[ArkUIMixedRefreshTemplate.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/ArkUIMixedRefreshTemplate.h#L15-L39) 

相关实现类说明：

 收起自动换行深色代码主题复制

```
// 混合模式交互类。 # include "ArkUIMixedRefreshTemplate.h" namespace NativeModule { namespace { napi_env g_env; napi_ref g_createRefresh; napi_ref g_updateRefresh; } // namespace napi_value ArkUIMixedRefresh::RegisterCreateAndUpdateRefresh (napi_env env, napi_callback_info info) { size_t argc = 1 ; napi_value args[ 1 ] = { nullptr }; napi_get_cb_info (env, info, &argc, args, nullptr , nullptr ); g_env = env; napi_ref refer; // 创建引用之后保存，防止释放。 napi_create_reference (env, args[ 0 ], 1 , &refer); g_createRefresh = refer; return nullptr ; } } // namespace NativeModule
```

[ArkUIMixedRefreshTemplate.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/ArkUIMixedRefreshTemplate.cpp#L15-L45) 

相关的CMakeLists的配置：

 收起自动换行深色代码主题复制

```
# CMakeLists.txt # the minimum version of CMake. cmake_minimum_required (VERSION 3.4 .1 ) project (testndk) # optional依赖C++17 set (CMAKE_CXX_STANDARD 17 ) set (NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR}) include_directories (${NATIVERENDER_ROOT_PATH} ${NATIVERENDER_ROOT_PATH}/include) add_library (entry SHARED NativeEntry.cpp ArkUIMixedRefresh.cpp napi_init.cpp) # target_link_libraries (entry PUBLIC libace_napi.z.so, libace_ndk.z.so, libhilog_ndk.z.so) find_library ( # Sets the name of the path variable. hilog-lib # Specifies the name of the NDK library that # you want CMake to locate. hilog_ndk.z ) find_library ( # Sets the name of the path variable. libace-lib # Specifies the name of the NDK library that # you want CMake to locate. ace_ndk.z ) find_library ( # Sets the name of the path variable. libnapi-lib # Specifies the name of the NDK library that # you want CMake to locate. ace_napi.z ) find_library ( # Sets the name of the path variable. libuv-lib uv ) target_link_libraries (entry PUBLIC ${hilog-lib} ${libace-lib} ${libnapi-lib} ${libuv-lib} )
```
4. 抽象混合模式下组件的基类，用于通用逻辑管理。

 收起自动换行深色代码主题复制

```
// ArkUIMixedNode.h // 混合模式基类。 # ifndef MYAPPLICATION_ARKUIMIXEDNODE_H # define MYAPPLICATION_ARKUIMIXEDNODE_H # include <js_native_api.h> # include <js_native_api_types.h> # include "ArkUIBaseNode.h" # include "NativeModule.h" namespace NativeModule { // Wrap ArkTS Node class ArkUIMixedNode : public ArkUIBaseNode { public: ArkUIMixedNode(ArkUI_NodeHandle handle, napi_env env, napi_ref componentContent) : ArkUIBaseNode(handle), env_(env), componentContent_(componentContent) {} // 在基类析构的时候需要把混合模式在ArkTS侧的对象释放掉。 ~ArkUIMixedNode() override { napi_delete_reference(env_, componentContent_); } protected: napi_env env_; napi_ref componentContent_; }; } // namespace NativeModule # endif // MYAPPLICATION_ARKUIMIXEDNODE_H
```

[ArkUIMixedNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/ArkUIMixedNode.h#L15-L47)
5. 实现Refresh组件的混合模式封装对象。

 收起自动换行深色代码主题复制

```
// ArkUIMixedRefresh.h // Refresh混合模式在Native侧的封装对象。 # ifndef MYAPPLICATION_ARKUIMIXEDREFRESH_H # define MYAPPLICATION_ARKUIMIXEDREFRESH_H # include "ArkUIMixedNode.h" # include "ArkUIBaseNode.h" # include <optional> # include <arkui/native_node_napi.h> # include <js_native_api_types.h> namespace NativeModule { // 定义Native侧和ArkTS侧的交互数据结构。 struct NativeRefreshAttribute { std ::optional< bool > isRefreshing; std ::optional< float > width; std ::optional< float > height; std ::optional< uint32_t > backgroundColor; std ::optional< float > refreshOffset; std ::optional< bool > pullToRefresh; std ::function< void ()> onRefreshing; std ::function< void ( float )> onOffsetChange; }; class ArkUIMixedRefresh : public ArkUIMixedNode { public: // 调用ArkTS的方法创建Refresh组件。 static const std :: shared_ptr <ArkUIMixedRefresh> Create ( const NativeRefreshAttribute &attribute) ; ArkUIMixedRefresh(ArkUI_NodeHandle handle, ArkUI_NodeContentHandle contentHandle, napi_env env, napi_ref componentContent, napi_ref nodeContent) : ArkUIMixedNode(handle, env, componentContent), contentHandle_(contentHandle), nodeContent_(nodeContent) {} ArkUIMixedRefresh() : ArkUIMixedNode(nullptr, nullptr, nullptr) {} ~ArkUIMixedRefresh() override { napi_delete_reference(env_, nodeContent_); } // 释放子节点占位组件插槽对象。 void SetWidth ( float width) { attribute_.width = width; } void SetHeight ( float height) { attribute_.height = height; } void SetBackgroundColor ( uint32_t color) { attribute_.backgroundColor = color; } void SetRefreshState ( bool isRefreshing) { attribute_.isRefreshing = isRefreshing; } void SetPullToRefresh ( bool pullToRefresh) { attribute_.pullToRefresh = pullToRefresh; } void SetRefreshOffset ( float offset) { attribute_.refreshOffset = offset; } void SetRefreshCallback ( const std ::function< void ()> &callback) { attribute_.onRefreshing = callback; } void SetOnOffsetChange ( const std ::function< void ( float )> &callback) { attribute_.onOffsetChange = callback; } // 避免频繁跨语言，在Native侧缓存属性事件，批量通知。 void FlushMixedModeCmd () ; static napi_value RegisterCreateRefresh (napi_env env, napi_callback_info info) ; static napi_value RegisterUpdateRefresh (napi_env env, napi_callback_info info) ; protected: void OnAddChild ( const std :: shared_ptr <ArkUIBaseNode> &child) override { // 使用NodeContent挂载组件（可以使用ArkTS在Native侧通过ComponentContent的转化对象，也可以是纯Native组件）到ArkTS组件下面。 OH_ArkUI_NodeContent_AddNode(contentHandle_, child->GetHandle()); } void OnRemoveChild ( const std :: shared_ptr <ArkUIBaseNode> &child) override { // 使用NodeContent卸载组件。 OH_ArkUI_NodeContent_RemoveNode(contentHandle_, child->GetHandle()); } void OnInsertChild ( const std :: shared_ptr <ArkUIBaseNode> &child, int32_t index) override { // 使用NodeContent插入组件。 OH_ArkUI_NodeContent_InsertNode(contentHandle_, child->GetHandle(), index); } private: // 使用napi接口创建ArkTS侧的数据结构。 static napi_value CreateRefreshAttribute ( const NativeRefreshAttribute &attribute, void *userData) ; static void Attribute2Descriptor ( const NativeRefreshAttribute &attribute, napi_property_descriptor *desc) ; ArkUI_NodeContentHandle contentHandle_; napi_ref nodeContent_; NativeRefreshAttribute attribute_; }; } // namespace NativeModule # endif // MYAPPLICATION_ARKUIMIXEDREFRESH_H
```

[ArkUIMixedRefresh.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/ArkUIMixedRefresh.h#L15-L112) 

相关实现类说明：

 收起自动换行深色代码主题复制

```
```

[ArkUIMixedRefresh.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/ArkUIMixedRefresh.cpp#L15-L223)
6. 定时器模块相关简单实现。

 收起自动换行深色代码主题复制

```
// UITimer.h // 定时器模块。 # ifndef MYAPPLICATION_UITIMER_H # define MYAPPLICATION_UITIMER_H # include <hilog/log.h> # include <js_native_api.h> # include <js_native_api_types.h> # include <node_api.h> # include <node_api_types.h> # include <string> # include <thread> # include <uv.h> namespace NativeModule { struct UIData { void *userData = nullptr; int32_t count = 0 ; int32_t totalCount = 0 ; void (*func)( void *userData, int32_t count) = nullptr; }; napi_threadsafe_function threadSafeFunction = nullptr; void CreateNativeTimer (napi_env env, void *userData, int32_t totalCount, void (*func)( void *userData, int32_t count)) { napi_value name; std :: string str = "UICallback" ; napi_create_string_utf8(env, str.c_str(), str.size(), &name); // UI主线程回调函数。 napi_create_threadsafe_function( env, nullptr, nullptr, name, 0 , 1 , nullptr, nullptr, nullptr, [](napi_env env, napi_value value, void *context, void *data) { auto userdata = reinterpret_cast<UIData *>(data); userdata->func(userdata->userData, userdata->count); delete userdata; }, &threadSafeFunction); // 启动定时器，模拟数据变化。 std ::thread timerThread ([data = userData, totalCount, func]() { uv_loop_t *loop = uv_loop_new(); uv_timer_t *timer = new uv_timer_t (); uv_timer_init(loop, timer); timer->data = new UIData{data, 0 , totalCount, func}; uint64_t timeout = 4000 ; uint64_t repeat = 4000 ; uv_timer_start( timer, []( uv_timer_t *handle) { OH_LOG_INFO(LOG_APP, "on timeout" ); napi_acquire_threadsafe_function(threadSafeFunction); auto *customData = reinterpret_cast<UIData *>(handle->data); // 创建回调数据。 auto *callbackData = new UIData{customData->userData, customData->count, customData->totalCount, customData->func}; napi_call_threadsafe_function(threadSafeFunction, callbackData, napi_tsfn_blocking); customData->count++; if (customData->count > customData->totalCount) { uv_timer_stop(handle); delete handle; delete customData; } }, timeout, repeat); uv_run(loop, UV_RUN_DEFAULT); uv_loop_delete(loop); }) ; timerThread.detach(); } } // namespace NativeModule # endif // MYAPPLICATION_UITIMER_H
```

[UITimer.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/UITimer.h#L15-L90)
7. 使用[接入ArkTS页面](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-access-the-arkts-page)章节的页面结构，将Refresh组件作为文本列表的父组件。

 收起自动换行深色代码主题复制

```
// MixedRefreshExample.h // 混合模式示例代码。 # ifndef MYAPPLICATION_MIXEDREFRESHEXAMPLE_H # define MYAPPLICATION_MIXEDREFRESHEXAMPLE_H # include "ArkUIBaseNode.h" # include "ArkUIMixedRefresh.h" # include "NormalTextListExample.h" # include "UITimer.h" # include <js_native_api_types.h> namespace NativeModule { std :: shared_ptr <ArkUIBaseNode> CreateMixedRefreshList (napi_env env) { auto list = CreateTextListExample(); // 混合模式创建Refresh组件并挂载List组件。 NativeRefreshAttribute nativeRefreshAttribute{ .backgroundColor = 0xFF89CFF0 , .refreshOffset = 64 , .pullToRefresh = true }; auto refresh = ArkUIMixedRefresh::Create(nativeRefreshAttribute); refresh->AddChild( list ); // 设置混合模式下的事件。 refresh->SetOnOffsetChange( []( float offset) { OH_LOG_INFO(LOG_APP, "on refresh offset changed: %{public}f" , offset); }); refresh->SetRefreshCallback([refreshPtr = refresh.get(), env]() { OH_LOG_INFO(LOG_APP, "on refreshing" ); // 启动定时器，模拟数据获取。 CreateNativeTimer(env, refreshPtr, 1 , []( void *userData, int32_t count) { // 数据获取后关闭刷新。 auto refresh = reinterpret_cast<ArkUIMixedRefresh *>(userData); refresh->SetRefreshState( false ); refresh->FlushMixedModeCmd(); }); }); // 更新事件到ArkTS侧。 refresh->FlushMixedModeCmd(); return refresh; } } // namespace NativeModule # endif // MYAPPLICATION_MIXEDREFRESHEXAMPLE_H
```

[MixedRefreshExample.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/MixedRefreshExample.h#L15-L62) 

替换入口组件创建为下拉刷新文本列表。

 收起自动换行深色代码主题复制

```
// NativeEntry.cpp # include "NativeEntry.h" # include "ArkUIMixedRefresh.h" # include "MixedRefreshExample.h" # include "NormalTextListExample.h" # include <arkui/native_node_napi.h> # include <arkui/native_type.h> # include <js_native_api.h> # include <uv.h> namespace NativeModule { napi_value CreateNativeRoot (napi_env env, napi_callback_info info) { size_t argc = 1 ; napi_value args[ 1 ] = { nullptr }; napi_get_cb_info (env, info, &argc, args, nullptr , nullptr ); // 获取NodeContent ArkUI_NodeContentHandle contentHandle; OH_ArkUI_GetNodeContentFromNapiValue (env, args[ 0 ], &contentHandle); NativeEntry:: GetInstance ()-> SetContentHandle (contentHandle); // 创建Refresh文本列表 auto refresh = CreateMixedRefreshList (env); // 保持Native侧对象到管理类中，维护生命周期。 NativeEntry:: GetInstance ()-> SetRootNode (refresh); return nullptr ; } napi_value DestroyNativeRoot (napi_env env, napi_callback_info info) { // 从管理类中释放Native侧对象。 NativeEntry:: GetInstance ()-> DisposeRootNode (); return nullptr ; } } // namespace NativeModule
```

[NativeEntry.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/NativeEntry.cpp#L15-L59)
8. 在Native侧提供Node-API的桥接方法，实现ArkTS侧的NativeNode模块接口。

 收起自动换行深色代码主题复制

```
export const createNativeRoot : ( content: Object ) => void ; export const destroyNativeRoot : () => void ; export const registerCreateMixedRefreshNode : ( content: Object ) => void ; export const registerUpdateMixedRefreshNode : ( content: Object ) => void ;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/NativeType/NdkEmbedArktsComponents/entry/src/main/cpp/types/libentry/Index.d.ts#L15-L21)
## 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[HiAppEvent C API文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h)。

**订阅接口功能介绍**：

  展开

| 接口名 | 描述 |
| --- | --- |
| int OH_HiAppEvent_AddWatcher(HiAppEvent_Watcher *watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH_HiAppEvent_RemoveWatcher(HiAppEvent_Watcher *watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

以实现对写数组越界场景生成的地址越界事件订阅为例，说明开发步骤。

### 步骤一：新建工程

1. 参考[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)README中**Using JsonCpp in your project**介绍的使用方法获取到jsoncpp.cpp、json.h和json-forwards.h三个文件。
2. 新建Native C++工程，并将上述文件导入到新建工程内，目录结构如下：

 收起自动换行深色代码主题复制

```
entry: src: main: cpp: - json: - json.h - json-forwards.h - types: libentry: - index.d.ts - CMakeLists.txt - napi_init.cpp - jsoncpp.cpp ets: - entryability: - EntryAbility.ets - pages: - Index.ets
```
3. 编辑"CMakeLists.txt"文件，添加源文件及动态库：

 收起自动换行深色代码主题复制

```
# 新增jsoncpp .cpp (解析订阅事件中的json字符串)源文件 add_library (entry SHARED napi_init.cpp jsoncpp.cpp) # 新增动态库依赖libhiappevent_ndk .z .so 和libhilog_ndk .z .so (日志输出) target_link_libraries (entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
```
4. 编辑"napi_init.cpp"文件，导入依赖的文件，并定义LOG_TAG：

 收起自动换行深色代码主题复制

```
# include "napi/native_api.h" # include "json/json.h" # include "hilog/log.h" # include "hiappevent/hiappevent.h" # undef LOG_TAG # define LOG_TAG "testTag"
```

### 步骤二：订阅地址越界事件

1. 订阅系统事件：

  - onReceive类型观察者：

编辑"napi_init.cpp"文件，定义onReceive类型观察者相关方法：

 收起自动换行深色代码主题复制

```
```
  - onTrigger类型观察者：

编辑"napi_init.cpp"文件，定义OnTrigger类型观察者相关方法：

 收起自动换行深色代码主题复制

```
```

### 步骤三：构造地址越界错误

1. 编辑"napi_init.cpp"文件，定义Test方法, 方法中对一个整数数组进行越界访问：

 收起自动换行深色代码主题复制

```
static napi_value Test (napi_env env, napi_callback_info info) { int a[ 10 ]; a[ 10 ] = 1 ; return {}; }
```
2. 将RegisterWatcher和Test注册为ArkTS接口，编辑"napi_init.cpp"文件，将RegisterWatcher和Test注册为ArkTS接口：

 收起自动换行深色代码主题复制

```
static napi_value Init (napi_env env, napi_value exports) { napi_property_descriptor desc[] = { { "registerWatcher" , nullptr , RegisterWatcher, nullptr , nullptr , nullptr , napi_default, nullptr }, { "test" , nullptr , Test, nullptr , nullptr , nullptr , napi_default, nullptr } }; napi_define_properties (env, exports, sizeof (desc) / sizeof (desc[ 0 ]), desc); return exports; }
```

编辑"index.d.ts"文件，定义ArkTS接口：

 收起自动换行深色代码主题复制

```
export const registerWatcher : () => void ; export const test : () => void ;
```
3. 编辑"EntryAbility.ets"文件，在onCreate()函数中新增接口调用：

 收起自动换行深色代码主题复制

```
// 导入依赖模块 import testNapi from 'libentry.so' ; // 在onCreate()函数中新增接口调用 // 启动时，注册系统事件观察者 testNapi. registerWatcher ();
```
4. 编辑“entry > src > main > ets > pages > Index.ets”文件，新增按钮触发地址越界事件：

 收起自动换行深色代码主题复制

```
import testNapi from 'libentry.so' ; @Entry @Component struct Index { build ( ) { Row () { Column () { Button ( "address-sanitizer" ). onClick ( () => { testNapi. test (); }) } . width ( '100%' ) } . height ( '100%' ) } }
```
5. 点击DevEco Studio界面中的“entry”，点击“Edit Configurations”，点击“Diagnostics”，勾选“Address Sanitizer”，保存设置。点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击按钮“address-sanitizer”，触发一次地址越界事件。应用崩溃后重新进入应用，可以在Log窗口看到对系统事件数据的处理日志：

 收起自动换行深色代码主题复制

```
HiAppEvent eventInfo.domain=OS HiAppEvent eventInfo.name=ADDRESS_SANITIZER HiAppEvent eventInfo.eventType=1 HiAppEvent eventInfo.params.time=1713148093326 HiAppEvent eventInfo.params.bundle_version=1.0.0 HiAppEvent eventInfo.params.bundle_name=com.example.myapplication HiAppEvent eventInfo.params.pid=3378 HiAppEvent eventInfo.params.uid=20020140 HiAppEvent eventInfo.params.type="stack-buffer-overflow" HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/ADDRESS_SANITIZER_1713148093326_3378.log"] HiAppEvent eventInfo.params.log_over_limit=false
```

### 步骤四：销毁事件观察者

1. 移除事件观察者：

 收起自动换行深色代码主题复制

```
static napi_value RemoveWatcher (napi_env env, napi_callback_info info) { // 使观察者停止监听事件 OH_HiAppEvent_RemoveWatcher (systemEventWatcher); return {}; }
```
2. 销毁事件观察者：

 收起自动换行深色代码主题复制

```
static napi_value DestroyWatcher (napi_env env, napi_callback_info info) { // 销毁创建的观察者，并置systemEventWatcher为nullptr。 OH_HiAppEvent_DestroyWatcher (systemEventWatcher); systemEventWatcher = nullptr ; return {}; }
```
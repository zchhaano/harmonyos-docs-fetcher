## 简介

本文介绍如何使用HiAppEvent提供的C/C++接口订阅应用崩溃事件。详细使用说明请参考[HiAppEvent C API文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h)。

 说明 

使用C/C++接口订阅JsError和NativeCrash崩溃事件。

## 接口说明

  展开

| 接口名 | 描述 |
| --- | --- |
| int OH_HiAppEvent_AddWatcher(HiAppEvent_Watcher *watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH_HiAppEvent_RemoveWatcher(HiAppEvent_Watcher *watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 添加事件观察者

**在应用启动后，在执行业务逻辑前添加事件观察者，以确保订阅到崩溃事件。否则，应用可能因崩溃而退出，无法订阅崩溃事件。**

以用户点击按钮触发崩溃事件为例，开发步骤如下：

1. 获取示例工程的依赖项jsoncpp。

参考[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)README中**Amalgamated source**部分，获取jsoncpp.cpp、json.h和json-forwards.h三个文件。
2. 新建Native C++工程，并将上述文件导入到新建工程，目录结构如下。

 收起自动换行深色代码主题复制

```
entry: src: main: cpp: - json: - json.h - json-forwards.h - types: libentry: - index.d.ts - CMakeLists.txt - napi_init.cpp - jsoncpp.cpp ets: - entryability: - EntryAbility.ets - pages: - Index.ets
```
3. 在"CMakeLists.txt"文件中，添加源文件和动态库。

 收起自动换行深色代码主题复制

```
# 新增jsoncpp .cpp (解析订阅事件中的json字符串)源文件 add_library (entry SHARED napi_init.cpp jsoncpp.cpp) # 新增动态库依赖libhiappevent_ndk .z .so 和libhilog_ndk .z .so (日志输出) target_link_libraries (entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
```
4. 在"napi_init.cpp"文件中，导入依赖文件，并定义LOG_TAG。

 收起自动换行深色代码主题复制

```
# include "napi/native_api.h" # include "json/json.h" # include "hilog/log.h" # include "hiappevent/hiappevent.h" # include "hiappevent/hiappevent_event.h" # undef LOG_TAG # define LOG_TAG "testTag"
```

[napi_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L16-L25)
5. 订阅系统事件。

  - onReceive类型观察者

在"napi_init.cpp"文件中，定义onReceive类型观察者的方法：

 收起自动换行深色代码主题复制

```
```
  - onTrigger类型观察者

在"napi_init.cpp"文件中，定义OnTrigger类型观察者：

 收起自动换行深色代码主题复制

```
```
6. 将RegisterWatcher注册为ArkTS接口。

在"napi_init.cpp"文件中，将RegisterWatcher注册为ArkTS接口：

 收起自动换行深色代码主题复制

```
static napi_value Init (napi_env env, napi_value exports) { napi_property_descriptor desc[] = { // ··· { "registerWatcherCrashEvent" , nullptr , RegisterWatcherCrashEvent, nullptr , nullptr , nullptr , napi_default, nullptr }, { "registerWatcherClickCrash" , nullptr , RegisterWatcherClickCrash, nullptr , nullptr , nullptr , napi_default, nullptr }, // ··· }; napi_define_properties (env, exports, sizeof (desc) / sizeof (desc[ 0 ]), desc); return exports; }
```

在"index.d.ts"文件中，定义ArkTS接口：

 收起自动换行深色代码主题复制

```
export const registerWatcherClickCrash : () => void ; export const registerWatcherCrashEvent : () => void ;
```
7. 在"EntryAbility.ets"文件的onCreate()函数中添加接口调用。

 收起自动换行深色代码主题复制

```
// 在onCreate()函数中添加C API接口调用 // 启动时，注册崩溃事件观察者 testNapi. registerWatcherClickCrash (); // 启动时，注册按钮点击事件观察者 testNapi. registerWatcherCrashEvent ();
```
8. 在"Index.ets"文件中，新增按钮触发崩溃事件。

 收起自动换行深色代码主题复制

```
Button ( 'JsError' ) . type ( ButtonType . Capsule ) . margin ({ top : 20 }) . backgroundColor ( '#0D9FFB' ) . width ( '80%' ) . height ( '5%' ) . onClick ( () => { // 在按钮点击函数中构造一个crash场景，触发应用崩溃事件 JSON . parse ( '' ); })
```
9. 点击运行按钮，启动应用工程。在应用界面中点击“JsError”按钮，触发崩溃事件。系统生成相应的崩溃日志并进行回调。

 说明 

JsError通过进程内采集故障信息触发回调，速度快。NativeCrash采取进程外采集故障信息，平均耗时约2秒，具体受业务线程数量和进程间通信影响。订阅崩溃事件后，故障信息采集完成会异步上报，不阻塞当前业务。

### 验证观察者是否订阅到崩溃事件

在应用未主动捕获崩溃异常和主动捕获崩溃异常的两种场景中，崩溃事件的回调时机不同。开发者需要在每种情况下验证是否订阅到崩溃事件。

**应用未主动捕获崩溃异常场景**

若应用未主动捕获崩溃异常，则系统处理崩溃后应用将退出。**应用下次启动时**，HiAppEvent将崩溃事件上报给已注册的监听，完成回调。

从API version 21开始，若应用无法启动或长时间未启动，开发者可以参考[使用FaultLogExtensionAbility订阅事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fault-log-extension-app-events-arkts)回调重写的函数，进行延迟上报。

**应用主动捕获崩溃异常场景**

若应用主动捕获崩溃异常，HiAppEvent事件将在**应用退出前**触发回调，例如：

1. 异常处理中未主动退出的应用崩溃后不会退出。

采用[errorManager.on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-errormanager#errormanageronerror)方法捕获异常会导致JsError类型的崩溃事件在应用退出前触发回调。若应用注册[崩溃信号](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cppcrash-guidelines#系统处理的崩溃信号)处理函数但未主动退出，会导致NativeCrash类型的崩溃事件在应用退出前触发回调。
2. 异常处理耗时过长，会导致应用退出延迟。

在开发调试阶段，HiAppEvent上报事件完成回调后，可在DevEco Studio的HiLog窗口查看订阅的崩溃事件内容。

 收起自动换行深色代码主题复制

```
HiAppEvent eventInfo.domain=OS HiAppEvent eventInfo.name=APP_CRASH HiAppEvent eventInfo.eventType=1 HiAppEvent eventInfo.params.time=1503045716054 HiAppEvent eventInfo.params.crash_type=JsError HiAppEvent eventInfo.params.foreground=1 HiAppEvent eventInfo.params.bundle_version=1.0.0 HiAppEvent eventInfo.params.bundle_name=com.samples.eventsub HiAppEvent eventInfo.params.pid=2610 HiAppEvent eventInfo.params.uid=20010044 HiAppEvent eventInfo.params.uuid=7c3b1579c8ca8629af3858f8145254c2867ee402dc16ee18034337aae258620b HiAppEvent eventInfo.params.exception={"message":"Unexpected Text in JSON: Empty Text","name":"SyntaxError","stack":"    at anonymous (entry|entry|1.0.0|src/main/ets/pages/Index.ts:163:22)\n","thread_name":"amples.eventsub"} HiAppEvent eventInfo.params.hilog.size=100 HiAppEvent eventInfo.params.process_life_time=25 HiAppEvent eventInfo.params.memory={"rss":181964,"sys_avail_mem":1230456,"sys_free_mem":676940,"sys_total_mem":2001932} HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/APP_CRASH_1503045716408_2610.log"] HiAppEvent eventInfo.params.log_over_limit=0
```

### 移除并销毁事件观察者

1. 移除事件观察者。

 收起自动换行深色代码主题复制

```
static napi_value RemoveWatcherCrash (napi_env env, napi_callback_info info) { // 使观察者停止监听crash事件 OH_HiAppEvent_RemoveWatcher (systemEventWatcherR); OH_HiAppEvent_RemoveWatcher (systemEventWatcherT); return {}; }
```
2. 销毁事件观察者。

 收起自动换行深色代码主题复制

```
static napi_value DestroyWatcherCrash (napi_env env, napi_callback_info info) { // 销毁创建的观察者，并置eventWatcher为nullptr。 OH_HiAppEvent_DestroyWatcher (systemEventWatcherR); OH_HiAppEvent_DestroyWatcher (systemEventWatcherT); systemEventWatcherR = nullptr ; systemEventWatcherT = nullptr ; return {}; }
```
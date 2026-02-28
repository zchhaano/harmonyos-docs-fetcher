## 接口说明

本文介绍如何使用HiAppEvent提供的C/C++接口订阅音频卡顿事件。详细使用说明请参考[HiAppEvent C API文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h)。

 展开

| 接口名 | 描述 |
| --- | --- |
| int OH_HiAppEvent_AddWatcher(HiAppEvent_Watcher *watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH_HiAppEvent_RemoveWatcher(HiAppEvent_Watcher *watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

1. 获取示例工程的依赖项jsoncpp。

参考[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)README中**Amalgamated source**部分，获取jsoncpp.cpp、json.h和json-forwards.h三个文件。
2. 新建Native C++工程，并将上述文件导入到新建工程，目录结构如下。收起自动换行深色代码主题复制

```
entry: src: main: cpp: - json: - json.h - json-forwards.h - types: libentry: - index.d.ts - CMakeLists.txt - napi_init.cpp - jsoncpp.cpp ets: - entryability: - EntryAbility.ets - pages: - Index.ets
```
3. 在“CMakeLists.txt”文件中，添加源文件和动态库。收起自动换行深色代码主题复制

```
# 新增jsoncpp .cpp (解析订阅事件中的json字符串)源文件 add_library (entry SHARED napi_init.cpp jsoncpp.cpp) # 新增动态库依赖libhiappevent_ndk .z .so 和libhilog_ndk .z .so (日志输出) target_link_libraries (entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
```
4. 在“napi_init.cpp”文件中，导入依赖文件，并定义LOG_TAG。收起自动换行深色代码主题复制

```
# include "napi/native_api.h" # include "json/json.h" # include "hilog/log.h" # include "hiappevent/hiappevent.h" # undef LOG_TAG # define LOG_TAG "testTag"
```
5. 订阅系统事件。

  - onReceive类型观察者在“napi_init.cpp”文件中，定义onReceive类型观察者的方法：收起自动换行深色代码主题复制

```
```
  - onTrigger类型观察者

在“napi_init.cpp”文件中，定义OnTrigger类型观察者：

 收起自动换行深色代码主题复制

```
```
6. 将RegisterWatcher注册为ArkTS接口。

在“napi_init.cpp”文件中，将RegisterWatcher注册为ArkTS接口：

 收起自动换行深色代码主题复制

```
static napi_value Init (napi_env env, napi_value exports) { napi_property_descriptor desc[] = { { "registerWatcher" , nullptr , RegisterWatcher, nullptr , nullptr , nullptr , napi_default, nullptr } }; napi_define_properties (env, exports, sizeof (desc) / sizeof (desc[ 0 ]), desc); return exports; }
```

在“index.d.ts”文件中，定义ArkTS接口：

 收起自动换行深色代码主题复制

```
export const registerWatcher : () => void ;
```
7. 在“EntryAbility.ets”文件的onCreate()函数中添加接口调用。收起自动换行深色代码主题复制

```
// 导入依赖模块 import testNapi from 'libentry.so' ; // 在onCreate()函数中新增接口调用 // 启动时，注册系统事件观察者 testNapi. registerWatcher ();
```
8. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加一个模拟写入音频数据回调函数normalCallback，在该回调中模拟卡顿主动返回INVALID（不送数据）来触发卡顿故障事件。收起自动换行深色代码主题复制

```
let g_invalidCount = 0 ; function normalCallback ( buffer: ArrayBuffer ) { if (g_invalidCount > 0 ) { g_invalidCount--; return audio. AudioDataCallbackResult . INVALID ; } //在此添加写数据逻辑 return audio. AudioDataCallbackResult . VALID ; }
```
9. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加一个卡顿触发按钮，改变INVALID返回次数，模拟相应音频卡顿。收起自动换行深色代码主题复制

```
Row() { Button( "卡顿" ).onClick( async () => { g_invalidCount = 30 ; }) }
```
10. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，在创建AudioRender实例时，进行耗时操作回调收起自动换行深色代码主题复制

```
audio. createAudioRenderer (audioRendererOptions, ( err, renderer ) => { // 创建AudioRenderer实例 if (!err) { console . info ( ` ${TAG} : creating AudioRenderer success` ); this . renderModel = renderer; if ( this . renderModel !== undefined ) { this . renderModel . on ( 'writeData' , normalCallback); } } else { console . info ( ` ${TAG} : creating AudioRenderer failed, error: ${err.message} ` ); } });
```
11. AudioRender正常播放时，点击卡顿按钮，即可触发耗时回调，触发音频卡顿事件。
12. 每次音频卡顿触发后，可以在Log窗口看到对系统事件数据的处理日志。收起自动换行深色代码主题复制

```
HiAppEvent eventInfo.domain=OS HiAppEvent eventInfo.name=AUDIO_JANK_FRAME HiAppEvent eventInfo.eventType= 1 HiAppEvent eventInfo. params .time= 1762739184665 HiAppEvent eventInfo. params .bundle_version= 1.0 .0 HiAppEvent eventInfo. params .bundle_name=com.samples.audio HiAppEvent eventInfo. params .fault_type=application HiAppEvent eventInfo. params .happen_time= 176273918 HiAppEvent eventInfo. params .max_frame_time= 220
```
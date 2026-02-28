## 简介

本文介绍如何使用HiAppEvent提供的ArkTS接口订阅应用冻屏事件。接口的详细使用说明（参数限制、取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent (应用事件打点)ArkTS API文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent)。

## 接口说明

  展开

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 添加事件观察者

以订阅应用冻屏事件为例，说明开发步骤。

1. 新建一个ArkTS应用工程，编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，导入依赖模块，示例代码如下：

 收起自动换行深色代码主题复制

```
import { BusinessError } from '@kit.BasicServicesKit' ; import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit' ;
```
2. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate函数中设置事件的自定义参数，示例代码如下：

 收起自动换行深色代码主题复制

```
// 开发者完成参数键值对赋值 let params : Record < string , hiAppEvent. ParamType > = { "test_data" : 100 , }; // 开发者可以设置应用冻屏事件的自定义参数 hiAppEvent. setEventParam (params, hiAppEvent. domain . OS , hiAppEvent. event . APP_FREEZE ). then ( () => { hilog. info ( 0x0000 , 'testTag' , `HiAppEvent success to set event param` ); }). catch ( ( err: BusinessError ) => { hilog. error ( 0x0000 , 'testTag' , `HiAppEvent code: ${err.code} , message: ${err.message} ` ); });
```
3. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate函数中添加系统事件的订阅，示例代码如下：

 收起自动换行深色代码主题复制

```
```
4. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加按钮并在其onClick函数构造应用无响应场景，以触发应用冻屏事件，示例代码如下：

 收起自动换行深色代码主题复制

```
Button ( "appFreeze" ). onClick ( ()=> { // 在按钮点击函数中构造一个freeze场景，触发应用冻屏事件 setTimeout ( () => { let t = Date . now (); while ( Date . now () - t <= 15000 ) {} }, 5000 ); })
```
5. 点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击按钮“appFreeze”，触发一次应用冻屏事件。

### 验证观察者是否订阅到应用冻屏事件

1. 应用无响应退出后，重新进入应用可以在Log窗口看到对系统事件数据的处理日志：

 收起自动换行深色代码主题复制

```
HiAppEvent onReceive: domain=OS HiAppEvent eventName=APP_FREEZE HiAppEvent eventInfo.domain=OS HiAppEvent eventInfo.name=APP_FREEZE HiAppEvent eventInfo.eventType=1 HiAppEvent eventInfo.params.time=1711440881768 HiAppEvent eventInfo.params.foreground=true HiAppEvent eventInfo.params.bundle_version=1.0.0 HiAppEvent eventInfo.params.bundle_name=com.example.myapplication HiAppEvent eventInfo.params.process_name=com.example.myapplication HiAppEvent eventInfo.params.pid=3197 HiAppEvent eventInfo.params.uid=20010043 HiAppEvent eventInfo.params.uuid=27fac7098da46efe1cae9904946ec06c5acc91689c365efeefb7a23a0c37df77 HiAppEvent eventInfo.params.exception={"message":"App main thread is not response!","name":"THREAD_BLOCK_6S"} HiAppEvent eventInfo.params.hilog.size=77 HiAppEvent eventInfo.params.event_handler.size=6 HiAppEvent eventInfo.params.event_handler_size_3s=5 HiAppEvent eventInfo.params.event_handler_size_6s=6 HiAppEvent eventInfo.params.peer_binder.size=0 HiAppEvent eventInfo.params.threads.size=28 HiAppEvent eventInfo.params.memory={"pss":0,"rss":0,"sys_avail_mem":1361464,"sys_free_mem":796232,"sys_total_mem":1992340,"vm_heap_total_size":"9961472","vm_heap_used_size":"7596424","vss":0} HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/APP_FREEZE_1711440899240_3197.log"] HiAppEvent eventInfo.params.log_over_limit=false HiAppEvent eventInfo.params.test_data=100 HiAppEvent eventInfo.params.process_life_time=18
```
2. 若应用无法启动或长时间未启动，开发者可以参考[使用FaultLogExtensionAbility订阅事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fault-log-extension-app-events-arkts)回调重写的函数，进行延迟上报。

## 从Faultlogger接口迁移应用冻屏事件

[@ohos.faultLogger (故障日志获取)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-faultlogger)接口从API version 18开始废弃使用, 不再维护。后续版本推荐使用[@ohos.hiviewdfx.hiAppEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent)订阅应用冻屏事件。该章节指导开发者从Faultlogger接口迁移至hiAppEvent接口，来订阅应用冻屏事件。

在Faultlogger的[FaultType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-faultlogger#faulttype)里定义的APP_FREEZE即为应用冻屏故障类型。

在hiAppEvent的hiAppEvent.addWatcher接口中设置事件名称为hiAppEvent.event.APP_FREEZE、事件领域为hiAppEvent.domain.OS，可以订阅应用冻屏事件。

通过[hiAppEvent.AppEventInfo.params](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events#params字段说明)中exception字段的name子字段可以区分具体是哪种应用冻屏事件。

[FaultLogInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-faultlogger#faultloginfo)与[hiAppEvent.AppEventInfo.params](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events#params字段说明)的字段对应关系如下：

  展开

| Faultlogger.FaultLogInfo | hiAppEvent.AppEventInfo.params | 说明 |
| --- | --- | --- |
| pid | pid | 无。 |
| uid | uid | 无。 |
| type | exception字段中的name子字段 | 类型不同，Faultlogger中是故障类型枚举，hiAppEvent中是字符串类型。 |
| timestamp | time | 无。 |
| module | bundle_name | 无。 |
| fullLog | external_log | fullLog为故障日志全文。external_log为故障日志文件在应用沙箱中的具体路径(/data/storage/el2/log/)，访问该路径的文件，可以得到故障日志全文。 |
| reason | external_log文件内容中的Reason字段 | 无。 |
| summary | external_log文件内容中特定段落 | APP_FREEZE的summary对应external_log文件中从appfreeze:进程名所在行到DisplayPowerInfo:所在行的这一段内容。 |

[FaultLogger.query(使用callback回调)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-faultlogger#faultloggerquery9)和[FaultLogger.query(使用Promise回调)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-faultlogger#faultloggerquery9-1)都可以使用[hiAppEvent.addWatcher](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent#hiappeventaddwatcher)实现相同功能。

查阅[开发步骤](/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events-arkts#开发步骤)和[验证观察者是否订阅到应用冻屏事件](/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events-arkts#验证观察者是否订阅到应用冻屏事件)，了解使用hiAppEvent订阅应用冻屏事件（ArkTS）的具体步骤。

## 示例代码

- [应用异常处理](https://gitcode.com/HarmonyOS_Samples/exception-handling)
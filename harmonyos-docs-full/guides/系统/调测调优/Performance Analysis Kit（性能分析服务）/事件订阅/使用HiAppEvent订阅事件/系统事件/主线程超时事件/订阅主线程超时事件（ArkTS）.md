## 简介

本文介绍如何使用HiAppEvent提供的ArkTS接口订阅主线程超时事件。接口的详细使用说明（参数限制、取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent (应用事件打点)ArkTS API文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent)。

## 接口说明

  展开

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 添加事件观察者

以主线程超时事件订阅为例，说明开发步骤。

1. 新建一个ArkTS应用工程，编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，导入依赖模块，示例代码如下：

 收起自动换行深色代码主题复制

```
import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit' ; import { buffer, util } from '@kit.ArkTS' import { fileIo as fs } from '@kit.CoreFileKit' ;
```
2. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，可在onCreate、onForeground等生命周期接口中添加系统事件的订阅（结合业务需求，在合适的位置添加订阅方法），示例代码如下：

 收起自动换行深色代码主题复制

```
```
3. 该步骤用于模拟主线程超时采样栈事件。

编辑工程中的“entry > src > main > ets > pages> Index.ets”文件，示例代码如下：

 收起自动换行深色代码主题复制

```
@Entry @Component struct Index { build ( ) { RelativeContainer () { Column () { Button ( "timeOut350" , { stateEffect : true , type : ButtonType . Capsule }) . width ( '75%' ) . height ( 50 ) . margin ( 15 ) . fontSize ( 20 ) . fontWeight ( FontWeight . Bold ) . onClick ( () => { let t = Date . now (); while ( Date . now () - t <= 350 ) {} }) }. width ( '100%' ) } . height ( '100%' ) . width ( '100%' ) } }
```
4. （可选）该步骤用于模拟自定义主线程超时参数，并触发主线程超时事件场景。

编辑工程中的“entry > src > main > ets > pages> Index.ets”文件，本示例中设置一个customSample的Button控件，在onClick中实现自定义设置采样栈参数代码，示例代码如下：

 收起自动换行深色代码主题复制

```
import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit' ; import { BusinessError } from '@kit.BasicServicesKit' ; //模拟超时事件函数定义，示例代码： function wait150ms ( ) { let t = Date . now (); while ( Date . now () - t <= 150 ){ } } function wait500ms ( ) { let t = Date . now (); while ( Date . now () - t <= 500 ){ } } @Entry @Component struct Index { build ( ) { RelativeContainer () { Column () { //自定义设置采样栈参数按钮 Button ( "customSample" , { stateEffect : true , type : ButtonType . Capsule }) . width ( '75%' ) . height ( 50 ) . margin ( 15 ) . fontSize ( 20 ) . fontWeight ( FontWeight . Bold ) . onClick ( () => { // 在按钮点击函数中进行事件打点，以记录按钮点击事件 let params : Record < string , hiAppEvent. ParamType > = { // 事件类型定义， 0-默认值，1-只采样栈 2-只收集trace "log_type" : "1" , // 超时时间 & 采样间隔 "sample_interval" : "100" , // 忽略启动开始时间 "ignore_startup_time" : "11" , // 采样次数 "sample_count" : "21" , // 事件上报次数定义 "report_times_per_app" : "3" }; hiAppEvent. setEventConfig (hiAppEvent. event . MAIN_THREAD_JANK , params). then ( () => { hilog. info ( 0x0000 , 'testTag' , `HiAppEvent success to set event params.` ) }). catch ( ( err: BusinessError ) => { hilog. error ( 0x0000 , 'testTag' , `HiAppEvent err.code: ${err.code} , err.message: ${err.message} ` ) }); }) //触发150ms超时事件按钮 Button ( "timeOut150" , { stateEffect : true , type : ButtonType . Capsule }) . width ( '75%' ) . height ( 50 ) . margin ( 15 ) . fontSize ( 20 ) . fontWeight ( FontWeight . Bold ) . onClick ( () => { wait150ms (); }) }. width ( '100%' ) } . height ( '100%' ) . width ( '100%' ) } }
```
5. 该步骤可用于模拟主线程超时采样trace事件。

编辑工程中的“entry > src > main > ets > pages> Index.ets”文件，添加按钮并在其onClick函数触发主线程超时采集trace功能，具体如下：

 注意 

启动主线程超时检测抓取trace的功能的前提是开发者使用[nolog版本](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/performance-analysis-kit-terminology#nolog版本)并且关闭开发者模式。

  收起自动换行深色代码主题复制

```
@Entry @Component struct Index { build ( ) { RelativeContainer () { Column () { Button ( "timeOut500" , { stateEffect : true , type : ButtonType . Capsule }) . width ( '75%' ) . height ( 50 ) . margin ( 15 ) . fontSize ( 20 ) . fontWeight ( FontWeight . Bold ) . onClick ( () => { let t = Date . now (); while ( Date . now () - t <= 500 ) {} }) }. width ( '100%' ) } . height ( '100%' ) . width ( '100%' ) } }
```
6. 点击DevEco Studio界面中的运行按钮，运行应用工程。

 注意 

默认情况下，由于应用启动过程本身较为耗时，系统将在**应用启动10s后再进行测试，开始主线程超时事件检测**；

若开发者使用setEventConfig接口设置自定义设置采样栈参数，系统将**在开发者设定的ignore_startup_time时间后，开始主线程超时事件检测**。

主线程超时触发的条件：在检测任务的间隔内，检测到连续两次超时事件后，才会开启采集堆栈。

用户可以快速点击2~3次触发超时的按钮（如：timeOut350、timeOut150或timeOut500三种不同卡顿场景的按钮），以触发主线程超时事件。

### 验证观察者是否订阅到主线程超时事件

1. 主线程超时事件上报后，系统会回调应用的onReceive函数，可以在Log窗口看到对系统事件数据的处理日志：

主线程超时事件采样栈示例：

 收起自动换行深色代码主题复制

```
HiAppEvent eventInfo.domain=OS HiAppEvent eventInfo.name=MAIN_THREAD_JANK HiAppEvent eventInfo.eventType=1 HiAppEvent eventInfo.params.time=1717593620518 HiAppEvent eventInfo.params.bundle_version=1.0.0 HiAppEvent eventInfo.params.bundle_name=com.example.main_thread_jank HiAppEvent eventInfo.params.pid=40986 HiAppEvent eventInfo.params.uid=20020150 HiAppEvent eventInfo.params.begin_time=1717593620016 HiAppEvent eventInfo.params.end_time=1717593620518 HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/watchdog/MAIN_THREAD_JANK_20240613211739_40986.XXX"] HiAppEvent eventInfo.params.log_over_limit=false HiAppEvent eventInfo.params.app_start_jiffies_time=XXXX HiAppEvent eventInfo.params.heaviest_stack=XXXX
```

主线程超时事件采样trace，与采样栈的结果大致相同，不同的地方：

 收起自动换行深色代码主题复制

```
栈： 采样栈增加两个参数：app_start_jiffies_time和heaviest_stack。 external_log=["/data/storage/el2/log/watchdog/MAIN_THREAD_JANK_yyyyMMDDHHmmss_xxxx.txt"]。xxxx：代表进程pid trace： external_log=["/data/storage/el2/log/watchdog/MAIN_THREAD_JANK_unix时间戳_xxxx.trace"]。xxxx：代表进程pid
```
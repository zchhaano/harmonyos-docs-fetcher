## 接口说明

本文介绍如何使用HiAppEvent提供的C/C++接口订阅资源泄漏事件。API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[HiAppEvent C API文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h)。

**订阅接口功能介绍**：

  展开

| 接口名 | 描述 |
| --- | --- |
| int OH_HiAppEvent_AddWatcher(HiAppEvent_Watcher *watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH_HiAppEvent_RemoveWatcher(HiAppEvent_Watcher *watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 步骤一：新建工程

1. 获取该示例工程依赖的jsoncpp文件，从[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)下载源码的压缩包，并按照README的**Amalgamated source**中介绍的操作步骤得到jsoncpp.cpp、json.h和json-forwards.h三个文件。

在DevEco Studio中新建工程，选择“Native C++”工程。目录结构如下：

 收起自动换行深色代码主题复制

```
entry: src: main: cpp: - json: - json.h - json-forwards.h - types: libentry: - index.d.ts - CMakeLists.txt - napi_init.cpp - jsoncpp.cpp ets: - entryability: - EntryAbility.ets - pages: - Index.ets
```
2. 编辑“CMakeLists.txt”文件，添加源文件及动态库：

 收起自动换行深色代码主题复制

```
# 新增jsoncpp .cpp (解析订阅事件中的json字符串)源文件 add_library (entry SHARED napi_init.cpp jsoncpp.cpp) # 新增动态库依赖libhiappevent_ndk .z .so 和libhilog_ndk .z .so (日志输出) target_link_libraries (entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
```
3. 编辑“napi_init.cpp”文件，导入依赖文件，并定义LOG_TAG：

 收起自动换行深色代码主题复制

```
# include "napi/native_api.h" # include "json/json.h" # include "hilog/log.h" # include "hiappevent/hiappevent.h" # undef LOG_TAG # define LOG_TAG "testTag"
```

### 步骤二：订阅系统事件

1. 订阅系统事件：

  - onReceive类型观察者：

编辑“napi_init.cpp”文件，定义onReceive类型观察者相关方法：

 收起自动换行深色代码主题复制

```
```
  - onTrigger类型观察者：

编辑“napi_init.cpp”文件，定义OnTrigger类型观察者相关方法：

 收起自动换行深色代码主题复制

```
```
2. 将RegisterWatcher注册为ArkTS接口：

编辑“napi_init.cpp”文件，将RegisterWatcher注册为ArkTS接口：

 收起自动换行深色代码主题复制

```
static napi_value Init (napi_env env, napi_value exports) { napi_property_descriptor desc[] = { { "registerWatcher" , nullptr , RegisterWatcher, nullptr , nullptr , nullptr , napi_default, nullptr } }; napi_define_properties (env, exports, sizeof (desc) / sizeof (desc[ 0 ]), desc); return exports; }
```

编辑“index.d.ts”文件，定义ArkTS接口：

 收起自动换行深色代码主题复制

```
export const registerWatcher : () => void ;
```
3. 编辑“EntryAbility.ets”文件，在onCreate()函数中添加接口调用：

 收起自动换行深色代码主题复制

```
import testNapi from 'libentry.so' import hidebug from '@kit.PerformanceAnalysisKit' export default class EntryAbility extends UIAbility { onCreate ( want, launchParam ) { // 启动时，注册系统事件观察者 testNapi. registerWatcher (); } }
```

### 步骤三：测试资源泄漏事件

1. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加按钮并在其 onClick 函数中构造资源泄漏场景，以触发资源泄漏事件。

此处需要使用[hidebug.setAppResourceLimit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug#hidebugsetappresourcelimit12)设置内存限制，造成内存泄漏，同步在“开发者选项”中打开“系统资源泄漏日志”(开关状态变更后需重启设备)。接口示例代码如下：

 收起自动换行深色代码主题复制

```
Button ( 'pss leak' ) . type ( ButtonType . Capsule ) . margin ({ top : 20 }) . backgroundColor ( '#0D9FFB' ) . width ( '80%' ) . height ( '5%' ) . onClick ( () => { // 设置一个简单的资源泄漏场景 hilog. info ( 0x0000 , 'testTag' , 'click pss leak button' ); testNapi. leakMB ( 3072 ); })
```
2. 添加 pss leak 相关内容：

编辑“napi_init.cpp”文件：

  - 头文件加入：

 收起自动换行深色代码主题复制

```
# include <iostream> # include <fstream> # include <sstream> # include <thread>
```

  - 定义 pss leak 相关方法：

 收起自动换行深色代码主题复制

```
// 读 /proc/self/smaps_rollup 中的 PSS 字段，统计当前进程的 PSS (单位 KB) static int GetCurrentProcessPss () { std :: ifstream smapsFile (" /proc /self /smaps_rollup "); if (! smapsFile . is_open ()) { std :: cerr << "Failed to open /proc/self/smaps_rollup" << std :: endl ; return 0 ; } std :: string line ; int totalPss = 0 ; while ( std :: getline ( smapsFile , line )) { if ( line . find ( "Pss:" ) == 0 ) { std :: istringstream iss ( line ); std :: string label ; int pss ; iss >> label >> pss ; totalPss += pss ; } } smapsFile . close (); std :: cout << "Current pss: " << totalPss << " KB\r" ; std :: cout . flush (); return totalPss ; } // 读取当前进程的 FD 数量 static int GetCurrentFd () { std :: ifstream fdFile (" /proc /self /fd_num "); if (! fdFile . is_open ()) { std :: cerr << "Failed to open /proc/self/fd_num" << std :: endl ; return 0 ; } std :: string line ; int totalPss = 0 ; std :: getline ( fdFile , line ); fdFile . close (); std :: cout << "Current fd: " << line << std :: endl ; std :: cout . flush (); return std :: stoi ( line ); } // 申请 size 字节内存并写入数据（用 'a' 填充），制造 native 内存增长 static bool InjectNativeLeakMallocWithSize ( int size , char * p ) { const size_t maxSafe = 1073741824 ; if ( size < 0 || size > maxSafe ) { printf ( "InjectNativeLeakMallocWithSize invalid size\n" ); return false ; } p = ( char *) malloc ( size + 1 ); if (! p ) { printf ( "InjectNativeLeakMallocWithSize malloc failed\n" ); return false ; } void * err = memset ( p , 'a' , size ); if ( err == nullptr ) { printf ( "InjectNativeLeakMallocWithSize memset failed\n" ); return false ; } return true ; } // 循环申请/释放内存，使进程 PSS 持续接近 target static void InjectNativeLeakMallocUntil ( int target ) { constexpr int leakSizePerTime = 5000000 ; std :: vector < char *> mems ; int curPss = GetCurrentProcessPss (); while ( curPss != 0 ) { char * p = nullptr ; if ( curPss < target ) { if (! InjectNativeLeakMallocWithSize ( leakSizePerTime , p )) { printf ( "InjectNativeLeakMallocUntil target = %d failed\n" , target ); } mems . push_back ( p ); std :: cout << "Inject size: " << leakSizePerTime << ", currentSize: " << mems . size () << std :: endl ; } else { if ( mems . size () > 0 ) { char * dst = mems [ 0 ]; mems . erase ( mems . begin ()); free ( dst ); } std :: cout << "Free size: " << leakSizePerTime << ", currentSize: " << mems . size () << std :: endl ; } curPss = GetCurrentProcessPss (); } std :: cout << std :: endl ; printf ( "InjectNativeLeakMallocUntil target = %d success\n" , target ); } // 启动后台执行的 InjectNativeLeakMallocUntil 线程，使 native 内存占用接近 leakSize static void StartNativeLeak ( int leakSize ) { std :: cout << "Start inject malloc until" << leakSize << "KB" << std :: endl ; std :: thread t1 ( InjectNativeLeakMallocUntil , leakSize ); t1 . detach (); std :: cout << "Inject finished." << std :: endl ; } // N-API 导出方法 static napi_value LeakMB ( napi_env env , napi_callback_info info ) { size_t argc = 1 ; napi_value args [ 1 ]; napi_get_cb_info ( env , info , & argc , args , nullptr , nullptr ); if ( argc < 1 ) { napi_throw_type_error ( env , nullptr , "Expected 1 argument" ); return nullptr ; } double x = 0 ; if ( napi_get_value_double ( env , args [ 0 ], & x ) != napi_ok ) { napi_throw_type_error ( env , nullptr , "Argument must be a number" ); return nullptr ; } const size_t kilobyte = 1024 ; StartNativeLeak ( static_cast < size_t >( x * kilobyte )); napi_value rtn ; napi_get_undefined ( env , & rtn ); return rtn ; }
```

  - 初始化：

 收起自动换行深色代码主题复制

```
static napi_value Init (napi_env env, napi_value exports) { napi_property_descriptor desc[] = { // ... { "leakMB" , nullptr , LeakMB, nullptr , nullptr , nullptr , napi_default, nullptr } }; napi_define_properties (env, exports, sizeof (desc) / sizeof (desc[ 0 ]), desc); return exports; }
```

编辑“Index.d.ts”文件：

  - 添加类型声明：

 收起自动换行深色代码主题复制

```
export const leakMB : ( size: number ) => void ;
```
3. 单击DevEco Studio界面中的运行按钮，运行应用工程，单击 pss leak 按钮后，等待15到30分钟，系统将上报应用内存泄漏事件。

同一个应用，24小时内至多上报一次资源泄漏事件，如果短时间内要二次上报，需要重启设备。
4. 内存泄漏事件上报后，可以在Log窗口看到对系统事件数据的处理日志：

 收起自动换行深色代码主题复制

```
08-07 03:53:35.314 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.domain=OS 08-07 03:53:35.314 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.name=RESOURCE_OVERLIMIT 08-07 03:53:35.314 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.eventType=1 08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.time=1502049167732 08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.pid=1587 08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.uid=20010043 08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.resource_type=pss_memory 08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.bundle_name=com.example.myapplication 08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.bundle_version=1.0.0 08-07 03:53:35.350 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.memory={"pss":2100257,"rss":1352644,"sys_avail_mem":250272,"sys_free_mem":60004,"sys_total_mem":1992340,"vss":2462936} 08-07 03:53:35.350 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1725614572401_6808.log","/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1725614572412_6808.log"] 08-07 03:53:35.350 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.log_over_limit=false
```

### 步骤四：移除观察者

1. 移除事件观察者：

 收起自动换行深色代码主题复制

```
static napi_value RemoveWatcher (napi_env env, napi_callback_info info) { // 移除观察者以停止监听事件 OH_HiAppEvent_RemoveWatcher (systemEventWatcher); return {}; }
```
2. 销毁事件观察者：

 收起自动换行深色代码主题复制

```
static napi_value DestroyWatcher (napi_env env, napi_callback_info info) { // 销毁创建的观察者，并置systemEventWatcher为nullptr。 OH_HiAppEvent_DestroyWatcher (systemEventWatcher); systemEventWatcher = nullptr ; return {}; }
```
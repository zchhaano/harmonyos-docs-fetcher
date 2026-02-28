# 使用ASan检测内存错误

为追求C/C++的极致性能，编译器和OS(Windows/Linux/Mac)运行框架不会对内存操作进行安全检测。针对该场景，DevEco Studio集成ASan（Address-Sanitizer）为开发者提供面向C/C++的地址越界检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于ASan的检测原理请参考[ASan检测原理](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-address-sanitizer-principle#section159561141247)。

## 使用约束

- 如果应用内的任一模块使能ASan，那么entry模块需同时使能ASan。如果entry模块未使能ASan，该应用在启动时将闪退，出现CPP Crash报错。
- ASan、TSan、UBSan、HWASan不能同时开启，四个只能开启其中一个。

## 使能ASan

可通过以下两种方式使能ASan。

### 方式一

1. 点击**Run > Edit Configurations >****Diagnostics**，勾选**Address Sanitizer**。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102025.38867303789540835673224733769035:50001231000000:2800:DB134300FEC3C718DE104BF650A5965B8EB3695D1CC361F0F8FAF20395FA9720.png)
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS_ENABLE_ASAN=ON”，表示以ASan模式编译so文件。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102025.96090022864728767700084181941765:50001231000000:2800:8EAF70F4D15CDA4B449C06DADC5C677EA459CC9DCCFAF33759AFE8747674D78D.png)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加ASan配置开关。

收起自动换行深色代码主题复制

```
"asanEnabled" : true
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102025.81871133865406265173531443233650:50001231000000:2800:59528FE7C9C94279D1B6D0930D17F718B679B84EEE977232C83D257C96AFB06A.png)
2. 设置模块级构建ASan插桩。

在需要使能ASan的模块中，通过添加构建参数开启ASan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

 收起自动换行深色代码主题复制

```
"arguments" : "-DOHOS_ENABLE_ASAN=ON"
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102025.24147456537323786387026708671126:50001231000000:2800:75AEF18ACF1C98E9BECDFEDE5964F6854C0B07A420DDC07C435BC0B839BB235A.png)

 说明

该参数未配置不会报错，但是除包含malloc和free函数等少数内存错误外，出现其他需要插桩检测的内存错误时，ASan无法检测到错误。

## 配置参数（可选）

ASAN_OPTIONS用于在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等。ASAN_OPTIONS支持在app.json5中配置，也支持在Run/Debug Configurations中配置。app.json5的优先级更高，即两种方式都配置后，以app.json5中的配置为准。关于ASAN_OPTIONS的配置方式和常用参数请参考[配置参数](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-asan-detection#section1496994494018)。

## 启用ASan

1. 运行或调试当前应用。
2. 当程序出现内存错误时，弹出ASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。日志中各字段的说明请参考[ASan日志规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/address-sanitizer-guidelines#asan日志规格)，异常检测类型请参考[ASan异常检测类型](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-asan-detection#section12508111110451)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102026.61599330618182559794394601870913:50001231000000:2800:BA42C323D2BB949105760B5F00BE23A8C92A359C33C7A247524865205ECDFBF9.png)
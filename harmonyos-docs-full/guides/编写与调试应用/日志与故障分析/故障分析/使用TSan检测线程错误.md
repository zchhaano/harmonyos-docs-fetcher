# 使用TSan检测线程错误

TSan（ThreadSanitizer）是一个检测数据竞争的工具。它包含一个编译器插桩模块和一个运行时库。TSan开启后，会使性能降低5到15倍，同时使内存占用率提高5到10倍。关于TSan的检测原理请参考[TSan](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-tsan-detection)。

## 功能介绍

### 应用场景

TSan能够检测出如下问题：

- 数据竞争检测

数据竞争（Data Race）是指两个或多个线程在没有适当的同步机制情况下同时访问相同的内存位置，其中至少有一个线程在写入。数据竞争是导致多线程程序行为不可预测的主要原因之一。

- 锁错误检测

TSan 不仅能检测数据竞争，还能检测与锁相关的错误：

  - 死锁（Deadlock）：死锁是指两个或多个线程互相等待对方释放锁，导致程序无法继续执行。
  - 双重解锁（Double Unlock）：同一线程尝试解锁已经解锁的锁。
  - 未持有锁解锁：一个线程尝试解锁一个它未持有的锁。

- 条件变量错误检测

条件变量用于线程之间的通信和同步，常见错误包括：

  - 未持有锁等待：一个线程在未持有相关锁的情况下调用 wait。
  - 未持有锁唤醒：一个线程在未持有相关锁的情况下调用 signal 或 broadcast。

### 错误报告

当 TSan 检测到错误时，它会生成详细的报告，包括：

- 错误类型：例如数据竞争、死锁等。
- 内存地址：涉及的内存地址。
- 线程信息：涉及的线程ID和线程创建的堆栈跟踪。
- 源代码位置：每一个内存访问的源代码位置和堆栈跟踪。
- 上下文信息：访问类型（读/写）、访问大小等。

## 使用约束

- TSan仅支持API 12及以上版本。
- ASan、TSan、UBSan、HWASan不能同时开启，四个只能开启其中一个。
- TSan开启后会申请大量虚拟内存，其他申请大虚拟内存的功能（如gpu图形渲染）可能会受影响。
- TSan不支持静态链接libc或libc++库。

## 使能TSan

可通过以下两种方式使能TSan。

### 方式一

1. 点击**Run > Edit Configurations >** **Diagnostics**，勾选**Thread Sanitizer**。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102030.29091028674974481293726814816090:50001231000000:2800:53D546436B4BD95B4FC15C5E08D5BC7295BACB0C5A5C03DFD79A501DA3DEE496.png)
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS_ENABLE_TSAN=ON”，表示以TSan模式编译so文件。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102030.52197949561659393399483072827815:50001231000000:2800:84178264EF115D827F350ECB072D4E4D0D6433716FFBF0F97A12496D58EBB138.png)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加TSan配置开关。

收起自动换行深色代码主题复制

```
"tsanEnabled" : true
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102030.50539096112605012775883336800864:50001231000000:2800:5A9F680E3B5E481F3C6290748B0C7BD01B3B66F1E31C791BA774EE8D88EC5C5A.png)
2. 设置模块级构建TSan插桩。

在需要使能TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

 收起自动换行深色代码主题复制

```
"arguments" : "-DOHOS_ENABLE_TSAN=ON"
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102030.77302243519948784865394590526748:50001231000000:2800:567E86DFE34D66940C15F44509511C4C553BA26EAD93B21A325AE664C6203023.png)

## 启用TSan

1. 运行或调试当前应用。
2. 当程序出现线程错误时，弹出TSan log信息，点击信息中的链接即可跳转至引起线程错误的代码处。日志中的异常检测类型请参考[TSan异常检测类型](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-tsan-detection#section1180812915516)。

说明

当前使用call_once接口会存在TSan误报的现象，开发者可以在调用该接口的函数前添加__attribute__((no_sanitize("thread")))来屏蔽该问题。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102030.40790295197029518134340519783444:50001231000000:2800:FD4549A5AA4C6CB02CF3E0C3C081B553A18ED11936FD2B92553DE57980494B2E.png)
3. 如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102030.88850811493853980861893690393697:50001231000000:2800:FC828F090131B24F592ADD560E62D49FA78BA74BDEFB1EC35F290C7139EB404F.png)
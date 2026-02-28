# 使用HWASan检测内存错误

HWASan（Hardware-Assisted Address Sanitizer）是一款类似于[ASan](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-asan)的内存错误检测工具。 与ASan相比，HWASan使用的内存减少很多，因而更适合用于整个系统的清理。关于HWASan的检测原理请参考[HWASan检测原理](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-address-sanitizer-principle#section187526511146)。

## 约束条件

- HWASan检测仅适用于AArch64架构的硬件。
- ASan、TSan、UBSan、HWASan不能同时开启，四个只能开启其中一个。

## 使能HWASan

### 方式一

点击**Run > Edit Configurations > Diagnostics**，勾选**Hardware-Assisted Address Sanitizer**开启检测。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102027.80047116428746429288638609792981:50001231000000:2800:09C4CC4A479F15702856FB2ECDB17128EE0C754A8ABC2E82031A411F81D08C66.png)

### 方式二

1. 修改工程目录下的AppScope/app.json5文件，添加HWASan配置开关。收起自动换行深色代码主题复制

```
"hwasanEnabled" : true
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102027.77251539784225779452045266993740:50001231000000:2800:660C15CDDA7880A5937767C3F89E980D9F93D794064219EB84F54AFBF9A83CC4.png)
2. 在需要使能HWASan的模块中，通过添加构建参数开启HWASan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：收起自动换行深色代码主题复制

```
"arguments" : "-DOHOS_ENABLE_HWASAN=ON"
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102027.95750183240650467005445198066531:50001231000000:2800:279D2486C612F9948D2ECDE3C29AF1A0FC0224CADF78F9C0053C0453CB5CD8EA.png)

## 启用HWASan

1. 运行或调试当前应用。
2. 当程序出现内存错误时，弹出HWASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。日志中各字段的说明请参考[HWASan日志规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/address-sanitizer-guidelines#hwasan日志规格)，异常检测类型请参考[HWASan异常检测类型](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-hwasan-detection#section207321025115510)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102027.00755646180320083984233695873422:50001231000000:2800:07FFDAB23C5BD606E028F497A84D9DD97FE2D6E123B19FFA4C68CDCA059A12F7.png)
3. 如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102027.45841891795066110189427224661299:50001231000000:2800:E032B25487C29F3CC4DA46E4801A7FEB6A4FD2A6CBB948644C27D061ADB21390.png)
# NativeChildProcess_Args

收起自动换行深色代码主题复制

```
typedef struct { ...} NativeChildProcess_Args
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

传递给子进程的参数。

**起始版本：** 13

**相关模块：** [ChildProcess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-childprocess)

**所在头文件：** [native_child_process.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-child-process-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char* entryParams | 入口参数，大小不能超过150KB。 |
| struct NativeChildProcess_FdList fdList | 传递给子进程的文件描述符信息列表。 |
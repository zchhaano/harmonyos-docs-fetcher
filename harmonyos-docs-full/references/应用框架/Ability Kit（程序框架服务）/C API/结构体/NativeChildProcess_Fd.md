# NativeChildProcess_Fd

收起自动换行深色代码主题复制

```
typedef struct { ...} NativeChildProcess_Fd
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

传递给子进程的文件描述符信息。

**起始版本：** 13

**相关模块：** [ChildProcess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-childprocess)

**所在头文件：** [native_child_process.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-child-process-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char* fdName | 文件描述符的键，最大长度为20字符。 |
| int32_t fd | 文件描述符的值。 |
| struct NativeChildProcess_Fd * next | 下一个文件描述记录指针。 |
# FileShare_PolicyErrorResult

```
typedef struct FileShare_PolicyErrorResult {...} FileShare_PolicyErrorResult
```

## 概述

支持设备PhonePC/2in1TabletTV

授予或使能权限失败的URI策略结果。

**起始版本：** 12

**相关模块：** [fileShare](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare)

**所在头文件：** [oh_file_share.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-file-share-h)

## 汇总

支持设备PhonePC/2in1TabletTV 

### 成员变量

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| char *uri | 授予或使能策略失败的URI。 |
| FileShare_PolicyErrorCode code | 授予或使能策略失败的URI对应的错误码。 |
| char *message | 授予或使能策略失败的URI对应的原因。 |
# UsbDdkInterface

收起自动换行深色代码主题复制

```
typedef struct UsbDdkInterface { ...} UsbDdkInterface
```

## 概述

支持设备PC/2in1

USB接口，是特定接口下备用设置的集合。

**起始版本：** 10

**相关模块：** [UsbDDK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk)

**所在头文件：** [usb_ddk_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usb-ddk-types-h)

## 汇总

支持设备PC/2in1 

### 成员变量

 支持设备PC/2in1展开

| 名称 | 描述 |
| --- | --- |
| uint8_t numAltsetting | 接口的备用设置数量。 |
| struct UsbDdkInterfaceDescriptor* altsetting | 接口的备用设置。 |
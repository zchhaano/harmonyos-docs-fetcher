## 概述

支持设备PhonePC/2in1TabletTV

此结构体描述通过[HMS_XEG_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties)接口查询到的XEngine扩展特性集合。

**起始版本：** 5.0.0(12)

**相关模块：**[XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

**所在头文件：**[xeg_vulkan_extension.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-extension-8h)

## 汇总

支持设备PhonePC/2in1TabletTV 

### 成员变量

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| char extensionName [ XEG_MAX_EXTENSION_NAME_SIZE ] | XEngine支持的扩展特性名称。 |
| uint32_t version | XEngine支持的扩展特性版本号。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTV 

### extensionName

支持设备PhonePC/2in1TabletTV

```
char XEG_ExtensionProperties::extensionName[XEG_MAX_EXTENSION_NAME_SIZE]
```

**描述**

XEngine支持的扩展特性名称。

### version

支持设备PhonePC/2in1TabletTV

```
uint32_t XEG_ExtensionProperties::version
```

**描述**

XEngine支持的扩展特性版本号。
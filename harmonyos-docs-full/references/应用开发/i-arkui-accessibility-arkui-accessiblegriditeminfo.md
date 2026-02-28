# ArkUI_AccessibleGridItemInfo

```
typedef struct {...} ArkUI_AccessibleGridItemInfo
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

用于配置特定组件（如List、Flex、Select、Swiper组件）的属性值。

**起始版本：** 13

**相关模块：** [ArkUI_Accessibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility)

**所在头文件：** [native_interface_accessibility.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-accessibility-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| bool heading | 是否是标题。true表示是标题，false表示不是标题。 |
| bool selected | 是否被选中。true表示被选中，false表示未被选中。 |
| int32_t columnIndex | 列下标。 |
| int32_t rowIndex | 行下标。 |
| int32_t columnSpan | 列跨度。 |
| int32_t rowSpan | 行跨度。 |
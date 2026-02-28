# ArkUI_ActiveChildrenInfo

收起自动换行深色代码主题复制

```
typedef struct ArkUI_ActiveChildrenInfo ArkUI_ActiveChildrenInfo
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

定义ActiveChildrenInfo类信息。

**起始版本：** 14

**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h)

**相关接口：**

 展开

| 名称 | 描述 |
| --- | --- |
| OH_ArkUI_NodeUtils_GetActiveChildrenInfo | 获取某个节点所有活跃的子节点。 |
| OH_ArkUI_ActiveChildrenInfo_GetNodeByIndex | 获取ActiveChildrenInfo结构体的下标为index的子节点。 |
| OH_ArkUI_ActiveChildrenInfo_GetCount | 获取ActiveChildrenInfo结构体内的节点数量。 |
| OH_ArkUI_ActiveChildrenInfo_Destroy | 销毁ActiveChildrenInfo实例。 |
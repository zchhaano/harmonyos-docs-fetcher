## 概述

支持设备PhonePC/2in1TabletTVWearable

定义通知服务API接口。

**引用文件：** <NotificationKit/notification.h>

**库：** libohnotification.so

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 13

**相关模块：** [NOTIFICATION](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-notification)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 函数

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| bool OH_Notification_IsNotificationEnabled(void) | 查询当前应用通知使能状态。 |

## 函数说明

支持设备PhonePC/2in1TabletTVWearable 

### OH_Notification_IsNotificationEnabled()

支持设备PhonePC/2in1TabletTVWearable

```
bool OH_Notification_IsNotificationEnabled(void)
```

**描述**

查询当前应用通知使能状态。

**起始版本：** 13

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| bool | true - 表示当前应用已使能通知。 false - 表示当前应用未使能通知。 |
# Notification Kit简介

Notification Kit（用户通知服务）为开发者提供本地通知发布通道，开发者可借助Notification Kit将应用产生的通知直接在客户端本地推送给用户，本地通知根据通知类型及发布场景会产生对应的铃声、震动、横幅、锁屏、息屏、通知栏提醒和显示。

## 使用场景

当应用进程处于运行时，开发者可以使用Notification Kit向用户发布通知。当应用进程终止后，本地通知发布通道关闭，开发者需要接入[Push Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-kit-introduction)进行云侧离线通知的发布。

开发者可以在多种场景中运用本地通知能力。如同步用户的上传下载进度、发布即时的客服支付通知、更新运动步数等。

## 能力范围

Notification Kit支持的能力主要包括：

- 发布文本、进度条等类型通知。
- 携带或更新应用通知数字角标。
- 取消曾经发布的某条或全部通知。
- 查询已发布的通知列表。
- 查询应用自身通知开关状态。
- 应用通知用户的能力默认关闭，开发者可拉起授权框，请求用户授权发布通知。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165456.83118601471101476091674184903353:50001231000000:2800:97A607140802AB9EF01BD67C74F9F5F9AE8491D0F49A29CB7BBC5876522AC024.png)

## 业务流程

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165456.06555880259787109461723892801825:50001231000000:2800:5E5BD203198A283796025B1839FC859E74B009929B44C164F8784EF0D1B87822.png)

使用Notification Kit的主要业务流程如下：

1.请求通知授权。

2.应用发布通知到通知服务。

3.将通知展示到通知中心。

## 通知样式

 说明 

实际显示效果依赖设备能力和通知中心UI设计样式。

Notification Kit中常用的通知样式如下：

  展开

| 类型 | 通知样式 | 规格描述 |
| --- | --- | --- |
| 文本 |  | 通知文本内容最多显示三行，超长后以“...”截断。 |
| 多行文本 |  | 最多可显示三行内容，每行内容超长后以“...”截断。 |
| 通知角标 |  | 以数字的形式展示在右上角。 |
| 进度条 |  | 进度类通知。 |

## 约束限制

- 单个应用已发布的通知在通知中心等系统入口的留存数量有限（当前规格最多24条）。
- 通知的长度不能超过200KB（跨进程序列化大小限制）。
- 通知的发布频次和更新频次需要满足如下要求，否则会导致发布或更新失败，返回相应错误码。       

  - 单个应用发布新通知的频次累计不能超过每秒10条，更新通知的频次累计不能超过每秒20条。
  - 所有三方应用发布新通知的频次累计不能超过每秒15条，更新通知的频次累计不能超过每秒30条。

## 违规处罚

应用发送的通知需遵守Push Kit的[通知内容原则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-detail-rules)，如出现违反通知内容原则的行为，将被视为违规。

违规行为及相应的处理措施请参见[违规分类、违规行为及违规处罚标准](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-punishment-standards)。

## 与相关Kit的关系

- Notification Kit创建的通知会即时显示在通知中心等系统入口。如果开发者希望在应用退到后台或进程终止后仍然有一些提醒用户的定时类通知，例如购物类应用抢购提醒等，可通过[Background Tasks Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/background-task-overview)创建。目前支持基于倒计时、日历、闹钟等类型的通知提醒功能。
- 开发者可通过[Ability Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/abilitykit-overview)的[getWantAgent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent#wantagentgetwantagent)接口设置用户点击通知后的行为意图。
- 开发者可通过[Push Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-kit-introduction)远程推送用户通知到本地。
# 应用内通知设置快捷入口开发指导

    

#### 使用场景

 

应用的通知设置页面属于3层页面，用户查找难度较大，导致应用的通知关闭率上升。

 

为改善这一情况，我们在通知消息的左滑菜单和系统的应用通知设置页面中，添加了快速进入应用内通知设置功能页面的入口，直接引导用户跳转至应用内的通知分类管理页面，提升用户通知管理的体验，降低应用通知关闭率。

 

“设置 > 通知和状态栏 > XX应用”页面

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/5OeV0ZHBRZyGaDHnrkVbnw/zh-cn_image_0000002543374764.png?HW-CC-KV=V1&HW-CC-Date=20260420T191248Z&HW-CC-Expire=86400&HW-CC-Sign=C4C54C5E4FB86889E19C46D369C06499EF7BA4EE76991915C4DEBEC2937EFE72)

 

通知中心页面

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/rY9Z1iGiTNq6JT85pnAIwA/zh-cn_image_0000002543215102.png?HW-CC-KV=V1&HW-CC-Date=20260420T191248Z&HW-CC-Expire=86400&HW-CC-Sign=CBDEB186F294CCDD529568547F1B9873633F091BB823FCF5B1D63F9342E9B687)

    

#### 开发准备

 

详情请参考[应用链接说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-uri-config)，其中[linkFeature](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-uri-config#linkfeature标签说明)使用AppNotificationMgmt即可。

    

#### 功能验证

 

- 场景1

 

  1. 在手机的“设置 > 通知和状态栏”页面，选择当前应用，进入应用详情页。
  2. 点击“前往XX应用管理”的选项，即可跳转至应用内对应的通知设置页面。
- 场景2

 

  1. 在手机通知中心页面，左滑应用已发布的通知。
  2. 点击“前往XX应用管理”的选项，即可跳转至应用内对应的通知设置页面。
# 查看ArkTS/JS预览效果

 

预览器支持ArkTS/JS应用/元服务“实时预览”和“动态预览”。

 ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/PKACb2PaQWC4-VReCr-LGQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194025Z&HW-CC-Expire=86400&HW-CC-Sign=0E835470A10A3CFB6A59FB50E1511E2CA8AC7CA952293A7011D9CDF759157726) 

- 预览支持Phone、Tablet、2in1、Car、Wearable、TV设备的ArkTS工程，支持LiteWearable和Wearable设备的JS工程。
- 预览器功能依赖于电脑显卡的OpenGL版本，OpenGL版本要求为3.2及以上。
- 预览时将不会运行Ability生命周期。
- 从DevEco Studio 6.0.0 Beta3版本开始，HAP/HSP引用HSP时支持预览，HAR模块引用HSP不支持预览，请直接在HSP内预览或为该HSP[设置Mock实现](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-mock)。
- 预览场景下，不支持通过相对路径及绝对路径的方式访问resources目录下的文件。
- 预览不支持组件拖拽。
- 部分API不支持预览，如Ability、App、MultiMedia等模块。
- Richtext、Web、Video、XComponent组件不支持预览。
- 不支持调用C++库的预览。
- HAR在被应用/元服务使用时真机效果有区别，真机上实际效果应用不显示menubar，元服务显示menubar，但预览器都以不显示menubar为准。若开发HAR模块，请注意被元服务使用时预览器效果与真机效果的不同。

  

- **实时预览**：在开发界面UI代码过程中，如果添加或删除了UI组件，您只需**Ctrl+S**进行保存，然后预览器就会立即刷新预览结果。如果修改了组件的属性，则预览器会实时（亚秒级）刷新预览结果，达到极速预览的效果（当前版本极速预览仅支持ArkTS组件。支持部分数据绑定场景，如@State装饰的变量）。实时预览默认开启，如果不需要实时预览，请单击预览器右上角![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/DNI6qy89TxCHjUrLZ4CPEw/zh-cn_image_0000002530912978.png?HW-CC-KV=V1&HW-CC-Date=20260420T194025Z&HW-CC-Expire=86400&HW-CC-Sign=FB2A8596B46EE7F962E5C72DDB19D079F7B65E9917D2D4E50722A8DC18A274B3)按钮，关闭实时预览功能。![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/n1HcottwSBGaTNH-_VeT6Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194025Z&HW-CC-Expire=86400&HW-CC-Sign=A89FBE621FE6411AB0072AA560FDC5689E275EA8866A2FE8000B5A46F154D913) 

开发者修改resources/base/profile目录下的配置文件（如main_pages.json/form_config.json），不支持触发实时预览，开发者需要点击重新加载![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/K98ZoVeIQtSz0171Fep_4Q/zh-cn_image_0000002561752919.png?HW-CC-KV=V1&HW-CC-Date=20260420T194025Z&HW-CC-Expire=86400&HW-CC-Sign=62F0EB86A8B74A3AABAD22E6ADFEF82C173108DF84293C93A68C374E1EFD376D)。

  

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/4-wMGIWITzCDkliyXdVbGg/zh-cn_image_0000002561832907.gif?HW-CC-KV=V1&HW-CC-Date=20260420T194025Z&HW-CC-Expire=86400&HW-CC-Sign=FCC7AC48D2AEC4216C075C000438470F4E13235DE4D1665756278D6F4F7DC941)
- **动态预览**：在预览器界面，可以在预览器中操作应用/元服务的界面交互动作，如单击、跳转、滑动等，与应用/元服务运行在真机设备上的界面交互体验一致。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/26nB0u-nRy2kRZLNy4-aAg/zh-cn_image_0000002561752927.gif?HW-CC-KV=V1&HW-CC-Date=20260420T194025Z&HW-CC-Expire=86400&HW-CC-Sign=F3F252DF142899FC0E626633C311675157AA29FE0BBE01D79993964F3215842D)

 

以ArkTS为例，使用预览器的方法如下：

 

1. 创建或打开一个ArkTS应用/元服务工程。本示例以打开一个本地ArkTS Demo工程为例。
2. 在工程目录下，打开任意一个.ets文件（JS工程请打开.hml/.css/.js页面）。
3. 可以通过如下任意一种方式打开预览器，启动预览。

  - 通过菜单栏，单击**View > Tool Windows > Previewer**打开预览器。
  - 在编辑窗口右上角的侧边工具栏，单击**Previewer**，打开预览器。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/yZBcG2OWRgy6GZ8FCikchQ/zh-cn_image_0000002561832905.png?HW-CC-KV=V1&HW-CC-Date=20260420T194025Z&HW-CC-Expire=86400&HW-CC-Sign=0ECB9C60D3A4ADE31079F52F19778790D747B261ABF7B23A44FA27248ADE6E72)
4. 点击按钮![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/vfg_98L6R8u0qR9uUBQEDA/zh-cn_image_0000002561752929.png?HW-CC-KV=V1&HW-CC-Date=20260420T194025Z&HW-CC-Expire=86400&HW-CC-Sign=F1B538E664C15A1A69E47FD66A8C8B75983B45FEA59188863A972804A9E5D995)，停止预览。
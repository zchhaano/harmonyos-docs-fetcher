# 查看ArkTS/JS预览效果

预览器支持ArkTS/JS应用/元服务“实时预览”和“动态预览”。

 说明

- 预览支持Phone、Tablet、2in1、Car、Wearable、TV设备的ArkTS工程，支持LiteWearable和Wearable设备的JS工程。
- 预览器功能依赖于电脑显卡的OpenGL版本，OpenGL版本要求为3.2及以上。
- 预览时将不会运行Ability生命周期。
- 从DevEco Studio 6.0.0 Beta3版本开始，HAP/HSP引用HSP时支持预览，HAR模块引用HSP不支持预览，请直接在HSP内预览或为该HSP[设置Mock实现](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-mock)。
- 预览场景下，不支持通过相对路径及绝对路径的方式访问resources目录下的文件。
- 预览不支持组件拖拽。
- 部分API不支持预览，如Ability、App、MultiMedia等模块。
- Richtext、Web、Video、XComponent组件不支持预览。
- 不支持调用C++库的预览。
- har在被应用/元服务使用时真机效果有区别，真机上实际效果应用不显示menubar，元服务显示menubar，但预览器都以不显示menubar为准。若开发har模块时，请注意被元服务使用时预览器效果与真机效果的不同。

- **实时预览**：在开发界面UI代码过程中，如果添加或删除了UI组件，您只需**Ctrl+S**进行保存，然后预览器就会立即刷新预览结果。如果修改了组件的属性，则预览器会实时（亚秒级）刷新预览结果，达到极速预览的效果（当前版本极速预览仅支持ArkTS组件。支持部分数据绑定场景，如@State装饰的变量）。实时预览默认开启，如果不需要实时预览，请单击预览器右上角![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102002.37936226333451599966837803537845:50001231000000:2800:24F505F7B55B84C33B8B0F26796BA09804D758B31D2D896BF978CFD7AE78FF5C.png)按钮，关闭实时预览功能。说明

开发者修改resources/base/profile目录下的配置文件（如main_pages.json/form_config.json），不支持触发实时预览，开发者需要点击重新加载![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102002.36942560588332109927891619217167:50001231000000:2800:D098F3CE5E41CFBA33A76EB98BD86E5FDE39BA5F6D37B647B764D258FF5AE5E8.png)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102002.69291554282912846983433148444965:50001231000000:2800:BB7997734ACE0EB83A57B359D55C1780630019149023C7887238E5024E3C5755.gif)
- **动态预览**：在预览器界面，可以在预览器中操作应用/元服务的界面交互动作，如单击、跳转、滑动等，与应用/元服务运行在真机设备上的界面交互体验一致。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102002.37476776704163058895988051539208:50001231000000:2800:CFDD6A6947152969D31A66437A61185F2CE7FF5999C4209B8A70782D0CC4F249.gif)

以ArkTS为例，使用预览器的方法如下：

1. 创建或打开一个ArkTS应用/元服务工程。本示例以打开一个本地ArkTS Demo工程为例。
2. 在工程目录下，打开任意一个.ets文件（JS工程请打开.hml/.css/.js页面）。
3. 可以通过如下任意一种方式打开预览器，启动预览。

  - 通过菜单栏，单击**View > Tool Windows > Previewer**打开预览器。
  - 在编辑窗口右上角的侧边工具栏，单击**Previewer**，打开预览器。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102002.41917735732300774689487574265805:50001231000000:2800:16F2F30D670485BDB90BE1E43006FC4D1F998484D8988C072BC87CD8CA5B80AF.png)
4. 点击按钮![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102002.15006552417749268678901900768254:50001231000000:2800:DAE7B28E32A6B291537E427C0FF2B3D9479F59950BAE485086F1760EBB610A1E.png)，停止预览。
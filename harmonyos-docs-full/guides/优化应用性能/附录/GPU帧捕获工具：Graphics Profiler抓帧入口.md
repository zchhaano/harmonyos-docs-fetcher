# GPU帧捕获工具：Graphics Profiler抓帧入口

Graphics Profiler（图形性能调优）是专为GPU分析和优化提供的一种调试分析解决方案，可帮助OpenGL ES游戏或Vulkan游戏提升性能，分析绘制和计算问题。从DevEco Studio 6.0.0 Beta1版本开始，提供Graphics Profiler工具的抓帧入口，该工具用于对HarmonyOS手机设备进行调试，需使用调试证书。

## 操作步骤

1. 将需要分析的使用OpenGL ES或Vulkan API接口开发的应用推送到设备，并确认应用完成安装。
2. 在DevEco Studio顶部菜单栏中点击View > Tool Windows > Graphics Profiler进入帧捕获页面。
3. 在帧捕获页面，可配置Ref All Resources和Verify Buffer Access两个参数，配置完成后点击Launch APP拉起应用。

  - Ref All Resources：默认关闭，在打开此选项后，抓帧时捕获所有活动资源，无论抓取的这一帧是否使用活动资源，都保存在Trace中。
  - Verify Buffer Access：默认关闭，设置校验Buffer是否可以访问。

此处为可选配置，不配置也可直接点击Launch APP拉起应用。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102126.74137343308835219767936707841027:50001231000000:2800:3D06D46FEA855BA69ACBE1A7B6C48BB54C56E8627E6A2B78053B4CDB9CF52945.png)
4. 在帧捕获界面拉起应用，成功建立连接后，Capture按钮点亮。设置抓帧数量，点击Capture按钮，等待帧捕获完成。

  - Scope：不可修改，默认为Frame。
  - Count：抓帧数量设置，范围为1-10帧。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102126.63206406412586963380124670386589:50001231000000:2800:D79C7C5C930B143809823EA459016940F1E45E040E40D70D1C143E1E755169E5.png)
5. 当抓帧完成，在下方显示界面中选择一条捕获帧，点击![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102126.57233855999222658244958265751356:50001231000000:2800:ECE0D427A8AF802D49063111B177E894281C6BB54C19EEC5D73686C7B0479BBA.png)按钮，可自动打开Graphics Profiler工具解析捕获帧信息。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102126.47954522598597012230902828954442:50001231000000:2800:0F6C8873858C3A34119120AE1428AFEDC965216496F11F229C70EDF63ABF2B05.png)说明

  - 抓帧文件名格式为：[应用包名] _ [抓帧时间] _frame [帧号].rdc。
  - Graphics Profiler工具一次只能解析一个rdc文件。
6. 若首次使用，需根据界面提示下载Graphics Profiler执行工具，并在菜单栏**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）**> Tools > Graphics Profiler**中配置工具路径。默认路径为：工具安装路径/frame_profiler/FrameProfiler.exe（macOS中为工具安装路径/Contents/macOS/FrameProfiler）。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102126.27122330685891613559852839492699:50001231000000:2800:F681FB0FB0DDCC44D18D68AC92F7521A039775960D2286D967476B1798D7A87F.png)
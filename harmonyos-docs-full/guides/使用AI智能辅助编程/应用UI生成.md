# 应用UI生成

UI Generator用于快速生成可编译、可运行的HarmonyOS UI工程，支持基于已有UI布局文件（XML），快速生成对应的HarmonyOS UI代码，其中包含HarmonyOS基础工程、页面布局、组件及属性和资源文件等。

## 使用约束

建议使用DevEco Studio 5.0.3.700及以上版本。

## 启用插件

1. 在DevEco Studio菜单栏，点击**File > Setting****s...**（macOS为**DevEco Studio > Preferences****/Settings**）**> Plugins**，在Installed列表中找到UI Generator插件，点击**Enable**启用。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101939.45753779465017585307579724418063:50001231000000:2800:C5CF46D6FB9368A969755AE541AA09219C233B1F6B9C1980F931BBE3D2133391.png)
2. 单击OK并关闭设置窗口，插件启用成功。

## 开始使用

1. 在DevEco Studio菜单栏点击**Tools > Generate Project From...**打开UI Generator工具，首次使用需要阅读并确认用户协议，确认后可继续使用。
2. 输入待配置项路径，点击**Next**进入下一步。 展开

| 待配置项 | 说明 |
| --- | --- |
| Installation package path | 待转换的APK应用包的路径，请提供未混淆的Debug版本应用包。 |
| SDK path | 等于或高于编译应用包所使用版本的SDK路径。 |
| Git Bash path | Git Bash工具存放路径。若本地已下载安装Git Bash，插件将自动获取其路径。 |

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101939.87402741516341918249199545468470:50001231000000:2800:5E7749A3E06B5ABAFE26C5042B75646CB30C1647C728FFDD4F46C9675D15DADF.png)
3. 选择将要生成的XML页面（可在搜索框进行搜索），勾选后点击向右箭头将选中的XML导入至右侧。点击**Next**开始生成。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101939.33933721754828906197174593812159:50001231000000:2800:B022780B56F7A4F63EA103DF9F0EBC07E989FCB73E580CB9FF8F9AFC288AFC09.png)
4. 配置输出工程待配置项，点击**Finish**进行生成。 展开

| 待配置项 | 说明 |
| --- | --- |
| Destination Path | 生成新工程的保存路径(默认生成到用户目录下UIGenerationProjects，用户可根据需要自行更改) |
| Compatible SDK | 生成的新工程所使用的SDK版本 |

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101939.36128008419448231566735062134531:50001231000000:2800:E6C2F18AA07A7D844C12181956387E15E1D7DBBF1CDFFD12EC5ADEBE5CF3887D.png)
5. （可选）如果所选XML无有效根节点，需要选择根节点信息。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101939.49546893763556800989569966882439:50001231000000:2800:619F535F74763366C9F50BA4B55D46928F6ADD98C52BF8823D4510045C89B557.png)
6. 点击**Finish**，在弹窗中点击确认，打开新工程。

生成的页面位于entry > src > main > ets > pages目录下，可以点击Previewer查看页面预览效果。不支持生成的组件、属性会以注释的形式给出，方便后续定位修改。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101940.43139493655757554239621410109798:50001231000000:2800:294562FADD4F79BA645D788F1FFF1AE9817AD20D92DD0B038FE4E019E29F84DF.png)
7. 生成的新工程内的entry > src > main > resources目录包含文本、图像、颜色资源。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101940.16790703967781874263175062623938:50001231000000:2800:BD53189D5CF0041AA7AE3DAD91A5B82570C56419B21BE4498ED85EBC50DCD3F3.png)

更多操作指导，请参考视频课程：[毕方HarmonyOS UI代码生成工具](https://developer.huawei.com/consumer/cn/training/course/live/C101731322888995220)。
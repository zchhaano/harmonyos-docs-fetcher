# Terminal环境变量说明

在DevEco Studio的Terminal中执行hvigor、ohpm等命令时，默认使用内置的环境变量，无需额外配置。

DevEco Studio内置环境变量的设置方式如下：

点击菜单栏**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）**> Tools > Terminal**，勾选以下选项表示开启内置环境变量。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102001.92604292242951083999406969199563:50001231000000:2800:F6A3698F888DC9EF299FEB3F74D10405A04AFBC163D212002DFB431B119A500C.png)

除了内置的环境变量外，开发者也可以在本地系统中配置PATH环境变量。如果同时配置了内置环境变量和本地系统环境变量，两者存在优先级关系，实际生效的环境变量如下。

- Windows：内置环境变量生效。
- macOS：根据使用的shell决定实际生效的环境变量。

  - 如果是bash，内置环境变量生效。
  - 如果是zsh，本地系统环境变量生效。
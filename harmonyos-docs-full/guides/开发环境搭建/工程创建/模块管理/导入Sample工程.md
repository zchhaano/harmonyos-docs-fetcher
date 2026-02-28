# 导入Sample工程

DevEco Studio支持Sample工程的导入功能，通过对接Gitee开源社区中的Sample资源，可一键导入Sample工程到DevEco Studio中。下面介绍导入Sample的方法。

## 约束与限制

### 支持的国家/地区

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

## 操作步骤

1. 在DevEco Studio的欢迎页，进入**Customize****> All Settings... > Version Control > Git**界面，单击**Test**按钮检测是否安装Git工具。

说明

在打开工程的情况下，可以单击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）进入设置界面。

  - 已安装，请根据[2](/consumer/cn/doc/harmonyos-guides/ide-import-sample#li1599692216194)开始导入Sample。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101902.27270685789517043709717950684574:50001231000000:2800:F78C7BEFAFAB8E46F79DB957D24325B65C59589434784BE192D4FAF3FF191573.png)
  - 未安装，请单击**Download and Install**，DevEco Studio会自动下载并安装。安装完成后，请根据[2](/consumer/cn/doc/harmonyos-guides/ide-import-sample#li1599692216194)开始导入Sample。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101902.47478973416843774964370108974741:50001231000000:2800:B4F67CFD44D0C09C97B244E7F9F64ABB9BAC929B4FDF44763C069252BCC6ED39.png)
2. 在DevEco Studio的欢迎页，在**Projects**页签下，单击**M****ore Action >****Import Sample**按钮，导入Sample工程。

说明

在打开工程的情况下，可以单击**File > New > Import > Import Sample**来进行导入。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101902.94137158522043211252703938337053:50001231000000:2800:67BA38DFB6A2A3FD8BCC862EE4823308BE490A83E2DA86A3836D1998A6A58CBE.png)
3. 选择需要导入的Sample工程，然后单击**Next**。
4. 设置**Project name**和**Project location**，然后单击**Finish**，等待Sample工程导入完成。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101902.13423686819574000037062490281504:50001231000000:2800:0BAA673CB6DC7441CBE55A362B553D1D4A4F34D77C5BC67C099ACC00A93AFFDF.png)
5. 导入Sample后，等待工程同步完成即可。

说明

如果网络受限，导入时会提示“Failed to connect to gitee.com port 443: Time out”连接超时错误，请[配置Git代理信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-2)。
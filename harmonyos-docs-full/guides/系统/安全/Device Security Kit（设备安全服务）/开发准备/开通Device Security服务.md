# 开通Device Security服务

在开通Device Security服务前，请先参考“[应用开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview)”完成基本准备工作，再继续进行以下开发活动。

 说明

Device Security包括应用设备状态检测、安全检测、可信应用服务、业务风险检测能力、数字盾服务，开发者请根据实际使用场景，选择开启某个或者多个能力开关。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170039.23701407922509642911935828931339:50001231000000:2800:A03F179C1870FA68AF8413AEA0015F181E93E8482376FE469F144FE5E7524047.png)
2. 在项目列表中找到需要开通Device Security服务的项目。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170039.06285150116077800019991676832390:50001231000000:2800:43D2F5A136B6F6791AA59019C74E2E790A28B037481013EDBF5F493078A37520.png)
3. 选择“开放能力管理”Tab页，找到需要使用的功能，点击左侧的按钮，开通相应的功能。

  - **应用设备状态检测**：勾选“应用设备状态检测”并点击“保存”，接入“应用设备状态检测”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170039.23278158456878905547295477863404:50001231000000:2800:06CFCD2A14A665646969F2817E02DC6385595D5C9CCB9A01F05BECD6CE4ED038.png)

  - **安全检测**：勾选“安全检测服务”并点击“保存”，接入“安全检测服务”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170039.46125532722108391114103167636505:50001231000000:2800:9F15BE6A5C35F2670543C5E035195FA7A332A705D5548E77791CC6AD83A02915.png)

  - **可信应用服务**：勾选“可信应用服务”并点击“保存”，接入“可信应用服务”。说明

开通“可信应用服务”需要先申请进入允许清单，请将Developer ID、公司名称、应用名称、申请使用的服务和使用该服务的场景，发送到agconnect@huawei.com。AGC运营将审核相关材料，通过后将为您配置受限开放服务使用的名单，审核周期为1-3个工作日，请耐心等待。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170040.25563832085454327743364859596454:50001231000000:2800:5CBFD6A48F453BD30897C7303A974C498DF08B2FAD9D13B7D41F5D38FEBD6AB3.png)

  - **业务风险检测****-涉诈剧本检测**：勾选“涉诈剧本检测”并点击“保存”，接入“涉诈剧本检测”。说明

目前“业务风险检测服务-涉诈剧本检测”仅限受邀开发者开放。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170040.87674831479261674420041329553921:50001231000000:2800:A83E32905D9EF8A4A7E86411920809DE920496895A8E84B996626173DCC705E0.png)
  - **数字盾服务**：点击“数字盾服务”右侧申请按钮，接入“数字盾服务”，审核通过后勾选对应服务并点击“保存”该服务配置。

① 在申请“数字盾服务”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](https://developer.huawei.com/consumer/cn/doc/start/edrna-0000001062678489)。

② 点击“数字盾服务”右侧申请按钮，接入“数字盾服务”，审核通过后勾选对应服务并点击“保存”该服务配置。

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170040.65665856307539871720863679588531:50001231000000:2800:E68D24556DD362687CDBF55CD1C9C17E2527B1BADD6C5B9F5B7594B0FEB73BA0.png)说明

请您在申请框填写“数字盾服务”申请原因和应用场景。AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。
4. 申请Profile（.p7b）文件，具体操作请参见[申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)。

说明

在开通服务后，需要重新申请Profile（.p7b）文件。
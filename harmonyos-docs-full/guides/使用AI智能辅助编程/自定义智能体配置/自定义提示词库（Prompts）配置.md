# 自定义提示词库（Prompts）配置

 

从DevEco Studio 6.1.0 Beta2开始，CodeGenie支持添加和管理提示词库。如果经常针对不同的文件或代码使用某个提示词向AI提问，可以将提示词添加到常用提示词库中，在需要时通过菜单栏快速触发，从而提高开发效率。

 

 

1. 点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下两种方式打开Prompts配置界面：

  - 点击界面右上方**Settings**![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/YOYOvsiOQL-ekaaiwyfhhw/zh-cn_image_0000002561753075.png?HW-CC-KV=V1&HW-CC-Date=20260420T193623Z&HW-CC-Expire=86400&HW-CC-Sign=032EFFDEB3491B385D23EBA3F19BCDD5084D8F302020ABA4C8C952E80F723AE6)按钮，选择**Prompts**。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/L_zdzwmLRFSZ-YQGipEA_g/zh-cn_image_0000002544580918.png?HW-CC-KV=V1&HW-CC-Date=20260420T193623Z&HW-CC-Expire=86400&HW-CC-Sign=6485E5E3DEE0CAD09CBC9138225B5D294A2ABA8026916B828221E1FE68D9E1E2)
  - 在代码编辑区右键唤醒菜单栏，点击**CodeGenie > Add New Prompts**。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/yIjNqeSZQoaoZ1-1X2k0lQ/zh-cn_image_0000002530753148.png?HW-CC-KV=V1&HW-CC-Date=20260420T193623Z&HW-CC-Expire=86400&HW-CC-Sign=068CF21DD2BC9738C161B8CA837453BBBAC53F8F5A06471DB1074E2EB25D918B)
2. 点击**Add Now**进入Prompts配置页面。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/KYch_JLsQ2mVDwYncqaW7Q/zh-cn_image_0000002544421564.png?HW-CC-KV=V1&HW-CC-Date=20260420T193623Z&HW-CC-Expire=86400&HW-CC-Sign=F66E5666672A4444375198BF15F66FE7E43B5576647A8F21F6502EF1C8291E32)
3. 填写提示词名称、提示词内容等，点击**Save**进行保存。

  - **Title**：提示词名称，长度不超过20个字符。
  - **Prompt**：提示词的具体内容，长度不超过5000个字符。
  - **Auto-reference selected code for context**：是否自动引用所选代码作为上下文，勾选该选项后，会将选中代码和提示词一并发送给CodeGenie。
  - **Auto send prompts to AI**：是否自动发送给CodeGenie，不勾选该选项时需手动点击![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/o_6H2-6ER7mTpnKv6UTAKw/zh-cn_image_0000002561833061.png?HW-CC-KV=V1&HW-CC-Date=20260420T193623Z&HW-CC-Expire=86400&HW-CC-Sign=AAB78D900C66C349195088940C9C5581E5577390B0FBEFD467E3CE3A37C8AC79)发送。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/QPu-jGrpQkyRonYQ0ZfMpA/zh-cn_image_0000002575102649.png?HW-CC-KV=V1&HW-CC-Date=20260420T193623Z&HW-CC-Expire=86400&HW-CC-Sign=96E74649AD4A0D5F55A4CB0490C1A4747EFA607D1917FCFDB04065F1B7750BBF)

 

将鼠标悬浮在自定义Prompts上，可出现编辑和删除按钮，方便开发者编辑或删除。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/cKv_qBEwTDCBjADJQ1SxYA/zh-cn_image_0000002544583224.png?HW-CC-KV=V1&HW-CC-Date=20260420T193623Z&HW-CC-Expire=86400&HW-CC-Sign=1670ADE9D8600F356AABE8819F5A1625FDFF97E8E66CCB8C6B629C6FC1ED2E4E)
4. 选中代码片或在编辑区空白位置右键，点击CodeGenie下的提示词（如安全检查），发送提示词后等待AI解析回复。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/BkM4_JQDQqm3LCQPh2ywmQ/zh-cn_image_0000002530753146.png?HW-CC-KV=V1&HW-CC-Date=20260420T193623Z&HW-CC-Expire=86400&HW-CC-Sign=70EE7BF920E19CCE6E8CB90B949901BF084A8DC4D3E6345BA41C0B17E71FE9DD)
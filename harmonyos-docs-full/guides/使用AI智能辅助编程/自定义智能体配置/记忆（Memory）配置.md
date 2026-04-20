# 记忆（Memory）配置

 

#### 功能介绍

CodeGenie搭载长期记忆功能，在应用开发过程中，会学习和提取个人偏好、项目细节等有价值的信息，进行主动记忆或自动记忆。伴随开发者的持续使用，逐步形成覆盖开发者信息、项目场景、问题沉淀的全域记忆体系。在长期交互中，记忆也会随时间更新。

 

依托这一核心能力，CodeGenie能够精准理解和生成符合开发者需求的代码、回答等，与开发者实现更高效的协作。

  

#### [h2]基本概念

- 主动记忆：开发者要求CodeGenie记住输入的内容，CodeGenie会保存这些信息。
- 自动记忆：自动提取对话中有价值的信息，记录任务执行进度，随时间推移学习开发者的编码风格和项目细节等。

  

#### [h2]使用约束

- 当前仅自定义Agent支持长期记忆检索和生成。
- 当CodeGenie记忆与[规则（Rules）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-rules)发生冲突时，以规则为准。

  

#### 操作步骤

1. 点击界面右上方**Settings**![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/M4TTIM9tSYuDNktrANYDxA/zh-cn_image_0000002530913008.png?HW-CC-KV=V1&HW-CC-Date=20260420T193623Z&HW-CC-Expire=86400&HW-CC-Sign=7FFC38F8B28A7F33CFB1EE5744BE246CDD198B24E6595A6BD00BC065E8AA4C87)按钮，选择**Memory**，进入配置页面。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/lWZKOcl0Tm67yENJ7L6UaQ/zh-cn_image_0000002544419464.png?HW-CC-KV=V1&HW-CC-Date=20260420T193623Z&HW-CC-Expire=86400&HW-CC-Sign=3F17DF8181553AC6D0505509D76C33310F5322F2A561C98432E07D958FB7D2CC)
2. 点击Memory后开关，开启和关闭记忆。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/8vxYmZ0zSKKOV2rKJG-w_Q/zh-cn_image_0000002574940769.png?HW-CC-KV=V1&HW-CC-Date=20260420T193623Z&HW-CC-Expire=86400&HW-CC-Sign=12EB7F1E047C101B3BB4029512A74A5CAD1E79FE0CC751A1B8B0A1A6D299AE82)
3. 在**Memory List**（记忆列表）下展示所有记忆，包括**Global**（记录用户相关信息）、**Project**（记录项目相关信息）。将鼠标悬浮在记忆上会显示具体信息，以及出现编辑、删除按钮，方便开发者管理记忆。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/8s-EUOTxShufdOjAKQJrwg/zh-cn_image_0000002547833062.png?HW-CC-KV=V1&HW-CC-Date=20260420T193623Z&HW-CC-Expire=86400&HW-CC-Sign=67DC8EE5D6B2FF44BBC423E9E56D222EC51EF2F0D0D076C39CF698BC50B7C64C)
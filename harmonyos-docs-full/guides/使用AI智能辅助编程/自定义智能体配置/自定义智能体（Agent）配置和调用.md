# 自定义智能体（Agent）配置和调用

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持用户添加模型和自定义Agent，增强AI问答能力，提升AI辅助编程和分析能力。

从DevEco Studio 6.0.2 Beta1开始，Agent配置时支持开启DevEco Studio内置工具Built-in Tools、Auto Run和Blocklist。

## Agent配置

1. 点击界面右上方**Settings**![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101946.60831845952138575236465522988683:50001231000000:2800:0D53001432CF177DE3E30FFEF4C63FBD3A9BFF5E7965ED185F2B9E53249EFFEA.png)按钮，选择**Agent**；或者在输入框左下角下拉框选择**Create Agent**，进入配置页面。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101946.51646110557014126302659544588058:50001231000000:2800:B2C7D220E9F798EC1FCEAA0C1ECC96E76AF75FCB1F5CB37048C108D800A0083F.png)
2. 点击![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101946.33728573631193541053135898935111:50001231000000:2800:11BE829FC69A796FF2622DBCE4C925FEE3EAA43A81060AB76DADB962DC39F075.png)按钮，填写自定义Agent的相关信息。点击**Add**，将创建自定义Agent。

  - **Name**：必填，自定义Agent的名称。
  - **Prompt Description**：可选，自定义Agent的提示词。
  - **MCP Tools**：可选，添加MCP工具，具体请参考[MCP配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-mcp)。
  - **Built-in Tools**：可选，DevEco Studio内置工具，包括File Manager、Terminal、Compile and Build。File Manager开启后，支持读写本地的代码文件；Terminal开启后，在CodeGenie对话框执行命令时可自动拉起Terminal终端；Compile and Build开启后，支持编译与构建项目。默认开启。
  - **Select Model**：必填，选择需要使用的模型，具体请参考[模型（Model）配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-model)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101946.95823882148261261470857311386402:50001231000000:2800:AE128BD4407D97EB45040FC5B62FA54D005A1406B64B5FD1753F9F115B1B7896.png)
3. 在**All Agents**下展示所有智能体。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101946.24864409262053555679012904895216:50001231000000:2800:8B3CD7E3733C6CB8B8E5F4B2C7DC813E409158F311CFA6DDE0303852DD2A7C8E.png)
4. 设置**Auto Run**和**Blocklist**。

  - Auto Run：Agent工具被调用过程中自动执行开关。开启时，MCP或hdc等工具被调用时可自动执行和输出内容；关闭时，MCP或hdc等工具被调用时需开发者授权。默认关闭。
  - Blocklist：开启Auto Run后，在调用命令行工具执行命令时，在Blocklist中的命令不会自动执行。点击命令后×，可将命令从Blocklist中删除；在Enter Command中输入命令，点击Add，可将命令添加至Blocklist列表。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101946.12077616888653311687800324966296:50001231000000:2800:5E1BDF9046B05E2AC8FE266C15DE6C28ABFCF350FDB09ED22FD93A6630C624CB.png)

## Agent调用

1. Agent配置完成后，可以通过如下两种方式开启调用：

  - 在对话区域输入"/"调出命令，选择自定义的Agent（如**figma2code**）。
  - 在输入框左下角HarmonyOS Ask处下拉框中选择自定义的Agent（如**figma2code**）。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101946.41354144248317586613751840520853:50001231000000:2800:7E4FDA115F941EE31947F5539165307A6726771DD9AF1A2D701A61B34F7FCDC9.png)
2. 选择自定义Agent后，在右侧可以切换模型，默认使用配置Agent时添加的模型。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101946.26500258110240470257284145777400:50001231000000:2800:C54DAACC165CC471872319FCEB185AE75691FC42181288B7502C634A8DCC38FD.png)
3. 根据业务需要，进行智能问答、代码生成、代码智能解读等，CodeGenie将会调用自定义Agent和选择的模型生成内容。
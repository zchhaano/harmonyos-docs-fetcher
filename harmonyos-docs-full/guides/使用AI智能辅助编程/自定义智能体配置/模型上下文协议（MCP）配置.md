## 功能介绍

模型上下文协议（Model Context Protocol，简称MCP）是一种开放协议，允许大型语言模型（LLMs）访问自定义的工具和服务，可以通过部署MCP Server并将其集成到自定义智能体中来使用。关于 MCP 的更多信息，请参考 [MCP 官方文档](https://modelcontextprotocol.io/introduction)。

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持配置MCP。

## 环境约束

为保证MCP Server正常启动，需要安装npx和uvx，并配置到环境变量。

- npx：依赖于Node.js，建议使用Node.js的LTS版本。
- uvx：基于Python的快速执行工具，建议安装Python 3.9 以上的版本。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标，完成登录后。点击界面右上方**Settings**![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101943.73139027407185235897971712640404:50001231000000:2800:29C3400CAA3B3B31E9CAF3B468ED58191ADC5C2021AD062DB08EBA4C17AD813F.png)按钮，选择**MCP**，进入配置页面。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101943.81594674445109664141493834375950:50001231000000:2800:401DBABCD7A6293159FE85CEB8D2CEEC163A9B1963D94BE95AB693DA064AA6FC.png)
2. 点击![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101943.61549996774663818793197651761944:50001231000000:2800:0128C3A905790F5C75C24E8C4DEBC72CDACF2F6CB144BC7BE0BA4D4D4685C714.png)按钮，添加MCP工具。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101944.53349901496488424537359600594420:50001231000000:2800:54D7C4711A28683390E3FA0D2DF88229B0C0E55E46D82016DC8B5602F619417E.png)
3. 在编辑框中填写MCP工具的配置信息，填写完成后点击**Add**。

说明

MCP  Server支持三种通信方式：Stdio 、Server-Sent Events (SSE) 和Streamable HTTP。

Stdio方式支持配置cmd、args和env字段，SSE和Streamable HTTP方式支持配置url字段。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101944.63899188302332948222398510654949:50001231000000:2800:0CFFD374E3D3C194367666CDDEA9163B6FA4F1247F3171C821CA723EC747273C.png)
4. 在**MCP Tools**列表中，展示所有MCP工具信息，包括名称、连接状态、启用状态。同时，将鼠标悬浮在工具上会显示三个操作按钮：刷新、编辑和删除，方便开发者管理工具。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101944.09710533506674991599922767016289:50001231000000:2800:6C722898B3FDA243458F7520C58C5CFDA119B5E48DF0DD3315A5F77ED48E5485.png)

  - 名称：MCP工具名称，如context7、Time。
  - 连接状态：工具连接状态，包括“成功”、“失败”和“连接中”三种状态。
  - 启用状态：工具是否已启用。
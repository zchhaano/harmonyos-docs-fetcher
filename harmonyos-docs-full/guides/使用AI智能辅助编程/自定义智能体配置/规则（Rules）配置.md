# 规则（Rules）配置

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持用户配置规则（Rules）。在自定义智能体模型下，智能问答时可生成更加符合Rules规范的代码。规则包括全局级别规则（Global Rules）和工程级别规则（Project Rules）。

**Global Rules**：支持开发者自行导入规则文件（Custom rule），或使用默认规则（Default rule），或不使用规则（No rules）；规则与用户绑定，对当前用户下所有工程生效；支持添加多个自定义规则，添加后可选择是否生效。

**Project Rules**：需开发者自行导入或创建规则；规则仅对当前工程有效；仅支持添加一个自定义规则，添加后即生效。

 说明

- 规则文件：扩展名称为.md的Markdown文件，.md文件中仅二级标题及以下的规则内容生效。
- 默认规则（Default rule）需联网使用，无网络或网络故障时用户可选择Custom rule或No rules。

## Global Rules配置

1. 点击页面右侧菜单栏CodeGenie图标，完成登录后。点击界面右上方**Settings**![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101945.59332656548059281539098884556950:50001231000000:2800:9FD94900840B6813C908115E7A641DC975E9ECC2999B29BEC43E3361F4399575.png)按钮，选择**Rules**，进入配置页面。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101945.88509935835569039746380167049175:50001231000000:2800:A398BDF9F8044FE59D66F88970C06DECA63B42E938DFCA3826FFBE7C64984F48.png)
2. 以有网络为例，点击![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101945.15476028823876426684162621602429:50001231000000:2800:F9CC77A41150A33072B47A950D7A1B79ACE19EC8E05F366FBD8DB7A467442157.png)图标导入规则文件。无网络时操作界面可能存在差异，以实际为准。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101945.62471144885074125534353028756496:50001231000000:2800:F0459DD0E18F64D7127F49C95E1A96A9A821DFADA354F68AE58E232035621FFB.png)
3. 选择和管理规则文件。Global Rules列表全量展示了默认规则、自定义规则和无规则，当前仅支持选择其中一个规则。若选择No rules，则全局规则不生效。

  - 将鼠标悬浮在默认规则上，点击![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101945.95324728899209409926017082463402:50001231000000:2800:E2C96ED6578653860B5FBCA65D472305DF42B006FEE5E8AA3F01AF8192DFA7EB.png)编辑图标，开发者可查看具体规则内容。
  - 将鼠标悬浮在自定义规则上，会出现编辑和删除按钮，方便开发者管理自定义规则。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101945.03810838594840901957494395459787:50001231000000:2800:03A3E223BA110204A345592F2F5B8D31FBB1053317887F71736F55C4987C3AC3.png)

## Project Rules配置

1. 点击页面右侧菜单栏CodeGenie图标，完成登录后。点击界面右上方**Settings**![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101945.73504365308227863233662354510144:50001231000000:2800:DF50E43A6261B9000BFBCC059B05A6C82072E51D5804637D68E8AE83E843661E.png)按钮，选择**Rules**，进入配置页面。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101945.86545884914447252823788918355839:50001231000000:2800:F4649028A29B870CFD97FEB46E84888515B4CBE323384A6A1FC053ADF9929E76.png)
2. 创建或导入Rule文件。

  - 创建Rule文件方法：点击**Create Rule**，工程目录中会新增/.codegenie/project_rule.md文件，在project_rule.md文件中输入规则内容。
  - 导入Rule文件方法：点击**Import Rule**，工程目录中会新增/.codegenie/project_rule.md文件，project_rule.md文件内容即为导入的规则文件内容。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101945.43257635501788659511979617603488:50001231000000:2800:6C25530D1DC1BD0C340142C4BC093273B86ABDD464CFD8FC09B28AF11384895A.png)
3. 管理规则文件。将鼠标悬浮在工程文件上，会出现编辑和删除按钮，方便开发者管理工程规则文件。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101945.99082453948207507668506599767498:50001231000000:2800:20A7AA04881ADAAB28DDCE98F07CDB17AE69217468C90AD11D6A2FF1972EC9AD.png)
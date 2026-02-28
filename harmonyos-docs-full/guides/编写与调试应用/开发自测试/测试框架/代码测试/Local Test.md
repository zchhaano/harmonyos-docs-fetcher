# Local Test

说明

当前不支持测试C/C++方法及系统API。

## 创建Local Test测试用例

1. 在工程目录下打开待测试模块（支持HAP、HAR、HSP模块）下的ets文件，将光标置于代码中任意位置，单击**右键 > Show Context Actions****> Create Local Test**或快捷键**Alt+Enter****（macOS为Option+Enter） > Create Local Test**创建测试类。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102036.49120482709165482784340134893701:50001231000000:2800:3D27FD83B6EA681F54FF2B45FE837E58D182692E9EA9BBE54F982ECFE7467D5A.png)
2. 在弹出的Create Local Test窗口，输入或选择如下参数。

  - **Testing library**：测试类型，默认为DECC-ArkTSUnit。
  - **ArkTS name**：创建的测试文件名称，测试文件中包含了测试用例。测试文件名称要求在工程目录范围内具有唯一性，仅支持字母、数字、下划线（_）和点（.）。
  - **Destination package**：测试文件存放的位置，建议存放在待测试模块的test目录下。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102036.11264980798550263595572361494791:50001231000000:2800:91D0DFA61D50D5397BC95B9E2F7A71BFDE4AE963D0AC2C64CC7DB48847419824.png)
3. DevEco Studio在test目录下自动生成对应的测试类。在测试类中，DevEco Studio会生成对应方法的用例模板，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[单元测试框架](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unittest-guidelines)。

说明

您也可以手动在test文件夹下创建测试用例，手动创建后，需要在List.test.ets文件中添加创建的用例类。

## 运行Local Test测试用例

### 运行模式

可以采用运行工程目录（test）、测试文件（如Index.test.ets）、测试套件（describe）、测试方法（it）的方式来执行Local Test，各级别测试执行入口如下。

|  |  |
| --- | --- |
| 目录级 | 文件级 |
|  |  |
| 套件级 | 方法级 |

以文件级别为例，在工程目录中，选中文件，单击**右键 > Run'测试文件名称'**，执行测试。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102036.30350460358240776552454871580287:50001231000000:2800:7BEB2BA32730D5ACCF08FD115083C5E313149C6D02758AC33FBC83D44B93E59B.png)

 也可以通过如下方式，执行Local Test：

- 在工具栏主菜单单击**Run > Run'测试名称'**。
- 在DevEco Studio的右上角，选择一项测试任务的配置，然后单击右侧的![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102036.93612626386187754334006512178647:50001231000000:2800:7D5614E96D99DB86E928A1F79CA2D0E5C2A4CB1BAA6A9AF871D1FB9EB9D3C5F0.png)按钮，执行Local Test。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102036.01462063591489183523537007162099:50001231000000:2800:861D3237550012F06A498C4354E4E329F55CB9DD12DF467F80E6BFBF75616A8D.png)

执行完测试任务后，查看测试结果。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102036.03301064538025822228513123939740:50001231000000:2800:FB2D4AEFBCD87EA3D43A8EB7D94078FDEB2B86F0DE0E5658EC24DAF639AE021D.png)

### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击**右键 > Debug'测试文件名称'**，以调试模式执行测试任务。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102036.59933408019606513933504339181943:50001231000000:2800:1F721F5948713F60C5DAC7A7AB47C58667744138ACC59D40B40ADF40B2DEEF44.png)

在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102036.59565804284585520504486211244926:50001231000000:2800:51D724BAC5FA2A7A4BEF461BE2E9CB19B2289F9A179F9EF9BFDF180FB7F9A0B0.png)

断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102036.00820874269606519226262197310907:50001231000000:2800:6B192D3995AC339C8FB78F59168319EAEA6C0ADFCF2F45DDEAC699ACEFCE8840.png)

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102036.24723657088650615262723965873848:50001231000000:2800:F914C97286632A78ADD5A97163707D497DEC2098DA2E43A2D432FEFF01F92E1E.png)

### 覆盖率统计模式

在LocalTest运行的基础上支持代码覆盖率统计，当前仅支持ArkTS工程。

开发者可以自定义需要参与覆盖率测试的文件，具体配置方法请参考[配置覆盖率过滤文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section13756446154)。

如前所述，覆盖率统计模式也有多级别入口，以文件级别为例，有两种方式启动测试：

- 方式一：在工程目录中，选中文件，单击**右键 > Run '测试文件名称' with Coverage**，以覆盖率统计模式执行测试任务。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102037.83932951541511310133492252070955:50001231000000:2800:BFA4D8ACBF345BB5728A78249473C861024672A5C5A1ABE5412BA0D23D3A9D91.png)

- 方式二：在DevEco Studio的右上角，选择测试任务，然后单击右侧的![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102037.15508442880976010069822851695630:50001231000000:2800:5CAAE17E71355107FA27B0C13AEC2D0BA4F7D49CFDD0878A10B8FE40077D8C24.png)按钮，执行测试。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102037.84844577203793413722706984382051:50001231000000:2800:0DB49E3F5DD5EF24348026B0E3ACC30ADCB2CF24C91D14B1AD02641C3F265FBD.png)

启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102037.52868953527973397371425659519780:50001231000000:2800:217C373D86D05F3D205BC9A601F1E6B612C38363A5DD2D22338FD3DCB65657F8.png)

点击链接可打开报告，查看代码覆盖率详情，关于覆盖率的计算方式请参考[查看覆盖率报告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section10394362109)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102037.43141949986902226195045893581424:50001231000000:2800:7D83B6EC35473C0C2723A0AC18F35562BA806C17B98777B4D8C389039C604D3F.png)

在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102037.76509038667681700096178039146016:50001231000000:2800:B6DD11FC123A0ECCB0026001EBACB7D731124B7D32EDA2C9CB6578D3D9F4D360.png)

## （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行。如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1. 在工具栏主菜单单击**Run**>**Edit Configurations**，进入Run/Debug Configurations界面。
2. 在**Run/Debug Configurations**界面，单击**+**按钮，在弹出的下拉菜单中，单击**Local Test**。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102037.02308913826422585191460022886083:50001231000000:2800:C66282B962D985E0587F8E17B6F0E6C48AFA13038D4594FB36C998DCEF9A63E5.png)
3. 根据实际情况，配置Local Test的运行参数。 然后单击**OK**，完成配置。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102037.33508633172302624502706418337398:50001231000000:2800:0937D55B708862877914BB408BE1E49ABB75B2F5BCD3C2BBC80482C4F3C538BA.png)

## 使用命令行执行Local Test

通过命令行方式执行Local Test，在工程根目录下执行命令：收起自动换行深色代码主题复制

```
hvigorw test -p module={moduleName} -p coverage={ true | false } -p scope={suiteName} #{methodName}
```

- module：执行测试的模块。缺省默认是执行所有模块的用例。
- coverage：是否生成覆盖率报告，缺省默认是true，在<module-path>/.test/default/outputs/test/reports路径下生成两份报告，一份是html格式（index.html），一份是json格式（coverageReport.json），具体参考[查看覆盖率报告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section10394362109)。
- scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。

 说明

- 多个module和scope之间用英文逗号隔开。
- 暂不支持在Linux上执行该命令。

测试结果文件：<module-path>/.test/default/intermediates/test/coverage_data/test_result.txt
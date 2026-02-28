## 创建ArkTS测试用例

### 创建默认测试用例

1. 在工程目录下打开待测试模块（支持HAP、HAR、HSP模块）下的ets文件，将光标置于代码中任意位置，单击**右键 > Show Context Actions****> Create Instrument Test**或快捷键**Alt+Enter****（macOS为Option+Enter）> Create Instrument Test**创建测试类。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102032.30631903564625244628044481385628:50001231000000:2800:5119809B45B167620C9555944029F9D58F213434093832967EA430A4C50502C0.png)
2. 在弹出的Create Instrument Test窗口，输入或选择如下参数。

  - **Testing library**：测试类型，默认为DECC-ArkTSUnit，JS语言默认为DECC-JSUnit。
  - **ArkTS name**：创建的测试文件名称，测试文件中包含了测试用例。测试文件名称要求在工程目录范围内具有唯一性，仅支持字母、数字、下划线（_）和点（.）。
  - **Destination package**：测试文件存放的位置，建议存放在待测试模块的test目录下。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102032.68840100389898895901015848419570:50001231000000:2800:256591897128AC098CF825A283CCF122358D5DC875B2D913F8274B1FAE75BE22.png)
3. DevEco Studio在ohosTest/ets/test目录下自动生成对应的测试类。在测试类中，DevEco Studio会生成对应方法的用例模板，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[自动化测试框架使用指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkxtest-guidelines)。

说明

  - 您也可以手动在ohosTest > ets > test文件夹下创建测试用例，手动创建后，需要在List.test.ets文件中添加创建的用例类。手动创建的工程或历史工程，ohosTest > ets > test文件夹下所有文件的文件名必须以.test.ets结尾，否则将在运行时弹窗提示“Error: Test files must end with '.test.ets'.”请点击**Fix**按钮，DevEco Studio将自动对ohosTest > ets > test目录下的文件名进行修改。
  - 首次在HarmonyOS设备上运行UI测试框架需要使用命令“hdc -n shell param set persist.ace.testmode.enabled 1”使能UiTest测试能力。

### 自定义Ability和Resources

从5.0.3.403版本开始，新创建的工程/模块的ohosTest目录下默认不创建testability、testrunner和resources目录，历史工程仍保留这些目录，如果新工程需要使用ability或resources能力，需要开发者自行创建。

 说明

如果需要使用ability能力，需要同时创建testrunner目录及OpenHarmonyTestRunner.ets文件。

  **表1****新旧版本ohosTest目录对比**

| 新版本 | 历史版本 |
| --- | --- |
|  |  |

1. 创建以下目录或文件，文件内容示例可在[运行Instrument Test测试用例](/consumer/cn/doc/harmonyos-guides/ide-instrument-test#section1574003717165)后，在对应模块的build/{productName}/intermediates/src/ohosTest下查看，其中productName是当前生效的product，可以通过点击DevEco Studio右上方![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102032.92800578937931784058262576121350:50001231000000:2800:DD8E45F7B7C61C9C35095B40E0347BD0856BDC7AAB4AF8876352BCBA554E704B.png)图标进行查看。

  - testability目录 > TestAbility.ets文件
  - testability目录 > pages目录 > Index.ets文件
  - testrunner目录 > OpenHarmonyTestRunner.ets文件
  - resources目录 > base目录 > element目录 > color.json文件
  - resources目录 > base目录 > element目录 > string.json文件
  - resources目录 > base目录 > profile目录 > test_pages.json文件
2. 在module.json5文件中补充ability配置字段mainElement、pages、abilities，关于字段的具体说明请参考[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)。

收起自动换行深色代码主题复制

```
{ "module" : { "name" : "entry_test" , "type" : "feature" , "description" : "$string:module_test_desc" , "mainElement" : "TestAbility" , // 对应下方abilities中的ability name。 "deviceTypes" : [ "phone" , "tablet" , "2in1" ], "deliveryWithInstall" : true , "installationFree" : false , "pages" : "$profile:test_pages" , // 对应resources目录 > base目录 > profile目录 > test_pages.json文件。 "abilities" : [ // 添加的ability的配置信息。 { "name" : "TestAbility" , "srcEntry" : "./ets/testability/TestAbility.ets" , "description" : "$string:TestAbility_desc" , "icon" : "$media:icon" , // 确保引用的资源都存在 "label" : "$string:TestAbility_label" , "exported" : true , "startWindowIcon" : "$media:icon" , "startWindowBackground" : "$color:start_window_background" } ] } }
```

## 运行测试用例

### 运行模式

使用DevEco Studio运行测试用例前，需要将设备与电脑进行连接，将工程编译成带签名信息的HAP，再安装到真机设备或模拟器上运行，具体请参考[使用本地真机运行应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-device)或[使用模拟器运行应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-emulator)。

 可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来运行测试用例：

- 在工程目录中，单击**右键 > Run'测试文件名称'**，执行测试。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102032.35463626156989389895846937652579:50001231000000:2800:64D33175FC6D3BD717F94EBF0F22CBE1ACE7B870E627B693DDF170D271A71136.png)
- 打开测试文件，单击测试套件左侧按钮。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102032.11308849226182991227025619336773:50001231000000:2800:5E94282FC69059FC8130EFFCC39723CB26397E93579981AD2CAB01B6C89FE58A.png)
- 如果要根据自定义的配置执行Instrument Test，在[创建测试用例运行任务](/consumer/cn/doc/harmonyos-guides/ide-instrument-test#section65264166107)后，通过如下方式的其中之一，执行Instrument Test：

  - 在工具栏主菜单单击**Run > Run'测试名称'**。
  - 在DevEco Studio的右上角，选择测试任务，然后单击右侧的![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102032.60575766970010470845539448647053:50001231000000:2800:1A4C0D9EB040EE47EA81CD99BEE7ECC92D1008ECBDDEEFF8D872EED1A258D268.png)按钮，执行Instrument Test。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102032.79253468610042396361464133182693:50001231000000:2800:FB1150E19FDED2D9ADCD54AD9ED09EABFEA18C5BAFF9BF7B4179FD460B850367.png)

执行完测试任务后，查看测试结果。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102032.32299078093896509535977731653549:50001231000000:2800:287ACFFFF4C9FEE9C92DEC00D0076E1C11E3178AEFC8B8EAC49BFDBBCDD64182.png)

### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击**右键 > Debug'测试文件名称'**，以调试模式执行测试任务。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102032.85449718153094248871969085980619:50001231000000:2800:06B18CF4AC3CF23550DEEC659014DF3F234775F6ABCF811D41A8A76A98B76A43.png)

在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.70245908900441218709093631103545:50001231000000:2800:9B13C85F87C78940A0813B188264D41701810660016007D7F7EF39160AC623D8.png)

断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.49295127010161843252616335330891:50001231000000:2800:FC7247D4921FE0200BCEAA41C63B2F7237F2DF41DA331F16E0E6ECBE563F7F0F.png)

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.60695219969634990414779793876124:50001231000000:2800:094A0EEA8BF7AE0CBC0FC393AC7BEC29ABC78D217A235B5F6B8DE04D63313819.png)

 说明

DevEco Studio支持设置调试代码类型，具体请参考[设置调试代码类型](/consumer/cn/doc/harmonyos-guides/ide-instrument-test#section0164586312)。

### 覆盖率统计模式

在Instrument Test运行的基础上支持代码覆盖率统计。

开发者可以自定义需要参与覆盖率测试的文件，具体配置方法请参考[配置覆盖率过滤文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section13756446154)。

可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来启动代码覆盖率的统计。

以文件级别为例，有两种方式启动测试：

- 方式一：在工程目录中，选中文件，单击**右键 > Run '测试文件名称' with Coverage**，执行测试。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.80517411775643425931290783206634:50001231000000:2800:2ABB30235541189932DC4A7F0333F1ACF2052029EA031B83C72B9A5DEB88DF44.png)
- 方式二：在DevEco Studio的右上角，选择测试任务，然后单击右侧的![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.01019456924805762373599052469092:50001231000000:2800:022DC6F217FC8AB9E1C11A6DAA154751A68AC91B1C4C98DD50544945C1A98502.png)按钮，执行测试。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.19211954734220521349989616668038:50001231000000:2800:623721EAB65C92C119EBC26342EA77216C2522F6DEE50A51F46F7E2C5DA0620F.png)

启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.70379639294483092530552795032940:50001231000000:2800:ADA6862B2F47285449257AC4ACCBF3D34F2DC45CFE9A84B45D380FFC50C765B4.png)

点击链接可打开报告，查看ArkTS代码覆盖率详情，关于覆盖率的计算方式请参考[查看覆盖率报告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section10394362109)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.78295976415519463785514153131105:50001231000000:2800:B7D451ABE9D886FC1687073482DA4973B8B2E303D02A26B8296842B433269E50.png)

在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.12257649442112944843587315553860:50001231000000:2800:49B03306E47B1824A593946F480FBA7F19F7D0C607CAAD0AD5A4EF460DB01CB6.png)

## （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行，如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1. 在工具栏主菜单单击**Run** >**Edit Configurations**进入Run/Debug Configurations界面。
2. 在**Run/Debug Configurations**界面，单击+按钮，在弹出的下拉菜单中，单击Instrument Test。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.33439974188643747325031718422817:50001231000000:2800:18251B710AE5C788F4C677CE3AAE2DDF29A3429CA40B94C71CA4E0E9C4606CF4.png)
3. 根据实际情况，配置Instrument Test的运行参数。然后单击**OK**，完成配置。

  - 如果模块依赖共享包，请提前设置HAP安装方式，勾选“**Keep Application Data**”，则表示采用覆盖安装方式，保留应用/元服务缓存数据。
  - 如果工程中HAP/HSP模块直接依赖其他HSP模块（如entry模块依赖HSP模块）或间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块）时，在测试阶段需要同时安装模块包及其所有依赖模块的包到设备中。此时，可以勾选“**Auto Dependencies**”，测试时会自动将所有依赖的模块都安装到设备上。该选项默认勾选。
  - 如果不涉及UI测试，勾选“**Only OhosTest Package**”，则只会推送OhosTest测试包到设备上，不会推送HAP/HSP包，可以缩短推包时间。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.56301308770655339991189351479680:50001231000000:2800:6D3AB13A27FB5868A611C90FCB429A3B43BDE86A0EE802F3DF10D07C2FEAB1E5.png)

### 使用过滤条件筛选待运行的测试用例

1. 在用例编写时，通过配置it的第二个入参，为每个用例添加过滤参数。此参数用于为测试用例添加标注，不添加则参数默认为0表示未被标注。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.96659666388908473175680796646635:50001231000000:2800:457BA3A5D6604715C48F9E55726F52D371B227230C7078281EABB96305AE24C9.png)
2. 打开**Run/Debug Configurations**窗口，点击Test Args![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.82277225559447361896502725458121:50001231000000:2800:AE291E2D3A20E8D3D5F116E8F0212EFC60AD18DDE86FAA3F0286E3A589A4D325.png)，打开**Test Args**界面，添加命令行参数。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.77583565225621890791898088434185:50001231000000:2800:A9385496CCD5D26163C955842D39C126541FDDA5DC577391342EC42B4AD2BF70.png)

例如将测试参数配置为level=1, size=medium

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.14957519653049682429945247166223:50001231000000:2800:0D8B01C201CD0906F114DCD1A7482218E07AD28393DC5BE5D2D7071D338DFE4A.png)

  **表2**参数规则参考展开

| Key | 含义说明 | Value取值范围 |
| --- | --- | --- |
| level | 用例级别 | "0","1","2","3","4", 例如：-s level 1 |
| size | 用例粒度 | "small","medium","large", 例如：-s size small |
| testType | 用例测试类型 | "function","performance","power","reliability","security","global","compatibility","user","standard","safety","resilience", 例如：-s testType function |
3. 完成以上配置后，在运行此项配置对应的测试任务时，只运行过滤后的测试用例。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102033.83672202317201570620958696196852:50001231000000:2800:911A72C52AA3F4742D6C5CF55511D45B79BE15F0D999F8E72B9CA6E87DE07025.png)

### 设置调试代码类型

点击**Run > Edit Configurations**，打开**Run/Debug Configurations**窗口，选择Instrument Test，点击**Debugger**页签，设置Debug type。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102034.17607973097604903712381157995937:50001231000000:2800:E2D27D9AA21D72F167A6C119DE84864F3C5B4747F80367C057A0970506F47C9B.png)

调试类型Debug type默认为Detect Automatically，关于各调试类型的说明如下表所示：

 展开

| 调试类型 | 调试代码 |
| --- | --- |
| Detect Automatically | 自动检测。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。 如果检测到是Native模块，出现两个调试窗口（PandaDebugger、Native）；如果不是Native模块，只出现PandaDebugger调试窗口。 |
| ArkTS/JS | 只调试ArkTS/JS，只出现PandaDebugger调试窗口。 |
| Native | 单独调试C++，只出现Native调试窗口。 |
| Dual(ArkTS/JS + Native) | 支持ArkTS/JS和C++混合调试，出现两个调试窗口（PandaDebugger、Native）。 |

  说明

调试C++代码时，当前模块及所有依赖的HSP模块的[Address Sanitizer配置](/consumer/cn/doc/harmonyos-guides/ide-instrument-test#section8352185341915)要保持一致，若不一致，可能无法进入C++代码的断点处。

### ASan检测

Instrument Test针对C/C++方法提供ASan检测能力，关于ASan的介绍请参考[ASan检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-asan)，当前不支持JS语言。

1. 在运行/调试配置窗口，选择对应的Instrument Test，点击**Diagnostics**页签，勾选**Address Sanitizer**选项，勾选后，测试包和源码包均开启ASan能力。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102034.21681388468867808522392962008486:50001231000000:2800:784E155544B03AA202D7474F9D79F98B547E3D477851231F92383A6724F4B6BF.png)
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS_ENABLE_ASAN=ON”，表示以ASan模式编译so文件。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102034.26480001041545681108383946921332:50001231000000:2800:1D20391ECBF7B6871A4B1151944B60BAC4A546AC12ED8F228EE8568643AFB4AA.png)
3. 运行测试用例。
4. 当程序出现内存错误时，弹出ASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102034.95816095221668583065994010838931:50001231000000:2800:E8C5B4F3D625AB8596886471FC23A328326BA0D6D9754C944DCEDA26FD6122B8.png)

## 测试C++代码

从DevEco Studio 6.0.0 Beta5版本开始，支持对C++代码进行测试，包括运行/调试C++测试代码、对C++代码进行覆盖率统计。

由于C++的测试so无法直接在设备上运行，需要通过Node-API的方式拉起，即通过ArkTS/JS语言拉起C/C++测试用例。

### 运行C++测试代码

1. 创建cpp测试目录，鼠标右键单击ohosTest目录，选择**New > C/C++ File(Napi)**，在ohosTest下生成cpp测试目录，以entry模块为例，目录结构如下。

  - **src > ohosTest > cpp > types**：用于存放C++的API接口描述文件。
  - **src > ohosTest > cpp > types** **> libentry_test > index.d.ts**：描述C++ API接口行为，如接口名、入参、返回参数等。
  - **src > ohosTest > cpp > types** **> libentry_test > oh-package.json5**：配置.so三方包声明文件的入口及包名。
  - **src > ohosTest > cpp > CMakeLists.txt**：CMake配置文件，提供CMake构建脚本。
  - **src > ohosTest > cpp > napi_init.cpp：**定义C++ API接口的文件**。**

 说明

DevEco Studio生成的cpp测试目录中不包含C++测试框架，需要开发者自行选择开源测试框架使用。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102034.23028508132185516337113886540894:50001231000000:2800:88DD90425B8E39ED86B43FEC453FB59022369FFAD62B3705977ECA257939BA95.png)
2. 通过ArkTS测试用例拉起C++测试，示例如下。收起自动换行深色代码主题复制

```
// ArkTS测试文件Ability.test.ets import entryTest from 'libentry_test.so' ; export default function abilityTest ( ) { describe ( 'ActsAbilityTest' , () => { ... it ( 'testNative' , 0 , () => { hilog. info ( 0x0000 , 'testTag' , '%{public}s' , 'testNative it begin' ); let result = entryTest. runNativeTest (); hilog. info ( 0x0000 , 'testTag' , '%{public}s' , result) expect (result). assertContain ( "ended" ); }) }) }
```
3. 运行testNative测试用例，查看测试结果。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102034.36941321201313473542869967212195:50001231000000:2800:C82F7F05BAE9ABF0A4FC99F8F3C8B08EEE378F6038CEA55C16150003B4B889CE.png)

### 收集代码覆盖率

DevEco Studio默认不收集C++代码覆盖率，需要通过以下方式开启。

1. 在测试目录下的CMakeLists.txt中添加以下代码，开启覆盖率编译插桩能力。收起自动换行深色代码主题复制

```
// DevEco Studio 6.0.2 Beta1之前版本 set (CMAKE_CXX_FLAGS " ${CMAKE_CXX_FLAGS} -fprofile-instr-generate -fcoverage-mapping" ) set (CMAKE_C_FLAGS " ${CMAKE_C_FLAGS} -fprofile-instr-generate -fcoverage-mapping" ) // DevEco Studio 6.0.2 Beta1及以上版本，OHOS_TEST_COVERAGE在覆盖率模式下为 true ，在调试/运行模式下为 false if (OHOS_TEST_COVERAGE) set (CMAKE_CXX_FLAGS " ${CMAKE_CXX_FLAGS} -fprofile-instr-generate -fcoverage-mapping" ) set (CMAKE_C_FLAGS " ${CMAKE_C_FLAGS} -fprofile-instr-generate -fcoverage-mapping" ) endif()
```
2. 在napi_init.cpp文件的RunNativeTest方法中，调用__llvm_profile_write_file方法，将覆盖率数据保存到设备的/data/storage/el2/base路径下的c++_coverage.profraw文件中，该路径和文件名不可修改，示例代码如下。

 收起自动换行深色代码主题复制

```
extern "C" { void __llvm_profile_set_filename( char *); int __llvm_profile_write_file( void ); } static napi_value RunNativeTest (napi_env env, napi_callback_info info) { char filename[ 256 ]; snprintf (filename, sizeof (filename), "/data/storage/el2/base/c++_coverage.profraw" ); // 覆盖率报告文件路径和文件名，不可修改 __llvm_profile_set_filename(filename); // 开启测试 ... // 结束测试，保存数据 __llvm_profile_write_file(); ... }
```
3. 运行覆盖率测试，选中ArkTS测试文件，单击**右键 >****Run '测试文件名称' with Coverage**，执行测试。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102034.25858561118900374180768929481970:50001231000000:2800:4051F809A892FC637F5E618F5382F4F2359963C42BFD78DC0F8E70AC6907CB48.png)

启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102034.24668730276811542254618526823640:50001231000000:2800:5801EEF27F653D8338903C7671B2972D7FC6E8C0B83B32DE243D4097E6CF62FB.png)

点击链接可打开报告，查看C++代码覆盖率详情。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102034.69517001495393675367535860692742:50001231000000:2800:7E7737EE44DF0BA61C6A93BBBCE4E5376B06282C95107D0505FD5B8602384644.png)

## 使用命令行执行测试Instrument Test

通过命令行方式执行Instrument Test，在工程根目录下执行命令：收起自动换行深色代码主题复制

```
hvigorw onDeviceTest -p module ={moduleName} -p coverage={ true | false } -p scope={suiteName}#{methodName} -p ohos- debug -asan={ true | false }
```

- module：执行测试的模块，缺省默认是执行所有模块的用例。
- coverage：是否生成覆盖率报告，缺省默认是true，在<module-path>/.test/default/outputs/ohosTest/reports路径下生成两份报告，一份是html格式（index.html），一份是json格式（coverageReport.json），具体参考[查看覆盖率报告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section10394362109)。

如果开启了C++代码覆盖率测试，会生成C++代码的覆盖率报告，路径：<module-path>/.test/default/outputs/ohosTest/cpp_reports/index.html
- scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。
- ohos-debug-asan：是否启用ASan检测，缺省默认是false。从DevEco Studio 5.1.1 Beta1版本开始支持。

ASan日志路径：<module-path>/.test/default/intermediates/ohosTest/coverage_data

  说明

多个module和scope之间用逗号隔开。

测试结果文件：<module-path>/.test/default/intermediates/ohosTest/coverage_data/test_result.txt
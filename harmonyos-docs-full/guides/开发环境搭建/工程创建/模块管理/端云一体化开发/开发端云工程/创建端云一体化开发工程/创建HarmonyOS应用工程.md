## 新建工程

### 前提条件

- 您已完成[开发准备工作](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-prerequisite)。
- 您已使用[已实名认证](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-account)、且注册地为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的华为开发者账号登录DevEco Studio。
- 请确保您的华为开发者账号无欠款，账户欠费将导致云存储服务开通失败。

### 选择模板

1. 选择以下任一种方式，打开工程创建向导界面。

  - 如果当前未打开任何工程，可以在DevEco Studio的欢迎页点击“Create Project”开始创建一个新工程。
  - 如果已经打开了工程，可以在菜单栏选择“File > New > Create Project”来创建一个新工程。
2. 在“Application”页签，选择合适的云开发模板，然后点击“Next”。说明

当前仅支持通用云开发模板（[CloudDev]Empty Ability）。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101922.93823010634485848960517014553918:50001231000000:2800:CE7332C9890F24F6E0AA2893A6AFB4105E121221FC20EF12E05B02B59688D6ED.png)

### 配置工程信息

1. 在工程配置界面，配置工程的基本信息。

其中，Device type和Enable CloudDev参数不可更改，其他参数请参考[创建一个新的工程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-create-new-project#section11644183711342)内对应的指导进行配置。

 展开

| 参数 | 说明 |
| --- | --- |
| Device type | 该工程模板支持的设备类型，目前仅支持手机设备。 |
| Enable CloudDev | 是否启用云开发。云开发模板默认启用且无法更改。 |

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101922.02177842837502189995022216921581:50001231000000:2800:2DE8359094ABB569BC93A73DBF960A5B03E5B329D04EDC1B34C596EC78ECE824.png)

1. 点击“Next”，开始关联云开发资源。

### 关联云开发资源

为工程关联云开发所需的资源，即将您账号团队在AGC创建的同包名应用关联到当前工程。具体操作如下：

1. （可选）如您尚未登录DevEco Studio，点击“Sign In”，在弹出的账号登录页面，使用[已实名认证](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-account)的华为开发者账号完成登录。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101923.88795023107367546372509379104282:50001231000000:2800:BBE6B91832F905F06C9192932EB3D5D366831AF4FCD64710B747044A4602E4AD.png)

登录成功后，界面将展示账号昵称。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101923.15753400017100377199590542736916:50001231000000:2800:CE76F618F4C29677786327FE76CF74661AB760C6744AFACECC5E2AF9CF877827.png)
2. 点击“Team”下拉框，选择开发团队。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101923.71385801224416821503303034423885:50001231000000:2800:5EE28C7AA6268D0AC1A627D69062104049DFA5437EB9D462ED97D387C64F45C8.png)
3. 关联应用。

选中团队后，系统根据工程Bundle name在该团队中自动查询AGC上的同包名应用。

  - 如查询到应用，选中该应用，点击“Finish”即可。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101923.43858079394685251021721192175119:50001231000000:2800:97B7F4842819FB9E69B6CF3425EA43CD6F2F8AAC60F28DF789EF2583B12E6817.png)
  - 如查询到的应用尚未关联任何项目（即为游离应用），则无法选中。请先[将游离应用添加到AGC项目下](/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-appproject#section152521927193013)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101923.96604470743169393493904536942883:50001231000000:2800:6415DD87C0AE2CC6387C781EC9D8AE93D114AAC2EB4F8E3A0BB143BF5CDC3FA3.png)
  - 如果查询到的应用所属项目尚未启用数据处理位置，请点击界面提示内的“AppGallery Connect”[设置数据处理位置](https://developer.huawei.com/consumer/cn/doc/app/agc-help-datalocation-0000001160439813)。设置完成后返回DevEco Studio界面，点击Bundle name后的![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101923.52558575351747444312082606264963:50001231000000:2800:0562551C1303749D8C3657053FC7947256D3D3AC284B4F7844751C78286EDEB5.png)刷新当前APP ID列表，即可看到设置的数据处理位置。注意

    - 由于云开发目前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），请确保项目启用的数据处理位置包含“中国”。
    - 无论项目启用的默认数据处理位置为哪个站点，后续开发的云服务资源都将部署在“中国”站点。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101923.94442007642042350726658890590816:50001231000000:2800:4FEFDD30C9BF0E27BDDA8CDFA81E7DD60BC00EB0FE6E1B8E23AEB19E2BC89E43.png)
  - 如查询到应用但出现如下提示，表明查询到的应用类型为元服务，与当前工程类型不一致。请修改以确保当前工程与AGC上同包名应用均为HarmonyOS应用类型。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101923.91049541912213733909512086154914:50001231000000:2800:0F75142512BE1F378CC3C4D2C1D2125B863623E4D2510AF67390E3EB26A23EA8.png)

  - 如在当前团队中未查询到同包名应用，请先确认填写的包名是否有误。

    - 如包名有误，点击界面提示中的“go back”返回工程信息配置界面进行修改。
    - 如包名无误，则表明当前团队尚未在AGC控制台创建与当前工程包名相同的应用。您可点击界面提示中的“AppGallery Connect”，[前往AGC控制台进行补充创建](/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-appproject#section397317130308)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101923.36751582418106065105765806432220:50001231000000:2800:58CB62E40F37DB12ECEFBACECB17E10373921EAAC97EEB3E684CA98BC2A98143.png)

完成以上操作后，DevEco Studio即可获取到同包名应用信息。选中应用后，点击“Finish”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101923.12507462187768730327533367452883:50001231000000:2800:6541FCF6D21349DCF2CA781ACA0F4E7DD069CC5C33B4B7D9127C9527C8F1713A.png)
4. 如您所属的团队尚未签署云开发相关协议，点击协议链接仔细阅读协议内容后，勾选同意协议，点击“Finish”。说明

只有账号持有者和法务角色才有权限签署协议。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101923.39088551324434873701027349821718:50001231000000:2800:405646F2A687403BCEA3E314CD792425020721D5A6CF5F39938600BBB44D9320.png)
5. 进入主开发界面，DevEco Studio执行工程同步操作，端侧工程会自动执行“ohpm install”，云侧工程会自动执行“npm install”，以分别下载端侧和云侧依赖。说明

若云侧执行“npm install”失败，请排查是否尚未[配置NPM代理](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-environment-config#section197296441787)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101923.31058548746844702559739163229816:50001231000000:2800:3B83637E1DDB5DC544BC6945FD5C55AD6EA2D08815CCA888793FEAF47CE53C4C.png)
6. 在主开发界面，可查看刚刚新建的工程。关于工程的详细目录结构介绍，请参见[端云一体化开发工程目录结构](/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-appproject#section20250910164411)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101923.93242395517539081885910804838385:50001231000000:2800:21724BB87C3854C74011E9E10B31F341410513A31A7D24797C04EB06075D264D.png)

## 工程初始化配置

当您成功创建工程并关联云开发资源后，DevEco Studio会为您的工程自动执行一些初始化配置。

### 自动开通云开发服务

DevEco Studio为工程关联的项目自动开通云函数、云数据库、云存储等云开发服务，您可在“Notifications”窗口查看服务开通状态。

 说明

- 如服务开通失败，您可通过[CloudDev云开发管理面板](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-console)快捷进入AGC控制台进行手动开通。
- 如云存储服务自动开通与手动开通均失败，可能是账户欠费导致。请您[检查账户是否余额不足](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/agc-account-bill-0000001200817917#section813072912208)，[补齐欠款](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/agc-account-recharge-0000001126625360)后再前往AGC控制台进行手动开通。

## 端云一体化开发工程目录结构

端云一体化开发工程主要包含端开发工程（Application）与云开发工程（CloudProgram）。

### 端开发工程（Application）

端开发工程主要用于开发应用端侧的业务代码，使用通用云开发模板创建的端开发工程目录结构如下图所示。“Application/cloud_objects”模块用于存放云对象的端侧调用接口类，“src/main/ets/pages”目录下包含了云存储、云数据库和云函数页面，其他目录文件介绍请参见[工程目录结构](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-project-structure)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101923.42987909117349293077902696330709:50001231000000:2800:6A4DA8D921847D0E5968609A75EDB10DB679DF2813BD021CC8EBA81BF5D0BB2C.png)

### 云开发工程（CloudProgram）

在云开发工程中，您可为您的应用开发云端代码，包括云函数和云数据库服务代码。使用通用云开发模板创建的云开发工程目录结构如下图所示。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101924.19824808778646402779525686766521:50001231000000:2800:E6C8D71FB67834ED4D9EBAA90BB8D328F55FC700A0A2B272F8A7BF485D844B4C.png)

- clouddb：云数据库目录，包含数据条目目录（dataentry）和对象类型目录（objecttype）。

  - dataentry：用于存放数据条目文件。

该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101924.12585198315698439105316365895058:50001231000000:2800:8E494AFA1A5798496CDE4F5A5F16E4D67093BF1B8D4365C8D6AA9D376B87C14F.png)
  - objecttype：用于存放对象类型文件。

该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101924.08808914839381173899446606818121:50001231000000:2800:1CA5678E10FAD0848C0867E8078AE70EFC97D2AED6E383CADCDC1AF8D5A1660C.png)
  - db-config.json：模块配置文件，主要包含云数据库工程的配置信息，如默认存储区名称、默认数据处理位置。
- cloudfunctions：云函数目录，包含各个云函数/云对象子目录。每个子目录下包含了云函数/云对象的配置文件、入口文件、依赖文件等。

该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101924.97502357031149333184179874078965:50001231000000:2800:02F462DF2C3C9E7ACBE5692229E94C13EE34AE06E49D63BBEA47C38428CE9101.png)
- node_modules：工程同步时执行“npm install”生成，包含“typescript”和“@types/node”公共依赖。
- cloud-config.json：云开发工程配置文件，包含应用名称与ID、项目名称与ID、启用的数据处理位置、支持的设备类型等。
- package.json：定义了“typescript”和“@types/node”公共依赖。
- package-lock.json：工程同步时执行“npm install”生成，记录当前状态下实际安装的各个npm package的具体来源和版本号。

## （可选）AGC应用管理

### 从DevEco Studio补充创建同包名应用

如创建工程时，发现尚未在AGC控制台创建与工程包名相同的应用，可进行补充创建。

1. 点击界面提示内的“AppGallery Connect”，浏览器打开AGC控制台页面。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101924.22228733448226628655258236567750:50001231000000:2800:C407A9C53E4B54BEDA9464B8F8E46420610B83B61456185E69E20C1C653245DC.png)
2. 在“应用开发基础信息”页面，填写待创建的应用信息，完成后点击“下一步”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101924.55779302688590289963077801743208:50001231000000:2800:41BD149133D8FA59625B336473939BE4C5F60B4D9ECAA6FCB2AB425C1317E854.png)

 展开

| 参数 | 说明 |
| --- | --- |
| 应用类型 | 创建的HarmonyOS应用形态，默认与您本地工程类型保持一致，不可更改。 |
| 应用名称 | 应用在华为应用市场详情页展示的名称。 |
| 应用包名 | 从DevEco Studio中带入自动填充，且不可更改。 |
| 应用分类 | 请选择普通应用或游戏类应用。 说明 应用分类设置后不支持修改，请谨慎选择。 |
3. 进入“所属项目信息”页面，为应用选择所属的项目后点击“下一步”。

  - 如需将应用添加到已有项目，点击下拉框进行选择。
  - 如需将应用添加到新项目，直接在框中填写新项目名称。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101924.89394489837841307527051030563671:50001231000000:2800:5477A62DA8F1848497C01C94DBED28E00F6346A498ED8432495A1EBD64AA19B5.png)
4. 进入“云开发数据处理位置”页面，设置或管理项目的数据处理位置。

  - 如项目尚未设置数据处理位置：

    1. 点击“启用”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101924.26585036871408202683070898170873:50001231000000:2800:B800ED37240D3C8F888FEF7C3E70B3D06B16121917988F2657C2624E18849CD0.png)
    2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。注意

启用的数据处理位置必须包含中国站点。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101924.18712001060714412394485191746546:50001231000000:2800:2CDBEC2B6817FE0E6ED554F8A2D093EB40C5FC8FAFE6912AE667F42DA817D42C.png)
  - 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101924.77384711037189584573092501114433:50001231000000:2800:84927EA7D7B570EB17180DCE802F813A537B9E179D0909B9AA0AADAA484FD20C.png)
5. 点击“确认”，应用创建完成。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101924.18926075273530214088939731110650:50001231000000:2800:E6314525B1B42BB4C1DF6235F990A1C03EDEBFBC1B0200F410FABE011F5E87DD.png)
6. 返回DevEco Studio，可看到界面已获取并展示了刚刚创建的应用信息。若不展示，可点击Bundle name后的![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101924.11121753456012503162213519261172:50001231000000:2800:5DA31D709B492F23023B61F7B5B56D3F1972B1DE553EFAE484B89A7E84FA1EE4.png)刷新。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101924.98107747907881884569811904111655:50001231000000:2800:D21998EEBBF10CEC713FE256EC9CA85DE500F4A679DDB02ABBAB53777DF73BF2.png)

### 将游离应用添加到AGC项目下

游离应用指未关联任何AGC项目的应用。创建工程时，如需要关联的AGC应用为游离应用，则您需要将该应用添加到您的AGC项目下。

 注意

应用与项目的关联关系一旦创建则无法再修改，请谨慎操作。

1. 点击“Not associated yet”，或点击界面下方提示内的“AppGallery Connect”，可打开AGC控制台“开发与服务”页面。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101924.31751381313811962994047410894582:50001231000000:2800:13272E1AB5476CEE89E505D8C51BD222E2DE8F646D9DE311C2A5DD3EEE40F3A1.png)
2. 点击选择希望为应用关联的项目，或者点击“添加项目”新建一个项目。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101925.37981669274739612717051356178918:50001231000000:2800:6CF3A143F574D59557EE305C5B6063B75BA91E28F51D61602B0EB7781E4146EC.png)
3. 如选择了新建一个项目，设置项目名称，点击“确认”。

如选择了已有项目，则忽略此步骤。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101925.83577801145910224151072862333962:50001231000000:2800:0E14F39CD1293CF07269347C565C0C7DAAA57E95AC8464A02C5AC2A60D574343.png)
4. 设置或管理项目的数据处理位置。

  - 如项目尚未设置数据处理位置：

    1. 点击“启用”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101925.75652186918712395214739803517542:50001231000000:2800:2245E3F8BBFFB912C96B03268246348CB7B30BE92F619E13E97F87D6537DD87E.png)
    2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。注意

启用的数据处理位置必须包含中国站点。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101925.87469564342287249632130966757756:50001231000000:2800:BD5018296413FF54620657B947EE40B34E07144340F30FCF6FC2B1EE682204F8.png)
  - 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101925.25597583722060324481142466385633:50001231000000:2800:5C5D8664C3046F2B4B0364ED9B5D51E94505443A8DE36BEFAEFBC47408FF62B3.png)
5. 点击“确认”，应用成功关联项目。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101925.00067827569671324763608798040544:50001231000000:2800:FF540236A97AFDCF87F30DD24D6FFB74AECCEFD8A54386ECF147E867EB56AC6E.png)
6. 返回DevEco Studio，可看到应用已关联上了项目。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101925.87205805588518866071558022875875:50001231000000:2800:3D9FF4DCD5EC3F968BB522B92ED04C03C8A3C546F85B9F1307927D296B450431.png)
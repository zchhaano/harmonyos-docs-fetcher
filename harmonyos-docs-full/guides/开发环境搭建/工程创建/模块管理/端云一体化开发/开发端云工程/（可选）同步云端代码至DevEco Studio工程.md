# （可选）同步云端代码至DevEco Studio工程

DevEco Studio还支持您将AGC云端当前项目下的代码同步至本地工程，包括之前从本地部署到AGC云端的代码、以及在AGC云端编写的代码，以保证云端和本地的版本一致性，方便您的日常开发。

云端代码同步目前支持以下模式：[仅同步云函数/云对象](/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-sync#section588213529814)、[仅同步云数据库](/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-sync#section474014335350)、[一键同步云侧代码](/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-sync#section1198316575339)。

## 同步云函数/云对象

说明

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

### 同步单个云函数/云对象

云函数/云对象部署到AGC云端后，如在云端又进行了新改动，您可再将云端的云函数/云对象同步到本地工程。云函数/云对象的同步方式一致，下文以云对象为例进行说明。

1. 右击云对象目录，选择“Sync '*云对象名*'”。下文以云对象“id-generator”为例。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101914.78042036449372352782846590780833:50001231000000:2800:F901A3F4093621D92ACFB6FAF407B10B0BDDFC73D49D796D36A4BD4EC4983079.png)
2. 在确认弹框中点击“Overwrite”，AGC云端的云对象“id-generator”将覆盖更新本地云对象“id-generator”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101914.33474199546579151133673889089921:50001231000000:2800:5C97220648CAC0450752E010B11785E08EB1BF9B049FA953463DC3C1F0C3D3F4.png)
3. 等待同步完成，“cloudfunctions”目录下将生成从云端同步下来的云对象“id-generator”，同时将本地原云对象“id-generator”备份在同路径下。说明

后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101914.10198631621779269029151053876055:50001231000000:2800:BEDEF5F2B20B33295BEEAFCEF06ED1D874F5230E0F0C996624E1ADD595FD1D88.png)

### 批量同步云函数/云对象

批量同步云函数/云对象即将AGC云端当前项目下的所有云函数/云对象同步至本地工程。

1. 右击“cloudfunctions”目录，选择“Sync Cloud Functions”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101914.35998757549900031610394493554083:50001231000000:2800:14D29750B1A55043ED2D849069E90BB502958AD35FDDA860D8546FFD2CAA24C1.png)
2. 弹窗提示您本地工程下存在同名云函数/云对象。

  - 选择“Skip”，同步时将跳过本地同名云函数/云对象。
  - 选择“Overwrite”，AGC云端的云函数/云对象将覆盖更新本地同名云函数/云对象。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101914.33744638338214139936482788006684:50001231000000:2800:528972F02D9E3B4D25A66CE4C731A99E6122BCF954A8A6DAAD0079FA724B2A3A.png)
3. 如选择“Skip”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的不同步。

如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，上图中本地已存在的云函数/云对象未被覆盖更新。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101914.26509762763943354774316742773614:50001231000000:2800:502AC5378DAE52CBAC20D4DEB50724C454C5E85B7A9308CD4B8A195940559526.png)
4. 如选择“Overwrite”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象；本地同名云函数/云对象也被覆盖更新，同时更新前的原云函数/云对象会备份在同路径下。

如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，本地已存在的几个云函数/云对象也被覆盖更新，并且均生成了备份文件“xxxx-*备份时间*.backup”。

 说明

后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101915.82211028403994778119526126291456:50001231000000:2800:AE3B75FF350E1246652EEA37130B5705569197060CDDD2D8D72AD7FBD347A7B3.png)

## 同步云数据库

说明

目前仅支持同步对象类型。

### 同步单个对象类型

对象类型部署到AGC云端后，如又发生了新改动，您可再将云端的对象类型同步到本地。

1. 右击对象类型JSON文件（以“objecttype1.json”为例），选择“Sync 'objecttype1.json'”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101915.43124720170633176262597476860191:50001231000000:2800:FE797A650AEC8C4E3E1AF23B015EEDA9B861D35755DF54FBB2DC46FED9D09C6D.png)
2. 在确认弹框中点击“Overwrite”，AGC云端的对象类型“objecttype1.json”将覆盖更新本地对象类型“objecttype1.json”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101915.45268625189120840127993569720420:50001231000000:2800:88D015C6862C4FC49CDB8571835FF54915F224E2E2897F50F3552B7FBFA16ABF.png)
3. 等待同步完成，“objecttype”目录下将生成从云端同步下来的对象类型“objecttype1.json”。

  - 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
  - 如果云端和本地的同名对象类型内容完全一致，则不生成备份。

 说明

后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101915.67032795561245147884767991520984:50001231000000:2800:5BD33B77363A4A58336781102C24280021D76538746937025929100DC7D5BB4D.png)

### 批量同步对象类型

您可以将AGC云端当前项目下所有的对象类型一键同步至本地。

1. 右击“objecttype”目录，选择“Sync Object Type”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101915.99832800141719969468893467548823:50001231000000:2800:154EC5EBA51E10F75E1585F3F715BCA3014E781F78F46DE9106210C452A81BE0.png)

1. 弹窗提示您本地工程下已存在同名对象类型，如下图“Post.json”与“objecttype1.json”。

  - 选择“Skip”，同步时将跳过本地同名对象类型。
  - 选择“Overwrite”，AGC云端的对象类型将覆盖更新本地同名对象类型。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101915.65128035366610931255293959734458:50001231000000:2800:3C8461C8B25EA3076C4A8BB20CE7E7A1DDC28F34BA5F4C1C84C2B020DBFE41A0.png)
2. 如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，本地已存在的不同步。

如下图，“objecttype”目录下新增了云端同步下来的“test_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101915.40321219908778822705086321818342:50001231000000:2800:705FC517D58ECBA8A83ABB399FAB56EAAD219F90EEC04F81C6B1329D700496A9.png)
3. 如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的所有对象类型，本地已存在的对象类型也被覆盖更新。

  - 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
  - 如果云端和本地的同名对象类型内容完全一致，则不生成备份。

 如下图，“objecttype”目录下生成了“test_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test_object.json”为从云端新同步下来的对象类型；“objecttype1.json”本地已存在且与云端内容一致，不生成备份；“Post.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“Post.json”备份为“Post.json-*备份时间*.backup”。说明

后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101915.91216295898379558151652157682637:50001231000000:2800:5E3A55C83067A703D9412DADAB887F303033EC29E0AE48A390BEF8BED60A5C52.png)

## 一键同步云侧代码

说明

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

1. 右击云开发工程（“CloudProgram”），选择“Sync Cloud Program”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101915.61126716301826081680456035358024:50001231000000:2800:9671E80B956D9A928046406E99B8B5C2ACAFDD35524B43C0F46A98D22EA8EE5F.png)
2. 弹窗提示您本地工程下已存在同名对象类型/云函数/云对象。

  - 选择“Skip”，同步时将跳过本地同名对象类型/云函数/云对象。
  - 选择“Overwrite”，AGC云端的对象类型/云函数/云对象将覆盖更新本地同名对象类型/云函数/云对象。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101915.25288861556503609527982902038150:50001231000000:2800:9828C09D894F7504F2B4A28540485AA8D5A3574864C0018E6F8638638EA14171.png)
3. 如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型均不同步。

如下图：

  - “objecttype”目录下新增了云端同步下来的“test_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。
  - “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”未被覆盖更新。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101915.34740330585216680743854653489915:50001231000000:2800:9BFF44F8765B4A0F16AE43F9DD48B16B45D85385D072972328C0068F058004CC.png)
4. 如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型也被覆盖更新。

  - 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
  - 如果云端和本地的同名对象类型内容完全一致，则不生成备份。
  - 无论云端和本地的同名云函数/云对象代码是否一致，均会将本地原云函数/云对象备份在同路径下。

如下图：

  - “objecttype”目录下生成了“test _object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test _object.json”为从云端新同步下来的对象类型；“Post.json”本地已存在且与云端内容一致，不生成备份；“objecttype1.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“objecttype1.json”备份为“objecttype1.json-*备份时间*.backup”。
  - “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”也被覆盖更新，并且均生成了备份文件“xxxx-*备份时间*.backup”。说明

后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101915.46997241663519601255721984995220:50001231000000:2800:649D94F23FB86101764DC3FC09709BC9BD3C94E3D43442581FC2512DB28B4F63.png)
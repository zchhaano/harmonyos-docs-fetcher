## 概述

### 系统能力与 API

SysCap，全称SystemCapability，即系统能力，指操作系统中每一个相对独立的特性，如蓝牙，WIFI，NFC，摄像头等，都是系统能力之一。每个系统能力对应多个API，随着目标设备是否支持该系统能力共同存在或消失，也会随着DevEco Studio一起提供给开发者做联想。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170137.37895798532915255050892814184352:50001231000000:2800:09C3BA8F73FC783BDF5A129B9A7A701C89D2E234CEA2523E664168C84E777310.png)

### 支持能力集，联想能力集与要求能力集

支持能力集，联想能力集与要求能力集都是系统能力的集合。

支持能力集描述的是设备能力，要求能力集描述的是应用能力。若应用A的要求能力集是设备N的支持能力集的子集，则应用A可分发到设备N上安装运行，否则不能分发。

联想能力集是该应用开发时，DevEco Studio可联想的API所在的系统能力集合。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170137.48787874406991629002611117601162:50001231000000:2800:9DFF774C6EFD2C008336C553D403B5332CDED80E5B97B20F233309FF9748F41D.png)

### 设备与支持能力集

每个设备根据其硬件能力，对应不同的支持能力集。

SDK将设备分为两组，典型设备和自定义设备，典型设备的支持能力集由HarmonyOS来定义，自定义设备由设备厂商给出。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170137.74611132903323000775634578466940:50001231000000:2800:D1F04255815A9B886AD605A79F24C4C7AF139848F930F9BAF0897C8CB7908CB3.png)

### 设备与SDK能力的对应

SDK向DevEco Studio提供全量API，DevEco Studio识别开发者项目中选择的设备形态，找到该设备的支持能力集，筛选支持能力集包含的API并提供API联想。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170137.08657225985366144712027505604657:50001231000000:2800:C1C554F3CED2850DABAC1C007ECB00C22DA6F17C29EB200CF777B73948198EA1.png)

## SysCap开发指导

### 加入自定义SysCap

在某具体的设备型号上，能力可能超出工程默认设备定义的能力集范围，如果需要使用此部分能力，需要额外配置自定义的SysCap。

请在DevEco Studio工程的模块/src/main目录下，手动创建syscap.json文件。如在entry/src/main目录右键，点击New > File。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170137.64067656526674131845428712347549:50001231000000:2800:EBEC2B01DB324A3875B944A7E6284DDBFEBDA391BE3EF8CA6CF71BA4A6A9EFEC.png)

新建文件命名为syscap.json。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170138.55238900906927815023740888615138:50001231000000:2800:4749B0922BB930C34C32AA8394E51273D94DF2374DD0A2A4515919F45E3F60D9.png)

打开新建的syscap.json文件。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170138.80924630597147848580509997713485:50001231000000:2800:7A8FC2BCCD3A6CE93F2910DB0AF21D8749EE3CA03B26D34357EE3E692AA57FD2.png)

按如下格式填入所需要使用的SysCaps。以使用NFC能力为例，syscap.json文件示例如下。

```
{
  "devices": {
    "general": [
      // 每一个典型设备对应一个SysCap支持能力集，可配置多个典型设备，应与工程所选择的设备一致
      "phone"
    ]
  },
  "development": {
    // addedSysCaps内的SysCap集合与devices中配置的各设备支持的SysCap集合的并集共同构成联想能力集。
    "addedSysCaps": [
      "SystemCapability.Communication.NFC.Core",
      "SystemCapability.Communication.NFC.CardEmulation",
      "SystemCapability.Communication.NFC.Tag"
    ]
  }
}
```

### 单设备应用开发

默认应用的联想能力集，要求系统能力集和设备的支持系统能力集相等，开发者修改要求能力集需要慎重。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170138.42453806993819739039701868097389:50001231000000:2800:A56EC8ADC48FF5BC1C64AA288FC8C913526830CE78B4DB659AAA9D79CC0E47BC.png)

### 跨设备应用开发

默认应用的联想能力集是多个设备支持能力集的并集，要求能力集则是交集。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170138.69907298409003509628981688325458:50001231000000:2800:651B87AE0A23557052F63ECE8ACBA9722A4187911578F1D9B218AB3924675BA4.png)

### 判断 API 是否可以使用

当前提供了ArkTS API和Native API用于帮助判断某个API是否可以使用。

- ArkTS API

  - 方法1：HarmonyOS定义了API canIUse帮助开发者来判断该设备是否支持某个特定的SysCap。

```
if (canIUse("SystemCapability.ArkUI.ArkUI.Full")) {
   console.info("该设备支持SystemCapability.ArkUI.ArkUI.Full");
} else {
   console.info("该设备不支持SystemCapability.ArkUI.ArkUI.Full");
}
```
  - 方法2：开发者可通过import的方式将模块导入，若当前设备不支持该模块，import的结果为undefined，开发者在使用其API时，需要判断其是否存在。

```
import { geoLocationManager } from '@kit.LocationKit';

try {
geoLocationManager.getCurrentLocation((location) => {
    console.info('current location: ' + JSON.stringify(location));
});
} catch(err) {
    console.error('该设备不支持位置信息' + err);
}
```
- Native API

```
#include <stdio.h>
#include <stdlib.h>
#include "syscap_ndk.h"

char syscap[] = "SystemCapability.ArkUI.ArkUI.Full";
bool result = canIUse(syscap);
if (result) {
    printf("SysCap: %s is supported!\n", syscap);
} else {
    printf("SysCap: %s is not supported!\n", syscap);
}
```

除此之外，开发者可以通过API参考文档查询API接口所属的SysCap。

### 不同设备相同能力的差异检查

即使是相同的系统能力，在不同的设备下，也会有能力的差异。比如同是摄像头的能力，平板设备优于智能穿戴设备。

以下示例通过人脸识别功能进行举例：

```
import { userAuth } from '@kit.UserAuthenticationKit';

const authParam : userAuth.AuthParam = {
  challenge: new Uint8Array(),
  authType: [userAuth.UserAuthType.PIN],
  authTrustLevel: userAuth.AuthTrustLevel.ATL1,
};
const widgetParam :userAuth.WidgetParam = {
  title: '请输入密码',
};

// 在使用接口时可通过try...catch捕获异常。如果接口的SysCap不支持当前设备，将返回801错误码。
try {
  let userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  userAuthInstance.start();
    console.info('设备认证成功');
} catch (error) {
    console.error('auth catch error: ' + JSON.stringify(error));
}
```

### 设备间的SysCap差异如何产生的

设备的SysCap因产品解决方案厂商拼装的部件组合不同而不同，整体流程如下图：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170138.27496908220493725937671855165930:50001231000000:2800:4553D8818AC40BC0211000FFC6F515FB872A1B19BCC8562B8668823B8847DFF7.png)

1. 一套操作系统源码由可选和必选部件集组成，不同的部件为对外体现的系统能力不同，即部件与 SysCap 之间映射关系。
2. 发布归一化的SDK，API与SysCap之间存在映射关系。
3. 产品解决方案厂商按硬件能力和产品诉求，可按需拼装部件。
4. 产品配置的部件可以是系统部件，也可以是三方开发的私有部件，由于部件与SysCap间存在映射，所有拼装后即可得到该产品的SysCap集合。
5. SysCap集编码生成 PCID (Product Compatibility ID， 产品兼容性标识)，应用开发者可将PCID导入IDE解码成SysCap，开发时对设备的SysCap差异做兼容性处理。
6. 部署到设备上的系统参数中包含了SysCap集，系统提供了native的接口和应用接口，可供系统内的部件和应用查询某个SysCap是否存在。
7. 应用开发过程中，应用必要的SysCap将被编码成RPCID（Required Product Compatibility ID），并写入应用安装包中。应用安装时，包管理器将解码RPCID得到应用需要的 SysCap，与设备当前具备的SysCap比较，若应用要求的SysCap都被满足，则安装成功。
8. 应用运行时，可通过canIUse接口查询设备的SysCap，保证在不同设备上的兼容性。
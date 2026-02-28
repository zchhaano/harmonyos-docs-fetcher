## 场景说明

开发者可以使用[@ohos.ai.mindSporeLite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mindsporelite)，在UI代码中集成MindSpore Lite能力，快速部署AI算法，进行AI模型推理，实现图像分类的应用。

图像分类可实现对图像中物体的识别，在医学影像分析、自动驾驶、电子商务、人脸识别等领域有广泛的应用。

## 基本概念

在进行开发前，请先了解以下概念。

**张量**：它与数组和矩阵非常相似，是MindSpore Lite网络运算中的基本数据结构。

**Float16推理模式**： Float16又称半精度，它使用16比特表示一个数。Float16推理模式表示推理的时候用半精度进行推理。

## 接口说明

这里给出MindSpore Lite推理的通用开发流程中涉及的一些接口，具体请见下列表格。更多接口及详细内容，请见[@ohos.ai.mindSporeLite (推理能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mindsporelite)。

  展开

| 接口名 | 描述 |
| --- | --- |
| loadModelFromFile(model: string, context?: Context): Promise<Model> | 从路径加载模型。 |
| getInputs(): MSTensor[] | 获取模型的输入。 |
| predict(inputs: MSTensor[]): Promise<MSTensor[]> | 推理模型。 |
| getData(): ArrayBuffer | 获取张量的数据。 |
| setData(inputArray: ArrayBuffer): void | 设置张量的数据。 |

## 开发流程

1. 选择图像分类模型。
2. 在端侧使用MindSpore Lite推理模型，实现对选择的图片进行分类。

## 环境准备

安装DevEco Studio，要求版本 >= 4.1，并更新SDK到API 11或以上。

## 开发步骤

本文以对相册的一张图片进行推理为例，提供使用MindSpore Lite实现图像分类的开发指导。

### 选择模型

本示例程序中使用的图像分类模型文件为[mobilenetv2.ms](https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite/1.5/mobilenetv2.ms)，放置在entry/src/main/resources/rawfile工程目录下。

如果开发者有其他图像分类的预训练模型，请参考[MindSpore Lite 模型转换](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-converter-guidelines)介绍，将原始模型转换成.ms格式。

### 编写推理代码

1. 工程默认设备定义的能力集可能不包含MindSporeLite。需在DevEco Studio工程的entry/src/main目录下，手动创建syscap.json文件，内容如下：

 收起自动换行深色代码主题复制

```
{ "devices" : { "general" : [ // 需跟module.json5中deviceTypes保持一致。 "default" ] } , "development" : { "addedSysCaps" : [ "SystemCapability.AI.MindSporeLite" ] } }
```
2. 调用[@ohos.ai.mindSporeLite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mindsporelite)实现端侧推理。具体开发过程及细节如下：

  1. 创建上下文，设置线程数、设备类型等参数。本样例模型，不支持使用NNRt推理。
  2. 加载模型。本文从内存加载模型。
  3. 加载数据。模型执行之前需要先获取输入，再向输入的张量中填充数据。
  4. 执行推理。使用predict接口进行模型推理。

 收起自动换行深色代码主题复制

```
// model.ets import { mindSporeLite } from '@kit.MindSporeLiteKit' import { hilog } from '@kit.PerformanceAnalysisKit' ; export default async function modelPredict ( modelBuffer: ArrayBuffer , inputsBuffer: ArrayBuffer [] ): Promise <mindSporeLite. MSTensor []> { // 1.创建上下文，设置线程数、设备类型等参数。本样例模型，不支持配置context.target = ["nnrt"]。 let context : mindSporeLite. Context = {}; context. target = [ 'cpu' ]; context. cpu = {} context. cpu . threadNum = 2 ; context. cpu . threadAffinityMode = 1 ; context. cpu . precisionMode = 'enforce_fp32' ; // 2.从内存加载模型。 let msLiteModel : mindSporeLite. Model = await mindSporeLite. loadModelFromBuffer (modelBuffer, context); // 3.设置输入数据。 let modelInputs : mindSporeLite. MSTensor [] = msLiteModel. getInputs (); for ( let i = 0 ; i < inputsBuffer. length ; i++) { let inputBuffer = inputsBuffer[i]; if (inputBuffer != null ) { modelInputs[i]. setData (inputBuffer as ArrayBuffer ); } } // 4.执行推理。 hilog. info ( 0xFF00 , 'MindSporeLiteArkTSDemo' , '%{public}s' , `=========MS_LITE_LOG: MS_LITE predict start=====` ); let modelOutputs : mindSporeLite. MSTensor [] = await msLiteModel. predict (modelInputs); return modelOutputs; }
```

[model.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteArkTSDemo/entry/src/main/ets/pages/model.ets#L16-L48)

### 实现图像输入和预处理，并执行推理

1. 此处以获取相册图片为例，调用[@ohos.file.picker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-picker) 实现相册图片文件的选择。
2. 根据模型的输入尺寸，调用[@ohos.multimedia.image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image) （实现图片处理）、[@ohos.file.fs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs) （实现基础文件操作） API对选择图片进行裁剪、获取图片buffer数据，并进行标准化处理。
3. 加载模型文件，调用推理函数，对相册选择的图片进行推理，并对推理结果进行处理。

 收起自动换行深色代码主题复制

```
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteArkTSDemo/entry/src/main/ets/pages/Index.ets#L16-L351)

### 调测验证

1. 在DevEco Studio中连接设备，点击Run entry，编译Hap，有如下显示：

 收起自动换行深色代码主题复制

```
Launching com.samples.mindsporelitearktsdemo $ hdc shell aa force-stop com.samples.mindsporelitearktsdemo $ hdc shell mkdir data/local/tmp/xxx $ hdc file send C:\Users\xxx\MindSporeLiteArkTSDemo\entry\build\default\outputs\default\entry-default-signed.hap "data/local/tmp/xxx" $ hdc shell bm install -p data/local/tmp/xxx $ hdc shell rm -rf data/local/tmp/xxx $ hdc shell aa start -a EntryAbility -b com.samples.mindsporelitearktsdemo
```
2. 在设备屏幕点击photo按钮，选择图片，点击确定。设备屏幕显示所选图片的分类结果，在日志打印结果中，过滤关键字”MS_LITE“，可得到如下结果：

 收起自动换行深色代码主题复制

```
08 - 06 03 : 24 : 33.743 22547 - 22547 A03d00 / JSAPP com . sampl ... liteark + I MS_LITE_LOG : PhotoViewPicker . select successfully , photoSelectResult uri : { "photoUris" :[ "file://media/Photo/13/IMG_1501955351_012/plant.jpg" ]} 08 - 06 03 : 24 : 33.795 22547 - 22547 A03d00 / JSAPP com . sampl ... liteark + I MS_LITE_LOG : readSync data to file succeed and inputBuffer size is : 32824 08 - 06 03 : 24 : 34.147 22547 - 22547 A03d00 / JSAPP com . sampl ... liteark + I MS_LITE_LOG : crop info . width = 224 08 - 06 03 : 24 : 34.147 22547 - 22547 A03d00 / JSAPP com . sampl ... liteark + I MS_LITE_LOG : crop info . height = 224 08 - 06 03 : 24 : 34.160 22547 - 22547 A03d00 / JSAPP com . sampl ... liteark + I MS_LITE_LOG : Succeeded in reading image pixel data , buffer : 200704 08 - 06 03 : 24 : 34.970 22547 - 22547 A03d00 / JSAPP com . sampl ... liteark + I ========= MS_LITE_LOG : MS_LITE predict start ===== 08 - 06 03 : 24 : 35.432 22547 - 22547 A03d00 / JSAPP com . sampl ... liteark + I ========= MS_LITE_LOG : MS_LITE predict success ===== 08 - 06 03 : 24 : 35.447 22547 - 22547 A03d00 / JSAPP com . sampl ... liteark + I MS_LITE_LOG : Default / head - MobileNetV2Head / Sigmoid - op466 : 0.0000034338463592575863 , 0.000014028532859811094 , 9.119685273617506e-7 , 0.000049100715841632336 , 9.502661555416125e-7 , 3.945370394831116e-7 , 0.04346757382154465 , 0.00003971960904891603 ... 08 - 06 03 : 24 : 35.499 22547 - 22547 A03d00 / JSAPP com . sampl ... liteark + I MS_LITE_LOG : max : 9497 , 7756 , 1970 , 435 , 46 08 - 06 03 : 24 : 35.499 22547 - 22547 A03d00 / JSAPP com . sampl ... liteark + I MS_LITE_LOG : maxIndex : 323 , 46 , 13 , 6 , 349 08 - 06 03 : 24 : 35.499 22547 - 22547 A03d00 / JSAPP com . sampl ... liteark + I ========= MS_LITE_LOG END =========
```

### 效果示意

在设备上，点击photo按钮，选择相册中的一张图片，点击确定。在图片下方显示此图片占比前4的分类信息。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165227.97277303446154969782500156009306:50001231000000:2800:E891E061930FA98E27ED35618C3C2035954CFCC15D75E0080F0D83C225C1FFCE.png) ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165227.88462100315666430785587241902024:50001231000000:2800:42D82B49BAB352CDCDBDDDA20DA03BCDDF81B9F0A119C750EC4021811E5B9C63.png)

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165227.65597855964845413410464194249140:50001231000000:2800:175DB5BF9DB49FE385304A93F9EFBCCF7EB08C74F7C48B1EFA380E9A82389A75.png) ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165227.33068282500625995830858261894004:50001231000000:2800:F9E6CC4BADC1F87D885CE55745F7B7A49625CE6EDEE52829545AD4E8D0B1313D.png)

## 示例代码

- [基于MindSporeLite接口实现图像分类（ArkTS）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteArkTSDemo)
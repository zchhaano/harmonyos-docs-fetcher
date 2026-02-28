# 使用PixelMap完成图像变换

图片处理指对PixelMap进行相关的操作，如获取图片信息、裁剪、缩放、偏移、旋转、翻转、设置透明度、读写像素数据等。图片处理主要包括图像变换、[位图操作](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-pixelmap-operation)，本文介绍图像变换。

## 开发步骤

图像变换相关API的详细介绍请参见[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)。

1. 完成[图片解码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-decoding)，获取PixelMap对象。
2. 获取图片信息。

 收起自动换行深色代码主题复制

```
import { BusinessError } from '@kit.BasicServicesKit' ; // 获取图片大小。 pixelMap. getImageInfo (). then ( ( info : image.ImageInfo ) => { console . info ( 'info.width = ' + info. size . width ); console . info ( 'info.height = ' + info. size . height ); }). catch ( ( err : BusinessError ) => { console . error ( "Failed to obtain the image pixel map information.And the error is: " + err); });
```
3. 进行图像变换操作。

原图：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165442.74124876173584537437245308451885:50001231000000:2800:2EA0A4156734CF6A9D67B0F495BD8D2D1D04FE7BCC2A95B32506CB865194FB31.jpeg)

  - 裁剪

 收起自动换行深色代码主题复制

```
// x：裁剪起始点横坐标0。 // y：裁剪起始点纵坐标0。 // height：裁剪高度400，方向为从上往下（裁剪后的图片高度为400）。 // width：裁剪宽度400，方向为从左到右（裁剪后的图片宽度为400）。 pixelMap. crop ({ x : 0 , y : 0 , size : { height : 400 , width : 400 } });
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165442.91284586466804280601649147658187:50001231000000:2800:4777CAB1BF3FEA6E02866BF3B528C0B4F1242A146048F56D7D1ADE5B125F1071.jpeg)
  - 缩放

 收起自动换行深色代码主题复制

```
// 宽为原来的0.5。 // 高为原来的0.5。 pixelMap. scale ( 0.5 , 0.5 );
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165442.05619769266644821256491108814954:50001231000000:2800:3DE66A60858C54470DAD7B88FAF4858F464AC75C1762B2D9D5B181B748E7EC4B.jpeg)
  - 偏移

 收起自动换行深色代码主题复制

```
// 向下偏移100。 // 向右偏移100。 pixelMap. translate ( 100 , 100 );
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165442.01138399426211244712799153665990:50001231000000:2800:90CFD410839766604699F561C0D34D7FC063460A2EB5BB06952F73468C356F4B.jpeg)
  - 旋转

 收起自动换行深色代码主题复制

```
// 顺时针旋转90°。 pixelMap. rotate ( 90 );
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165442.75973253272905300283906272362496:50001231000000:2800:A7EA56CF5391890B724B5D4149EADF09DDB9F12A1B8E25955FCAE8F51F32BF96.jpeg)
  - 翻转

 收起自动换行深色代码主题复制

```
// 垂直翻转。 pixelMap. flip ( false , true );
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165442.11983175193746220378167004150786:50001231000000:2800:6956D7BD9BE30A722F73F13B4ECBD955710C0F405734D7BD8EAFFBF9C71E843B.jpeg)

 收起自动换行深色代码主题复制

```
// 水平翻转。 pixelMap. flip ( true , false );
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165443.62649779426382154401362229038655:50001231000000:2800:551B3D540D7AE086506BE8A7781ED1AC28AED0109D79FB6E1D0F149C5FB02533.jpeg)
  - 透明度

 收起自动换行深色代码主题复制

```
// 透明度0.5。 pixelMap. opacity ( 0.5 );
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165443.78769184804981080989392595483331:50001231000000:2800:E073FCBC4A11AD18799B46128099CD69F374C6183AAA58835D190B3D3E851EB3.png)

## 示例代码

- [拼图](https://gitcode.com/HarmonyOS_Samples/game-puzzle)
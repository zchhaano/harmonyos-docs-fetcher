# @ohos.effectKit (图像效果)

图像效果模块提供了处理图像的基础能力，包括亮度调节、模糊化、灰度调节和智能取色等。effectKit用于离线处理图像（如pixelmap、png、jpeg）以获得视觉效果，而uiEffect则实时接入渲染服务，针对屏幕帧缓存进行处理以获得动态视觉效果。

该模块提供以下图像效果相关的常用功能：

- [Filter](/consumer/cn/doc/harmonyos-references/js-apis-effectkit#filter)：效果类，用于添加指定效果到图像源。
- [Color](/consumer/cn/doc/harmonyos-references/js-apis-effectkit#color)：颜色类，用于保存取色的结果。
- [ColorPicker](/consumer/cn/doc/harmonyos-references/js-apis-effectkit#colorpicker)：智能取色器。

 说明 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

 支持设备PhonePC/2in1TabletTVWearable

```
import { effectKit } from "@kit.ArkGraphics2D";
```

## effectKit.createEffect

 支持设备PhonePC/2in1TabletTVWearable

createEffect(source: image.PixelMap): Filter

通过传入的PixelMap创建Filter实例。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | image.PixelMap | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见 Image Kit简介 。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Filter | 返回不带任何效果的Filter链表头节点，失败时返回null。 |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  let headFilter = effectKit.createEffect(pixelMap);
})
```

## effectKit.createColorPicker

 支持设备PhonePC/2in1TabletTVWearable

createColorPicker(source: image.PixelMap): Promise<ColorPicker>

通过传入的PixelMap创建ColorPicker实例，使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | image.PixelMap | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见 Image Kit简介 。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise< ColorPicker > | Promise对象。返回创建的ColorPicker实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";
import { BusinessError } from "@kit.BasicServicesKit";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}

image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap).then(colorPicker => {
    console.info("color picker=" + colorPicker);
  }).catch( (reason : BusinessError) => {
    console.error("error=" + reason.message);
  })
})
```

## effectKit.createColorPicker 10+

 支持设备PhonePC/2in1TabletTVWearable

createColorPicker(source: image.PixelMap, region: Array<number>): Promise<ColorPicker>

通过传入的PixelMap创建选定取色区域的ColorPicker实例，使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | image.PixelMap | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见 Image Kit简介 。 |
| region | Array<number> | 是 | 指定图片的取色区域。 数组元素个数为4，取值范围为[0, 1]，分别表示图片区域的左、上、右、下位置，图片最左侧和最上侧对应位置0，最右侧和最下侧对应位置1。数组第三个元素需大于第一个元素，第四个元素需大于第二个元素。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise< ColorPicker > | Promise对象。返回创建的ColorPicker实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";
import { BusinessError } from "@kit.BasicServicesKit";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}

image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, [0, 0, 1, 1]).then(colorPicker => {
    console.info("color picker=" + colorPicker);
  }).catch( (reason : BusinessError) => {
    console.error("error=" + reason.message);
  })
})
```

## effectKit.createColorPicker

 支持设备PhonePC/2in1TabletTVWearable

createColorPicker(source: image.PixelMap, callback: AsyncCallback<ColorPicker>): void

通过传入的PixelMap创建ColorPicker实例，使用callback异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | image.PixelMap | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见 Image Kit简介 。 |
| callback | AsyncCallback< ColorPicker > | 是 | 回调函数。返回创建的ColorPicker实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
    }
  })
})
```

## effectKit.createColorPicker 10+

 支持设备PhonePC/2in1TabletTVWearable

createColorPicker(source: image.PixelMap, region:Array<number>, callback: AsyncCallback<ColorPicker>): void

通过传入的PixelMap创建选定取色区域的ColorPicker实例，使用callback异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | image.PixelMap | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见 Image Kit简介 。 |
| region | Array<number> | 是 | 指定图片的取色区域。 数组元素个数为4，取值范围为[0, 1]，数组元素分别表示图片区域的左、上、右、下位置，图片最左侧和最上侧对应位置0，最右侧和最下侧对应位置1。数组第三个元素需大于第一个元素，第四个元素需大于第二个元素。 |
| callback | AsyncCallback< ColorPicker > | 是 | 回调函数。返回创建的ColorPicker实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, [0, 0, 1, 1], (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
    }
  })
})
```

## Color

 支持设备PhonePC/2in1TabletTVWearable

颜色类，用于保存取色的结果。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

  展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| red | number | 否 | 否 | 红色分量值，取值范围[0x0, 0xFF]。 |
| green | number | 否 | 否 | 绿色分量值，取值范围[0x0, 0xFF]。 |
| blue | number | 否 | 否 | 蓝色分量值，取值范围[0x0, 0xFF]。 |
| alpha | number | 否 | 否 | 透明通道分量值，取值范围[0x0, 0xFF]。 |

## TileMode 14+

 支持设备PhonePC/2in1TabletTVWearable

着色器效果平铺模式的枚举。

**系统能力：** SystemCapability.Multimedia.Image.Core

  展开

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CLAMP | 0 | 如果着色器效果超出其原始边界，剩余区域使用着色器的边缘颜色填充。 |
| REPEAT | 1 | 在水平和垂直方向上重复着色器效果。 |
| MIRROR | 2 | 在水平和垂直方向上重复着色器效果，交替镜像图像，以便相邻图像始终接合。 |
| DECAL | 3 | 仅在其原始边界内渲染着色器效果。 |

## ColorPicker

 支持设备PhonePC/2in1TabletTVWearable

取色类，用于从一张图像数据中获取它的主要颜色。在调用ColorPicker的方法前，需要先通过[createColorPicker](/consumer/cn/doc/harmonyos-references/js-apis-effectkit#effectkitcreatecolorpicker)创建一个ColorPicker实例。

### getMainColor

 支持设备PhonePC/2in1TabletTVWearable

getMainColor(): Promise<Color>

读取图像主色的颜色值，结果写入[Color](/consumer/cn/doc/harmonyos-references/js-apis-effectkit#color)里，使用Promise异步回调。该接口通过图像缩放算法，根据周围像素的加权计算，将原图缩小到1个像素以得到主色。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise< Color > | Promise对象。返回图像主色对应的颜色值，失败时返回错误信息。 |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
     } else {
       console.info('Succeeded in creating color picker.');
       colorPicker.getMainColor().then(color => {
        console.info('Succeeded in getting main color.');
         console.info(`color[ARGB]=${color.alpha},${color.red},${color.green},${color.blue}`);
      })
    }
  })
})
```

### getMainColorSync

 支持设备PhonePC/2in1TabletTVWearable

getMainColorSync(): Color

读取图像主色的颜色值，结果写入[Color](/consumer/cn/doc/harmonyos-references/js-apis-effectkit#color)里，使用同步方式返回。该接口通过图像缩放算法，根据周围像素的加权计算，将原图缩小到1个像素以得到主色。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Color | Color实例，即图像主色对应的颜色值，失败时返回null。 |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getMainColorSync();
      console.info('get main color =' + color);
    }
  })
})
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170140.13229760142536692047579254235450:50001231000000:2800:DD620E0F127F164C45BD6D2923342ECC14666D028C4232A0FC3D0A64FE1E4016.png)

### getLargestProportionColor 10+

 支持设备PhonePC/2in1TabletTVWearable

getLargestProportionColor(): Color

读取图像中占比最多的颜色值，结果写入[Color](/consumer/cn/doc/harmonyos-references/js-apis-effectkit#color)里，使用同步方式返回。该接口使用中位切分算法划分颜色空间，获取占比最多的颜色空间的平均颜色。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Color | Color实例，即图像占比最多的颜色值，失败时返回null。 |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getLargestProportionColor();
      console.info('get largest proportion color =' + color);
    }
  })
})
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170140.78382775740022687637027325222037:50001231000000:2800:D682FE69CC9A95D9EFE1C639D2DCC9BB163F56A2957FE3EF9D9DA03BDB714541.png)

### getTopProportionColors 12+

 支持设备PhonePC/2in1TabletTVWearable

getTopProportionColors(colorCount: number): Array<Color | null>

读取图像占比靠前的颜色值，个数由colorCount指定，结果写入[Color](/consumer/cn/doc/harmonyos-references/js-apis-effectkit#color)的数组里，使用同步方式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorCount | number | 是 | 需要取主色的个数，取值范围为[1, 10]，向下取整。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Array< Color \| null> | Color数组，即图像占比前colorCount的颜色值数组，按占比排序。 - 当实际读取的特征色个数小于colorCount时，数组大小为实际特征色个数。 - 取色失败或取色个数小于1返回[null]。 - 取色个数大于10视为取前10个。 |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let colors = colorPicker.getTopProportionColors(2);
      for(let index = 0; index < colors.length; index++) {
        if (colors[index]) {
          console.info('get top proportion colors: index ' + index + ', color ' + colors[index]);
        }
      }
    }
  })
})
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170140.00370071152514387304030347088130:50001231000000:2800:AF207AA709F6F5FCA6677A897801DBCE3F60890295F92906A3ADE042B389C55C.png)

### getHighestSaturationColor 10+

 支持设备PhonePC/2in1TabletTVWearable

getHighestSaturationColor(): Color

读取图像饱和度最高的颜色值，结果写入[Color](/consumer/cn/doc/harmonyos-references/js-apis-effectkit#color)里，使用同步方式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Color | Color实例，即图像饱和度最高的颜色值，失败时返回null。 |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getHighestSaturationColor();
      console.info('get highest saturation color =' + color);
    }
  })
})
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170140.86440274686637099438721022142438:50001231000000:2800:7E21DA9A20C153785208E272B234342519A2F4322448DEF2BDE1DC95C0D8CA87.png)

### getAverageColor 10+

 支持设备PhonePC/2in1TabletTVWearable

getAverageColor(): Color

读取图像平均的颜色值，结果写入[Color](/consumer/cn/doc/harmonyos-references/js-apis-effectkit#color)里，使用同步方式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Color | Color实例，即图像平均的颜色值，失败时返回null。 |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getAverageColor();
      console.info('get average color =' + color);
    }
  })
})
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170141.82708655763845885935325320363471:50001231000000:2800:E0757B9D99D6A909955673551E8D2F6C7185229925991B89E70E969A78484447.png)

### isBlackOrWhiteOrGrayColor 10+

 支持设备PhonePC/2in1TabletTVWearable

isBlackOrWhiteOrGrayColor(color: number): boolean

判断图像是否为黑白灰颜色，返回true或false。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | number | 是 | 需要判断是否黑白灰色的颜色值，取值范围[0x0, 0xFFFFFFFF]。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| boolean | 如果图像为黑白灰颜色，则返回true；否则返回false。 |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let bJudge = colorPicker.isBlackOrWhiteOrGrayColor(0xFFFFFFFF);
      console.info('is black or white or gray color[bool](white) =' + bJudge);
    }
  })
})
```

## Filter

 支持设备PhonePC/2in1TabletTVWearable

图像效果类，用于将指定的效果添加到输入图像中。在调用Filter的方法前，需要先通过[createEffect](/consumer/cn/doc/harmonyos-references/js-apis-effectkit#effectkitcreateeffect)创建一个Filter实例。

### blur

 支持设备PhonePC/2in1TabletTVWearable

blur(radius: number): Filter

将模糊效果添加到效果链表中，返回链表的头节点。

 说明 

该接口为静态模糊接口，为静态图像提供模糊化效果，如果要对组件进行实时渲染的模糊，可以使用[动态模糊](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-blur-effect)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number | 是 | 模糊半径，单位是像素。模糊效果与所设置的值成正比，值越大效果越明显。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Filter | 返回已添加的图像效果。 |

**示例：**

```
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// 传入读取的图片数据
function ImageBlur(Image: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    let imageSource = image.createImageSource(Image);
    imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      let radius = 5;
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // 对图片添加效果标识
        headFilter.blur(radius);
      }
      // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
      headFilter.getEffectPixelMap().then(imageData => {
        resolve(imageData);
      })
    })
  })
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
    this.imagePixelMap = await ImageBlur(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170141.76539827297202814619737013533225:50001231000000:2800:77B654F5D79862D6A0D63E541BBEB829919B6965CA35214EC07A355DCAE0336E.png)

### blur 14+

 支持设备PhonePC/2in1TabletTVWearable

blur(radius: number, tileMode: TileMode): Filter

将模糊效果添加到效果链表中，返回链表的头节点。

 说明 

该接口为静态模糊接口，为静态图像提供模糊化效果，如果要对组件进行实时渲染的模糊，可以使用[动态模糊](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-blur-effect)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number | 是 | 模糊半径，单位是像素。模糊效果与所设置的值成正比，值越大效果越明显。 |
| tileMode | TileMode | 是 | 着色器效果平铺模式。影响图像边缘的模糊效果。目前仅支持CPU渲染，所以目前着色器平铺模式仅支持DECAL。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Filter | 返回已添加的图像效果。 |

**示例：**

```
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// 传入读取的图片数据
function ImageBlur(Image: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    let imageSource = image.createImageSource(Image);
    imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      let radius = 30;
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // 对图片添加效果标识
        headFilter.blur(radius, effectKit.TileMode.DECAL);
      }
      // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
      headFilter.getEffectPixelMap().then(imageData => {
        resolve(imageData);
      })
    })
  })
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
    this.imagePixelMap = await ImageBlur(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170141.10695898604203160615488792835141:50001231000000:2800:9D674F83D326FB6A883D464E13B35B66084EDD6265E3A8A35F6A5692684458AE.png)

### invert 12+

 支持设备PhonePC/2in1TabletTVWearable

invert(): Filter

将反转效果添加到效果链表中，返回链表的头节点。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Filter | 返回已添加的图像效果。 |

**示例：**

```
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// 传入读取的图片数据
function ImageInvert(Image: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    let imageSource = image.createImageSource(Image);
    imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // 对图片添加效果标识
        headFilter.invert();
      }
      // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
      headFilter.getEffectPixelMap().then(imageData => {
        resolve(imageData);
      })
    })
  })
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
    this.imagePixelMap = await ImageInvert(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170141.03811388421502500578474327948877:50001231000000:2800:73176E41D0312718BECD8F0E696B9F12D0368ED276401DA31559A1A2A1C83C56.png)

### setColorMatrix 12+

 支持设备PhonePC/2in1TabletTVWearable

setColorMatrix(colorMatrix: Array<number>): Filter

将自定义效果添加到效果链表中，返回链表的头节点。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorMatrix | Array<number> | 是 | 自定义颜色矩阵。 用于创建效果滤镜的 5x4 大小的矩阵，矩阵元素取值范围为[0, 1]，0和1代表的是矩阵中对应位置的颜色通道的权重，0代表该颜色通道不参与计算，1代表该颜色通道参与计算并保持原始权重。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Filter | 返回已添加的图像效果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// 传入读取的图片数据
function ImageColorFilter(Image: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    let imageSource = image.createImageSource(Image);
    imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      let colorMatrix:Array<number> = [
      0.2126,0.7152,0.0722,0,0,
      0.2126,0.7152,0.0722,0,0,
      0.2126,0.7152,0.0722,0,0,
      0,0,0,1,0
      ];
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // 对图片添加效果标识
        headFilter.setColorMatrix(colorMatrix);
      }
      // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
      headFilter.getEffectPixelMap().then(imageData => {
        resolve(imageData);
      })
    })
  })
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
    this.imagePixelMap = await ImageColorFilter(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

### brightness

 支持设备PhonePC/2in1TabletTVWearable

brightness(bright: number): Filter

将高亮效果添加到效果链表中，返回链表的头节点。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bright | number | 是 | 高亮程度，取值范围在0-1之间，取值为0时图像保持不变。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Filter | 返回已添加的图像效果。 |

**示例：**

```
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// 传入读取的图片数据
function ImageBrightness(Image: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    let imageSource = image.createImageSource(Image);
    imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      let bright = 0.5;
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // 对图片添加效果标识
        headFilter.brightness(bright);
      }
      // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
      headFilter.getEffectPixelMap().then(imageData => {
        resolve(imageData);
      })
    })
  })
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
    this.imagePixelMap = await ImageBrightness(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170141.74304142039832446774021666659330:50001231000000:2800:10D064C52FDD953BFA0E3865A46D6FE058F8A79F64158932715179FCF5A782E2.png)

### grayscale

 支持设备PhonePC/2in1TabletTVWearable

grayscale(): Filter

将灰度效果添加到效果链表中，返回链表的头节点。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Filter | 返回已添加的图像效果。 |

**示例：**

```
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// 传入读取的图片数据
function ImageGrayscale(Image: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    let imageSource = image.createImageSource(Image);
    imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // 对图片添加效果标识
        headFilter.grayscale();
      }
      // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
      headFilter.getEffectPixelMap().then(imageData => {
        resolve(imageData);
      })
    })
  })
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
    this.imagePixelMap = await ImageGrayscale(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170141.08471526935206007273892962144760:50001231000000:2800:FC83F63D9449F212A1F3F8803296693C6932678A404715EF34C14D93A9C4DBD4.png)

### getEffectPixelMap 11+

 支持设备PhonePC/2in1TabletTVWearable

getEffectPixelMap(): Promise<image.PixelMap>

获取已添加链表效果的源图像的image.PixelMap，使用CPU渲染，使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<image.PixelMap> | Promise对象。返回已添加链表效果的源图像的image.PixelMap。 |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createEffect(pixelMap).grayscale().getEffectPixelMap().then(data => {
    console.info('getPixelBytesNumber = ', data.getPixelBytesNumber());
  })
})
```

### getEffectPixelMap 20+

 支持设备PhonePC/2in1TabletTVWearable

getEffectPixelMap(useCpuRender : boolean): Promise<image.PixelMap>

获取已添加链表效果的源图像的image.PixelMap，支持指定渲染模式（CPU渲染或者GPU渲染），使用Promise异步回调。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| useCpuRender | boolean | 是 | 指定渲染模式。true表示使用CPU渲染，false表示使用GPU渲染。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise< image.PixelMap > | Promise对象。返回已添加链表效果的源图像的image.PixelMap。 |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createEffect(pixelMap).grayscale().getEffectPixelMap(false).then(data => {
    console.info('getPixelBytesNumber = ', data.getPixelBytesNumber());
  })
})
```

### getPixelMap (deprecated)

 支持设备PhonePC/2in1TabletTVWearable

getPixelMap(): image.PixelMap

获取已添加链表效果的源图像的image.PixelMap。

 说明 

从API version 9开始支持，从API version 11开始废弃，建议使用[getEffectPixelMap](/consumer/cn/doc/harmonyos-references/js-apis-effectkit#geteffectpixelmap11)替代。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| image.PixelMap | 已添加效果的源图像的image.PixelMap。 |

**示例：**

```
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(color, opts).then((pixelMap) => {
  let pixel = effectKit.createEffect(pixelMap).grayscale().getPixelMap();
  console.info('getPixelBytesNumber = ', pixel.getPixelBytesNumber());
})
```
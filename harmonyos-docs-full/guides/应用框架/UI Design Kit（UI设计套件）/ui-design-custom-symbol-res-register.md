# 应用加载自定义Symbol

    

#### 场景介绍

 

从5.1.1 (19)版本开始，新增支持资源注册。

 

适用于需要快速定制应用内[Symbol图标](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-symbolregister)，不想强依赖于系统版本中预制的系统Symbol图标资源。

    

#### 约束条件

 

资源注册支持Phone、Tablet、PC/2in1设备，并且从5.1.1(19)版本开始，新增支持TV设备。

    

#### 开发步骤

 

1. 将UX设计师提供的Symbol图标资源（TTF文件）与动效参数资源（JSON文件）放入entry/src/main/resources/rawfile下，可新建目录。

 

说明：[Symbol资源制作流程参考](https://developer.huawei.com/consumer/cn/doc/design-guides/system-icons-0000001929854962)

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/ce1jqwIKQ9agr5YNTVGINA/zh-cn_image_0000002543374044.png?HW-CC-KV=V1&HW-CC-Date=20260420T191107Z&HW-CC-Expire=86400&HW-CC-Sign=37490D0E3C3886571936F541357A38CBA6C361B9285C7BD168A0F3F82794D6BC)
2. 多语言场景，在entry/src/main/resources目录中对应语言目录下的string.json文件中配置对应的Symbol图标Unicode值。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/U728qWg-RYuB2PLueeSDTg/zh-cn_image_0000002543214382.png?HW-CC-KV=V1&HW-CC-Date=20260420T191107Z&HW-CC-Expire=86400&HW-CC-Sign=4F91E1BBED18EED9E7E20C4C1472CCCFC87597BB7020A698FA97C5FC80176DBF)

 

```
{
  "string": [
    {
      "name": "symbol_custom_phone_fill_1",
      "value": "0x100016"
    }
  ]
}

```
3. 导入相关模块。

 

```
import { symbolRegister } from '@kit.UIDesignKit';
import { BusinessError } from '@kit.BasicServicesKit';

```
4. 在通过SymbolGlyph/SymbolSpan组件展示自定义Symbol图标前，需要注册加载图标资源与动效参数资源。

 

```
try {
  let result = symbolRegister.registerSymbol($rawfile("symbol/symbol_register.ttf"), $rawfile("symbol/symbol_register.json"));
} catch (error) {
  let err = error as BusinessError;
  console.error("errCode: " + err.code)
  console.error("error: " + err.message);
}

```
5. 在需要展示自定义Symbol图标的页面通过SymbolGlyph/SymbolSpan组件展示该图标。

 

```
struct test {
  build() {
    Column(){
      SymbolGlyph($r('app.string.symbol_custom_phone_fill_1'))
    }
  }
}

```

    

#### 开发实例

 

```
import { symbolRegister } from '@kit.UIDesignKit';
import { BusinessError } from '@ohos.base';

@Entry
@Component
struct test {
  aboutToAppear(): void {
    try {
      let result = symbolRegister.registerSymbol($rawfile("symbol/symbol_register.ttf"), $rawfile("symbol/symbol_register.json"));
    } catch (error) {
      let err = error as BusinessError;
      console.error("errCode: " + err.code)
      console.error("error: " + err.message);
    }
  }
  build() {
    Column(){
      SymbolGlyph($r('app.string.symbol_custom_phone_fill_1'))
    }
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/HEkIOwoFQsWVubF2h9vXvQ/zh-cn_image_0000002573854297.png?HW-CC-KV=V1&HW-CC-Date=20260420T191107Z&HW-CC-Expire=86400&HW-CC-Sign=392880892ED9812C358C95ABB7691630564DAD6FFBCCE9903F9A49677B0C0138)
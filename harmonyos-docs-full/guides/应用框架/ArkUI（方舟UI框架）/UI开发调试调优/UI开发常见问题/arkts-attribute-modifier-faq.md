# 动态属性设置常见问题

  

本文档介绍动态属性设置的常见问题并提供参考。

   

#### 使用AttributeModifier设置组件动态属性，出现jscrash

 

**问题现象**

 

使用AttributeModifier对组件进行[动态属性设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier)，设置某些属性后出现[JS Crash](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jscrash-guidelines)。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/KwtsOVzuSMmb03CGIJ2PdA/zh-cn_image_0000002543373866.png?HW-CC-KV=V1&HW-CC-Date=20260420T191051Z&HW-CC-Expire=86400&HW-CC-Sign=2ACFA79CF02CE4C4B31B1DB47726261CE812D5DD51B5831B3F78798635056F4B)

 

**解决措施**

 

根据提示跳转至报错日志，查看具体的报错原因，进行相应的修改，具体的跳转方法请参考下方示例代码。

 

**示例代码**

 

该示例通过Button绑定AttributeModifier，展示了AttributeModifier在设置不支持的属性时会抛出异常的场景，运行示例代码后会出现jscrash报错，参考下方的动图，跳转至具体的报错场景。在本示例中，删除reuseId相关代码即可正常运行。

 

```
// xxx.ets
// 设置Button组件属性的自定义AttributeModifier
class MyButtonModifier implements AttributeModifier<ButtonAttribute> {

  applyNormalAttribute(instance: ButtonAttribute): void {
    instance.reuseId('String') // 删除本行可以让程序正常运行
    instance.backgroundColor(Color.Red)
  }
}

@Entry
@Component
struct attributeDemo {
  @State modifier: MyButtonModifier = new MyButtonModifier();

  build() {
    Row() {
      Column() {
        Button('Button')
          .attributeModifier(this.modifier)
      }
      .width('100%')
    }
    .height('100%')
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/k5dSxKyWTz-TFSkVh_4TeQ/zh-cn_image_0000002543214204.gif?HW-CC-KV=V1&HW-CC-Date=20260420T191051Z&HW-CC-Expire=86400&HW-CC-Sign=27EF510105FFD97B50F77B1336907AE4FAA42EB35520DB2C8C0197F2E702735B)
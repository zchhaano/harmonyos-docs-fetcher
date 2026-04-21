# 图标小符号 (SymbolGlyph/SymbolSpan)

  

SymbolGlyph是图标小符号组件，便于使用精美的图标，如渲染多色图标和使用动效图标。SymbolSpan作为Text组件的子组件，可在文本中穿插显示图标小符号。具体用法请参考[SymbolGlyph](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph)和[SymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)组件的API文档。

   

#### 创建图标

 

SymbolGlyph通过$r引用Resource资源来创建，目前仅支持系统预置的Symbol资源名。

 

相关资源可参考[系统图标](https://developer.huawei.com/consumer/cn/doc/design-guides/system-icons-0000001929854962)。

 

```
SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
  .fontSize(96)
  .renderingStrategy(SymbolRenderingStrategy.SINGLE)
  .fontColor([Color.Black, Color.Green, Color.White])

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/0UBXbruLT62l3hxwgw4BRw/zh-cn_image_0000002573853779.png?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=72BDFEE73FF8485E0CAF1988327CCC100E8638202A33DC6983493B2C3D26D820)

    

#### 添加到文本中

 

[SymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)可作为[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)的子组件用于显示图标小符号。可以在一个Text组件内添加多个SymbolSpan，从而展示一串连续的图标。

 

- 创建SymbolSpan。

 

SymbolSpan组件需嵌入在Text组件中才能显示，单独使用不会呈现任何内容。

 

```
Text() {
  SymbolSpan($r('sys.symbol.ohos_trash'))
    .fontWeight(FontWeight.Normal)
    .fontSize(96)
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/2KzwtEDNSnyeFKiKqUimaQ/zh-cn_image_0000002573973757.png?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=208E7EC10729EFAB46843BE0367581E8F79A4EC77150B4804CFEEE03D7F3B380)
- 通过[fontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontsize)属性设置SymbolSpan的大小。

 

```
Row() {
  Column() {
    Text('48')
    Text() {
      SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
        .fontSize(48)
        .renderingStrategy(SymbolRenderingStrategy.SINGLE)
        .fontColor([Color.Black, Color.Green, Color.White])
    }
  }

  Column() {
    Text('72')
    Text() {
      SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
        .fontSize(72)
        .renderingStrategy(SymbolRenderingStrategy.SINGLE)
        .fontColor([Color.Black, Color.Green, Color.White])
    }
  }

  Column() {
    Text('96')
    Text() {
      SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
        .fontSize(96)
        .renderingStrategy(SymbolRenderingStrategy.SINGLE)
        .fontColor([Color.Black, Color.Green, Color.White])
    }
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/0Lv6-ZodTyCW8pF1cWOG3g/zh-cn_image_0000002543373530.png?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=D4E93644B6053B7EDA92701F21444F6BDB444C5CAD5F1F8AF8953BE33B16E97C)
- 通过[fontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontweight)属性设置SymbolSpan组件的粗细。

 

```
Row() {
  Column() {
    Text('Light')
    Text() {
      SymbolSpan($r('sys.symbol.ohos_trash'))
        .fontWeight(FontWeight.Lighter)
        .fontSize(96)
    }
  }

  Column() {
    Text('Normal')
    Text() {
      SymbolSpan($r('sys.symbol.ohos_trash'))
        .fontWeight(FontWeight.Normal)
        .fontSize(96)
    }
  }

  Column() {
    Text('Bold')
    Text() {
      SymbolSpan($r('sys.symbol.ohos_trash'))
        .fontWeight(FontWeight.Bold)
        .fontSize(96)
    }
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/rm_OxCReTIeNsk74-sVvEA/zh-cn_image_0000002543213868.png?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=A44ABCCA74FDB5FC2137F0A0F7AA8509FCF5412E3A789C90D3E9551B28BB70E3)
- 通过[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontcolor)属性设置SymbolSpan的颜色。

 

```
Row() {
  Column() {
    Text('Black')
    Text() {
      SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
        .fontSize(96)
        .fontColor([Color.Black])
    }
  }

  Column() {
    Text('Green')
    Text() {
      SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
        .fontSize(96)
        .fontColor([Color.Green])
    }
  }

  Column() {
    Text('Pink')
    Text() {
      SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
        .fontSize(96)
        .fontColor([Color.Pink])
    }
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/9WaUrEODRuqB4B1axrVIxA/zh-cn_image_0000002573853781.png?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=CEFFF079EF014851F85638B8C8B34D21E0D8343F67611C5B3B9329B10AD3CC7E)
- 通过[renderingStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#renderingstrategy)属性设置SymbolSpan的渲染策略。

 

```
Row() {
  Column() {
    // 请将$r('app.string.single_color')替换为实际资源文件，在本示例中该资源文件的value值为"单色"
    Text($r('app.string.single_color'));
    Text() {
      SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
        .fontSize(96)
        .renderingStrategy(SymbolRenderingStrategy.SINGLE)
        .fontColor([Color.Black, Color.Green, Color.White])
    }
  }

  Column() {
    // 请将$r('app.string.multi_color')替换为实际资源文件，在本示例中该资源文件的value值为"多色"
    Text($r('app.string.multi_color'));
    Text() {
      SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
        .fontSize(96)
        .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
        .fontColor([Color.Black, Color.Green, Color.White])
    }
  }

  Column() {
    // 请将$r('app.string.hierarchical')替换为实际资源文件，在本示例中该资源文件的value值为"分层"
    Text($r('app.string.hierarchical'));
    Text() {
      SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
        .fontSize(96)
        .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
        .fontColor([Color.Black, Color.Green, Color.White])
    }
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/fafg-ZMVR1O9bEQiPldDRw/zh-cn_image_0000002573973759.png?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=CB402ABDDA97B962B053460E1619B9873171E8613F6104FB581E42E9EF244E48)
- 通过[effectStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#effectstrategy)属性设置SymbolSpan的动效策略。

 

```
Row() {
  Column() {
    // 请将$r('app.string.no_action')替换为实际资源文件，在本示例中该资源文件的value值为"无动效"
    Text($r('app.string.no_action'));
    Text() {
      SymbolSpan($r('sys.symbol.ohos_wifi'))
        .fontSize(96)
        .effectStrategy(SymbolEffectStrategy.NONE)
    }
  }

  Column() {
    // 请将$r('app.string.overall_scaling_animation_effect')替换为实际资源文件，在本示例中该资源文件的value值为"整体缩放动效"
    Text($r('app.string.overall_scaling_animation_effect'));
    Text() {
      SymbolSpan($r('sys.symbol.ohos_wifi'))
        .fontSize(96)
        .effectStrategy(SymbolEffectStrategy.SCALE)
    }
  }

  Column() {
    // 请将$r('app.string.hierarchical_animation')替换为实际资源文件，在本示例中该资源文件的value值为"层级动效"
    Text($r('app.string.hierarchical_animation'));
    Text() {
      SymbolSpan($r('sys.symbol.ohos_wifi'))
        .fontSize(96)
        .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)
    }
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/U8OYwXTzQtChPJyQr-800A/zh-cn_image_0000002543373532.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=96E44CD41E112C6B51CA382DA14596449610D299CF295195CA656CC95FB8B59A)
- SymbolSpan不支持通用事件。

    

#### 自定义图标动效

 

相较于effectStrategy属性在启动时即触发动效，可以通过以下两种方式来控制动效的播放状态，以及选择更多样化的动效策略。

 

关于effectStrategy属性与symbolEffect属性的多种动态属性使用及生效原则，详情请参阅[SymbolGlyph.symbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symboleffect12-1)属性的说明。

 

- 通过设置SymbolEffect属性，可以同时配置SymbolGlyph的动效策略和播放状态。

 

```
@State isActive: boolean = true;

```

 

```
Column() {
  // 请将$r('app.string.variable_color_animation')替换为实际资源文件，在本示例中该资源文件的value值为"可变颜色动效"
  Text($r('app.string.variable_color_animation'));
  SymbolGlyph($r('sys.symbol.ohos_wifi'))
    .fontSize(96)
    .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)
  // 请将$r('app.string.off')替换为实际资源文件，在本示例中该资源文件的value值为"关闭"
  // 请将$r('app.string.on')替换为实际资源文件，在本示例中该资源文件的value值为"播放"
  Button(this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {
    this.isActive = !this.isActive;
  })
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/274hQIXMRfKnugxfhutjGw/zh-cn_image_0000002543213870.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=FAA603DD84E3E6DC97BD06D6363963B0C955CD449D7C8B2A1B5BDCDBC4032D49)
- 通过设置SymbolEffect属性，可以同时指定SymbolGlyph的动画效果策略及其播放触发条件。

 

```
@State triggerValueReplace: number = 0;

```

 

```
Column() {
  // 请将$r('app.string.bounce_animation')替换为实际资源文件，在本示例中该资源文件的value值为"弹跳动效"
  Text($r('app.string.bounce_animation'));
  SymbolGlyph($r('sys.symbol.ellipsis_message_1'))
    .fontSize(96)
    .fontColor([Color.Gray])
    .symbolEffect(new BounceSymbolEffect(EffectScope.WHOLE, EffectDirection.UP),
                  this.triggerValueReplace)
  Button('trigger').onClick(() => {
    this.triggerValueReplace = this.triggerValueReplace + 1;
  })
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/NbZgG9gBQAuEirQsKEupvA/zh-cn_image_0000002573853783.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=47D877098F13EEF62E378E4F01EF151D6545945A4D9A9EF11ACFDA95E08BBC63)
- 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.SLASH_OVERLAY，可以指定SymbolGlyph的禁用动画效果及其播放触发条件。

 

```
@State triggerValueReplace: number = 0;
replaceFlag: boolean = true;
@State renderMode: number = 1;

```

 

```
Column() {
  // 请将$r('app.string.disable_animation')替换为实际资源文件，在本示例中该资源文件的value值为"禁用动效"
  Text($r('app.string.disable_animation'));
  SymbolGlyph(this.replaceFlag ? $r('sys.symbol.eye_slash') : $r('sys.symbol.eye'))
    .fontSize(96)
    .renderingStrategy(this.renderMode)
    .symbolEffect(new ReplaceSymbolEffect(EffectScope.LAYER, ReplaceEffectType.SLASH_OVERLAY),
                  this.triggerValueReplace)
  Button('trigger').onClick(() => {
    this.replaceFlag = !this.replaceFlag;
    this.triggerValueReplace = this.triggerValueReplace + 1;
  })
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/MmXSmRnGSJyfrumQVTor6A/zh-cn_image_0000002573973761.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=8AB362DED953FF2B4A48FFFEBD5EBF94C0296A70856850016D62AC56D3A9E32A)
- 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.CROSS_FADE，可以指定SymbolGlyph的快速替换动画效果及其播放触发条件。

 

```
@State triggerValueReplace: number = 0;
replaceFlag: boolean = true;

```

 

```
Column() {
  // 请将$r('app.string.quick_replacement_animation')替换为实际资源文件，在本示例中该资源文件的value值为"快速替换动效"
  Text($r('app.string.quick_replacement_animation'));
  SymbolGlyph(this.replaceFlag ? $r('sys.symbol.checkmark_circle') : $r('sys.symbol.repeat_1'))
    .fontSize(96)
    .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE, ReplaceEffectType.CROSS_FADE),
                  this.triggerValueReplace)
  Button('trigger').onClick(() => {
    this.replaceFlag = !this.replaceFlag;
    this.triggerValueReplace = this.triggerValueReplace + 1;
  })
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/wiH7Eo0rSpOB3XZtB17o-A/zh-cn_image_0000002543373534.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=8543BD3E3C96A976E7DA5649F785C56C49E92030060491957535A33270D5D337)

    

#### 设置阴影和渐变色

 

- 从API version 20开始，支持通过[symbolShadow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symbolshadow20)接口实现了symbolGlyph组件显示阴影效果。

 

```
@State isActive: boolean = true;

options: ShadowOptions = {
  radius: 10.0,
  color: Color.Blue,
  offsetX: 10,
  offsetY: 10,
};

```

 

```
Column() {
  // 请将$r('app.string.shadow_ability')替换为实际资源文件，在本示例中该资源文件的value值为"阴影能力"
  Text($r('app.string.shadow_ability'));
  SymbolGlyph($r('sys.symbol.ohos_wifi'))
    .fontSize(96)
    .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), !this.isActive)
    .symbolShadow(this.options)
  // 请将$r('app.string.off')替换为实际资源文件，在本示例中该资源文件的value值为"关闭"
  // 请将$r('app.string.on')替换为实际资源文件，在本示例中该资源文件的value值为"播放"
  Button(!this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {
    this.isActive = !this.isActive;
  })
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/6sNH6EWMSmOhnwymPhf89A/zh-cn_image_0000002543213872.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=6834DCD0696729880602CFC4519B5AA9EDFE46EF6DB13223B1056BA147A25DBC)
- 从API version 20开始，支持通过[shaderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#shaderstyle20)接口实现了symbolGlyph组件显示渐变色效果。

 

```
radialGradientOptions: RadialGradientOptions = {
  center: ['50%', '50%'],
  radius: '20%',
  colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],
  repeating: true,
};

```

 

```
Column() {
  // 请将$r('app.string.radial_gradient')替换为实际资源文件，在本示例中该资源文件的value值为"径向渐变"
  Text($r('app.string.radial_gradient'))
    .fontSize(18)
    .fontColor(0xCCCCCC)
    .textAlign(TextAlign.Center)
  SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
    .fontSize(96)
    .shaderStyle([new RadialGradientStyle(this.radialGradientOptions)])
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/uU5C7ocvTp2kYPQaXkwI4Q/zh-cn_image_0000002573853785.jpg?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=6F18529BA95CA517FB802F722C7334429B6B615EF41E0BAFBEBF08C3EF116213)

    

#### 添加事件

 

SymbolGlyph组件可以添加通用事件，例如绑定[onClick](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click#onclick)、[onTouch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch#ontouch)等事件来响应操作。

 

```
@State wifiColor: ResourceColor = Color.Black;

```

 

```
SymbolGlyph($r('sys.symbol.ohos_wifi'))
  .fontSize(96)
  .fontColor([this.wifiColor])
  .onClick(() => {
    this.wifiColor = Color.Gray;
  })

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/y5D85552T7aST9YaZy_D5A/zh-cn_image_0000002573973763.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=1E318E431765C2307D4CD0409E0FE23DD969B3833A40FEB294F2D1A69B454BF9)

    

#### 场景示例

 

该示例通过symbolEffect、fontSize、fontColor属性展示了播放列表的效果。

 

```
// resourceGetString封装工具，从资源中获取字符串
import resourceGetString from '../../common/resource';

@Entry
@Component
struct SymbolMusicDemo {
  @State triggerValueReplace: number = 0;
  @State symbolSources: Resource[] =
    [$r('sys.symbol.repeat'), $r('sys.symbol.repeat_1'), $r('sys.symbol.arrow_left_arrow_right')];
  @State symbolSourcesIndex: number = 0;
  @State symbolText: string[] = [
    // 请将$r('app.string.play_in_order')替换为实际资源文件，在本示例中该资源文件的value值为"顺序播放"
    this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.play_in_order').id),
    // 请将$r('app.string.play_in_single_repeat')替换为实际资源文件，在本示例中该资源文件的value值为"单曲循环"
    this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.play_in_single_repeat').id),
    // 请将$r('app.string.shuffle_play')替换为实际资源文件，在本示例中该资源文件的value值为"随机播放"
    this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.shuffle_play').id),
  ];
  @State symbolTextIndex: number = 0;
  @State fontColorValue: ResourceColor = Color.Grey;
  @State fontColorValue1: ResourceColor = '#E8E8E8';

  build() {
    Column({ space: 10 }) {
      Row() {
        Text() {
          // 请将$r('app.string.current_playlist')替换为实际资源文件，在本示例中该资源文件的value值为"当前播放列表"
          Span(this.getUIContext()
            .getHostContext()!.resourceManager.getStringSync($r('app.string.current_playlist').id))
            .fontSize(20)
            .fontWeight(FontWeight.Bolder)
          Span('（101）')
        }
      }

      Row() {
        Row({ space: 5 }) {
          SymbolGlyph(this.symbolSources[this.symbolSourcesIndex])
            .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE), this.triggerValueReplace)
            .fontSize(20)
            .fontColor([this.fontColorValue])
          Text(this.symbolText[this.symbolTextIndex])
            .fontColor(this.fontColorValue)
        }
        .onClick(() => {
          this.symbolTextIndex++;
          this.symbolSourcesIndex++;
          this.triggerValueReplace++;
          if (this.symbolSourcesIndex > (this.symbolSources.length - 1)) {
            this.symbolSourcesIndex = 0;
            this.triggerValueReplace = 0;
          }
          if (this.symbolTextIndex > (this.symbolText.length - 1)) {
            this.symbolTextIndex = 0;
          }
        })
        .width('75%')

        Row({ space: 5 }) {
          Text() {
            SymbolSpan($r('sys.symbol.arrow_down_circle_badge_vip_circle_filled'))
              .fontColor([this.fontColorValue])
              .fontSize(20)
          }

          Text() {
            SymbolSpan($r('sys.symbol.heart_badge_plus'))
              .fontColor([this.fontColorValue])
              .fontSize(20)
          }

          Text() {
            SymbolSpan($r('sys.symbol.ohos_trash'))
              .fontColor([this.fontColorValue])
              .fontSize(20)
          }
        }
        .width('25%')
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲一"
          Text($r('app.string.song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.song_again')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲二"
          Text($r('app.string.song_again'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.again_song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲三"
          Text($r('app.string.again_song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.song_repeat')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲四"
          Text($r('app.string.song_repeat'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.repeat_song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲五"
          Text($r('app.string.repeat_song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.song_play')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲六"
          Text($r('app.string.song_play'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.play_song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲七"
          Text($r('app.string.play_song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Column() {
        // 请将$r('app.string.off')替换为实际资源文件，在本示例中该资源文件的value值为"关闭"
        Text($r('app.string.off'))
      }
      .alignItems(HorizontalAlign.Center)
      .width('98%')
    }
    .alignItems(HorizontalAlign.Start)
    .width('100%')
    .height(400)
    .padding({
      left: 10,
      top: 10
    })
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/CbH52gWSR8efW4HztOBVDQ/zh-cn_image_0000002543373536.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193724Z&HW-CC-Expire=86400&HW-CC-Sign=D1C9F6FFDAACA2A62201F97A29C543006F5D8B789589E3B4004704344292B6BE)
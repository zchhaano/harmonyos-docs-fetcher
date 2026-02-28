# @AnimatableExtend装饰器：定义可动画属性

@AnimatableExtend装饰器用于自定义可动画的属性方法，在这个属性方法中修改组件不可动画的属性。在动画执行过程中，通过逐帧回调函数修改不可动画属性值，让不可动画属性也能实现动画效果。也可通过逐帧回调函数修改可动画属性的值，实现逐帧布局的效果。

- 可动画属性：如果一个属性方法在[animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation)属性前调用，改变这个属性的值可以使animation属性的动画效果生效，这个属性称为可动画属性。比如height、width、backgroundColor、translate属性，和Text组件的fontSize属性等。
- 不可动画属性：如果一个属性方法在animation属性前调用，改变这个属性的值不能使animation属性的动画效果生效，这个属性称为不可动画属性。比如Polyline组件的points属性等。

 说明 

 该装饰器从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

从API version 11开始，该装饰器支持在元服务中使用。

## 装饰器使用说明

### 语法

收起自动换行深色代码主题复制

```
@AnimatableExtend ( UIComponentName ) function functionName ( value: typeName ) { . propertyName (value) }
```

- @AnimatableExtend仅支持定义在全局，不支持在组件内部定义。
- @AnimatableExtend定义的函数参数类型必须为number类型或者实现 AnimatableArithmetic<T>接口的自定义类型。
- @AnimatableExtend定义的函数体内只能调用@AnimatableExtend括号内组件的属性方法。

### AnimatableArithmetic<T>接口说明

该接口定义非number数据类型的动画运算规则。对非number类型的数据（如数组、结构体、颜色等）做动画，需要实现AnimatableArithmetic<T>接口中加法、减法、乘法和判断相等函数，使得该数据能参与动画的插值运算和识别该数据是否发生改变。即定义它们为实现了AnimatableArithmetic<T>接口的类型。

 展开

| 名称 | 入参类型 | 返回值类型 | 说明 |
| --- | --- | --- | --- |
| plus | AnimatableArithmetic<T> | AnimatableArithmetic<T> | 定义该数据类型的加法运算规则 |
| subtract | AnimatableArithmetic<T> | AnimatableArithmetic<T> | 定义该数据类型的减法运算规则 |
| multiply | number | AnimatableArithmetic<T> | 定义该数据类型的乘法运算规则 |
| equals | AnimatableArithmetic<T> | boolean | 定义该数据类型的相等判断规则 |

## 使用场景

以下示例通过改变Text组件宽度实现逐帧布局的效果。

 收起自动换行深色代码主题复制

```
@AnimatableExtend ( Text ) function animatableWidth ( width: number ) { . width (width) } @Entry @Component struct AnimatablePropertyText { @State textWidth : number = 80 ; build ( ) { Column () { Text ( 'AnimatableProperty' ) . animatableWidth ( this . textWidth ) . animation ({ duration : 2000 , curve : Curve . Ease }) Button ( 'Play' ) . onClick ( () => { this . textWidth = this . textWidth == 80 ? 160 : 80 ; }) }. width ( '100%' ) . padding ( 10 ) } }
```

[AnimatablePropertyText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ComponentExtension/entry/src/main/ets/pages/AnimatableExtendDecorator/AnimatablePropertyText.ets#L16-L40) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165959.16228106363885944697380388686419:50001231000000:2800:2B9343BF6FBFF40B0062972A64FFD38D33B41EECEC2724C3616846108F3326D7.gif)

以下示例实现折线的动画效果。

 收起自动换行深色代码主题复制

```
```

[AnimatablePropertyExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ComponentExtension/entry/src/main/ets/pages/AnimatableExtendDecorator/AnimatablePropertyExample.ets#L16-L135) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165959.46979372590765553912356994075018:50001231000000:2800:4B8723874DD65C458E3629AD4576C07BFEC39D653DFB8E17A49C9E8CD7D0776F.gif)
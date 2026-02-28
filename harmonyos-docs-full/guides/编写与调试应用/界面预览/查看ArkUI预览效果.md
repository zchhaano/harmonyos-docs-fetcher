# 查看ArkUI预览效果

ArkUI预览支持页面预览、组件预览和卡片预览，下图中左侧图标![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102005.73970473816371877820589528392341:50001231000000:2800:738D25C8564B691B20044983E505D31C39C30F7D0EAF8B12E504D4CF9DCE458C.png)为页面预览，右侧图标![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102005.52464439182962143555960837306292:50001231000000:2800:6FA6066C99A1F2E5D5CDDA552FED093C397767B58DAFA94873D052C8B47BBCBD.png)为组件预览，卡片预览在创建卡片文件后可直接预览。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102005.01383457421532838325520231777458:50001231000000:2800:B81A9E41FDE0E2A1E584B01EDE35C56A628088FA2E2D47567CA10B71E6CB1724.png)

## 页面预览

ArkTS应用/元服务支持页面预览。页面预览通过在工程的ets文件头部添加@Entry实现。

@Entry的使用参考如下示例：

 收起自动换行深色代码主题复制

```
@Entry @Component struct Index { @State message : string = 'Hello World' build ( ) { Row () { Column () { Text ( this . message ) . fontSize ( 50 ) . fontWeight ( FontWeight . Bold ) } . width ( '100%' ) } . height ( '100%' ) } }
```

## 组件预览

ArkTS应用/元服务支持组件预览。组件预览支持实时预览，不支持动态图和动态预览。组件预览通过在组件前添加注解@Preview实现，在单个源文件中，最多可以使用10个@Preview装饰自定义组件。

 @Preview的使用参考如下示例：收起自动换行深色代码主题复制

```
@Preview ({ title : 'ContentTable' }) @Component struct ContentTablePreview { build () { Flex () { ContentTable ({ foodItem: getDefaultFoodData() }) } } }
```

以上示例的组件预览效果如下图所示：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102005.81625944154117640513951665114107:50001231000000:2800:4B4E9AE859528B03F624B51892D7037F29364406AF87554CE8822F9551F087A0.gif)

 组件预览默认的预览设备为Phone，若您想查看不同的设备，或者不同的屏幕形状，或者不同设备语言等情况下的组件预览效果，可以通过设置@Preview的参数，指定预览设备的相关属性。若不设置@Preview的参数，默认的设备属性如下所示：收起自动换行深色代码主题复制

```
@ Preview ({ title : 'Component1' , //预览组件的名称 deviceType : 'phone' , //指定当前组件预览渲染的设备类型，默认为Phone width : 1080 , //预览设备的宽度，单位：px height : 2340 , //预览设备的长度，单位：px colorMode : 'light' , //显示的亮暗模式，当前支持取值为light dpi : 480 , //预览设备的屏幕DPI值 locale : 'zh_CN' , //预览设备的语言，如zh_CN、en_US等 orientation : 'portrait' , //预览设备的横竖屏状态，取值为portrait或landscape roundScreen : false //设备的屏幕形状是否为圆形 })
```

请注意，如果被预览的组件是依赖参数注入的组件，建议的预览方式是：定义一个组件片段，在该片段中声明将要预览的组件，以及该组件依赖的入参，并在组件片段上标注@Preview注解，以表明将预览该片段中的内容。例如，要预览如下组件：

 收起自动换行深色代码主题复制

```
@Component struct Title { @Prop context : string; build () { Text(this.context) } }
```

建议按如下方式预览：

 收起自动换行深色代码主题复制

```
@Preview @Component //定义组件片段TitlePreview struct TitlePreview { build () { Title ({ context: 'MyTitle' }) //在该片段中声明将要预览的组件Title，以及该组件依赖的入参 {context: 'MyTitle'} } }
```

## 卡片预览

创建卡片并选中卡片文件后，点击右侧边栏**Previewer**按钮即可预览卡片。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102005.81206331240722618702804399757458:50001231000000:2800:253340D3EFF84D4C45D87EB2B5A294A9F2C5CE3BF5C5A560A2477606ACA11513.png)
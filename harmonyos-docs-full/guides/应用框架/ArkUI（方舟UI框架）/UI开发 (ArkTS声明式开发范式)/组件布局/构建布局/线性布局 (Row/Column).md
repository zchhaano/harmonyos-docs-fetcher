## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

 说明 

在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165904.47176572760074143401409752760192:50001231000000:2800:E004E36710F3855C188BE5DB20C9CD640BBB0FE61C398C55DCE42FECB9BC4128.png)

**图2** Row容器内子元素排列示意图

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165904.26539419103479352218513954738902:50001231000000:2800:F3F2C4375E27D5B83440B8A53F07549CA5A0C552578CA42FFC8191FED09387D7.png)

## 基本概念

- 布局容器：具有布局能力的容器组件，可以承载其他元素作为其子元素，布局容器会对其子元素进行尺寸计算和布局排列。
- 布局子元素：布局容器内部的元素。
- 主轴：线性布局容器在布局方向上的轴线，子元素默认沿主轴排列。Row容器主轴为水平方向，Column容器主轴为垂直方向（图示可参考弹性布局[基本概念](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout#基本概念)中的主轴）。
- 交叉轴：垂直于主轴方向的轴线。Row容器交叉轴为垂直方向，Column容器交叉轴为水平方向（图示可参考弹性布局[基本概念](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout#基本概念)中的交叉轴）。
- 间距：布局子元素的间距。

## 布局子元素在排列方向上的间距

在布局容器内，可以通过space属性设置排列方向上子元素的间距，使各子元素在排列方向上有等间距效果。

### Column容器内排列方向上的间距

**图3** Column容器内排列方向的间距图

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165904.56689340912545276785054760466929:50001231000000:2800:912740A00D889444B8AB298974F3EC849F76366A0D512B748F66B995C0F79266.png)

 收起自动换行深色代码主题复制

```
Column ({ space : 20 }) { Text ( 'space: 20' ). fontSize ( 15 ). fontColor ( Color . Gray ). width ( '90%' ) Row (). width ( '90%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) Row (). width ( '90%' ). height ( 50 ). backgroundColor ( 0xD2B48C ) Row (). width ( '90%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' )
```

[ColumnLayoutExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutExample.ets#L20-L27) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.75307380119426038505841084226216:50001231000000:2800:2854CF5B63BFC5969A8C2172922B8E6E9835C9774D5C63F0C85112B537524A51.png)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.54339365988849291331464678781677:50001231000000:2800:979BCAE36B3F8B7AB4627F557C41A7E9245B5D7656DF4AF4B87D6E1D691BA65D.png)

 收起自动换行深色代码主题复制

```
Row ({ space : 35 }) { Text ( 'space: 35' ). fontSize ( 15 ). fontColor ( Color . Gray ) Row (). width ( '10%' ). height ( 150 ). backgroundColor ( 0xF5DEB3 ) Row (). width ( '10%' ). height ( 150 ). backgroundColor ( 0xD2B48C ) Row (). width ( '10%' ). height ( 150 ). backgroundColor ( 0xF5DEB3 ) }. width ( '90%' )
```

[RowLayoutExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutExample.ets#L20-L27) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.14520072373776479228164092802735:50001231000000:2800:2B9BE8C73F00A24752B7B770C1D3E41755BE7E030A833E7885196DE96880D662.png)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.42074530166800417786583507942080:50001231000000:2800:D5479F142C49BC71B04144A89326E051136788403B920E207332D608459714E2.png)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

 收起自动换行深色代码主题复制

```
Column ({}) { Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 300 ). backgroundColor ( 'rgb(242,242,242)' ). justifyContent ( FlexAlign . Start )
```

[ColumnLayoutJustifyContentStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentStart.ets#L20-L48) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.09007412915740071042940132109565:50001231000000:2800:F9AEE80828145C12A56F36C5079DAA087ABC682621F22BDD6042254E57264BA8.png)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

 收起自动换行深色代码主题复制

```
Column ({}) { Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 300 ). backgroundColor ( 'rgb(242,242,242)' ). justifyContent ( FlexAlign . Center )
```

[ColumnLayoutJustifyContentCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentCenter.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.23334769086019384621232911544894:50001231000000:2800:CC86ABCA87CDE1335C63FA364EFBC6D8701E9EF8525D5267D2003ACD69F3C284.png)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

 收起自动换行深色代码主题复制

```
Column ({}) { Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 300 ). backgroundColor ( 'rgb(242,242,242)' ). justifyContent ( FlexAlign . End )
```

[ColumnLayoutJustifyContentEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentEnd.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.63151662821444706439398422891721:50001231000000:2800:BE2232F77B44BB9F13666FFC3088DB15BE031AF64988DBD1F3B52EEEA58930A4.png)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

 收起自动换行深色代码主题复制

```
Column ({}) { Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 300 ). backgroundColor ( 'rgb(242,242,242)' ). justifyContent ( FlexAlign . SpaceBetween )
```

[ColumnLayoutJustifyContentSpaceBetween.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentSpaceBetween.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.60703140063852104455121018204202:50001231000000:2800:2766D89356A9CAF84C81ACF9CC8388C78CED36633750F11672CAA6C3C086E713.png)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

 收起自动换行深色代码主题复制

```
Column ({}) { Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 300 ). backgroundColor ( 'rgb(242,242,242)' ). justifyContent ( FlexAlign . SpaceAround )
```

[ColumnLayoutJustifyContentSpaceAround.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentSpaceAround.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.07010892446187207489865882305033:50001231000000:2800:6E73ED2653A49071DFD5B020A2E2AA254688160C98694863CDCE26AA7B6AC1E4.png)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

 收起自动换行深色代码主题复制

```
Column ({}) { Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 300 ). backgroundColor ( 'rgb(242,242,242)' ). justifyContent ( FlexAlign . SpaceEvenly )
```

[ColumnLayoutJustifyContentSpaceEvenly.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentSpaceEvenly.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.21071166569443860674681341446334:50001231000000:2800:F53820B117B6D8A598485C2C35DB67214AA2A4A1D2A50431D2E27401F1109356.png)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.58866260163317238220637570065499:50001231000000:2800:95A54E29E9642CADAE56C9321FDCB8517B5091799C8A8712DBFD021AD07EC15E.png)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

 收起自动换行深色代码主题复制

```
Row ({}) { Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 200 ). backgroundColor ( 'rgb(242,242,242)' ). justifyContent ( FlexAlign . Start )
```

[RowLayoutJustifyContentStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentStart.ets#L20-L29) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.63630346940168767828206146285441:50001231000000:2800:9C44FB47B59CD32355B69B188F209645EC5DC322F5EC0467F3AE121499E4CF7F.png)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

 收起自动换行深色代码主题复制

```
Row ({}) { Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 200 ). backgroundColor ( 'rgb(242,242,242)' ). justifyContent ( FlexAlign . Center )
```

[RowLayoutJustifyContentCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentCenter.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.30855695831470106170909112646881:50001231000000:2800:5898E7CD4BD52817DAC0BBCFF9E340C0A425BA6EB1E6347DD209CDC69F2E6AB1.png)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

 收起自动换行深色代码主题复制

```
Row ({}) { Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 200 ). backgroundColor ( 'rgb(242,242,242)' ). justifyContent ( FlexAlign . End )
```

[RowLayoutJustifyContentEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentEnd.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.18101235083916754631372405655131:50001231000000:2800:8C1302C5A086D3A01FADB0AC59FA8E2D2884D1C4CE6CF73CE78D99E89337A778.png)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

 收起自动换行深色代码主题复制

```
Row ({}) { Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 200 ). backgroundColor ( 'rgb(242,242,242)' ). justifyContent ( FlexAlign . SpaceBetween )
```

[RowLayoutJustifyContentSpaceBetween.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentSpaceBetween.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.10313025549661997990233813649686:50001231000000:2800:1C4C231F5BB6E34F5B591BCC185288B3C02AF36E65A100737E3C50FC1E73ACB0.png)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

 收起自动换行深色代码主题复制

```
Row ({}) { Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 200 ). backgroundColor ( 'rgb(242,242,242)' ). justifyContent ( FlexAlign . SpaceAround )
```

[RowLayoutJustifyContentSpaceAround.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentSpaceAround.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.76713068483280605368049844531490:50001231000000:2800:928E968F9C6515D7F57593AF191500CB1C05CD1286D9CA62A8FCF40AD54973CE.png)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

 收起自动换行深色代码主题复制

```
Row ({}) { Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 200 ). backgroundColor ( 'rgb(242,242,242)' ). justifyContent ( FlexAlign . SpaceEvenly )
```

[RowLayoutJustifyContentSpaceEvenly.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentSpaceEvenly.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.87082137707896209162324638592450:50001231000000:2800:362DF4291CE46D883280E6B6E2D246E21402446F0DB4EC59870F458D5403A0DE.png)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165905.27733742670066185978026489079644:50001231000000:2800:70F1678E24BAA199AA25686C385FADFC1E3AD206936C0B6B7B036541ACF16D7E.png)

- HorizontalAlign.Start：子元素在水平方向左对齐。

 收起自动换行深色代码主题复制

```
Column ({}) { Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). alignItems ( HorizontalAlign . Start ). backgroundColor ( 'rgb(242,242,242)' )
```

[RowLayoutHorizontalAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutHorizontalAlignStart.ets#L20-L40) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.03040844540782546902309535797037:50001231000000:2800:2D9A2EB94B7BEC3B7FB90BE72931C9D13D33E80E98D2314EFDF1E3492B360F73.png)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。

 收起自动换行深色代码主题复制

```
Column ({}) { Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). alignItems ( HorizontalAlign . Center ). backgroundColor ( 'rgb(242,242,242)' )
```

[RowLayoutHorizontalAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutHorizontalAlignCenter.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.06295188314066312394360335440522:50001231000000:2800:8960F43E163B010D7B4A0046EE192D29A70DEEC71D67E4DAF071EF6866D8D363.png)
- HorizontalAlign.End：子元素在水平方向右对齐。

 收起自动换行深色代码主题复制

```
Column ({}) { Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '80%' ). height ( 50 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). alignItems ( HorizontalAlign . End ). backgroundColor ( 'rgb(242,242,242)' )
```

[RowLayoutHorizontalAlignEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutHorizontalAlignEnd.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.28684898757021323958013143536644:50001231000000:2800:FC05C41D7547ADEF2B2A4988CE6E55A6455E537CEBCFEFA6412BCFC5FD6FC854.png)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.09666114025558403419155856041648:50001231000000:2800:16B8D54B11E3034BC689124591C5031E3201F5393018F61221B9E52DF50D4BA0.png)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。

 收起自动换行深色代码主题复制

```
Row ({}) { Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 200 ). alignItems ( VerticalAlign . Top ). backgroundColor ( 'rgb(242,242,242)' )
```

[RowLayoutVerticalAlignTop.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutVerticalAlignTop.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.00124384403145632120165918903679:50001231000000:2800:EAD29C95E3E37A0BF45A66A3EB8FA27D3FBF4EF707AA4655A88D52094AF3C72F.png)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。

 收起自动换行深色代码主题复制

```
Row ({}) { Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 200 ). alignItems ( VerticalAlign . Center ). backgroundColor ( 'rgb(242,242,242)' )
```

[RowLayoutVerticalAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutVerticalAlignCenter.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.72076523555146364893074008672964:50001231000000:2800:94D47FDC7544382C871EC7897AEB46077566965BB6EB704DD72C7C015C97DBBD.png)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。

 收起自动换行深色代码主题复制

```
Row ({}) { Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xD2B48C ) Column () { }. width ( '20%' ). height ( 30 ). backgroundColor ( 0xF5DEB3 ) }. width ( '100%' ). height ( 200 ). alignItems ( VerticalAlign . Bottom ). backgroundColor ( 'rgb(242,242,242)' )
```

[RowLayoutVerticalAlignBottom.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutVerticalAlignBottom.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.21994267553683589691394453702053:50001231000000:2800:611C68553562C07D1167304CB8EFBAAB5E937C6D268E6568A0C0EECD2E681F96.png)

## 自适应拉伸

在线性布局下，常用空白填充组件[Blank](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-blank)，在容器主轴方向自动填充空白空间，达到自适应拉伸效果。Row和Column作为容器，只需要添加宽高为百分比，当屏幕宽高发生变化时，会产生自适应效果。

 收起自动换行深色代码主题复制

```
@Entry @Component struct BlankExample { build ( ) { Column () { Row () { Text ( 'Bluetooth' ). fontSize ( 18 ) Blank () Toggle ({ type : ToggleType . Switch , isOn : true }) }. backgroundColor ( 0xFFFFFF ). borderRadius ( 15 ). padding ({ left : 12 }). width ( '100%' ) }. backgroundColor ( 0xEFEFEF ). padding ( 20 ). width ( '100%' ) } }
```

[BlankExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/BlankExample.ets#L15-L29) 

**图9** 竖屏（自适应屏幕窄边）

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.51124150035241968612839115275623:50001231000000:2800:5277EB75C6E40D189CBFFCCAF34D598979EB0C1948784760BBEB7A97240A8E40.png)

**图10** 横屏（自适应屏幕宽边）

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.01375107416415225400539775987548:50001231000000:2800:9E4E30AFA9BE3DAE6488046A1EC296C983B22D4CD8404F47C242D8765B53A1B8.png)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。

 收起自动换行深色代码主题复制

```
@Entry @Component struct LayoutWeightExample { build ( ) { Column () { Text ( '1:2:3' ). width ( '100%' ) Row () { Column () { Text ( 'layoutWeight(1)' ) . textAlign ( TextAlign . Center ) }. layoutWeight ( 1 ). backgroundColor ( 0xF5DEB3 ). height ( '100%' ) Column () { Text ( 'layoutWeight(2)' ) . textAlign ( TextAlign . Center ) }. layoutWeight ( 2 ). backgroundColor ( 0xD2B48C ). height ( '100%' ) Column () { Text ( 'layoutWeight(3)' ) . textAlign ( TextAlign . Center ) }. layoutWeight ( 3 ). backgroundColor ( 0xF5DEB3 ). height ( '100%' ) }. backgroundColor ( 0xffd306 ). height ( '30%' ) Text ( '2:5:3' ). width ( '100%' ) Row () { Column () { Text ( 'layoutWeight(2)' ) . textAlign ( TextAlign . Center ) }. layoutWeight ( 2 ). backgroundColor ( 0xF5DEB3 ). height ( '100%' ) Column () { Text ( 'layoutWeight(5)' ) . textAlign ( TextAlign . Center ) }. layoutWeight ( 5 ). backgroundColor ( 0xD2B48C ). height ( '100%' ) Column () { Text ( 'layoutWeight(3)' ) . textAlign ( TextAlign . Center ) }. layoutWeight ( 3 ). backgroundColor ( 0xF5DEB3 ). height ( '100%' ) }. backgroundColor ( 0xffd306 ). height ( '30%' ) } } }
```

[LayoutWeightExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/LayoutWeightExample.ets#L15-L60) 

**图11** 横屏

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.74876927762460344567176758681379:50001231000000:2800:B524F99A29DFE018F9F5858603D52A1EADF2794C7139B24C427A65D730893FC7.png)

**图12** 竖屏

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.24605579721697064490973393384312:50001231000000:2800:928F3BA6CD2AF832E2A78C03EB5DF386C951BEAA4B613133B708E1E32D0F0216.png)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。

 收起自动换行深色代码主题复制

```
@Entry @Component struct WidthExample { build ( ) { Column () { Row () { Column () { Text ( 'left width 20%' ) . textAlign ( TextAlign . Center ) }. width ( '20%' ). backgroundColor ( 0xF5DEB3 ). height ( '100%' ) Column () { Text ( 'center width 50%' ) . textAlign ( TextAlign . Center ) }. width ( '50%' ). backgroundColor ( 0xD2B48C ). height ( '100%' ) Column () { Text ( 'right width 30%' ) . textAlign ( TextAlign . Center ) }. width ( '30%' ). backgroundColor ( 0xF5DEB3 ). height ( '100%' ) }. backgroundColor ( 0xffd306 ). height ( '30%' ) } } }
```

[WidthExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/WidthExample.ets#L15-L40) 

**图13** 横屏

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.51539782932195030785539981803516:50001231000000:2800:75942B241FEA546588D59CAA999BE8AEE5321F674B915506F322A6AF626F2B0B.png)

**图14** 竖屏

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.06098456064697279277623149760969:50001231000000:2800:A89CEBD72C7A3B278C2CF5A1F85FE20051D31BBB95F307E26152255FAEF70358.png)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。

垂直方向布局中使用Scroll组件：

 收起自动换行深色代码主题复制

```
@Entry @Component struct ScrollVerticalExample { scroller : Scroller = new Scroller (); private arr : number [] = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]; build ( ) { Scroll ( this . scroller ) { Column () { ForEach ( this . arr , ( item?: number | undefined ) => { if (item){ Text (item. toString ()) . width ( '90%' ) . height ( 150 ) . backgroundColor ( 0xFFFFFF ) . borderRadius ( 15 ) . fontSize ( 16 ) . textAlign ( TextAlign . Center ) . margin ({ top : 10 }) } }, ( item: number ) => item. toString ()) }. width ( '100%' ) } . backgroundColor ( 0xDCDCDC ) . scrollable ( ScrollDirection . Vertical ) // 滚动方向为垂直方向 . scrollBar ( BarState . On ) // 滚动条常驻显示 . scrollBarColor ( Color . Gray ) // 滚动条颜色 . scrollBarWidth ( 10 ) // 滚动条宽度 . edgeEffect ( EdgeEffect . Spring ) // 滚动到边沿后回弹 } }
```

[ScrollVerticalExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ScrollVerticalExample.ets#L15-L47) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.03891126629126828860277750094643:50001231000000:2800:A80F47F54C7CDD1EF1332E02DB8C025809041AADADB0B91CB0FE5958D57F68A7.gif)

水平方向布局中使用Scroll组件：

 收起自动换行深色代码主题复制

```
@Entry @Component struct ScrollHorizontalExample { scroller : Scroller = new Scroller (); private arr : number [] = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]; build ( ) { Scroll ( this . scroller ) { Row () { ForEach ( this . arr , ( item?: number | undefined ) => { if (item){ Text (item. toString ()) . height ( '90%' ) . width ( 150 ) . backgroundColor ( 0xFFFFFF ) . borderRadius ( 15 ) . fontSize ( 16 ) . textAlign ( TextAlign . Center ) . margin ({ left : 10 }) } }) }. height ( '100%' ) } . backgroundColor ( 0xDCDCDC ) . scrollable ( ScrollDirection . Horizontal ) // 滚动方向为水平方向 . scrollBar ( BarState . On ) // 滚动条常驻显示 . scrollBarColor ( Color . Gray ) // 滚动条颜色 . scrollBarWidth ( 10 ) // 滚动条宽度 . edgeEffect ( EdgeEffect . Spring ) // 滚动到边沿后回弹 } }
```

[ScrollHorizontalExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ScrollHorizontalExample.ets#L15-L47) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165906.58436920892675359829345851224893:50001231000000:2800:6704310B6DFA7E3C6F866A5A8D58896F896F020CA05F266484039CBFF000CF55.gif)
# 线性布局 (Row/Column)

    

#### 概述

 

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/h4XkzyUFRMq6KZR1pMqwww/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=6722AE94C153971D5DE40CA8746F4C5F9F3ADAF4150572BAA80DB4733ABC012B)   

在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

   

**图1** Column容器内子元素排列示意图

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/dXy56nMgRC6FDWRv6TKGXg/zh-cn_image_0000002543213726.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=B00614F7FF4712C6446576AA9D68EF4794FD7BA9B89AB4B7895307CEE9CAA5F9)

 

**图2** Row容器内子元素排列示意图

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/qBRbBAsVQLGEiNGYQ0tI_Q/zh-cn_image_0000002573853639.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=D784774D19C0F3B348DD695243511CC718DA64E036F7F307967348B3C1936876)

    

#### 基本概念

 

- 布局容器：具有布局能力的容器组件，可以承载其他元素作为其子元素，布局容器会对其子元素进行尺寸计算和布局排列。
- 布局子元素：布局容器内部的元素。
- 主轴：线性布局容器在布局方向上的轴线，子元素默认沿主轴排列。Row容器主轴为水平方向，Column容器主轴为垂直方向（图示可参考弹性布局[基本概念](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout#基本概念)中的主轴）。
- 交叉轴：垂直于主轴方向的轴线。Row容器交叉轴为垂直方向，Column容器交叉轴为水平方向（图示可参考弹性布局[基本概念](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout#基本概念)中的交叉轴）。
- 间距：布局子元素的间距。

    

#### 布局子元素在排列方向上的间距

 

在布局容器内，可以通过space属性设置排列方向上子元素的间距，使各子元素在排列方向上有等间距效果。

    

#### [h2]Column容器内排列方向上的间距

 

**图3** Column容器内排列方向的间距图

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/2v-S9a6vQVaAL0NijsiC6w/zh-cn_image_0000002573973617.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=3DB8E7D1C94009B6BCBE5CCC7E41AC094C8EAF494C15D563B3285508F18BD7DB)

 

```
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/5ojFGnA1QwyebIw3E7K9TA/zh-cn_image_0000002543373388.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=C62802A2E091D194ECCA7EAC5AC1500FCFDE2B52C60043905354440588F932D5)

    

#### [h2]Row容器内排列方向上的间距

 

**图4** Row容器内排列方向的间距图

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/VFM-4igGRsuD86yg0UyJjQ/zh-cn_image_0000002543213728.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=D4F73ED63B58B8BFBFDC3AC38DCEEDC85A9A20B346E516ABF0B74BE1BFDF6199)

 

```
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/KXP3RFJxQ7OqrhEh54sUNQ/zh-cn_image_0000002573853641.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=BC2509D6F299D5BF37468152CB9782D82F4448C355ACF4E4B63BB1FBDB101D5C)

    

#### 布局子元素在主轴上的排列方式

 

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

    

#### [h2]Column容器内子元素在垂直方向上的排列

 

**图5** Column容器内子元素在垂直方向上的排列图

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/S2leR0OxSJyGL_7Ve9K4tQ/zh-cn_image_0000002573973619.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=B43EBA6B3D1F09924310D8E89D1BE9DE5BA6E2BFD5DA5FDAC1ABD0ECF9872628)

 

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

 

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/NeDCX6t1TlyOPeOcss0zsA/zh-cn_image_0000002543373392.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=6D62A33E80A33A51C0065C73DECA4752A8B67D9FDAE14E542D76202AC7D9633C)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

 

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/jH_dFe0UT8Ce1t4hL1x9DA/zh-cn_image_0000002543213730.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=9B482B7BB5DF038CDF80C81C89AC57D65855D423D878EC5F87F91C59F38CE8DF)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

 

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/MRzmuLNASkS3veEwYQk_XQ/zh-cn_image_0000002573853643.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=FEAB1CD5B136C3C095C7E9C169C7E013FDF945E0165EF2DDFAA5FD8B584C1BCC)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

 

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/tqgDF_pPTtOgWKzolgvjzA/zh-cn_image_0000002573973621.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=88CF63491F1B85207BB17CA7FB48E35072FB5909944B9B6F08C8C18E02F0ECFD)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

 

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/nYKTsko7TQO51PEUGahL9Q/zh-cn_image_0000002543373394.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=3AD807A98A0570B0722ED036896978247FE46B6C5EF4403609971796DBF853A0)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

 

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Sju3QacqST-vSvK6Hr1GJw/zh-cn_image_0000002543213732.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=A3ECEBB63550F842643F18DEAAF2CB3F0421495F1FBB68DF0969DDC4FBDDF58C)

    

#### [h2]Row容器内子元素在水平方向上的排列

 

**图6** Row容器内子元素在水平方向上的排列图

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/jrKHN7ZLRsayQgYm3S-eCQ/zh-cn_image_0000002573853645.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=B5FC1DCAAA63E4334E161CAACFB449AA5F522B168EB3C3683BB1C6C0D69AD293)

 

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

 

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/gY3E5OBnTA-sogfn5wOwVw/zh-cn_image_0000002573973623.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=CEE8157E2BA31FA4245E1526B1C7ED62639E652873C486E77D0C7FD49428DFD2)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

 

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/ARc_1OQER4WvixuNtoTghw/zh-cn_image_0000002543373396.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=3080B98889D2A86CAEA29BBC734F7AC547216CC21689F2B528FAF11D9E186F2D)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

 

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/IPc5RRmoSnSdNBApBUS58Q/zh-cn_image_0000002543213734.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=CCFED682C3D4BFD9084510935D2D7B0795A986EAD0AEE1E29679163100A852E3)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

 

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/o_3DLGqQQ4uyTfVzfdvHPg/zh-cn_image_0000002573853647.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=EB368EB9ED0AD0AF21E4A8249AF0EECF834841A4EB4499F167FB1D3FDFA38327)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

 

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/7PFV0Qd3QVqC_sYda_kK_w/zh-cn_image_0000002573973625.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=99A6D8B2579B228F339DBF95427C5E2E7B17637DDDB36B070CB7596F72E0578D)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

 

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/tqeaLrUDShifj9zaAgbOFw/zh-cn_image_0000002543373398.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=122EC47BD92A840577E18C684E17501C51328111C4EC3707DBA70B4310084C61)

    

#### 布局子元素在交叉轴上的对齐方式

 

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

 

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

    

#### [h2]Column容器内子元素在水平方向上的排列

 

**图7** Column容器内子元素在水平方向上的排列图

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/2P1HtikCQ-S_c5_O09yNiw/zh-cn_image_0000002543213736.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=3CD4105941584CD9EE43D9B486BE06FF1A16DAF96552BEA41F15902C39A47BF6)

 

- HorizontalAlign.Start：子元素在水平方向左对齐。

 

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)')

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/KUhQOhjNQ1ymM28cSdcjLA/zh-cn_image_0000002573853649.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=A8A0CA1B446E44FB2E4B707920591078F6BE5066477D3315CE42BA50F303A35F)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。

 

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)')

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/w6YQddo7QHWK_1MzG9Fn_g/zh-cn_image_0000002573973627.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=B69C09E5276846E29E819D5F56C231D10E3440CD8F18C8DAE7D9520AF78FCBBC)
- HorizontalAlign.End：子元素在水平方向右对齐。

 

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)')

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/_2_aJUKPTOGGklEWBdb7sA/zh-cn_image_0000002543373400.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=6BF88F699566D6C3D8C96F9396A576640F67A28FF9F12E55BF3A2A93ED4F1732)

    

#### [h2]Row容器内子元素在垂直方向上的排列

 

**图8** Row容器内子元素在垂直方向上的排列图

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/Z7hmneEpQWOpBEXG1JivJA/zh-cn_image_0000002543213738.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=1C4E439D033F8CC3F4B3C5005F8CADAB07DBA30C042D576F3CFB81CBABCB0C63)

 

- VerticalAlign.Top：子元素在垂直方向顶部对齐。

 

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)')

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/8LHazsuZRiupiUznKSOzDQ/zh-cn_image_0000002573853651.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=3246ECA2B1CFFBDB6B1B95064A96D3D525D06A0E46BAAA9509F86B364F7DEDE3)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。

 

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)')

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/kxHHAR6zR3qzwEK4s7H_Qw/zh-cn_image_0000002573973629.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=C250925A8CB084E9C3C08D803DE7155099D0FEA3B031570194EC8729C22FC77A)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。

 

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)')

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Lxv2aj_vRkGUcZ9tKqnIUQ/zh-cn_image_0000002543373402.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=928F42A119C7CE90F7C173456B057257BA32CF2CB244ACB5F426D97A045A1665)

    

#### 自适应拉伸

 

在线性布局下，常用空白填充组件[Blank](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-blank)，在容器主轴方向自动填充空白空间，达到自适应拉伸效果。Row和Column作为容器，只需要添加宽高为百分比，当屏幕宽高发生变化时，会产生自适应效果。

 

```
@Entry
@Component
struct BlankExample {
  build() {
    Column() {
      Row() {
        Text('Bluetooth').fontSize(18)
        Blank()
        Toggle({ type: ToggleType.Switch, isOn: true })
      }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 }).width('100%')
    }.backgroundColor(0xEFEFEF).padding(20).width('100%')
  }
}

```

 

**图9** 竖屏（自适应屏幕窄边）

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/r5oT5931SWCSvVyYYbxkDw/zh-cn_image_0000002543213740.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=B3630092B7A59AB7529B7A90A6426861CDAD8C5B4AB73F179D4E1F1854196546)

 

**图10** 横屏（自适应屏幕宽边）

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/TOF_i85aTaG6Yktc5Lep5Q/zh-cn_image_0000002573853653.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=C5F06CE3EC149D0B8FE802B8CEFB0A0E130980A264E3E36DA57745C5CBFF0BC1)

    

#### 自适应缩放

 

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

 

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。

 

```
@Entry
@Component
struct LayoutWeightExample {
  build() {
    Column() {
      Text('1:2:3').width('100%')
      Row() {
        Column() {
          Text('layoutWeight(1)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')

        Column() {
          Text('layoutWeight(2)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')

        Column() {
          Text('layoutWeight(3)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')

      }.backgroundColor(0xffd306).height('30%')

      Text('2:5:3').width('100%')
      Row() {
        Column() {
          Text('layoutWeight(2)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')

        Column() {
          Text('layoutWeight(5)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')

        Column() {
          Text('layoutWeight(3)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')
      }.backgroundColor(0xffd306).height('30%')
    }
  }
}

```

 

**图11** 横屏

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/JuZukb3gSU6SiHMFcKV4vw/zh-cn_image_0000002573973631.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=F1393163F350F340603EC9919F656B44830A6DE4CE314520A5F9C52B797A38EA)

 

**图12** 竖屏

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/7vPXyFzbQQiRAJkTNaVw_g/zh-cn_image_0000002543373404.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=B4E9AC42D8028B8C995B0164DA0E928366FE92FB0A4615671BB6934DCF642465)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。

 

```
@Entry
@Component
struct WidthExample {
  build() {
    Column() {
      Row() {
        Column() {
          Text('left width 20%')
            .textAlign(TextAlign.Center)
        }.width('20%').backgroundColor(0xF5DEB3).height('100%')

        Column() {
          Text('center width 50%')
            .textAlign(TextAlign.Center)
        }.width('50%').backgroundColor(0xD2B48C).height('100%')

        Column() {
          Text('right width 30%')
            .textAlign(TextAlign.Center)
        }.width('30%').backgroundColor(0xF5DEB3).height('100%')
      }.backgroundColor(0xffd306).height('30%')
    }
  }
}

```

 

**图13** 横屏

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/31Oh1JN1SG-WKEw2MdozUQ/zh-cn_image_0000002543213742.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=60153A2A93621C440B6117762B1C09B22A306EAB8FCB1535B57C409FDA5734FB)

 

**图14** 竖屏

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/XYBmAwMbRQ6yzrgBEPz2bQ/zh-cn_image_0000002573853655.png?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=728C3B7EA3343846E830ECCBD1CDCA17313A6BE912E232DF35670D69DEB0305E)

    

#### 自适应延伸

 

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

 

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。

 

垂直方向布局中使用Scroll组件：

 

```
@Entry
@Component
struct ScrollVerticalExample {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Scroll(this.scroller) {
      Column() {
        ForEach(this.arr, (item?:number|undefined) => {
          if(item != undefined){
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }
        }, (item:number) => item.toString())
      }.width('100%')
    }
    .backgroundColor(0xDCDCDC)
    .scrollable(ScrollDirection.Vertical) // 滚动方向为垂直方向
    .scrollBar(BarState.On) // 滚动条常驻显示
    .scrollBarColor(Color.Gray) // 滚动条颜色
    .scrollBarWidth(10) // 滚动条宽度
    .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/HBCougYUSAWDEMR-41ExbA/zh-cn_image_0000002573973633.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=BE638663B399C3578B13DB2A0F5BF32ACF70BB1763F2F3F54B6FB9C64DE5756E)

 

水平方向布局中使用Scroll组件：

 

```
@Entry
@Component
struct ScrollHorizontalExample {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Scroll(this.scroller) {
      Row() {
        ForEach(this.arr, (item?:number|undefined) => {
          if(item != undefined){
            Text(item.toString())
              .height('90%')
              .width(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ left: 10 })
          }
        })
      }.height('100%')
    }
    .backgroundColor(0xDCDCDC)
    .scrollable(ScrollDirection.Horizontal) // 滚动方向为水平方向
    .scrollBar(BarState.On) // 滚动条常驻显示
    .scrollBarColor(Color.Gray) // 滚动条颜色
    .scrollBarWidth(10) // 滚动条宽度
    .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/UTm9v0xVRsCdOvzQpfp4bQ/zh-cn_image_0000002543373406.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193731Z&HW-CC-Expire=86400&HW-CC-Sign=030409011E7F6AB37A3E9210640FCB571F2B798036DD42B929BC38F6D3257CB6)
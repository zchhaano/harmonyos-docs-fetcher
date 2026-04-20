# Navigation分栏开发

  

[Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)作为一个容器组件，提供了两种布局样式：单栏布局、分栏布局。分栏布局一般适用于宽屏设备，在分栏布局下，导航栏（navBar）会固定显示， 子页面（NavDestination）通过导航控制器（NavPathStack）切换显示， 在导航栏和子页面之间有一条分割线， 可以通过分割线拖拽控制左右显示的比例。架构图详见[Navigation基础架构介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-architecture)。

   

#### 分栏相关接口介绍

    

#### [h2]mode

 

[mode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#mode9)属性用于控制Navigation的显示模式，有三种模式：单栏，分栏，自适应。

 

**图1** 单栏（NavigationMode.Stack）效果

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/Slc90Z7eRtaURV1_QU-ouQ/zh-cn_image_0000002573973607.png?HW-CC-KV=V1&HW-CC-Date=20260420T191042Z&HW-CC-Expire=86400&HW-CC-Sign=D04B35D97D2EB5A734EB9917919C0E3B66F90931FDD62E87A7C9F79A71B5B109)

 

**图2** 分栏（NavigationMode.Split）效果

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/6cLtkuEvQ4WgxiA-y_PVIQ/zh-cn_image_0000002543373378.png?HW-CC-KV=V1&HW-CC-Date=20260420T191042Z&HW-CC-Expire=86400&HW-CC-Sign=F5ED4ADC4F6E164831C2D803D28A676E38FBFE60C59FC9B6CC43CB77B0395DDD)

 

**图3** 自适应（NavigationMode.Auto）效果

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/sKALWhIeRaKi5ZeI10zGHQ/zh-cn_image_0000002543213718.gif?HW-CC-KV=V1&HW-CC-Date=20260420T191042Z&HW-CC-Expire=86400&HW-CC-Sign=CEB6043C2E994F0B29D62C168AA91DE52D6C6F7826817310F4CDFD132575BD9D)

    

#### [h2]navBarPosition

 

[navBarPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navbarposition9)用于控制导航栏显示的位置，用navBarPosition控制导航栏显示位置时，会被系统语言所影响。比如，在以汉语、英语为代表的LTR语言体系下，NavBarPosition.Start指代的是导航栏出现在左侧，而在以阿拉伯语为代表的RTL语言体系下，NavBarPosition.Start则指代导航栏出现在右侧。类似的效果也出现在NavBarPosition.End上。

 

**NavBarPosition.Start**

 

**图4** 系统语言为LTR时NavBarPosition.Start效果

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/fbFbpzgBRYqosTel0O6Mpw/zh-cn_image_0000002573853631.png?HW-CC-KV=V1&HW-CC-Date=20260420T191042Z&HW-CC-Expire=86400&HW-CC-Sign=7ADEFD32F6A28B9791E2F96C6A6F08CF34EC7FA4815FADE28DA1991AC4DBEBC3)

 

**图5** 系统语言为RTL时NavBarPosition.Start效果

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/Z62PSOaiSgShCG-w5kexHg/zh-cn_image_0000002573973609.png?HW-CC-KV=V1&HW-CC-Date=20260420T191042Z&HW-CC-Expire=86400&HW-CC-Sign=0DF88BAA45B228C0903F8437B4918A930914386AA2B77FAEA397BA62AEB7BEDA)

 

**NavBarPosition.End**

 

**图6** 系统语言为LTR时NavBarPosition.End效果

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/0rQI6WxDSYqBon7ILXNj8Q/zh-cn_image_0000002543373380.png?HW-CC-KV=V1&HW-CC-Date=20260420T191042Z&HW-CC-Expire=86400&HW-CC-Sign=8837B8C0E387F0075889072B8BB86DC25A4FA901E341C62BEF29AE1A0B9694D6)

 

**图7** 系统语言为RTL时NavBarPosition.End效果

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/JkMLD0n_SCaXviLUwdUQYQ/zh-cn_image_0000002543213720.png?HW-CC-KV=V1&HW-CC-Date=20260420T191042Z&HW-CC-Expire=86400&HW-CC-Sign=835944CA65FAC4D713C9D33885EA02BD78C69AF2249A28E2201A673EEDC07C84)

    

#### [h2]enableDragBar

 

[enableDragBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#enabledragbar14)用于控制是否显示分栏的拖动按钮。

 

**图8** enableDragBar为false效果

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/mV6qyUZ6TZqBhtfPb6odTA/zh-cn_image_0000002573853633.png?HW-CC-KV=V1&HW-CC-Date=20260420T191042Z&HW-CC-Expire=86400&HW-CC-Sign=44474CE08EAA5192880B364B0336FA91543FC4A052809DCA475827EB5EE05D83)

 

**图9** enableDragBar为true

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/1EMYxEEuQJSeeUEUiLO_9Q/zh-cn_image_0000002573973611.png?HW-CC-KV=V1&HW-CC-Date=20260420T191042Z&HW-CC-Expire=86400&HW-CC-Sign=A8EF34A2BB1137840AA3503849D7805B0BF6C18D6A091CB58923B50359BA6922)

    

#### [h2]navBarWidth

 

[navBarWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navbarwidth9)用于控制导航栏的宽度。

    

#### [h2]navBarWidthRange

 

[navBarWidthRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navbarwidthrange10)用于设置导航栏宽度可调整的范围。

    

#### [h2]minContentWidth

 

[minContentWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#mincontentwidth10)用于控制分栏子页的最小宽度；分栏模式导航栏和子页中间会有一个分割线，在可调范围内，用户可以通过拖动分割线来调整导航栏和子页的显示大小。

    

#### [h2]hideNavBar

 

[hideNavBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#hidenavbar9)用于控制导航栏的显示状态，默认值为false。如果同时将mode配置为NavigationMode.Split且hideNavBar设置为true，则实际效果会显示为单栏。

    

#### [h2]enableModeChangeAnimation

 

[enableModeChangeAnimation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#enablemodechangeanimation15)用于控制是否开启单双栏切换的动画，默认开启。

    

#### [h2]splitPlaceholder

 

[splitPlaceholder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#splitplaceholder20)用于设置分栏模式下内容区的默认占位页。分栏模式在默认情况下，栈中没有页面时内容区展示空白，可使用此接口设置此区域的UI布局。

 

需要注意的是，占位页仅作为UI展示页，仅分栏模式空栈的情况下才展示，不受路由栈管理也不可获焦和响应事件。

    

#### 分栏开发示例

 

以开发一个新闻app的demo来演示如何使用Navigation分栏相关接口。

 

1. 新闻主页内容会放到左侧NavBar中，其中内容是一个新闻列表，用户点击每一条新闻标题时，右边会push一个详情页，用来展示新闻的信息。
2. 给左侧NavBar设置一个宽度范围，右侧子页区域也设置一个最小宽度。

 

配置的路由表：

 

```
{
  "routerMap": [
    {
      "name": "NewsDetail",
      "pageSourceFile": "src/main/ets/pages/navigation/splitmode/NewsDetail.ets",
      "buildFunction": "NewsDetailPageBuilder",
      "data": {
        "description": "this is DetailPageA"
      }
    }
  ]
}

```

 

子页代码：

 

```
// 自定义的参数类型，用于在push页面时给子页传递参数
export class NewsItem {
  public title: string;
  public overview: string;
  public content: string;

  constructor(title: string, overview: string, content: string) {
    this.title = title;
    this.overview = overview;
    this.content = content;
  }
}

@Builder
export function NewsDetailPageBuilder() {
  NewsDetail()
}

@Component
struct NewsDetail {
  @State title: string = '';
  @State content: string = '';

  build() {
    NavDestination() {
      Column() {
        Text(this.content)
      }
    }
    .title(this.title)
    .backgroundColor('#fff6e3c8')
    .onReady((ctx: NavDestinationContext) => {
      // 在onReady生命周期拿到传来的页面参数
      let param = ctx.pathInfo.param as NewsItem;
      this.title = param?.title;
      this.content = param?.content;
    })
  }
}

```

 

主页代码：

 

```
import { NewsItem } from './NewsDetail'

@Component
struct NewsHome {
  private newsItemArray: Array<NewsItem> = [];
  private stack: NavPathStack | undefined = undefined;

  aboutToAppear(): void {
    // 这里省略了从网络获取新闻信息的过程
    for (let i = 0; i < 50; i++) {
      this.newsItemArray.push(new NewsItem(`新闻标题${i + 1}`, `新闻概述${i + 1}`, `新闻详情${i + 1}`))
    }
    let info = this.queryNavigationInfo();
    this.stack = info?.pathStack;
  }

  build() {
    List() {
      ForEach(this.newsItemArray, (item: NewsItem, index: number) => {
        ListItem() {
          Column() {
            Text(`${item.title}`).margin(15).fontSize(25).fontColor(Color.Black)
            Text(`${item.overview}`).fontSize(13).fontColor(Color.Gray)
          }.margin({bottom: 15}).backgroundColor('#eeeeee').width('100%')
          .borderRadius(15).height(120).onClick(() => {
            // 用户点击某一个新闻标签时，就在右侧子页区域push一个NavDestination页面，用来展示新闻详情
            this.stack?.pushPath({name: 'NewsDetail', param: item})
          })
        }.width('100%')
      }, (item: NewsItem, index: number) => {
        return item.title;
      })
    }.width('100%').height('100%').padding(15)
  }
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();
  @State navWidth: number = 100;

  build() {
    RelativeContainer() {
      Navigation(this.stack) {
        NewsHome().width('100%').height('100%')
      }
      .mode(NavigationMode.Split)
      .enableDragBar(true)
      .hideNavBar(false)
      .navBarWidthRange([100, 700]) // 指定NavBar区域的宽度范围
      .minContentWidth(100) // 指定子页区域的最小宽度
      .hideTitleBar(true)
      .hideToolBar(true)
      .height('100%')
      .width(`${this.navWidth}%`)
      .alignRules({
        top: { anchor: '__container__', align: VerticalAlign.Top },
        left: { anchor: '__container__', align: HorizontalAlign.Start }
      })
    }
  }
}

```

 

**图10** 运行效果

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/b8zrwGTZSNWG6pxC5gE3Wg/zh-cn_image_0000002543373382.gif?HW-CC-KV=V1&HW-CC-Date=20260420T191042Z&HW-CC-Expire=86400&HW-CC-Sign=B667DD575C2E77FE0BEB2EB5B4E34D8FAC3023C5312A4822F03CAB874FE92D13)
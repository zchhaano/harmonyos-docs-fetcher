# Navigation基础架构介绍

  

导航组件（[Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)）主要用于实现[NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)页面间的跳转，支持在不同NavDestination间传递参数，提供灵活的跳转栈操作，从而更便捷地实现对不同页面的访问和复用。

   

#### Navigation整体架构

 

Navigation组件结构较为复杂，包含几个关键概念：

 

- [Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)：导航根视图容器，所有的导航页面都被此容器包裹，提供分栏显示的能力，一般用作全局的根容器。
- [NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)：子页面容器，导航的所有页面路由操作均是针对NavDestination的操作，主要包含：       

  - [标题栏](#标题栏)：位于NavDestination顶部，包括返回按钮、标题，系统提供默认风格，同时支持自定义。
  - [菜单栏](#菜单栏)：位于NavDestination顶部，系统提供默认风格，同时支持自定义。
  - 内容区：NavDestination的子组件，内容由开发者自定义。
  - [工具栏](#工具栏)：位于NavDestination底部，系统提供默认风格，同时支持自定义。
- [NavBar](#navbar导航栏)：导航栏，也称为主页面，主要包含：       

  - [标题栏](#标题栏)：位于NavBar顶部，包括返回按钮、标题，系统提供默认风格，同时支持自定义。
  - [菜单栏](#菜单栏)：位于NavBar顶部，系统提供默认风格，同时支持自定义。
  - 内容区：位于NavBar中心区域，内容由开发者自定义。
  - [工具栏](#工具栏)：位于NavBar底部，系统提供默认风格，同时支持自定义。
- [NavPathStack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navpathstack10)：导航控制器，用于管理NavDestination页面栈，其封装了各种控制页面跳转的接口，支持继承后重写，需与Navigation绑定使用。

 

**图1** Navigation总体架构图

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/YcPzWcM8QzO4MGqwq70ToA/zh-cn_image_0000002543373370.png?HW-CC-KV=V1&HW-CC-Date=20260420T191037Z&HW-CC-Expire=86400&HW-CC-Sign=73AE634EA88840DB6EF6202A1EE28C59741BBA22133292E1A4EC697E34F746ED)

 

此外Navigation提供两种布局模式：单栏模式、分栏模式，不同模式下的结构如下。

 

- 单栏模式：

 

当Navigation容器宽度小于600vp时，建议使用单栏模式。此模式下发生路由跳转时，整个页面都会被替换。

 

**图2** 单栏布局示意图

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/78gS4l9sRZO0-SjkhTsTiw/zh-cn_image_0000002543213710.png?HW-CC-KV=V1&HW-CC-Date=20260420T191037Z&HW-CC-Expire=86400&HW-CC-Sign=C63DB9096F5B3E78DC7A701CCC41051CEB3EE2EA77221C4BE5999E71F53F0F1C)

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/0m2jnQocTfajGPRkIM30Mw/zh-cn_image_0000002573853623.jpg?HW-CC-KV=V1&HW-CC-Date=20260420T191037Z&HW-CC-Expire=86400&HW-CC-Sign=79F7D0A91500757D76257928D5576CEB4931D9BD1151BF436B23D83B84B154B9)
- 分栏模式：

 

当Navigation容器宽度大于等于600vp时，建议使用分栏模式。此模式下Navigation分为左右两部分，左侧为导航栏（NavBar），右侧为子页面（NavDestination）。发生路由跳转时，只有右边子页会被替换。

 

**图3** 分栏布局示意图

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Of67W8GwRdK5ISWdIHSPFQ/zh-cn_image_0000002573973601.png?HW-CC-KV=V1&HW-CC-Date=20260420T191037Z&HW-CC-Expire=86400&HW-CC-Sign=89FA83EC119D7BCE49FEBDD44929025A1DE2BF6B4946DF136C826B3C33AD093F)

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/A3jB2ADmQQWw3dG3XUS_aw/zh-cn_image_0000002543373372.jpg?HW-CC-KV=V1&HW-CC-Date=20260420T191037Z&HW-CC-Expire=86400&HW-CC-Sign=AA78722130A969DA056C0239B51EBCABFFACF35011C92C8A523C9C122AAB4BC2)

    

#### Navigation（导航容器）

 

Navigation是路由导航的根视图容器，通常作为页面（@Entry修饰的自定义组件，定义为Router页面）的根容器（作为全局导航使用），包括单栏（Stack）、分栏（Split）和自适应（Auto）三种显示模式，Auto模式会基于Navigation组件的宽度自动在Stack和Split中切换。

 

Navigation组件本身可不作为显示容器，只用于承载路由的相关功能，如绑定导航控制器对象、路由切换、分栏显示、自定义转场动画控制等。

 

Navigation组件主要包含导航栏（NavBar）和子页（NavDestination），子页通过栈结构管理，存在NavPathStack中。导航栏又称Navbar，作为Navigation的子组件，直接挂载到Navigation上，可以通过[hideNavBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#hidenavbar9)属性进行隐藏（单栏应用推荐隐藏导航页），导航栏不存在页面栈中。

 

子页面是一个以NavDestination为根节点的子树，通过[@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)构造出来，再通过NavPathStack提供的栈操作方法挂载到Navigation上显示，详见[Navigation子页面](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-navdestination)。

    

#### NavDestination（子页面容器）

 

Navigation子页面的根容器，每个子页面都需要包裹在一个NavDestination中，通过NavPathStack提供的栈操作方法（push、pop等）将子页面挂载到Navigation上显示或删除。

 

NavDestination作为页面根容器，除了支持普通组件的通用属性外，还支持页面相关的属性，如：[页面的生命周期](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#事件)，页面[工具栏](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#toolbarconfiguration13)、[标题栏](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#title)与[菜单栏](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#menus12)，[自定义页面转场动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#customtransition15)，页面级窗口属性控制（横竖屏、系统状态栏、系统导航条）等能力。

    

#### NavBar（导航栏）

 

Navigation中直接加载的孩子节点称为导航栏（NavBar），单栏显示时它是整个导航的首页，分栏显示时它是固定的导航栏。分栏显示时默认显示在左边，也可以通过[navBarPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navbarposition9)属性控制。

 

开发者可以通过[hideNavBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#hidenavbar9)控制导航栏的显隐，也可以通过[navBarWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navbarwidth9)属性控制双栏显示下的Navbar宽度，NavBar本身不属于页面栈中的页面，不具备页面的生命周期等，不能通过NavPathStack的方法控制。 开发者可以通过[onNavBarStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#onnavbarstatechange9)去感知导航栏的显隐，通过[mode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#mode9)属性控制单双栏切换，也可以通过[onNavigationModeChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#onnavigationmodechange11)去感知单双栏的切换。

 

NavBar的内容区可以通过两种方式指定：

 

- 方式一：直接指定Navigation的子节点。

 

```
@Entry
@Component
struct NavigationDemo {
  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();
  private listArray: Array<string> = ['WLAN', 'Bluetooth', 'Personal Hotspot', 'Connect & Share'];
  context = this.getUIContext().getHostContext();
  build() {
    Column() {
      Navigation(this.navPathStack) {
        // 请将$r('app.string.enterKeyWordsToSearch')替换为实际资源文件，在本示例中该资源文件的value值为"输入关键字搜索"
        TextInput({ placeholder: $r('app.string.enterKeyWordsToSearch') })
          .width('90%')
          .height(40)
          .margin({ bottom: 10 })

        // 通过List定义导航的一级界面
        List({ space: 12, initialIndex: 0 }) {
          ForEach(this.listArray, (item: string) => {
            ListItem() {
              Row() {
                Row() {
                  Text(`${item.slice(0, 1)}`)
                    .fontColor(Color.White)
                    .fontSize(14)
                    .fontWeight(FontWeight.Bold)
                }
                .width(30)
                .height(30)
                .backgroundColor('#a8a8a8')
                .margin({ right: 20 })
                .borderRadius(20)
                .justifyContent(FlexAlign.Center)

                Column() {
                  Text(item)
                    .fontSize(16)
                    .margin({ bottom: 5 })
                }
                .alignItems(HorizontalAlign.Start)

                Blank()

                Row()
                  .width(12)
                  .height(12)
                  .margin({ right: 15 })
                  .border({
                    width: { top: 2, right: 2 },
                    color: 0xcccccc
                  })
                  .rotate({ angle: 45 })
              }
              .borderRadius(15)
              .shadow({ radius: 100, color: '#ededed' })
              .width('90%')
              .alignItems(VerticalAlign.Center)
              .padding({ left: 15, top: 15, bottom: 15 })
              .backgroundColor(Color.White)
            }
            .width('100%')
            .onClick(() => {
              // $r('app.string.detailsPageParameters')需要替换为开发者所需的字符串资源文件,资源文件中的value值为“详情页面参数”
              this.navPathStack.pushPathByName(`${item}`,
                // 将name指定的NaviDestination页面信息入栈,传递的参数为param
                this.context!.resourceManager.getStringSync($r('app.string.detailsPageParameters').id));
            })
          }, (item: string): string => item)
        }
        .listDirection(Axis.Vertical)
        .edgeEffect(EdgeEffect.Spring)
        .sticky(StickyStyle.Header)
        .chainAnimation(false)
        .width('100%')
      }
      .width('100%')
      .mode(NavigationMode.Auto)
      // $r('app.string.settings')需要替换为开发者所需的字符串资源文件,资源文件中的value值为“设置”
      .title($r('app.string.settings')) // 设置标题文字
    }
    .size({ width: '100%', height: '100%' })
    .backgroundColor(0xf4f4f5)
  }
}

```

 

- 方式二：从API version 20开始，使用[主页类型NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navigation20)将某个NavDestination直接指定为导航栏内容，此方法需要配置路由表，配置方式请参考[路由表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-cross-package#路由表能力对比)。

    

#### NavPathStack（导航控制器）

 

Navigation的子页面栈存在NavPathStack中，每个Navigation都需要绑定一个NavPathStack对象，NavPathStack用于控制Navigation中所有子页的切换。NavPathStack提供了很多基础的路由切换方法，如：[pushPath](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pushpath10)、[pop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pop10)、[replacePath](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#replacepath11)等，以及路由拦截、转场动画控制、路由栈信息获取等能力。

 

NavPathStack也支持开发者继承并复写相关路由操作方法。NavPathStack跟Navigation一一对应，在每个子页中可以通过NavDestination的[onReady](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#onready11)回调获取，也可以全局维护一个单例的NavPathStack，在任意地方获取并执行路由操作（注意：页面切换动画和布局必须在UI线程中才可以生效，依赖Vsync信号）。

    

#### 标题栏

 

标题栏在界面顶部，用于呈现界面名称和操作入口，Navigation组件通过[title](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#title)属性设置标题内容，通过[titleMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#titlemode)属性设置标题栏模式。NavDestination同样支持[title](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#title)属性用于设置标题内容。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/Kuw45cadT1i3JvK5qRZB5A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T191037Z&HW-CC-Expire=86400&HW-CC-Sign=506D452158203CBADA44782A8A02F56134AEA0478B113C52B3B325E1A2CD77F5)   

Navigation未设置[title](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#title)、[titleMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#titlemode)、[menus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#menus)等与标题、菜单栏相关的属性时，即使将[hideBackButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#hidebackbutton)设置为false，返回按钮也不会展示。

   

- Mini模式：

 

普通型标题栏，用于一级页面不需要突出标题的场景。

 

**图4** Mini模式标题栏

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/ZkA4LLH8QSS_wFV-DXev4g/zh-cn_image_0000002543213712.jpg?HW-CC-KV=V1&HW-CC-Date=20260420T191037Z&HW-CC-Expire=86400&HW-CC-Sign=F328965B2D7881E994660E5D2A016EBB4A7F8206D7B1BF448D69131E48DB0B74)

 

```
Navigation() {
  // ...
}
.titleMode(NavigationTitleMode.Mini)

```
- Full模式：

 

强调型标题栏，用于一级页面需要突出标题的场景。

 

**图5** Full模式标题栏

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ojnw990kScaGk2WqhPlOHA/zh-cn_image_0000002573853625.jpg?HW-CC-KV=V1&HW-CC-Date=20260420T191037Z&HW-CC-Expire=86400&HW-CC-Sign=2A39C8BE7A4F433DEA659CB2B8BCB54F5B5573A5B5B9B4227F90304EF24F8ED4)

 

```
Navigation() {
  // ...
}
.titleMode(NavigationTitleMode.Full)

```

    

#### 菜单栏

 

菜单栏位于组件的顶部，开发者可以通过[menus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#menus)属性设置Navigation的菜单栏。menus支持Array<[NavigationMenuItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navigationmenuitem)>和[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)两种参数类型。使用Array<[NavigationMenuItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navigationmenuitem)>类型时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。NavDestination同样支持[menus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#menus12)属性用于设置菜单栏。

 

**图6** 设置了3个图标的菜单栏

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/exRcFYAzTxyLVT4B8i8zBA/zh-cn_image_0000002573973603.jpg?HW-CC-KV=V1&HW-CC-Date=20260420T191037Z&HW-CC-Expire=86400&HW-CC-Sign=87C284E3C0DA04F432D9D86D868CC5945A2823FA0B14497DDC5AA7691EEC33BD)

 

```
let menuItem: NavigationMenuItem  = {
  'value': 'func',
  'icon': 'ets/pages/navigation/template1/image/ic_public_add.svg',
  'action': () => {}
};
// ...
      Navigation(this.navPathStack) {
        // ...
      }
      .menus([menuItem, menuItem, menuItem])

```

 

图片也可以引用resources中的资源。

 

```
let menuItem: NavigationMenuItem  = {
  'value': 'func',
  'icon': 'resources/base/media/ic_public_add.svg',
  'action': () => {}
};
// ...
      Navigation(this.navPathStack) {
        // ...
      }
      .menus([menuItem, menuItem, menuItem])

```

 

**图7** 设置了4个图标的菜单栏

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/PzBiyE7IS0OpArEOWdfzdg/zh-cn_image_0000002543373374.jpg?HW-CC-KV=V1&HW-CC-Date=20260420T191037Z&HW-CC-Expire=86400&HW-CC-Sign=1219707295FEEC1B678D87425C2857F33784B1683209463DDB8253432CFF8B69)

 

竖屏状态下菜单栏，最多支持显示3个按钮，当按钮超过3个时，多余的按钮会被折叠。

 

```
let menuItem: NavigationMenuItem  = {
  'value': 'func',
  'icon': 'ets/pages/navigation/template1/image/ic_public_add.svg',
  'action': () => {}
};
// ...
      Navigation(this.navPathStack) {
        // ...
      }
      // 竖屏最多支持显示3个图标，多余的图标会被放入自动生成的更多图标
      .menus([menuItem, menuItem, menuItem, menuItem])

```

    

#### 工具栏

 

工具栏位于组件的底部，开发者可以通过[toolbarConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#toolbarconfiguration10)属性设置Navigation的工具栏。NavDestination同样支持[toolbarConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#toolbarconfiguration13)属性用于设置工具栏。

 

**图8** 工具栏

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/Lv5ZMXfzTfK4UsWRbv3p7g/zh-cn_image_0000002543213714.jpg?HW-CC-KV=V1&HW-CC-Date=20260420T191037Z&HW-CC-Expire=86400&HW-CC-Sign=E6C70C20FD78D11B4A5EBA50BAF99EAB40907BF5F995E520B24F7DB4B3381D9A)

 

```
let toolTmp: ToolbarItem = {
  'value': 'func',
  'icon': 'ets/pages/navigation/template1/image/ic_public_highlights.svg',
  'action': () => {}
};
let toolBar: ToolbarItem[] = [toolTmp,toolTmp,toolTmp];
// ...
      Navigation(this.navPathStack) {
        // ...
      }
      .toolbarConfiguration(toolBar)

```
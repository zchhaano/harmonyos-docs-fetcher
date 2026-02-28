# 基于Page的装饰器方案

开发者使用@InsightIntentPage装饰器进行基于Page的意图声明，可快速将已有的Page页面接入意图框架，以购买电影票的意图为例，详细说明如下：

1. 装饰器添加位置：基于Page的装饰器需要添加在Entry页面组件上，建议在目标页面中进行声明。收起自动换行深色代码主题复制

```
import { InsightIntentPage } from "@ohos.app.ability.InsightIntentDecorator" ; @Builder export function PurchaseMovieTicketsIntentPageBuilder ( pageName: string , param: object ) { PurchaseMovieTicketsIntentPage ({ param : param }); } @InsightIntentPage ({ intentName : 'PurchaseMovieTickets' , domain : 'PurchaseTickets' , intentVersion : '1.0.1' , displayName : '购买电影票' , llmDescription : '用于在线购买电影票，允许用户选择指定影院、电影和场次时间进行购票。在用户明确表达购票需求，且已提供所有必要信息（cinema, film, time）时使用。如果信息不全或者用户只是查询电影信息、放映时间或票价，不应调用此工具。' , uiAbility : 'EntryAbility' , pagePath : './ets/pages/MainPage' , navDestinationName : 'PurchaseMovieTicketsIntentPage' , parameters : { "type" : "object" , "properties" : { "cinema" : { "type" : "string" , "description" : "目标影院名称，仅支持平台合作的影院" }, "film" : { "type" : "string" , "description" : "目标电影名称，需为当前上映或即将上映且在影院排片列表中的电影" }, "time" : { "type" : "string" , "description" : "放映时间，必须为未来的场次，且需为影院当天有效排片时间；时间格式应为'YYYY-MM-DD HH:MM'（例如'2025-07-01 19:30'）" } }, "required" : [ "cinema" , "film" , "time" ] } }) @Entry @Component struct PurchaseMovieTicketsIntentPage { param : object = new Object (); cinema : string = '' ; film : string = '' ; time : string = '' ; aboutToAppear (): void { this . cinema = this . param ?.[ 'cinema' ]; this . film = this . param ?.[ 'film' ]; this . time = this . param ?.[ 'time' ]; } build ( ) { NavDestination (){ Text ( ` ${ this .cinema} ${ this .film} ${ this .time} ` ) . fontSize ( 30 ) . fontWeight ( FontWeight . Bolder ) } . title ( 'IntentPage' ) . width ( '100%' ) } }
```
2. 装饰器的字段说明以及示例：@InsightIntentPage字段以及具体说明如下。 展开

| 字段名称 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| intentName | string | 是 | 意图名称，最大长度：64。 |
| domain | string | 是 | 意图所属的功能垂域。 |
| intentVersion | string | 是 | 意图的版本号，用于兼容性管理。 |
| displayName | string | 是 | 意图的展示名称，用于界面显示，最大长度：64。 |
| llmDescription | string | 否 | 意图的描述，详细描述该意图可实现的能力，便于大模型理解并调用。 |
| parameters | Record<string, object> | 否 | 意图参数定义，描述参数类型以及含义。 |
| uiAbility | string | 否 | 页面依赖的UiAbility名，如果不传递默认使用EntryAbility。 |
| pagePath | string | 是 | Navigation组件所在页面的路径，路径基于Module的根目录的相对路径。 |
| navDestinationName | string | 否 | Navigation子页面名称，如果不填写，则跳转到pagePath指定的页面。 |

为便于大模型理解和调用，相关参数定义需要遵照[自定义意图相关信息定义规范](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-specification)。
3. 装饰器的添加方式：装饰器可以直接手动添加，同时也支持一键生成装饰器，建议使用后者，此方式需要安装相应插件，详细步骤如下。

  1. 打开CodeGenie插件：在DevEco Studio右侧边栏点击CodeGenie或输入快捷键Alt/Option+U，可以进入DevEco CodeGenie。若使用非最新版本的DevEco Studio，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取并使用相关功能，具体请参考[插件获取及安装](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codegenie#section18337533718)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165259.34995839458194885665978733625808:50001231000000:2800:CDED2D6D15881240404182DE380C4B64103385A3B17E4390437A6DE6123826E5.png)
  2. 框选想要接入意图框架功能的代码。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165259.38347560459092285015778781353491:50001231000000:2800:1D585E2BA29F60FF080E92C3FCD54560F6E734A394CA53726DC5C9913CE79E34.png)
  3. 在选中的代码块上右键CodeGenie > Insight Intent > 选择适合的装饰器。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165259.42578848705126338910839982304586:50001231000000:2800:756F41B192914727A62A0AE051A103F6E14490384BC4B76F9B2B72A75BB240F1.png)
  4. 在DevEco CodeGenie对话框中对意图定义，功能，参数等进行描述。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165259.83408340498335236341764435461191:50001231000000:2800:2D3F6DF9196EE0935E3007639310C40EFC158E612FC5E2012C30F1391E5F2825.png)
  5. 回车或者点击发送按钮，即可生成对应的装饰器内容。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165259.19275503681234000439258393654129:50001231000000:2800:71C97F45B8D57C3B4878AD3C793F809580E3E3FDCFF308A05F48F8F308D844BD.png)
  6. 将光标放置于要插入装饰器的位置，点击插入图标，即可在对应位置插入装饰器。

插入前：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165300.36871719242074498213594509460838:50001231000000:2800:4CFB579136DA6F5C8B66E3C5E8301CB14453D2C1CAFB9AC28D44CF1938B86B91.png)

插入后：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165300.90987782914160539125243939989341:50001231000000:2800:21CCAEB2C4D8B38BB4C9DA69CB058ECF8CE5F321F8B237553E9064F70FA6F004.png)
4. 装饰器的使用约束和说明：

  - 仅支持Navigation页面架构跳转。
  - 该跳转不能有自定义上下文依赖，比如必须打开前置页面才能跳转，开发者需要进行验证，确认兜底策略。
  - 跳转页面时，默认使用Navigation页面栈进行push，如果开发者需要实现其他跳转逻辑，则需要自行适配。
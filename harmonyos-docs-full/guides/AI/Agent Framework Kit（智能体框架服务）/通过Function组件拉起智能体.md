## 场景介绍

- Function组件分为图标组件和按钮组件，无标题时默认显示图标组件，有标题时默认显示按钮组件。       

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165225.29545986033622162710305070897405:50001231000000:2800:C7F57F3F48AFC074E550A7059EA6523DA5F750DFB4046EF225460957BD0FC29D.png)
- Function图标组件效果：综合型入口。不带用户意图，可作为应用内智能体主入口。       

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165225.60288981952784887358975743953857:50001231000000:2800:C1974EDA297309A69F3E4F96866D774C8BBA3AA42688ECE86DF8469C64423C56.png)
- Function按钮组件：允许应用自定义功能描述的组件。       

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165225.04453185775598071643871511302226:50001231000000:2800:53D424165F3DC9CCB3265C9AFE32009646807282D0FC18C573944C0FA6995857.png)

## 开发前准备

- 创建智能体，具体请参见[快速创建智能体](https://developer.huawei.com/consumer/cn/doc/service/quick-start-0000002469548009)。
- 关联应用，具体请参见[关联应用](https://developer.huawei.com/consumer/cn/doc/service/related-applications-0000002437785706)。
- 确保已在终端设备上登录华为账号，并且处于联网状态。

## 开发步骤

1. 从项目根目录进入/src/main/ets/pages/Index.ets文件，将FunctionComponent及相关其它类引入到工程。 

 收起自动换行深色代码主题复制

```
import { FunctionComponent , FunctionController } from '@kit.AgentFrameworkKit' ; import { BusinessError } from "@kit.BasicServicesKit" ; import { hilog } from "@kit.PerformanceAnalysisKit" ; import { common } from '@kit.AbilityKit'
```
2. （可选）可以在组件加载前通过[isAgentSupport](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/hmaf-function-component#section123851974413)来判断当前的AgentId是否可用，若agentId有效且Agent功能支持时再加载组件。 

 收起自动换行深色代码主题复制

```
@State isAgentSupport : boolean = false ; aboutToAppear ( ) { this . checkAgentSupport () } async checkAgentSupport ( ) { try { let context = this . getUIContext ()?. getHostContext () as common. UIAbilityContext ; this . isAgentSupport = await this . controller . isAgentSupport (context, this . agentId ) } catch (err) { hilog. error ( 0x0001 , 'AgentExample' , `err code: ${err.code} , message: ${err.message} ` ) } } build ( ) { Column () { if ( this . isAgentSupport ) { FunctionComponent ({ agentId : this . agentId , onError : ( err: BusinessError ) => { hilog. error ( 0x0001 , 'AgentExample' , `err: ${ JSON .stringify(err)} , message: ${err.message} ` ) }, options : { title : '智能创建' , queryText : '创建一个新的模式' } }) } } }
```
3. 构建一个简单配置的页面，在页面中引入FunctionComponent组件，并传入对应的参数。其中agentId、onError是必填参数。其他可选参数可参见[FunctionComponent（功能组件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/hmaf-function-component)。Function组件布局可参考[组件布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development)。 

 收起自动换行深色代码主题复制

```
@Entry @Component export struct AgentExample { private controller : FunctionController = new FunctionController (); private agentId : string = 'agentproxy65481da1fa2293a8482d45' ; // 拉起智能体时对应的agentid，创建智能体时从小艺智能体平台获取 build ( ) { Column () { FunctionComponent ({ agentId : this . agentId , onError : ( err: BusinessError ) => { hilog. error ( 0x0001 , 'AgentExample' , `err: ${ JSON .stringify(err)} , message: ${err.message} ` ) }, options : { title : '' , queryText : '' }, controller : this . controller }) } } }
```
4. 添加订阅事件。 

 收起自动换行深色代码主题复制

```
aboutToAppear ( ) { this . initListeners () } initListeners ( ) { this . controller ?. on ( 'agentDialogOpened' , this . onAgentOpenedCallback ) this . controller ?. on ( 'agentDialogClosed' , this . onAgentClosedCallback ) } onAgentOpenedCallback = () => { hilog. info ( 0x0001 , 'AgentExample' , 'agent dialog opened callback' ) } onAgentClosedCallback = () => { hilog. info ( 0x0001 , 'AgentExample' , 'agent dialog closed callback' ) } aboutToDisappear ( ) { this . controller ?. off ( 'agentDialogOpened' ) this . controller ?. off ( 'agentDialogClosed' ) } build ( ) { Column () { FunctionComponent ({ agentId : this . agentId , onError : ( err: BusinessError ) => { hilog. error ( 0x0001 , 'AgentExample' , `err: ${ JSON .stringify(err)} , message: ${err.message} ` ) }, controller : this . controller }) } }
```

## 开发实例

       点击按钮，打开智能体对话框。      收起自动换行深色代码主题复制

```
import { BusinessError } from "@kit.BasicServicesKit" ; import { hilog } from "@kit.PerformanceAnalysisKit" ; import { FunctionComponent , FunctionController } from "@kit.AgentFrameworkKit" ; @Entry @Component export struct AgentExample { private controller : FunctionController = new FunctionController (); private agentId : string = 'agentproxy65481da1fa2293a8482d45' ; // 拉起智能体时对应的agentid，创建智能体时从小艺智能体平台获取 aboutToAppear ( ) { this . initListeners () } initListeners ( ) { this . controller ?. on ( 'agentDialogOpened' , this . onAgentOpenedCallback ) this . controller ?. on ( 'agentDialogClosed' , this . onAgentClosedCallback ) } onAgentOpenedCallback = () => { hilog. info ( 0x0001 , 'AgentExample' , 'agent dialog opened callback' ) } onAgentClosedCallback = () => { hilog. info ( 0x0001 , 'AgentExample' , 'agent dialog closed callback' ) } aboutToDisappear ( ) { this . controller ?. off ( 'agentDialogOpened' ) this . controller ?. off ( 'agentDialogClosed' ) } build ( ) { Column () { FunctionComponent ({ agentId : this . agentId , onError : ( err: BusinessError ) => { hilog. error ( 0x0001 , 'AgentExample' , `err: ${ JSON .stringify(err)} , message: ${err.message} ` ) }, options : { title : '智能创建' , queryText : '创建一个新的情景' , isShowShadow : true }, controller : this . controller }) } } }
```
# 拉起邮件类应用（startAbilityByType）

本章节介绍如何拉起邮件类应用扩展面板。

 说明 

如果拉起方的参数为mailto协议字符串，可以[使用mailto方式拉起邮件应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-email-apps-by-mailto)。邮件应用会解析收到的mailto协议字符串，并填充发件人、收件人、邮件内容等信息。

## 邮件类应用扩展面板参数说明

startAbilityByType接口中type字段为mail，对应的wantParam参数：

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| email | string[ ] | 否 | 收件人邮箱地址（支持多个且以逗号分隔）。 |
| cc | string[ ] | 否 | 抄送人邮箱地址（支持多个且以逗号分隔）。 |
| bcc | string[ ] | 否 | 密送人邮箱地址（支持多个且以逗号分隔）。 |
| subject | string | 否 | 邮件主题。 |
| body | string | 否 | 邮件内容。 |
| ability.params.stream | string[ ] | 否 | 邮件附件（附件的uri地址列表）。 |
| ability.want.params.uriPermissionFlag | wantConstant.Flags | 否 | 给邮件附件赋予至少读权限。邮件附件参数存在时，该参数也必须要传。 |
| sceneType | number | 否 | 意图场景，表明本次请求对应的操作意图。1：发邮件。默认为1。 |

  说明 

- 邮件类应用扩展面板中的类型为string的参数，都要经过encodeURI编码。
- 邮件类应用扩展面板中的类型为string[]的参数，数组中的元素都要经过encodeURI编码。

## 拉起方开发步骤

1. 导入相关模块。

 收起自动换行深色代码主题复制

```
import { common, wantConstant } from '@kit.AbilityKit' ;
```
2. 构造接口参数并调用startAbilityByType接口。

 收起自动换行深色代码主题复制

```
@Entry @Component struct Index { @State hideAbility : string = 'hideAbility' build ( ) { Row () { Column () { Text ( this . hideAbility ) . fontSize ( 30 ) . fontWeight ( FontWeight . Bold ) . onClick ( () => { let context = this . getUIContext (). getHostContext () as common. UIAbilityContext ; let wantParam : Record < string , Object > = { 'sceneType' : 1 , 'email' : [ encodeURI ( 'xxx@example.com' ), encodeURI ( 'xxx@example.com' )], // 收件人邮箱地址，多值以逗号分隔，对数组内容使用encodeURI()方法进行url编码 'cc' : [ encodeURI ( 'xxx@example.com' ), encodeURI ( 'xxx@example.com' )], // 抄送人邮箱地址，多值以逗号分隔，对数组内容使用encodeURI()方法进行url编码 'bcc' : [ encodeURI ( 'xxx@example.com' ), encodeURI ( 'xxx@example.com' )], // 密送人邮箱地址，多值以逗号分隔，对数组内容使用encodeURI()方法进行url编码 'subject' : encodeURI ( '邮件主题' ), // 邮件主题，对内容使用encodeURI()方法进行url编码 'body' : encodeURI ( '邮件正文' ), // 邮件正文，对内容使用encodeURI()方法进行url编码 'ability.params.stream' : [ encodeURI ( '附件uri1' ), encodeURI ( '附件uri2' )], // 附件uri，多值以逗号分隔，对数组内容使用encodeURI()方法进行url编码 'ability.want.params.uriPermissionFlag' : wantConstant. Flags . FLAG_AUTH_READ_URI_PERMISSION }; let abilityStartCallback : common. AbilityStartCallback = { onError : ( code: number , name: string , message: string ) => { console . error ( `onError code ${code} name: ${name} message: ${message} ` ); }, onResult : ( result ) => { console . info ( `onResult result: ${ JSON .stringify(result)} ` ); } } context. startAbilityByType ( "mail" , wantParam, abilityStartCallback, ( err ) => { if (err) { console . error ( `startAbilityByType fail, err: ${ JSON .stringify(err)} ` ); } else { console . info ( `success` ); } }); }); } . width ( '100%' ) } . height ( '100%' ) } }
```

效果示例图：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165929.42044944304975142454908258820989:50001231000000:2800:6FA97FF73314D723E8DD98DF67988F1F2929B48BD8DC72032D056CDE35F44CEA.png)

## 目标方开发步骤

1. 在module.json5中新增[linkFeature](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#skills标签)属性并设置声明当前应用支持的特性功能，从而系统可以从设备已安装应用中找到当前支持该特性的应用，取值范围如下：

  展开

| 取值 | 含义 |
| --- | --- |
| ComposeMail | 声明应用支持撰写邮件功能 |

  收起自动换行深色代码主题复制

```
{ "abilities" : [ { "skills" : [ { "uris" : [ { "scheme" : "mailto" , // 这里仅示意，应用需确保这里声明的uri能被外部正常拉起 "host" : "" , "path" : "" , "linkFeature" : "ComposeMail" // 声明应用支持撰写邮件功能 } ] } ] } ] }
```
2. 解析面板传过来的参数并做对应处理。

 收起自动换行深色代码主题复制

```
UIAbility . onCreate ( want : Want , launchParam : AbilityConstant . LaunchParam ): void
```

在参数**want.parameters**中会携带Caller方传入的参数（与调用方传入的有些差异），如下表所示：

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| email | string[ ] | 否 | 收件人邮箱地址（支持多个且以逗号分隔）。 |
| cc | string[ ] | 否 | 抄送人邮箱地址（支持多个且以逗号分隔）。 |
| bcc | string[ ] | 否 | 密送人邮箱地址（支持多个且以逗号分隔）。 |
| subject | string | 否 | 邮件主题。 |
| body | string | 否 | 邮件内容。 |
| stream | string[ ] | 否 | 邮件附件列表（附件的uri地址列表）。 |

  说明 

  - 目标方接收的类型为string的参数，都要经过decodeURI解码。
  - 目标方接收的类型为string[]的参数，数组中的元素都要经过decodeURI解码。

**完整示例：**

 收起自动换行深色代码主题复制

```
```
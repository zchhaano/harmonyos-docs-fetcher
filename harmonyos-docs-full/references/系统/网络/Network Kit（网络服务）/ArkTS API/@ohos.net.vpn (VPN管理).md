# @ohos.net.vpn (VPN管理)

  

本模块是操作系统提供的内置VPN功能，允许用户通过系统的网络设置进行VPN连接，通常提供的功能较少，而且有比较严格的限制。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/TCXnD8kXSWGCASNIsf3dmg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194349Z&HW-CC-Expire=86400&HW-CC-Sign=2F28567297B16ABB276BB815A7FF78AE6271CC071E94FD2DB656FEBC168052CE)   

本模块首批接口从 API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

     

#### 导入模块

 

```
import { vpn } from '@kit.NetworkKit';

```

    

#### LinkAddress

 

type LinkAddress = connection.LinkAddress

 

获取网络链接信息。

 

**系统能力**：SystemCapability.Communication.NetManager.Core

  

| 类型 | 说明 |
| --- | --- |
| connection.LinkAddress | 网络链路信息。 |

     

#### RouteInfo

 

type RouteInfo = connection.RouteInfo

 

获取网络路由信息。

 

**系统能力**：SystemCapability.Communication.NetManager.Core

  

| 类型 | 说明 |
| --- | --- |
| connection.RouteInfo | 网络路由信息。 |

     

#### AbilityContext

 

type AbilityContext = _AbilityContext

 

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

  

| 类型 | 说明 |
| --- | --- |
| _AbilityContext | 需要保存状态的UIAbility所对应的context，继承自 Context ，提供UIAbility的相关配置信息以及操作UIAbility和ServiceExtensionAbility的方法。 |
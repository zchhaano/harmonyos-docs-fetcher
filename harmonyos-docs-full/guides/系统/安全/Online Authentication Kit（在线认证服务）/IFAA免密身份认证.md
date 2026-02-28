## 场景介绍

- 开通：提供移动端开通生物特征（指纹/3D人脸）IFAA免密身份认证的能力。使用用户已有的生物特征类型进行开通，会开通移动端对应生物特征类型的IFAA免密身份认证能力。
- 认证：提供移动端认证生物特征（指纹/3D人脸）IFAA免密身份认证的能力。使用用户已开通的生物特征进行认证，认证成功；使用未开通的生物特征进行认证，认证失败。
- 注销：提供移动端注销生物特征（指纹/3D人脸）IFAA免密身份认证的能力。使用用户已开通的生物特征类型进行注销，会注销移动端对应生物特征类型的IFAA免密身份认证能力。

## 基本概念

互联网金融身份认证联盟（IIFAA），全称为International Internet Finance Authentication Alliance，是一个生物识别框架，它由IIFAA联盟推出并持续维护。

## 相关权限

获取生物识别权限：ohos.permission.ACCESS_BIOMETRIC。

## 约束与限制

- 开发者应用已接入IIFAA联盟，可以从IIFAA中心服务器获取签名数据。
- 移动端设备需要支持生物特征（指纹/3D人脸），查询当前移动端设备是否支持ATL4级别的认证可信等级。       收起自动换行深色代码主题复制

```
import { BusinessError } from '@kit.BasicServicesKit' ; import { userAuth } from '@kit.UserAuthenticationKit' ; try { // 示例，查询设备人脸识别是否支持 ATL4 级别的认证可信等级 userAuth . getAvailableStatus ( userAuth . UserAuthType . FACE , userAuth . AuthTrustLevel . ATL4 ) ; console . info ( 'current auth trust level is supported' ) ; } catch ( error ) { const err : BusinessError = error as BusinessError ; console . error ( `current auth trust level is not supported. Code is ${ err ?. code } , message is ${ err ?. message } ` ) ; }
```
- 移动端设备使用此服务时需要处于联网状态。

## 业务流程

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170029.72426276363086691095375963738921:50001231000000:2800:3B7CAA395FCFD5FE21FD4AA31D2AC71BA63D6ECEA8B7A5A515AE5B2C53880018.png)

## 接口说明

   **表1**开通、认证、注销的所需要的接口       展开

| 接口名 | 描述 |
| --- | --- |
| register (registerData: Uint8Array): Promise<Uint8Array> | 开通指定用户的指定生物信息类型（指纹/3D人脸）的IFAA免密身份认证能力。 |
| auth (authToken: Uint8Array, authData: Uint8Array): Promise<Uint8Array> | 使用指定用户的生物信息类型进行IFAA免密身份认证。 |
| deregisterSync (deregisterData: Uint8Array): void | 注销指定用户指定生物信息类型（指纹/3D人脸）的IFAA免密身份认证能力。 |
| getAnonymousIdSync (userToken: Uint8Array): Uint8Array | 获取移动端设备标识ID。 |

## 开发步骤

1. 注册IFAA免密身份认证。 

 收起自动换行深色代码主题复制

```
import { ifaa } from '@kit.OnlineAuthenticationKit' ; import { BusinessError } from '@kit.BasicServicesKit' ; // 开发者根据 IIFAA协议 构造 TLV 入参，转换为 Uint8Array, 再使用 ifaa.getAnonymousIdSync 接口。此处 new Uint8Array([0]) 需要替换为开发者定义的用户标识。 let arg = new Uint8Array ([ 0 ]) ; let getAnonIdResult : Uint8Array = ifaa . getAnonymousIdSync ( arg ) ; // 开发者需使用 getAnonIdResult从 服务端获取签名后的开通数据 // 开发者将开通数据（ IIFAA协议 的 TLV 格式）转换为 Uint8Array, 再使用 ifaa.register 接口。此处 new Uint8Array([0]) 需要替换为有效数据。 let TLV_Register_fp = new Uint8Array ([ 0 ]) ; let registerPromise : Promise < Uint8Array > = ifaa . register ( TLV_Register_fp ) ; registerPromise . then ( registerResult = > { console . info ( "Succeeded in doing register ." ); // 开通成功，开发者获取 ifaa.register 结果并处理。 } ) . catch ( ( err : BusinessError ) = > { console . error ( `Failed to call register . Code: ${err.code} , message: ${err.message} ` ); // 开通失败，开发者获取 ifaa.register 错误并处理。 } ) ;
```
2. 使用IFAA免密身份认证进行认证。 

 收起自动换行深色代码主题复制

```
import { ifaa } from '@kit.OnlineAuthenticationKit' ; import { userAuth } from '@kit.UserAuthenticationKit' ; import { BusinessError } from '@kit.BasicServicesKit' ; // 开发者根据 IIFAA协议 构造 TLV 入参，转换为 Uint8Array, 再使用 ifaa.getAnonymousIdSync 接口。 arg 需要替换开发者自定义数据。 let arg = new Uint8Array ([ 0 ]) ; let getAnonIdResult : Uint8Array = ifaa . getAnonymousIdSync ( arg ) ; // 开发者需使用 getAnonIdResult 从服务端获取签名后的认证数据 // 获取此次免密支付的 challenge let ifaaChallenge : Uint8Array = ifaa . preAuthSync () ; let authParam : userAuth . AuthParam = { challenge : ifaaChallenge , authType : [ userAuth . UserAuthType . FINGERPRINT ] , authTrustLevel : userAuth . AuthTrustLevel . ATL4 , } ; // 使用 preAuthResult 请求身份认证 let userAuthInstance = userAuth . getUserAuthInstance ( authParam , { title : ' ' } ) ; userAuthInstance . on ( 'result' , { async onResult ( result ) { let authToken = result . token ; try { // 生物特征认证成功后，调用 IFAA 认证 console . info ( "IFAA auth start" ) ; // 开发者将认证数据（ IIFAA协议 的 TLV 格式）转换为 Uint8Array, 再使用 ifaa.auth 接口。此处 new Uint8Array([0]) 需要替换为有效数据。 let TLV_Auth_fp = new Uint8Array ([ 0 ]) ; // 开发者根据业务需求选择同步 / 异步接口 let authResult : Uint8Array = ifaa . authSync ( authToken , TLV_Auth_fp ) ; console . info ( "authSyn authResult" + authResult ) ; // 开发者处理 authResult } catch ( error ) { const err : BusinessError = error as BusinessError ; console . error ( `Failed to call auth . Code is ${err.code} , message is ${err.message} ` ); } } } ) ; userAuthInstance . start () ;
```
3. 注销IFAA免密身份认证。 

 收起自动换行深色代码主题复制

```
import { ifaa } from '@kit.OnlineAuthenticationKit' // 开发者根据 IIFAA协议 构造 TLV 入参，转换为 Uint8Array, 再使用 ifaa.getAnonymousIdSync 接口。此处 new Uint8Array([0]) 需要替换为开发者定义的用户标识。 let arg = new Uint8Array ([ 0 ]) ; let getAnonIdResult : Uint8Array = ifaa . getAnonymousIdSync ( arg ) ; // 开发者需使用 getAnonymousId 的结果从服务端获取签名后的注销数据 // 开发者将注销数据（ IIFAA协议 的 TLV 格式）转换为 Uint8Array, 再使用 ifaa.deregisterSync 接口。此处 new Uint8Array([0]) 需要替换为有效数据。 let TLV_deregister_fp = new Uint8Array ([ 0 ]) ; ifaa . deregisterSync ( TLV_deregister_fp ) ;
```

## 常见问题

现象描述：开通IFAA免密身份认证失败。

可能原因：移动端设备没有联网。

处理步骤：移动端设备连接WIFI或热点，再次尝试。
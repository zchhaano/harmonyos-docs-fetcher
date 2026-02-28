## 接口说明

通行密钥服务主要接口如下表。

  展开

| 接口名 | 描述 |
| --- | --- |
| getClientCapabilities (context: common.Context): Promise<Map< ClientCapability , boolean>> | 查询当前设备支持的客户端能力列表。 |
| getPlatformAuthenticators (context: common.Context): Promise<Array< AuthenticatorMetadata >> | 查询当前设备支持的平台认证器能力列表（人脸、指纹、PIN码）。 |
| register (context: common.Context, options: CredentialCreationOptions , tokenBinding?: TokenBinding ): Promise< PublicKeyAttestationCredential > | 进行通行密钥的注册。 |
| authenticate (context: common.Context, options: CredentialRequestOptions , tokenBinding?: TokenBinding ): Promise< PublicKeyAssertionCredential > | 进行通行密钥的认证。 |

## 开发步骤

通行密钥服务提供基于FIDO2标准协议的FIDO客户端实现，这里仅演示FIDO客户端相关API的使用，涉及FIDO服务器的相关处理由开发者自行实现，请参考[FIDO2标准协议](https://fidoalliance.org/passkeys/)（见[网站链接免责声明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-website-disclaimer)）。

1. 需要业务方自行根据FIDO2标准协议部署FIDO服务器。
2. 导入相关模块。       收起自动换行深色代码主题复制

```
import { BusinessError } from '@kit.BasicServicesKit' ; import { UIContext } from '@kit.ArkUI' ; import { common } from '@kit.AbilityKit' ; import { fido2 } from '@kit.OnlineAuthenticationKit' ;
```
3. 注册通行密钥。       

  1. 获取能力信息，调用getClientCapabilities接口获取客户端能力列表，并且调用getPlatformAuthenticators接口获取平台认证器能力信息。         收起自动换行深色代码主题复制

```
uiContext1 : UIContext = this . getUIContext () ; uiContext : common . UIAbilityContext = this . uiContext1 . getHostContext () as common . UIAbilityContext ; // 使用 uiContext 需要获取页面 UIAbility 的 Context ，一个页面获取一次即可 try { // 获取 客户端能力列表 let clientCapabilities : Map < fido2 . ClientCapability , boolean > = await fido2 . getClientCapabilities ( this . uiContext ) ; console . info ( "Succeeded in doing getClientCapabilities." ) ; } catch ( error ) { let message = ( error as BusinessError ) . message ; let code = ( error as BusinessError ) . code ; console . error ( `Failed to call getClientCapabilities error code is ${ code } , message is ${ message } ` ) ; // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考 } try { // 获取平台认证器能力 let platformAuthenticators : Array < fido2 . AuthenticatorMetadata > = await fido2 . getPlatformAuthenticators ( this . uiContext ) ; console . info ( "Succeeded in doing getPlatformAuthenticators." ) ; } catch ( error ) { let message = ( error as BusinessError ) . message ; let code = ( error as BusinessError ) . code ; console . error ( `Failed to call getPlatformAuthenticators error code is ${ code } , message is ${ message } ` ) ; // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考 }
```
  2. 访问FIDO服务器，获取注册报文，调用register接口进行注册。         收起自动换行深色代码主题复制

```
// pkOptions 为应用从 FIDO 服务端获取的注册报文 , credentialCreationOp 为应用组装注册信息 let credentialCreationOp : fido2 . CredentialCreationOptions = { publicKey : pkOptions } ; try { // 调用 register进行通行密钥注册 let publicKeyAttestationCredential : fido2 . PublicKeyAttestationCredential = await fido2 . register ( this . uiContext , credentialCreationOp ) ; } catch ( error ) { let message = ( error as BusinessError ) . message ; let code = ( error as BusinessError ) . code ; console . error ( `Failed to call register error code is ${ code } , message is ${ message } ` ) ; // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考 }
```
  3. 应用使用注册结果（publicKeyAttestationCredential）组装注册响应报文，发送至FIDO服务端进行验证，获取注册结果报文。
4. 使用通行密钥进行身份认证。       

  1. 获取能力信息，调用getClientCapabilities接口获取客户端能力列表，并且调用getPlatformAuthenticators接口获取平台认证器能力信息。         收起自动换行深色代码主题复制

```
// 使用 uiContext 需要获取页面 UIAbility 的 Context ，一个页面获取一次即可 let uiContext : common. UIAbilityContext = getContext ( this ) as common. UIAbilityContext ; try { // 获取 客户端能力列表 let clientCapabilities : Map < fido2 . ClientCapability , boolean > = await fido2 . getClientCapabilities ( this . uiContext ) ; console . info ( "Succeeded in doing getClientCapabilities." ) ; } catch ( error ) { let message = ( error as BusinessError ) . message ; let code = ( error as BusinessError ) . code ; console . error ( `Failed to call getClientCapabilities error code is ${ code } , message is ${ message } ` ) ; // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考 } try { // 获取平台认证器能力 let platformAuthenticators : Array < fido2 . AuthenticatorMetadata > = await fido2 . getPlatformAuthenticators ( this . uiContext ) ; console . info ( "Succeeded in doing getPlatformAuthenticators." ) ; } catch ( error ) { let message = ( error as BusinessError ) . message ; let code = ( error as BusinessError ) . code ; console . error ( `Failed to call getPlatformAuthenticators error code is ${ code } , message is ${ message } ` ) ; // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考 }
```
  2. 访问FIDO服务器，获取认证报文，调用authenticate接口进行认证。         收起自动换行深色代码主题复制

```
// authPub 为应用从 FIDO 服务端获取的认证报文， authCredentialRequestOptions 为应用组装的认证信息 let authCredentialRequestOptions : fido2 . CredentialRequestOptions = { publicKey : authPub , mediation : "optional" as fido2 . CredentialMediationRequirement } try { // 调用 authenticate 接口进行认证 let pkAssertionCredential : fido2 . PublicKeyAssertionCredential = await fido2 . authenticate ( this . uiContext , authCredentialRequestOptions ) ; } catch ( error ) { let message = ( error as BusinessError ) . message ; let code = ( error as BusinessError ) . code ; console . error ( `Failed to call authenticateerror code is ${ code } , message is ${ message } ` ) ; // 业务根据错误码判断异常类型，进行相应处理，详见错误码参考 }
```
  3. 应用使用认证结果（pkAssertionCredential）组装认证响应报文，发送至FIDO服务端进行验证，获取认证结果报文。
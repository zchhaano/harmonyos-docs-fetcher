# 使用NDK接口实现画中画功能开发（C/C++）

本文以视频播放为例，介绍通过NDK接口实现画中画功能的基本开发步骤。

 说明

- 从API version 20开始，支持使用NDK接口实现画中画功能开发。
- 支持在Phone、PC/2in1、Tablet设备使用NDK接口实现画中画功能开发。

## 约束与限制

- 画中画窗口中画面的呈现不通过传入XComponent Controller实现，而是通过渲染surfaceId（在开启画中画回调中获取）对应的组件实现。
- 与typeNode实现方式相同，系统不缓存页面。如需进行页面操作，应用需要开启画中画生命周期监听，在对应周期内进行对应操作。
- 不支持设置自动拉起画中画。

## 开发步骤

示例中的视频播放器简易实现逻辑如下：

1. 通过OH_PictureInPicture_CreatePipConfig创建画中画参数配置器，并通过OH_PictureInPicture_SetPipMainWindowId、OH_PictureInPicture_SetPipTemplateType、OH_PictureInPicture_SetPipRect、OH_PictureInPicture_SetPipControlGroup、OH_PictureInPicture_SetPipNapiEnv接口在画中画参数配置器中设置初始配置信息。
2. 创建画中画控制器，后续可根据返回的控制器标识controllerId注册生命周期事件以及控制事件回调。通过OH_PictureInPicture_CreatePip接口创建画中画控制器实例，并缓存对应的控制器标识。建议在创建完成后立即调用OH_PictureInPicture_DestroyPipConfig销毁画中画参数配置器，以免发生内存泄漏。
3. 通过OH_PictureInPicture_RegisterStartPipCallback接口注册启动画中画回调，并根据返回的surfaceId渲染视频画面。同时应用可以按需注册其他需要监听的事件回调。
4. 通过OH_PictureInPicture_StartPip启动画中画。
5. 通过OH_PictureInPicture_UpdatePipContentSize更新媒体源尺寸信息。
6. 通过OH_PictureInPicture_StopPip关闭画中画。
7. 通过OH_PictureInPicture_UnregisterStartPipCallback解注册画中画启动回调，避免内存泄漏。同时应用可以按需解注册其他已注册的事件回调。

以上步骤涉及的各文件及示例可见下文。

Node-API模块注册，具体使用请参考[Native API在应用工程中的使用指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-guidelines)。

本文件仅作为参考示例，异常处理及错误码打印由开发者按需处理。

 收起自动换行深色代码主题复制

```
```

[napi_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUIWindowPipSamples/WindowPip/entry/src/main/cpp/napi_init.cpp#L17-L349) 

Node-API接口声明。

 收起自动换行深色代码主题复制

```
// Index.d.ts export enum PiPControlGroup { VIDEO_PLAY_VIDEO_PREVIOUS_NEXT = 101 , VIDEO_PLAY_FAST_FORWARD_BACKWARD = 102 , VIDEO_CALL_MICROPHONE_SWITCH = 201 , VIDEO_CALL_HANG_UP_BUTTON = 202 , VIDEO_CALL_CAMERA_SWITCH = 203 , VIDEO_CALL_MUTE_SWITCH = 204 , VIDEO_MEETING_HANG_UP_BUTTON = 301 , VIDEO_MEETING_CAMERA_SWITCH = 302 , VIDEO_MEETING_MUTE_SWITCH = 303 , VIDEO_MEETING_MICROPHONE_SWITCH = 304 , VIDEO_LIVE_VIDEO_PLAY_PAUSE = 401 , VIDEO_LIVE_MUTE_SWITCH = 402 , } export interface PiPConfig { mainWindowId : number ; pipTemplateType : number ; width : number ; height : number ; controlGroup : Array < PiPControlGroup >; } export declare const createPip : ( config: PiPConfig ) => number ; export declare const startPip : ( controllerId: number ) => number ; export declare const registerStartPip : ( controllerId: number , jsCallback: Function ) => number ; export declare const deletePip : ( controllerId: number ) => number ; export declare const stopPip : ( controllerId: number ) => number ; export declare const registerLifecycleListener : ( controllerId: number , jsCallback: Function ) => number ;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUIWindowPipSamples/WindowPip/entry/src/main/cpp/types/libentry/Index.d.ts#L17-L44) 

CMakeLists.txt文件，用于生成对应的库文件。

 收起自动换行深色代码主题复制

```
# CMakeLists .txt # the minimum version of CMake. cmake_minimum_required (VERSION 3.5 . 0 ) set (CMAKE_CXX_STANDARD 17 ) set (CMAKE_CXX_STANDARD_REQUIRED ON) project (MyApplication) set (NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR}) if (DEFINED PACKAGE_FIND_FILE) include (${PACKAGE_FIND_FILE}) endif () include_directories (${NATIVERENDER_ROOT_PATH} ${NATIVERENDER_ROOT_PATH}/include) add_library (entry SHARED napi_init.cpp) target_link_libraries (entry PUBLIC libace_napi.z.so libace_ndk.z.so libnative_window_manager.so libhilog_ndk.z.so)
```

[CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUIWindowPipSamples/WindowPip/entry/src/main/cpp/CMakeLists.txt#L2-L15) 

EntryAbility文件示例。

 收起自动换行深色代码主题复制

```
// entryability/EntryAbility.ets import { BusinessError } from '@kit.BasicServicesKit' ; import { AbilityConstant , ConfigurationConstant , UIAbility , Want } from '@kit.AbilityKit' ; import { window } from '@kit.ArkUI' ; import { PipManager } from '../nodefree/PipManager' ; import { Logger } from '../util/LogUtil' ; export default class EntryAbility extends UIAbility { onCreate ( want : Want , launchParam : AbilityConstant . LaunchParam ): void { AppStorage . setOrCreate ( 'UIAbilityContext' , this . context ); this . context . getApplicationContext (). setColorMode ( ConfigurationConstant . ColorMode . COLOR_MODE_NOT_SET ); } onDestroy (): void { Logger . info ( 'testTag' , '%{public}s' , 'Ability onDestroy' ); } onWindowStageCreate ( windowStage : window . WindowStage ): void { // Main window is created, set main page for this ability Logger . info ( 'testTag' , '%{public}s' , 'Ability onWindowStageCreate' ); let windowClass : window . Window | undefined = undefined ; let windowClassId : number = - 1 ; windowStage. getMainWindow (). then ( ( window ) => { if ( window == null ) { Logger . error ( 'Failed to obtaining the window. Cause: The data is empty' ); return ; } windowClass = window ; windowClass. setUIContent ( 'pages/Index' ); windowClassId = windowClass. getWindowProperties (). id ; AppStorage . setOrCreate ( 'windowId' , windowClassId); Logger . info ( 'Succeeded in obtaining the window' ) let ctx = window . getUIContext (); AppStorage . setOrCreate ( 'UIContext' , ctx); // 通过主窗口UIContext创建typeNode节点 PipManager . getInstance (). makeTypeNode (ctx); }). catch ( ( err: BusinessError ) => { Logger . error ( `Failed to obtaining the window. Cause code: ${err.code} , message: ${err.message} ` ); }); windowStage. loadContent ( 'pages/Index' , ( err ) => { if (err. code ) { Logger . error ( 'testTag' , 'Failed to load the content. Cause: %{public}s' , JSON . stringify (err)); return ; } Logger . info ( 'testTag' , 'Succeeded in loading the content.' ); }); } onWindowStageDestroy (): void { // Main window is destroyed, release UI related resources Logger . info ( 'testTag' , '%{public}s' , 'Ability onWindowStageDestroy' ); } onForeground (): void { // Ability has brought to foreground Logger . info ( 'testTag' , '%{public}s' , 'Ability onForeground' ); } onBackground (): void { // Ability has back to background Logger . info ( 'testTag' , '%{public}s' , 'Ability onBackground' ); } }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUIWindowPipSamples/WindowPip/entry/src/main/ets/entryability/EntryAbility.ets#L18-L96) 

示例中的视频播放需要使用AVPlayer，具体实现可参考[视频播放](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-playback)。

 收起自动换行深色代码主题复制

```
// model/AVPlayer.ets // 视频播放器简单实现 import media from '@ohos.multimedia.media' ; import common from '@ohos.app.ability.common' ; import { BusinessError } from '@ohos.base' ; import resourceManager from '@ohos.resourceManager' ; import { Logger } from '../util/LogUtil' ; export class AVPlayer { public avPlayer?: media.AVPlayer; private count: number = 0 ; private surfaceID: string; // surfaceID用于播放画面显示，具体的值需要通过Xcomponent接口获取，相关文档链接见上面Xcomponent创建方法 public jumpNext: boolean = false ; public type: number = 0 ; // 用于区分主界面的player还是pip界面的player public state_: string = '' public playStatus: boolean = true ; constructor (surfaceID: string, type: number) { this .surfaceID = surfaceID; this .type = type } setSurfaceId(id: string) { if ( this .avPlayer) { this .surfaceID = id; this .avPlayer.surfaceId = id; } } updatePlayStatus(status: boolean) { this .playStatus = status; } // 注册avplayer回调函数 setAVPlayerCallback() { // seek操作结果回调函数 this .avPlayer?.on( 'seekDone' , (seekDoneTime: number) => { Logger.info(`PipMain AVPlayer seek succeeded, seek time is ${seekDoneTime}`); }) // error回调监听函数,当avPlayer在操作过程中出现错误时调用reset接口触发重置流程 this .avPlayer?.on( 'error' , (err: BusinessError) => { Logger.error(`PipMain Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`); this .avPlayer?.reset(); // 调用reset重置资源，触发idle状态 }) // 状态机变化回调函数 this .avPlayer?.on( 'stateChange' , async (state, reason) => { if (! this .avPlayer) { return ; } this .state_ = state; switch (state) { case 'idle' : // 成功调用reset接口后触发该状态机上报 Logger.info( 'AVPlayer state idle called.' ); if (! this .jumpNext) { this .avPlayer.release(); // 调用release接口销毁实例对象 } else { let uiContext: UIContext = AppStorage. get ( 'UIAbilityContext' ) as UIContext; let context = uiContext.getHostContext() as common.UIAbilityContext; let fileDescriptor: resourceManager.RawFileDescriptor; fileDescriptor = await context.resourceManager.getRawFd( '640x360.mp4' ); // 为fdSrc赋值触发initialized状态机上报 this .avPlayer.fdSrc = fileDescriptor; } break ; case 'initialized' : // avplayer 设置播放源后触发该状态上报 Logger.info( 'initialized called.' ); this .avPlayer.surfaceId = this .surfaceID; // 设置显示画面，当播放的资源为纯音频时无需设置 this .avPlayer.prepare().then(() => { Logger.info( 'AVPlayer prepare succeeded.' ); }, (err: BusinessError) => { Logger.error(`Invoke prepare failed, code is ${err.code}, message is ${err.message}`); }); break ; case 'prepared' : // prepare调用成功后上报该状态机 Logger.info( 'AVPlayer state prepared called.' ); this .avPlayer.play(); // 调用播放接口开始播放 break ; case 'playing' : // play成功调用后触发该状态机上报 Logger.info( 'AVPlayer state playing called.' ); this .jumpNext = false ; this .count++; break ; case 'paused' : // pause成功调用后触发该状态机上报 Logger.info( 'AVPlayer state paused called.' ); // this.avPlayer.play(); // 再次播放接口开始播放 break ; case 'completed' : // 播放结束后触发该状态机上报 Logger.info( 'AVPlayer state completed called.' ); this .playNext(); ; //调用播放结束接口 break ; case 'stopped' : // stop接口成功调用后触发该状态机上报 Logger.info( 'AVPlayer state stopped called.' ); this .avPlayer.reset(); // 调用reset接口初始化avplayer状态 break ; case 'released' : Logger.info( 'AVPlayer state released called.' ); break ; default: Logger.info( 'AVPlayer state unknown called.' ); break ; } }) this .avPlayer?.on( 'videoSizeChange' , (width: number, height: number) => { Logger.info( 'videoSizeChange width:' + width + ' height:' + height); let context = AppStorage. get ( 'UIAbilityContext' ) as common.UIAbilityContext; }) } // 以下demo为使用资源管理接口获取打包在HAP内的媒体资源文件并通过fdSrc属性进行播放示例 async avPlayerFdSrc() { // 创建avPlayer实例对象 Logger.info( 'avPlayerFdSrc' ); this .avPlayer = await media.createAVPlayer(); // 创建状态机变化回调函数 this .setAVPlayerCallback(); // 通过UIAbilityContext的resourceManager成员的getRawFd接口获取媒体资源播放地址 // 返回类型为{fd,offset,length},fd为HAP包fd地址，offset为媒体资源偏移量，length为播放长度 let context = AppStorage. get ( 'UIAbilityContext' ) as common.UIAbilityContext; let fileDescriptor = await context.resourceManager.getRawFd( '640x360.mp4' ); Logger.info( 'getRawFd' ); // 为fdSrc赋值触发initialized状态机上报 this .avPlayer.fdSrc = fileDescriptor; } async playNext() { if ( this .avPlayer === null ) { return ; } this .jumpNext = true ; this .avPlayer?.stop(); } play() { if ( this .state_ === 'paused' ) { this .avPlayer?.play(); } } pause() { if ( this .state_ === 'playing' ) { this .avPlayer?.pause(); } } stopAvPlayer() { Logger.info( 'stopAvPlayer>>>' ) if (! this .avPlayer) { return ; } this .avPlayer.stop(); Logger.info( 'stopping>>>' ); this .avPlayer.reset(); } }
```

[NDKAVPlayer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUIWindowPipSamples/WindowPip/entry/src/main/ets/model/NDKAVPlayer.ets#L17-L172) 

应用界面布局文件，用于演示画中画基本功能。

 收起自动换行深色代码主题复制

```
// pages/Index.ets // 应用首页 import { router } from '@kit.ArkUI' ; @Entry @Component struct Index { pathStack : NavPathStack = new NavPathStack (); build ( ) { Navigation ( this . pathStack ) { Scroll () { Flex ({ direction : FlexDirection . Column }) { // ... this . featureButton ( '使用NDK接口实现画中画（C++）' , this . ndkImplement ); } } } . hideBackButton ( true ) . titleMode ( NavigationTitleMode . Mini ) . backgroundColor ( '#FFF1F3F5' ) . mode ( NavigationMode . Stack ) . title ( '画中画SampleCode' ) } @Builder featureButton ( buttonText: string , callbackOnClick: () => void ) { Button ({ type : ButtonType . Normal }) { Row () { Column () { Text (buttonText) . fontSize ( 24 ) . fontWeight ( FontWeight . Bold ) . fontColor ( '#000000' ) Rect () . radius ( 1 ) . fill ( '#0A59F7' ) . height ( 2 ) . width ( 30 ) } . width ( '100%' ) . alignItems ( HorizontalAlign . Start ) } . width ( '100%' ) } . width ( '90%' ) . padding ( '5%' ) . margin ({ top : '3%' , bottom : '2%' , right : '3%' }) . backgroundColor ( '#FFFFFF' ) . borderRadius ( 20 ) . onClick (callbackOnClick) } // ... private ndkImplement = () => { this . getUIContext (). getRouter (). pushUrl ({ url : 'pages/NDKImplementPage' }, router. RouterMode . Standard ) } }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUIWindowPipSamples/WindowPip/entry/src/main/ets/pages/Index.ets#L19-L112) 收起自动换行深色代码主题复制

```
```

[NDKImplementPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUIWindowPipSamples/WindowPip/entry/src/main/ets/pages/NDKImplementPage.ets#L17-L206) 

以上示例代码对应的示意图如下所示：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165848.31767207761990935440060395984873:50001231000000:2800:C05701578016623616A5D81DE31C65DAF00DBE312B34B22B3152C5C9D3A96EAB.gif)

## 示例代码

- [实现画中画效果](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/HarmonyOS-feature-20251117/ArkUIWindowPipSamples/WindowPip)
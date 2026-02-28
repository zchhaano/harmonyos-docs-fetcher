## 场景说明

开发者可以使用[MindSpore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore)，在UI代码中集成MindSpore Lite能力，快速部署AI算法，进行AI模型推理，实现语音识别的应用。

语音识别可以将一段音频信息转换为文本，在智能语音助手、语音输入、语音搜索等领域有广泛的应用。

## 环境配置

若需要使用模拟器运行该示例，请参考：[使用模拟器运行应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-emulator)

## 基本概念

- N-API：用于构建ArkTS本地化组件的一套接口。可利用N-API，将C/C++开发的库封装成ArkTS模块。

## 开发流程

1. 选择语音识别模型。
2. 在端侧使用MindSpore Lite推理模型，实现对语音文件的语音识别。

## 开发步骤

本文以对语音识别模型进行推理为例，提供使用MindSpore Lite实现语音识别应用的开发指导。

### 选择模型

本示例程序中使用的语音识别模型文件为tiny-encoder.ms、tiny-decoder-main.ms、tiny-decoder-loop.ms，放置在entry/src/main/resources/rawfile工程目录下。

### 编写播放音频代码

调用[@ohos.multimedia.media](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media)、[@ohos.multimedia.audio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio)，实现播放音频的功能。

 收起自动换行深色代码主题复制

```
// player.ets import { media } from '@kit.MediaKit' ; import { common } from '@kit.AbilityKit' ; import { BusinessError } from '@kit.BasicServicesKit' ; import { audio } from '@kit.AudioKit' ; import { UIContext } from '@kit.ArkUI' ; import { hilog } from '@kit.PerformanceAnalysisKit' ; const TAG = 'MindSporeLite' ; export default class AVPlayerDemo { private isSeek : boolean = false ; // 用于区分模式是否支持seek操作。 // 注册avplayer回调函数。 setAVPlayerCallback ( avPlayer: media.AVPlayer ) { // seek操作结果回调函数。 avPlayer. on ( 'seekDone' , ( seekDoneTime: number ) => { hilog. info ( 0xFF00 , TAG , '%{public}s' , `MS_LITE_LOG: AVPlayer seek succeeded, seek time is ${seekDoneTime} ` ); }); // error回调监听函数，当avPlayer在操作过程中出现错误时调用reset接口触发重置流程。 avPlayer. on ( 'error' , ( err: BusinessError ) => { hilog. error ( 0xFF00 , TAG , '%{public}s' , `MS_LITE_ERR: Invoke avPlayer failed, code is ${err.code} , message is ${err.message} ` ); avPlayer. reset (); // 调用reset重置资源，触发idle状态。 }); // 状态机变化回调函数。 avPlayer. on ( 'stateChange' , async ( state : string , reason : media. StateChangeReason ) => { switch (state) { case 'idle' : // 成功调用reset接口后触发该状态机上报。 hilog. info ( 0xFF00 , TAG , '%{public}s' , 'MS_LITE_LOG: AVPlayer state idle called.' ); avPlayer. release (); // 调用release接口销毁实例对象。 break ; case 'initialized' : // avplayer 设置播放源后触发该状态上报。 hilog. info ( 0xFF00 , TAG , '%{public}s' , 'MS_LITE_LOG: AVPlayer state initialized called.' ); avPlayer. audioRendererInfo = { usage : audio. StreamUsage . STREAM_USAGE_MUSIC , // 音频流使用类型：音乐。根据业务场景配置。 rendererFlags : 0 // 音频渲染器标志。 }; avPlayer. prepare (); break ; case 'prepared' : // prepare调用成功后上报该状态机。 hilog. info ( 0xFF00 , TAG , '%{public}s' , 'MS_LITE_LOG: AVPlayer state prepared called.' ); avPlayer. play (); // 调用播放接口开始播放。 break ; case 'playing' : // play成功调用后触发该状态机上报。 hilog. info ( 0xFF00 , TAG , '%{public}s' , 'MS_LITE_LOG: AVPlayer state playing called.' ); if ( this . isSeek ) { hilog. info ( 0xFF00 , TAG , '%{public}s' , 'MS_LITE_LOG: AVPlayer start to seek.' ); avPlayer. seek ( 0 ); // 将播放位置移动到音频的开始。 } else { // 当播放模式不支持seek操作时继续播放到结尾。 hilog. info ( 0xFF00 , TAG , '%{public}s' , 'MS_LITE_LOG: AVPlayer wait to play end.' ); } break ; case 'paused' : // pause成功调用后触发该状态机上报。 hilog. info ( 0xFF00 , TAG , '%{public}s' , 'MS_LITE_LOG: AVPlayer state paused called.' ); setTimeout ( () => { hilog. info ( 0xFF00 , TAG , '%{public}s' , 'MS_LITE_LOG: AVPlayer paused wait to play again' ); avPlayer. play (); // 暂停3s后再次调用播放接口开始播放。 }, 3000 ); break ; case 'completed' : // 播放结束后触发该状态机上报。 hilog. info ( 0xFF00 , TAG , '%{public}s' , 'MS_LITE_LOG: AVPlayer state completed called.' ); avPlayer. stop (); // 调用播放结束接口。 break ; case 'stopped' : // stop接口成功调用后触发该状态机上报。 hilog. info ( 0xFF00 , TAG , '%{public}s' , 'MS_LITE_LOG: AVPlayer state stopped called.' ); avPlayer. reset (); // 调用reset接口初始化avplayer状态。 break ; case 'released' : hilog. info ( 0xFF00 , TAG , '%{public}s' , 'MS_LITE_LOG: AVPlayer state released called.' ); break ; default : hilog. info ( 0xFF00 , TAG , '%{public}s' , 'MS_LITE_LOG: AVPlayer state unknown called.' ); break ; } }); } // 使用资源管理接口获取音频文件并通过fdSrc属性进行播放。 async avPlayerFdSrcDemo ( ) { // 创建avPlayer实例对象。 let avPlayer : media. AVPlayer = await media. createAVPlayer (); // 创建状态机变化回调函数。 this . setAVPlayerCallback (avPlayer); // 通过UIAbilityContext的resourceManager成员的getRawFd接口获取媒体资源播放地址。 // 返回类型为{fd,offset,length},fd为HAP包fd地址，offset为媒体资源偏移量，length为播放长度。 let context = new UIContext (). getHostContext () as common. UIAbilityContext ; let fileDescriptor = await context. resourceManager . getRawFd ( 'zh.wav' ); let avFileDescriptor : media. AVFileDescriptor = { fd : fileDescriptor. fd , offset : fileDescriptor. offset , length : fileDescriptor. length }; this . isSeek = true ; // 支持seek操作。 // 为fdSrc赋值触发initialized状态机上报。 avPlayer. fdSrc = avFileDescriptor; } }
```

[player.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/ets/pages/player.ets#L16-L111)   

### 编写识别音频代码

在 entry/src/main/cpp/mslite_napi.cpp，调用[MindSpore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore)，依次对3个模型进行推理，推理代码流程如下。

1. 引用对应的头文件。说明：需要用户下载三方库，其中librosa来源是[LibrosaCpp](https://github.com/ewan-xu/LibrosaCpp)，libsamplerate来源是[libsamplerate](https://github.com/libsndfile/libsamplerate)，下载后置于entry/src/main/cpp/third_party目录下。AudioFile.h的来源是[AudioFile](https://github.com/adamstark/AudioFile/blob/1.1.2/AudioFile.h)，base64.h、base64.cpp的来源是[whisper.axera](https://github.com/ml-inory/whisper.axera/tree/main/cpp/src)下载后置于entry/src/main/cpp/src目录下。

 收起自动换行深色代码主题复制

```
# include "AudioFile.h" # include "base64.h" # include "napi/native_api.h" # include "utils.h" # include <algorithm> # include <cstdlib> # include <fstream> # include <hilog/log.h> # include <iostream> # include <librosa/librosa.h> # include <mindspore/context.h> # include <mindspore/model.h> # include <mindspore/status.h> # include <mindspore/tensor.h> # include <mindspore/types.h> # include <numeric> # include <rawfile/raw_file_manager.h> # include <sstream> # include <vector>
```

[mslite_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L16-L36)
2. 读取音频文件、模型文件等，转换为buffer数据。

 收起自动换行深色代码主题复制

```
#define LOGI (...) ((void) OH_LOG_Print (LOG_APP, LOG_INFO, LOG_DOMAIN, "[MSLiteNapi]", __VA_ARGS__)) #define LOGD (...) ((void) OH_LOG_Print (LOG_APP, LOG_DEBUG, LOG_DOMAIN, "[MSLiteNapi]", __VA_ARGS__)) #define LOGW (...) ((void) OH_LOG_Print (LOG_APP, LOG_WARN, LOG_DOMAIN, "[MSLiteNapi]", __VA_ARGS__)) #define LOGE (...) ((void) OH_LOG_Print (LOG_APP, LOG_ERROR, LOG_DOMAIN, "[MSLiteNapi]", __VA_ARGS__))
```

[mslite_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L38-L43) 收起自动换行深色代码主题复制

```
using BinBuffer = std::pair< void *, size_t >;
```

[mslite_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L63-L65) 收起自动换行深色代码主题复制

```
BinBuffer ReadBinFile (NativeResourceManager *nativeResourceManager, const std::string &modelName) { auto rawFile = OH_ResourceManager_OpenRawFile (nativeResourceManager, modelName. c_str ()); if (rawFile == nullptr ) { LOGE ( "MS_LITE_ERR: Open model file failed" ); return BinBuffer ( nullptr , 0 ); } long fileSize = OH_ResourceManager_GetRawFileSize (rawFile); if (fileSize <= 0 ) { LOGE ( "MS_LITE_ERR: FileSize not correct" ); return BinBuffer ( nullptr , 0 ); } void *buffer = malloc (fileSize); if (buffer == nullptr ) { LOGE ( "MS_LITE_ERR: OH_ResourceManager_ReadRawFile failed" ); return BinBuffer ( nullptr , 0 ); } int ret = OH_ResourceManager_ReadRawFile (rawFile, buffer, fileSize); if (ret == 0 ) { LOGE ( "MS_LITE_ERR: OH_ResourceManager_ReadRawFile failed" ); OH_ResourceManager_CloseRawFile (rawFile); return BinBuffer ( nullptr , 0 ); } OH_ResourceManager_CloseRawFile (rawFile); return BinBuffer (buffer, fileSize); } BinBuffer ReadTokens (NativeResourceManager *nativeResourceManager, const std::string &modelName) { auto rawFile = OH_ResourceManager_OpenRawFile (nativeResourceManager, modelName. c_str ()); if (rawFile == nullptr ) { LOGE ( "MS_LITE_ERR: Open model file failed" ); return BinBuffer ( nullptr , 0 ); } long fileSize = OH_ResourceManager_GetRawFileSize (rawFile); if (fileSize <= 0 ) { LOGE ( "MS_LITE_ERR: FileSize not correct" ); return BinBuffer ( nullptr , 0 ); } void *buffer = malloc (fileSize); if (buffer == nullptr ) { LOGE ( "MS_LITE_ERR: OH_ResourceManager_ReadRawFile failed" ); return BinBuffer ( nullptr , 0 ); } int ret = OH_ResourceManager_ReadRawFile (rawFile, buffer, fileSize); if (ret == 0 ) { LOGE ( "MS_LITE_ERR: OH_ResourceManager_ReadRawFile failed" ); OH_ResourceManager_CloseRawFile (rawFile); return BinBuffer ( nullptr , 0 ); } OH_ResourceManager_CloseRawFile (rawFile); BinBuffer res (buffer, fileSize) ; return res; }
```

[mslite_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L79-L134)
3. 创建上下文，设置设备类型，并加载模型。

 收起自动换行深色代码主题复制

```
void DestroyModelBuffer ( void **buffer) { if (buffer == nullptr ) { return ; } free (*buffer); *buffer = nullptr ; } OH_AI_ModelHandle CreateMSLiteModel (BinBuffer &bin) { // 创建并配置上下文 auto context = OH_AI_ContextCreate (); if (context == nullptr ) { DestroyModelBuffer (&bin.first); LOGE ( "MS_LITE_ERR: Create MSLite context failed.\n" ); return nullptr ; } auto cpu_device_info = OH_AI_DeviceInfoCreate (OH_AI_DEVICETYPE_CPU); OH_AI_DeviceInfoSetEnableFP16 (cpu_device_info, false ); OH_AI_ContextAddDeviceInfo (context, cpu_device_info); // 创建模型 auto model = OH_AI_ModelCreate (); if (model == nullptr ) { DestroyModelBuffer (&bin.first); LOGE ( "MS_LITE_ERR: Allocate MSLite Model failed.\n" ); return nullptr ; } // 加载与编译模型，模型的类型为OH_AI_MODELTYPE_MINDIR auto build_ret = OH_AI_ModelBuild (model, bin.first, bin.second, OH_AI_MODELTYPE_MINDIR, context); DestroyModelBuffer (&bin.first); if (build_ret != OH_AI_STATUS_SUCCESS) { OH_AI_ModelDestroy (&model); LOGE ( "MS_LITE_ERR: Build MSLite model failed.\n" ); return nullptr ; } LOGI ( "MS_LITE_LOG: Build MSLite model success.\n" ); return model; }
```

[mslite_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L136-L178)
4. 设置模型输入数据，执行模型推理。

 收起自动换行深色代码主题复制

```
constexpr int K_NUM_PRINT_OF_OUT_DATA = 20 ;
```

[mslite_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L59-L61) 收起自动换行深色代码主题复制

```
int FillInputTensor (OH_AI_TensorHandle input, const BinBuffer &bin) { if ( OH_AI_TensorGetDataSize (input) != bin.second) { return OH_AI_STATUS_LITE_INPUT_PARAM_INVALID; } char *data = ( char *) OH_AI_TensorGetMutableData (input); memcpy (data, ( const char *)bin.first, OH_AI_TensorGetDataSize (input)); return OH_AI_STATUS_SUCCESS; }
```

[mslite_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L67-L77) 收起自动换行深色代码主题复制

```
// 执行模型推理 int RunMSLiteModel (OH_AI_ModelHandle model, std::vector<BinBuffer> inputBins) { // 设置模型的输入数据 auto inputs = OH_AI_ModelGetInputs (model); for ( int i = 0 ; i < inputBins. size (); i++) { auto ret = FillInputTensor (inputs.handle_list[i], inputBins[i]); if (ret != OH_AI_STATUS_SUCCESS) { LOGE ( "MS_LITE_ERR: set input %{public}d error.\n" , i); return OH_AI_STATUS_LITE_ERROR; } } // 获取模型的输出张量 auto outputs = OH_AI_ModelGetOutputs (model); // 模型推理 auto predict_ret = OH_AI_ModelPredict (model, inputs, &outputs, nullptr , nullptr ); if (predict_ret != OH_AI_STATUS_SUCCESS) { OH_AI_ModelDestroy (&model); LOGE ( "MS_LITE_ERR: MSLite Predict error.\n" ); return OH_AI_STATUS_LITE_ERROR; } LOGD ( "MS_LITE_LOG: Run MSLite model Predict success.\n" ); // 打印输出数据 LOGD ( "MS_LITE_LOG: Get model outputs:\n" ); for ( size_t i = 0 ; i < outputs.handle_num; i++) { auto tensor = outputs.handle_list[i]; LOGD ( "MS_LITE_LOG: - Tensor %{public}d name is: %{public}s.\n" , static_cast < int >(i), OH_AI_TensorGetName (tensor)); LOGD ( "MS_LITE_LOG: - Tensor %{public}d size is: %{public}d.\n" , static_cast < int >(i), ( int ) OH_AI_TensorGetDataSize (tensor)); LOGD ( "MS_LITE_LOG: - Tensor data is:\n" ); auto out_data = reinterpret_cast < const float *>( OH_AI_TensorGetData (tensor)); std::stringstream outStr; for ( int i = 0 ; (i < OH_AI_TensorGetElementNum (tensor)) && (i <= K_NUM_PRINT_OF_OUT_DATA); i++) { outStr << out_data[i] << " " ; } LOGD ( "MS_LITE_LOG: %{public}s" , outStr. str (). c_str ()); } return OH_AI_STATUS_SUCCESS; }
```

[mslite_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L207-L251)
5. 调用以上方法，实现3个模型的推理流程。

 收起自动换行深色代码主题复制

```
const float NEG_INF = -std::numeric_limits< float >:: infinity (); const int WHISPER_SOT = 50258 ; const int WHISPER_TRANSCRIBE = 50359 ; const int WHISPER_TRANSLATE = 50358 ; const int WHISPER_NO_TIMESTAMPS = 50363 ; const int WHISPER_EOT = 50257 ; const int WHISPER_BLANK = 220 ; const int WHISPER_NO_SPEECH = 50362 ; const int WHISPER_N_TEXT_CTX = 448 ; const int WHISPER_N_TEXT_STATE = 384 ; constexpr int WHISPER_SAMPLE_RATE = 16000 ;
```

[mslite_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L45-L57) 收起自动换行深色代码主题复制

```
BinBuffer GetMSOutput (OH_AI_TensorHandle output) { float *outputData = reinterpret_cast < float *>( OH_AI_TensorGetMutableData (output)); size_t size = OH_AI_TensorGetDataSize (output); return {outputData, size}; }
```

[mslite_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L263-L270) 收起自动换行深色代码主题复制

```
void SuppressTokens (BinBuffer &logits, bool isInitial) { auto logits_data = static_cast < float *>(logits.first); if (isInitial) { logits_data[WHISPER_EOT] = NEG_INF; logits_data[WHISPER_BLANK] = NEG_INF; } // 其他令牌的抑制 logits_data[WHISPER_NO_TIMESTAMPS] = NEG_INF; logits_data[WHISPER_SOT] = NEG_INF; logits_data[WHISPER_NO_SPEECH] = NEG_INF; logits_data[WHISPER_TRANSLATE] = NEG_INF; }
```

[mslite_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L280-L296) 收起自动换行深色代码主题复制

```
```

[mslite_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L374-L611)
6. 编写CMake脚本，链接MindSpore Lite动态库。

 收起自动换行深色代码主题复制

```
# the minimum version of CMake. cmake_minimum_required (VERSION 3.5 . 0 ) project (test) # AudioFile .h set (CMAKE_CXX_STANDARD 17 ) set (CMAKE_CXX_STANDARD_REQUIRED TRUE) set (NATIVERENDER_PATH ${CMAKE_CURRENT_SOURCE_DIR}) if (DEFINED PACKAGE_FIND_FILE) include (${PACKAGE_FIND_FILE}) endif () include_directories (${NATIVERENDER_PATH} ${NATIVERENDER_PATH}/include) # libsamplerate set (LIBSAMPLERATE_DIR ${NATIVERENDER_PATH}/third_party/libsamplerate) include_directories (${LIBSAMPLERATE_DIR}/include) add_subdirectory (${LIBSAMPLERATE_DIR}) include_directories (${NATIVERENDER_PATH}/third_party/opencc/include/opencc) # src aux_source_directory (src SRC_DIR) include_directories (${NATIVERENDER_PATH}/src) include_directories (${CMAKE_SOURCE_DIR}/third_party) file (GLOB SRC src/*.cc) add_library (entry SHARED mslite_napi.cpp ${SRC}) target_link_libraries (entry PUBLIC samplerate) target_link_libraries (entry PUBLIC mindspore_lite_ndk) target_link_libraries (entry PUBLIC hilog_ndk.z) target_link_libraries (entry PUBLIC rawfile.z) target_link_libraries (entry PUBLIC ace_napi.z)
```

### 使用N-API将C++动态库封装成ArkTS模块

1. 在 entry/src/main/cpp/types/libentry/Index.d.ts，定义ArkTS接口runDemo() 。内容如下：

 收起自动换行深色代码主题复制

```
export const runDemo : ( a: Object ) => string ;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/types/libentry/Index.d.ts#L16-L18)
2. 在 oh-package.json5 文件，将API与so相关联，成为一个完整的ArkTS模块：

 收起自动换行深色代码主题复制

```
{ "name" : "libentry.so" , "types" : "./Index.d.ts" , "version" : "1.0.0" , "description" : "MindSpore Lite inference module." }
```

### 调用封装的ArkTS模块进行推理并输出结果

在 entry/src/main/ets/pages/Index.ets 中，调用封装的ArkTS模块，最后对推理结果进行处理。若提示@nutpi/chinese_transverter不存在，请参考[中文简繁体转换器三方库](https://developer.huawei.com/consumer/cn/forum/topic/0202169478029484501?fid=0109140870620153026)安装@nutpi/chinese_transverter组件。

 收起自动换行深色代码主题复制

```
// Index.ets import msliteNapi from 'libentry.so' import AVPlayerDemo from './player' ; import { transverter, TransverterType , TransverterLanguage } from "@nutpi/chinese_transverter" import { hilog } from '@kit.PerformanceAnalysisKit' ; const TAG = 'MindSporeLite' ; @Entry @Component struct Index { @State message : string = 'MSLite Whisper Demo' ; @State wavName : string = 'zh.wav' ; @State content : string = '' ; build ( ) { Row () { Column () { Text ( this . message ) . fontSize ( 30 ) . fontWeight ( FontWeight . Bold ); Button () { Text ( '播放示例音频' ) . fontSize ( 20 ) . fontWeight ( FontWeight . Medium ) } . type ( ButtonType . Capsule ) . margin ({ top : 20 }) . backgroundColor ( '#0D9FFB' ) . width ( '40%' ) . height ( '5%' ) . onClick ( async () =>{ // 通过实例调用类中的函数 hilog. info ( 0xFF00 , TAG , '%{public}s' , `MS_LITE_LOG: begin to play wav.` ); let myClass = new AVPlayerDemo (); myClass. avPlayerFdSrcDemo (); }) Button () { Text ( '识别示例音频' ) . fontSize ( 20 ) . fontWeight ( FontWeight . Medium ) } . type ( ButtonType . Capsule ) . margin ({ top : 20 }) . backgroundColor ( '#0D9FFB' ) . width ( '40%' ) . height ( '5%' ) . onClick ( () => { let resMgr = this . getUIContext ()?. getHostContext ()?. getApplicationContext (). resourceManager ; if (resMgr === undefined || resMgr === null ) { hilog. error ( 0xFF00 , TAG , '%{public}s' , `MS_LITE_ERR: get resourceManager failed.` ); return } // 调用封装的runDemo函数 hilog. info ( 0xFF00 , TAG , '%{public}s' , `MS_LITE_LOG: *** Start MSLite Demo ***` ); let output = msliteNapi. runDemo (resMgr); if (output === null || output. length === 0 ) { hilog. error ( 0xFF00 , TAG , '%{public}s' , `MS_LITE_ERR: runDemo failed.` ); return } hilog. info ( 0xFF00 , TAG , '%{public}s' , `MS_LITE_LOG: output length = ${output.length} ; value = ${output.slice( 0 , 20 )} ` ); this . content = output; hilog. info ( 0xFF00 , TAG , '%{public}s' , `MS_LITE_LOG: *** Finished MSLite Demo ***` ); }) // 显示识别内容 if ( this . content ) { Text ( '识别内容: \n' + transverter ({ type : TransverterType . SIMPLIFIED , str : this . content , language : TransverterLanguage . ZH_CN }) + '\n' ). focusable ( true ). fontSize ( 20 ). height ( '20%' ) } }. width ( '100%' ) } . height ( '100%' ) } }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/ets/pages/Index.ets#L16-L99)   

### 调测验证

1. 在DevEco Studio中连接设备，点击Run entry，编译Hap，有如下显示：

 收起自动换行深色代码主题复制

```
Launching com.samples.mindsporelitecdemoasr $ hdc shell aa force-stop com.samples.mindsporelitecdemoasr $ hdc shell mkdir data/local/tmp/xxx $ hdc file send E:\xxx\entry\build\default\outputs\default\entry-default-signed.hap "data/local/tmp/xxx" $ hdc shell bm install -p data/local/tmp/xxx $ hdc shell rm -rf data/local/tmp/xxx $ hdc shell aa start -a EntryAbility -b com.samples.mindsporelitecdemoasr com.samples.mindsporelitecdemoasr successfully launched...
```
2. 在设备屏幕点击播放示例音频按钮，会播放本示例音频文件。点击识别示例音频按钮，设备屏幕显示本示例音频文件的中文内容。在日志打印结果中，过滤关键字”MS_LITE_LOG“，可得到如下结果：

 收起自动换行深色代码主题复制

```
```

### 效果示意

在设备上，点击**播放示例音频**按钮，会播放本示例音频文件。点击**识别示例音频**按钮，设备屏幕显示本示例音频文件的中文内容。

  展开

| 初始页面 | 点击识别示例音频按钮后 |
| --- | --- |
|  |  |

## 示例代码

- [基于MindSporeLite接口实现语音识别（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/HarmonyOS-feature-20251117/MindSporeLiteKit/MindSporeLiteCDemoASR)
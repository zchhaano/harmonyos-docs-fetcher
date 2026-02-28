# 录像实践(C/C++)

在开发相机应用时，需要先[申请相关权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-preparation)。

当前示例提供完整的录像流程及其接口调用顺序的介绍。对于单个流程（如[设备输入](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-device-input)、[会话管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-session-management)、[录像](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-recording)）的介绍请参考具体章节。

## 开发流程

在获取到相机支持的输出流能力后，开始创建录像流，开发流程如下。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165432.16397249118022943723877083723655:50001231000000:2800:29FB6771259761EAE8163E7CB8141F786ED7EECE787B76F25974E4B89A5B0F9C.png)

## 完整示例

1. 在CMake脚本中链接相关动态库。

 收起自动换行深色代码主题复制

```
target_link_libraries(entry PUBLIC libace_napi.z.so libohcamera.so libhilog_ndk.z.so )
```
2. 创建头文件ndk_camera.h。

 收起自动换行深色代码主题复制

```
# include "ohcamera/camera.h" # include "ohcamera/camera_input.h" # include "ohcamera/capture_session.h" # include "ohcamera/photo_output.h" # include "ohcamera/preview_output.h" # include "ohcamera/video_output.h" # include "ohcamera/camera_manager.h" class NDKCamera { public : ~ NDKCamera (); NDKCamera ( char * previewId, char * videoId); };
```
3. cpp侧导入NDK接口，并根据传入的SurfaceId进行录像。

 收起自动换行深色代码主题复制

```
```

## 示例代码

- 录像示例代码请参考[NDKPhotoVideoSample(C/C++)](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/CameraKit/NDKPhotoVideoSample)。
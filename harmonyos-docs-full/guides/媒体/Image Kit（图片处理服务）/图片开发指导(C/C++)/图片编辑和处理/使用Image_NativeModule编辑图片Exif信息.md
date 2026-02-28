# 使用Image_NativeModule编辑图片Exif信息

Image Kit提供图片Exif信息的读取与编辑能力。

Exif（Exchangeable image file format）是专门为数码相机的照片设定的文件格式，可以记录数码照片的属性信息和拍摄数据。当前支持JPEG、PNG、HEIF、WEBP23+格式，且需要图片包含Exif信息。

在图库等应用中，需要查看或修改数码照片的Exif信息。当摄像机的手动镜头参数无法自动写入到Exif信息中，或者相机断电等原因会导致拍摄时间出错时，可手动修改错误的Exif数据。

HarmonyOS目前仅支持对部分Exif信息的查看和修改，具体支持的范围请参见：[OHOS_IMAGE_PROPERTY_XXX](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h#变量)。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target_link_libraries依赖中添加libimage_source.so 以及日志依赖libhilog_ndk.z.so。

 收起自动换行深色代码主题复制

```
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so)
```

### Native接口调用

Exif信息的读取与编辑相关C API接口的详细介绍请参见[OH_ImageSource_GetImageProperty](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_getimageproperty) 和 [OH_ImageSource_ModifyImageProperty](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_modifyimageproperty)。

在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**读取和编辑图片Exif信息接口使用示例**

 说明 

部分接口在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1. 导入相关头文件。

 收起自动换行深色代码主题复制

```
# include <string> # include <hilog/log.h> # include <multimedia/image_framework/image/image_source_native.h> # include "napi/native_api.h"
```
2. 日志宏定义可参考下述代码按实际需求自行修改。

 收起自动换行深色代码主题复制

```
# undef LOG_DOMAIN # undef LOG_TAG # define LOG_DOMAIN 0x3200 # define LOG_TAG "IMAGE_SAMPLE"
```
3. 定义ImageSourceNative类。

 收起自动换行深色代码主题复制

```
class ImageSourceNative { public: OH_ImageSource_Info *imageInfo; OH_ImageSourceNative *source = nullptr; OH_PixelmapNative *resPixMap = nullptr; OH_Pixelmap_ImageInfo *pixelmapImageInfo = nullptr; uint32_t frameCnt = 0 ; ImageSourceNative() {} ~ImageSourceNative() {} };
```
4. 创建ImageSourceNative的一个实例。

 收起自动换行深色代码主题复制

```
static ImageSourceNative *g_thisImageSource = new ImageSourceNative ();
```
5. 创建GetJsResult函数处理napi返回值。

 收起自动换行深色代码主题复制

```
// 处理napi返回值。 napi_value GetJsResult (napi_env env, int result) { napi_value resultNapi = nullptr ; napi_create_int32 (env, result, &resultNapi); return resultNapi; }
```
6. 在成功创建ImageSource对象后，读取、编辑Exif信息。

 说明 

创建ImageSource对象可参考[图片解码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-source-c)。

  收起自动换行深色代码主题复制

```
```
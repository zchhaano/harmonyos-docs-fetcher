# 使用Image_NativeModule完成多图对象解码

创建ImageSource实例，解码获取Picture，然后释放ImageSource实例。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target_link_libraries依赖中添加libimage_source.so 以及日志依赖libhilog_ndk.z.so。

 收起自动换行深色代码主题复制

```
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so)
```

### Native接口调用

具体接口说明请参考[API文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)。

在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**解码接口使用示例**

 说明 

部分接口在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1. 导入相关头文件。

 收起自动换行深色代码主题复制

```
# include <hilog/log.h> # include <multimedia/image_framework/image/image_native.h> # include <multimedia/image_framework/image/image_packer_native.h> # include <multimedia/image_framework/image/image_source_native.h> # include <multimedia/image_framework/image/picture_native.h> # include <multimedia/image_framework/image/pixelmap_native.h>
```
2. 日志宏定义可参考下述代码按实际需求自行修改。

 收起自动换行深色代码主题复制

```
# undef LOG_DOMAIN # undef LOG_TAG # define LOG_DOMAIN 0x3200 # define LOG_TAG "IMAGE_SAMPLE"
```
3. 定义ImagePictureNative类。

 收起自动换行深色代码主题复制

```
class ImagePictureNative { public: Image_ErrorCode errorCode = IMAGE_SUCCESS; OH_DecodingOptionsForPicture *options = nullptr; OH_ImagePackerNative *imagePacker = nullptr; OH_PackingOptions *packerOptions = nullptr; OH_PictureNative *picture = nullptr; OH_ImageSourceNative *source = nullptr; ImagePictureNative() {} ~ImagePictureNative() {} };
```
4. 创建一个ImagePictureNative实例。

 收起自动换行深色代码主题复制

```
static ImagePictureNative *g_thisPicture = new ImagePictureNative ();
```
5. 定义ImageAuxiliaryPictureNative类。

 收起自动换行深色代码主题复制

```
class ImageAuxiliaryPictureNative { public: Image_ErrorCode errorCode = IMAGE_SUCCESS; Image_AuxiliaryPictureType type = AUXILIARY_PICTURE_TYPE_GAINMAP; OH_AuxiliaryPictureNative *auxiliaryPicture = nullptr; size_t buffSize = 640 * 480 * 4 ; // 辅助图size：`长 * 宽 * 每个像素占用的字节数`。 ImageAuxiliaryPictureNative() {} ~ImageAuxiliaryPictureNative() {} };
```
6. 创建一个ImageAuxiliaryPictureNative实例。

 收起自动换行深色代码主题复制

```
static ImageAuxiliaryPictureNative *g_thisAuxiliaryPicture  = new ImageAuxiliaryPictureNative ();
```
7. 创建GetJsResult函数处理napi返回值。

 收起自动换行深色代码主题复制

```
// 处理napi返回值。 napi_value GetJsResult (napi_env env, int result) { napi_value resultNapi = nullptr ; napi_create_int32 (env, result, &resultNapi); return resultNapi; }
```
8. 创建解码参数，配置解码参数，调用解码接口进行解码并获取辅助图。

 收起自动换行深色代码主题复制

```
```
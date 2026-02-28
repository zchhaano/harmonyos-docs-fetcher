# OH_NativeBuffer_Planes

收起自动换行深色代码主题复制

```
typedef struct OH_NativeBuffer_Planes { ...} OH_NativeBuffer_Planes
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

OH_NativeBuffer的图像平面格式信息。

**起始版本：** 12

**相关模块：** [OH_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer)

**所在头文件：** [native_buffer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-buffer-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| uint32_t planeCount | 不同平面的数量。 |
| OH_NativeBuffer_Plane planes[4] | 图像平面格式信息数组。 |
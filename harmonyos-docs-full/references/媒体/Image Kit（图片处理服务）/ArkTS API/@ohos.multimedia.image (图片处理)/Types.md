# Types

说明 

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## HdrMetadataValue 12+

支持设备PhonePC/2in1TabletTVWearable

type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata

PixelMap使用的HDR元数据值类型，和[HdrMetadataKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-e#hdrmetadatakey12)关键字相对应。

**系统能力：** SystemCapability.Multimedia.Image.Core

 展开

| 类型 | 说明 |
| --- | --- |
| HdrMetadataType | HdrMetadataKey 中HDR_GAINMAP_METADATA关键字对应的元数据值类型。 |
| HdrStaticMetadata | HdrMetadataKey 中HDR_STATIC_METADATA关键字对应的元数据值类型。 |
| ArrayBuffer | HdrMetadataKey 中HDR_DYNAMIC_METADATA关键字对应的元数据值类型。 |
| HdrGainmapMetadata | HdrMetadataKey 中HDR_GAINMAP_METADATA关键字对应的元数据值类型。 |
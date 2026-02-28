# Subpass Shading

随着游戏场景的复杂化，越来越多的光照效果被应用到游戏场景中，随之也带来大量的光照计算以及带宽消耗。目前通过Tile-Based Deferred Rendering（TBDR）和Forward+等方法可以解决大量光照的渲染时间消耗，但是大量带宽的占用问题还是没有解决，Subpass Shading能力主要减少计算过程中的读写从而减少带宽的占用。

下图说明Subpass Shading节省渲染通道1和Compute Pass从Device memory上面的一次读写带宽。

 **图1**Forward+读取过程 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165347.86408504690326060871592686035931:50001231000000:2800:7FEED62325D5674958D3F4421D275CEC54A3E503CCC42B4348669459ABD735AD.png)

 **图2**Subpass Shading读取过程 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165348.13263178689010731288470198799265:50001231000000:2800:CF32FFB94C9D83EE5157CC740F8B14729AF196D9CE739A4F7F934851839AC6AC.png)

## 约束与限制

支持的设备类型：Phone，从5.0.2(14)版本开始，新增支持Tablet、PC/2in1设备，从5.1.0(18)版本开始新增支持TV设备。

## 接口说明

通过Vulkan扩展接口[VK_HUAWEI_subpass_shading](https://registry.khronos.org/vulkan/specs/latest/man/html/VK_HUAWEI_subpass_shading.html)提供Subpass Shading API，该扩展支持在Subpass中使用Compute Shader，并在Compute Shader中使用SubpassLoad从Tile buffer中直接读取数据，可用于降低DDR带宽，适用于TBDR和Forward+管线。

Subpass Shading能力具体使用请参见[Demo（GPU加速引擎-Subpass Shading）](https://gitcode.com/harmonyos_samples/xengine-samplecode-subpass-shading-demo-cpp)。
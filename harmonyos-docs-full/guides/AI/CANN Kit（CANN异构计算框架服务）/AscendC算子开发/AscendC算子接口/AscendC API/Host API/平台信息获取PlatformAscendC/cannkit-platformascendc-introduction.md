# 简介

  

#### 函数功能

在实现Host侧的Tiling函数时，可能需要获取一些硬件平台的信息，来支撑Tiling的计算，比如获取硬件平台的核数等信息。PlatformAscendC类提供获取这些平台信息的功能。

 ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/fJ8lY0o4QVOL8AgHT8mnyQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T191604Z&HW-CC-Expire=86400&HW-CC-Sign=1CFF1F443B03B3B404A4E5D7E82B0555F103544B611AF723A735DBD8A8B610F2)  

使用该功能需要包含"tiling/platform/platform_ascendc.h"头文件。

   

#### 函数原型

```
PlatformAscendC() = delete
~PlatformAscendC() = default
explicit PlatformAscendC(fe::PlatFormInfos *platformInfo): platformInfo_(platformInfo) {}

```

  

#### 参数说明

 

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| platformInfo | 输入 | platformInfo结构体，通过 GetPlatformInfo 接口可以获取。 |

   

#### 返回值

无

  

#### 约束说明

无

  

#### 调用示例

```
ge::graphStatus TilingXXX(gert::TilingContext* context) {
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
    uint64_t ub_size, l1_size;
    ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, ub_size);
    ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::L1, l1_size);
    auto aicNum = ascendcPlatform.GetCoreNumAic();
    auto aivNum = ascendcPlatform.GetCoreNumAiv();
    // ... 按照aivNum切分
    context->SetBlockDim(ascendcPlatform.CalcTschBlockDim(aivNum, aicNum, aivNum));
    return ret;
}

```
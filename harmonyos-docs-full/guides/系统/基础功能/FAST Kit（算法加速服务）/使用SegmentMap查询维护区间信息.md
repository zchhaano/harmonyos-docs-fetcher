# 使用SegmentMap查询维护区间信息

FAST Kit提供Segment Map用于查询维护区间信息，实现数据序列区间段的快速更新和快速查询。线段表（Segment Map）是一种用于高效处理区间段信息的数据结构，适用于需要频繁对数据序列的某个区间段进行统计或修改的场景。其典型操作包括单点修改、区间修改、区间查询等。

线段表有多种实现方式，其中最常见的是使用二分树的方案，也被称为线段树（Segment Tree）。与直接遍历区间相比，线段表能将许多区间操作的时间复杂度从 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170022.84163517241229911948340270618832:50001231000000:2800:0BDBEEDBDE64F8D7B90EB3C2D26EC24E07FDB1F6CF96D94803BD6C5C30EA59AA.png) 优化至![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170022.38978387711499700104894848525052:50001231000000:2800:3AFB0D3270428D838BE88CA8FA3D01E6A1891B9E32A5DC7468C53F0E7AE303A5.png)，在处理大规模数据时优势显著，为构建高性能、响应迅速的应用程序提供数据结构基础。

## 接口说明

具体API说明详见[接口文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)。

  展开

| 名称 | 描述 |
| --- | --- |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_CreateConfig ( FAST_SegmentMapConfig **config) | 创建线段表的不透明配置。 |
| FAST_EXPORT void HMS_FAST_SegmentMap_DestroyConfig ( FAST_SegmentMapConfig *config) | 销毁线段表的不透明配置。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_SetQueryType ( FAST_SegmentMapConfig *config, FAST_SegmentMapQueryType type) | 设置线段表不透明配置中的查询类型。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_SetUpdateType ( FAST_SegmentMapConfig *config, FAST_SegmentMapUpdateType type) | 设置线段表不透明配置中的更新类型。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Create ( FAST_SegmentMapHandle *handle, size_t size, const int32_t *array, FAST_SegmentMapConfig *config) | 创建线段表。 |
| FAST_EXPORT void HMS_FAST_SegmentMap_Destroy ( FAST_SegmentMapHandle handle) | 销毁线段表实例，释放内存，再次调用为未定义行为。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Update ( FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t value) | 更新线段表的区间，根据配置按照赋值、加法、减法等操作更新。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Query ( FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t *result) | 查询线段表的区间，根据配置返回最大值、最小值、求和等数据。 |

## 开发步骤

1. 首先在CMake脚本中链接相关动态库。 

 收起自动换行深色代码主题复制

```
target_link_libraries (entry PUBLIC libfast_ads.so)
```
2. 调用HMS_FAST_SegmentMap_CreateConfig生成线段表配置实例（FAST_SegmentMapConfig）。
3. 调用HMS_FAST_SegmentMap_SetQueryType设置查询类型。
4. 调用HMS_FAST_SegmentMap_SetUpdateType设置更新类型。
5. 调用HMS_FAST_SegmentMap_Create生成线段表实例 （FAST_SegmentMapHandle）。生成实例之后，无法再修改查询和更新类型。
6. 调用HMS_FAST_SegmentMap_Query进行高效区间查询操作。
7. 调用HMS_FAST_SegmentMap_Update进行高效区间更新操作。
8. 调用HMS_FAST_SegmentMap_Destroy销毁线段表实例。
9. 调用HMS_FAST_SegmentMap_DestroyConfig销毁线段表配置实例。

 收起自动换行深色代码主题复制

```
```
## 概述

支持设备PhonePC/2in1Tablet

提供与检索结果相关的接口。

**引用文件：** #include "dataaugmentation/retrieval/aip_retrieval_record.h"

**库：** libnative_aip_retrieval_ndk.so

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**相关模块：** [Retrieval](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval)

## 汇总

支持设备PhonePC/2in1Tablet 

### 类型定义

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| typedef struct OH_Retrieval_Record OH_Retrieval_Record | 定义检索结果，包含检索知识库得到的字段和字段取值。 |
| typedef struct OH_Retrieval_RecordItem OH_Retrieval_RecordItem | 定义检索结果中的数据库bucket数组。 |

### 函数

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| int OH_Retrieval_DestroyRecord ( OH_Retrieval_Record *record) | 销毁通过检索接口 OH_Retrieval_Retrieve 获得的检索结果。 |
| int OH_Retrieval_GetRecordLength (const OH_Retrieval_Record *record, uint32_t *length) | 获取检索结果 OH_Retrieval_Record 中的数据库bucket数组长度。 |
| int OH_Retrieval_GetRecordItem (const OH_Retrieval_Record *record, uint32_t index, const OH_Retrieval_RecordItem **item) | 获取检索结果 OH_Retrieval_Record 中的数据库bucket数组。 |
| int OH_Retrieval_GetItemSize (const OH_Retrieval_RecordItem *items, const char *fieldName, size_t *size) | 获取数据库bucket数组 OH_Retrieval_RecordItem 中指定字段的值的size。size值包含结束符。 |
| int OH_Retrieval_GetItemText (const OH_Retrieval_RecordItem *items, const char *fieldName, char *value, size_t size) | 获取数据库bucket数组 OH_Retrieval_RecordItem 中指定字段的值。 |
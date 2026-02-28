## 场景介绍

智慧化数据检索可用于文件整理，文件搜索等场景，例如：关键词检索、语义检索（文搜文）和跨模态检索（文搜图）。智慧化数据检索通过召回和重排两个阶段实现：

- 召回是指通过不同的策略或算法从海量数据中快速筛选出候选结果集。这些策略可针对不同的特征、模型或者数据来源，旨在尽可能覆盖各种潜在场景。ArkData提供了向量召回的能力，并支持灵活的条件过滤。
- 重排是针对召回得到的候选结果集进行二次筛选，通过简单规则或者更复杂的模型（如机器学习或深度学习模型）计算各个结果的相关性分数，并重新排列顺序。

## 向量检索召回

向量召回是通过将用户查询转化为向量（需使用嵌入模型进行向量化处理）来检索相似向量，从而实现语义相近内容的召回。向量近似的阈值在召回配置中设定。

## 排序模块

排序模块包括对结果进行分档以及档内排序，使用的算法有RRF和分数融合排序。

### 对结果进行分档

以召回结果作为输入，基于召回的特征值或者召回分数，实现召回结果的相关性分档。档位共三个，分为高、中、低档位，供业务对最终检索结果相关性进行判断。

对于向量召回，基于配置的一个或多个向量分数阈值对档位进行划分，当文档的向量分数大于等于某档位的阈值时，则划分至该档位。向量分数阈值是由1个或2个范围在[0,1]的数字组成。向量分数阈值有两个值时，分别表示高档位和中档位的阈值，向量分数小于中档位阈值则均为低档位；阈值有一个值时，该值表示高档位阈值，向量分数小于该值则均为低档位，无中档位。

## 约束限制

- 当前只支持基于向量数据库的召回。
- 查询词长度不超过512字符。

## 接口说明

  展开

| 名称 | 描述 |
| --- | --- |
| int OH_Retrieval_CreateRetriever (const OH_Retrieval_Config *config, OH_Retrieval_Retriever **retriever) | 获取检索器。 |
| int OH_Retrieval_DestroyRetriever ( OH_Retrieval_Retriever *retriever) | 销毁通过 OH_Retrieval_CreateRetriever 获得的检索器。 |
| OH_Retrieval_Config * OH_Retrieval_CreateConfig () | 获取检索器配置。 |
| int OH_Retrieval_DestroyConfig ( OH_Retrieval_Config *config) | 销毁通过 OH_Retrieval_CreateConfig 获得的检索配置。 |
| OH_Retrieval_DbConfig * OH_Retrieval_CreateDbConfig () | 创建一个配置项以打开数据库。 |
| int OH_Retrieval_DestroyDbConfig ( OH_Retrieval_DbConfig *dbConfig) | 销毁 OH_Retrieval_CreateDbConfig 创建的 OH_Retrieval_DbConfig 。 |
| int OH_Retrieval_SetDbConfig ( OH_Retrieval_DbConfig *dbConfig, OH_Rdb_ConfigV2 *rdbConfig) | 设置 OH_Retrieval_DbConfig 中的数据库配置。 |
| int OH_Retrieval_AddConfig ( OH_Retrieval_Config *config, Retrieval_Channel_Type channelType, OH_Retrieval_DbConfig *dbConfig) | 设置 OH_Retrieval_Config 中的数据库配置。 |
| int OH_Retrieval_Retrieve (const OH_Retrieval_Retriever *retriever, const OH_Retrieval_Query *query, const OH_Retrieval_Condition *condition, void *context, const OH_Retrieval_Callback *callback) | 执行检索。获得检索器句柄后，输入检索查询词，根据检索条件执行检索，得到检索结果。 |
| OH_Retrieval_Condition * OH_Retrieval_CreateCondition () | 创建检索条件，作为检索接口的入参。 |
| int OH_Retrieval_DestroyCondition ( OH_Retrieval_Condition *condition) | 销毁通过 OH_Retrieval_CreateCondition 获得的检索条件。 |
| int OH_Retrieval_DestroySubCondition ( OH_Retrieval_SubCondition *condition) | 销毁 OH_Retrieval_SubCondition 对象。 |
| int OH_Retrieval_AddSubCondition ( OH_Retrieval_Condition *condition, OH_Retrieval_SubCondition *subCondition) | 在检索条件中，增加子检索条件。 |
| OH_Retrieval_VectorCondition * OH_Retrieval_CreateVectorCondition () | 创建向量检索条件。 |
| int OH_Retrieval_DestroyVectorCondition ( OH_Retrieval_VectorCondition *condition) | 销毁通过 OH_Retrieval_CreateVectorCondition 获得的检索条件。 |
| int OH_Retrieval_SetVectorRecallLimit ( OH_Retrieval_VectorCondition *condition, uint32_t limit) | 在检索条件中，设置向量检索结果数量上限1000。 |
| int OH_Retrieval_SetSimilarityThreshold ( OH_Retrieval_VectorCondition *condition, double threshold) | 在检索条件中，设置向量检索的相似度阈值。 |
| OH_Retrieval_Query * OH_Retrieval_CreateQuery () | 创建检索词，作为检索接口的入参。 |
| int OH_Retrieval_DestroyQuery ( OH_Retrieval_Query *query) | 销毁通过 OH_Retrieval_CreateQuery 获得的检索词。 |
| int OH_Retrieval_SetOriginalQuestion ( OH_Retrieval_Query *query, const char *question) | 设置 OH_Retrieval_Query 中的检索词。 |
| int OH_Retrieval_DestroyRecord ( OH_Retrieval_Record *record) | 销毁通过检索接口 OH_Retrieval_Retrieve 获得的检索结果。 |
| int OH_Retrieval_GetRecordLength (const OH_Retrieval_Record *record, uint32_t *length) | 获取检索结果 OH_Retrieval_Record 中的数据库bucket数组长度。 |
| int OH_Retrieval_GetRecordItem (const OH_Retrieval_Record *record, uint32_t index, const OH_Retrieval_RecordItem **item) | 获取检索结果 OH_Retrieval_Record 中的数据库bucket数组。 |
| int OH_Retrieval_GetItemSize (const OH_Retrieval_RecordItem *items, const char *fieldName, size_t *size) | 获取数据库bucket数组 OH_Retrieval_RecordItem 中指定字段的值的size。size值包含结束符。 |
| int OH_Retrieval_GetItemText (const OH_Retrieval_RecordItem *items, const char *fieldName, char *value, size_t size) | 获取数据库bucket数组 OH_Retrieval_RecordItem 中指定字段的值。 |

## 开发步骤

1. 在CMake脚本中链接动态库。      收起自动换行深色代码主题复制

```
find_library (aip_retrieval_ndk libnative_aip_retrieval_ndk.z.so) target_link_libraries ( entry PUBLIC libace_napi.z.so ${aip_retrieval_ndk} )
```
2. 导入头文件。      收起自动换行深色代码主题复制

```
# include "dataaugmentation/retrieval/aip_retrieval.h" # include "dataaugmentation/retrieval/aip_retrieval_condition.h" # include "dataaugmentation/retrieval/aip_retrieval_condition_vector.h" # include "dataaugmentation/retrieval/aip_retrieval_query.h" # include "dataaugmentation/retrieval/aip_retrieval_record.h" # include "dataaugmentation/aip_error_code.h"
```
3. 初始化数据。      收起自动换行深色代码主题复制

```
```
4. 配置数据库相关的信息和上下文对象，并且生成检索器对象，用于后面的检索。      收起自动换行深色代码主题复制

```
// 创建检索器 // 创建检索器配置 OH_Retrieval_Config *config = OH_Retrieval_CreateConfig (); // 创建数据库配置 OH_Retrieval_DbConfig *dbConfig = OH_Retrieval_CreateDbConfig (); // 创建关系型数据库的配置 OH_Rdb_ConfigV2 *rdbConfig = OH_Rdb_CreateConfig (); // 设置关系型数据库配置的目录 int ret = OH_Rdb_SetDatabaseDir (rdbConfig, RDB_TEST_PATH); // 设置关系型数据库配置的数据库名 ret = OH_Rdb_SetStoreName (rdbConfig, "vector_test.db" ); // 设置关系型数据库配置的应用包名 ret = OH_Rdb_SetBundleName (rdbConfig, "retrievalTest" ); // 设置关系型数据库配置的加密状态 ret = OH_Rdb_SetEncrypted (rdbConfig, false ); // 设置关系型数据库配置的加密级别 ret = OH_Rdb_SetSecurityLevel (rdbConfig, OH_Rdb_SecurityLevel :: S1 ); // 设置关系型数据库配置的安全区域 ret = OH_Rdb_SetArea (rdbConfig, RDB_SECURITY_AREA_EL1); // 设置数据库配置 ret = OH_Retrieval_SetDbConfig (dbConfig, rdbConfig); // 把数据库配置添加到检索器中 ret = OH_Retrieval_AddConfig (config, Retrieval_TYPE_VECTOR, dbConfig);
```
5. 使用前一步获取到的检索器，配合检索条件进行检索。      收起自动换行深色代码主题复制

```
// 创建检索器 OH_Retrieval_Retriever* retriever = nullptr ; ret = OH_Retrieval_CreateRetriever (config, &retriever); // 创建检索词 // 创建检索词query OH_Retrieval_Query *query = OH_Retrieval_CreateQuery (); // 设置检索词 const char *question = "how old are you" ; int ret = OH_Retrieval_SetOriginalQuestion (query, question); // 创建检索条件 OH_Retrieval_Condition *condition = OH_Retrieval_CreateCondition (); // 创建向量检索条件 OH_Retrieval_SubCondition *subCondition = OH_Retrieval_CreateVectorCondition (); // 在检索条件中，设置向量检索结果数量上限 int ret = OH_Retrieval_SetVectorRecallLimit (subCondition, 10 ); // 在检索条件中，设置向量检索的相似度阈值 ret = OH_Retrieval_SetSimilarityThreshold (subCondition, 0.35 ); // 把向量检索条件添加到检索条件中 ret = OH_Retrieval_AddSubCondition (condition, subCondition); // 创建检索结果 OH_Retrieval_Record *records = AipRetrievalRecordBuilder:: CreateAipRetrievalRecord (); // 定义检索完成返回结果的回调函数 static void Callback ( void *context, OH_Retrieval_Record *record) { // 获取Record长度 uint32_t length = 0 ; int ret = OH_Retrieval_GetRecordLength (record, &length); // 获取Record OH_Retrieval_RecordItem *item = nullptr ; ret = OH_Retrieval_GetRecordItem (record, 0 , &item); // 根据字段名获取Item size std::string fieldName = "filename_text" ; size_t size = 0 ; ret = OH_Retrieval_GetItemSize (item, fieldName. c_str (), &size); // 获取Item char value[size + 1 ]; ret = OH_Retrieval_GetItemText (item, fieldName. c_str (), value, size); } // 执行检索 // 进行检索，入参依次为上面创建的检索器retriever，检索词query，检索条件condition，以及检索完成返回结果的回调函数Callback int ret = OH_Retrieval_Retrieve (retriever, query, condition, &Callback);
```
6. 销毁相关资源。      收起自动换行深色代码主题复制

```
// 销毁检索器配置 int ret = OH_Retrieval_DestroyConfig (config); // 销毁数据库配置 ret = OH_Retrieval_DestroyDbConfig (dbConfig); // 销毁关系型数据库的配置 ret = OH_Rdb_DestroyConfig (rdbConfig); // 销毁检索器 ret = OH_Retrieval_DestroyRetriever (retriever); // 销毁检索词query ret = OH_Retrieval_DestroyQuery (query); // 销毁向量检索条件 ret = OH_Retrieval_DestroyVectorCondition (subCondition); // 销毁检索条件 ret = OH_Retrieval_DestroyCondition (condition);
```

## C++完整示例

 收起自动换行深色代码主题复制

```
# include "dataaugmentation/retrieval/aip_retrieval.h" # include "dataaugmentation/retrieval/aip_retrieval_condition.h" # include "dataaugmentation/retrieval/aip_retrieval_condition_vector.h" # include "dataaugmentation/retrieval/aip_retrieval_query.h" # include "dataaugmentation/retrieval/aip_retrieval_record.h" # include "dataaugmentation/aip_error_code.h" # include < string > size_t g_size = 0 ; char g_value[ 50 ] ; static const char *RETRIEVE_RDB_TEST_PATH = "/data/storage/el2/database/" ; const std::string RDB_STORE_PATH = "test.db" ; void test () { OH_Retrieval_Retriever* retriever = nullptr ; OH_Retrieval_Config *config = OH_Retrieval_CreateConfig () ; OH_Retrieval_DbConfig *dbConfig = OH_Retrieval_CreateDbConfig () ; OH_Rdb_ConfigV2 *rdbConfig = OH_Rdb_CreateConfig () ; auto ret = OH_Rdb_SetDatabaseDir (rdbConfig , RETRIEVE_RDB_TEST_PATH) ; ret = OH_Rdb_SetStoreName (rdbConfig , RDB_STORE_PATH. c_str ()) ; ret = OH_Rdb_SetBundleName (rdbConfig , "retrievalTest" ) ; ret = OH_Rdb_SetEncrypted (rdbConfig , false ) ; ret = OH_Rdb_SetSecurityLevel (rdbConfig , 1 ) ; ret = OH_Rdb_SetArea (rdbConfig , 1 ) ; ret = OH_Retrieval_SetDbConfig (dbConfig , rdbConfig) ; ret = OH_Retrieval_AddConfig (config , RETRIEVAL_TYPE_VECTOR , dbConfig) ; ret = OH_Retrieval_CreateRetriever (config , &retriever) ; // build query OH_Retrieval_Query *query = OH_Retrieval_CreateQuery () ; const char *question = " 运动 " ; ret = OH_Retrieval_SetOriginalQuestion (query , question) ; // build condition OH_Retrieval_Condition *condition = OH_Retrieval_CreateCondition () ; OH_Retrieval_SubCondition *subCondition = OH_Retrieval_CreateVectorCondition () ; ret = OH_Retrieval_SetVectorRecallLimit (subCondition , 10 ) ; ret = OH_Retrieval_SetSimilarityThreshold (subCondition , 0.35 ) ; ret = OH_Retrieval_AddSubCondition (condition , subCondition) ; const OH_Retrieval_Callback callback = []( void *context , OH_Retrieval_Record *record , int errCode)  { uint32_t length = 0 ; auto ret = OH_Retrieval_GetRecordLength (record , &length) ; const OH_Retrieval_RecordItem *item = nullptr ; ret = OH_Retrieval_GetRecordItem (record , 0 , &item) ; std::string fieldName = "subject" ; ret = OH_Retrieval_GetItemSize (item , fieldName. c_str () , &g_size) ; ret = OH_Retrieval_GetItemText (item , fieldName. c_str () , g_value , g_size) ; ret = OH_Retrieval_DestroyRecord (record) ; } ; ret = OH_Retrieval_Retrieve (retriever , query , condition , nullptr , &callback) ; // destroy ret = OH_Retrieval_DestroyConfig (config) ; ret = OH_Retrieval_DestroyDbConfig (dbConfig) ; ret = OH_Rdb_DestroyConfig (rdbConfig) ; ret = OH_Retrieval_DestroyRetriever (retriever) ; ret = OH_Retrieval_DestroyQuery (query) ; ret = OH_Retrieval_DestroyVectorCondition (subCondition) ; ret = OH_Retrieval_DestroyCondition (condition) ; }
```
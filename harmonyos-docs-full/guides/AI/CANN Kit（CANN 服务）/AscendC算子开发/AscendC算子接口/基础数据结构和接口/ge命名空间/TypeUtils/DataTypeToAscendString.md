## 函数功能

将DataType类型值转化为字符串表达。

使用该接口需要包含type_utils.h头文件。

 收起自动换行深色代码主题复制

```
# include "graph/utils/type_utils.h"
```

## 函数原型

收起自动换行深色代码主题复制

```
static AscendString DataTypeToAscendString ( const DataType &data_type) ;
```

## 参数说明

 展开

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| data_type | 输入 | 待转换的DataType，支持的DataType请参考 DataType 。 |

## 返回值

转换后的DataType字符串，[AscendString](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ascendstring-construction-and-destructor)类型。

## 约束说明

无

## 调用示例

收起自动换行深色代码主题复制

```
DataType data_type = ge::DT_UINT32; auto type_str = DataTypeToAscendString (data_type); // "DT_UINT32" const char *ptr = type_str. GetString (); // 获取char*指针
```
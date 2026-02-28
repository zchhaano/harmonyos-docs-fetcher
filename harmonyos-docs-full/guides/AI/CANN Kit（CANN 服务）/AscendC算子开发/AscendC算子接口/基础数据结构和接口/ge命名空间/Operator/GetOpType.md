## 函数功能

获取算子类型。

## 函数原型

注意

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

  收起自动换行深色代码主题复制

```
std::string GetOpType () const ; graphStatus GetOpType (AscendString &type) const ;
```

## 参数说明

 展开

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| type | 输出 | 算子类型。 |

## 返回值

 展开

| 类型 | 描述 |
| --- | --- |
| graphStatus | GRAPH_FAILED：失败。 GRAPH_SUCCESS：成功。 |

## 异常处理

无

## 约束说明

无
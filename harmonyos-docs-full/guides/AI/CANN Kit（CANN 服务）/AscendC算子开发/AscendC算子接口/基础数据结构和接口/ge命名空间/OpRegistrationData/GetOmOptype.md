## 函数功能

获取模型的算子类型。

## 函数原型

注意

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

  收起自动换行深色代码主题复制

```
std::string GetOmOptype () const ; Status GetOmOptype (ge::AscendString &om_op_type) const ;
```

## 参数说明

 展开

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| om_op_type | 输出 | 模型的算子类型。 |

## 约束说明

无
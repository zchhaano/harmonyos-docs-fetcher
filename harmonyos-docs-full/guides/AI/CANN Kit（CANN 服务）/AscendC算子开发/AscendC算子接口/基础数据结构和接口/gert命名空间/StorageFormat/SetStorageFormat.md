## 函数功能

设置运行时format。

## 函数原型

收起自动换行深色代码主题复制

```
void SetStorageFormat ( const ge::Format storage_format)
```

## 参数说明

 展开

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| storage_format | 输入 | 运行时format。 |

## 返回值

无

## 约束说明

无

## 调用示例

收起自动换行深色代码主题复制

```
ExpandDimsType dim_type ( "1100" ) ; StorageFormat format (ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type) ; format. SetStorageFormat (ge::Format::FORMAT_NC);
```
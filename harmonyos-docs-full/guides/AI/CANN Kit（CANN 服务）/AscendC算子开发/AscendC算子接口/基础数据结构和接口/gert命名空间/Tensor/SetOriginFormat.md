## 函数功能

设置Tensor的原始format。

## 函数原型

收起自动换行深色代码主题复制

```
void SetOriginFormat ( const ge::Format origin_format)
```

## 参数说明

 展开

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| origin_format | 输入 | 原始format。 关于ge::Format类型的定义，请参见 Format 。 |

## 返回值

无

## 约束说明

无

## 调用示例

收起自动换行深色代码主题复制

```
Tensor t = {{}, {}, {}, {}, nullptr }; t. SetOriginFormat (ge::FORMAT_NHWC); t. SetStorageFormat (ge::FORMAT_NC1HWC0); auto fmt = t. GetOriginFormat (); // ge::FORMAT_NHWC
```
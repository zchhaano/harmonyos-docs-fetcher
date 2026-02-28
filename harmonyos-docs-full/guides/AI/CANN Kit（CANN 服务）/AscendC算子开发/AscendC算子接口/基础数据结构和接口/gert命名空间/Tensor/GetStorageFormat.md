## 函数功能

获取运行时Tensor的format。

## 函数原型

收起自动换行深色代码主题复制

```
ge::Format GetStorageFormat () const
```

## 参数说明

无

## 返回值

返回运行时format。

关于ge::Format类型的定义，请参见[Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-format)。

## 约束说明

无

## 调用示例

收起自动换行深色代码主题复制

```
Tensor t = {{}, {}, {}, {}, nullptr }; t. SetOriginFormat (ge::FORMAT_NHWC); t. SetStorageFormat (ge::FORMAT_NC1HWC0); auto fmt = t. GetStorageFormat (); // ge::FORMAT_NC1HWC0
```
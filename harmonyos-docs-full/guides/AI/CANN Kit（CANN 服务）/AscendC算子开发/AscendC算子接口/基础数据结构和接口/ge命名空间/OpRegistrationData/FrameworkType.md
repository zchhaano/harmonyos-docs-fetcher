## 函数功能

设置原始模型的框架类型。

## 函数原型

收起自动换行深色代码主题复制

```
OpRegistrationData & FrameworkType ( const domi::FrameworkType &fmk_type)
```

## 参数说明

 展开

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| fmk_type | 输入 | 框架类型。 CAFFE TENSORFLOW ONNX FrameworkType枚举值的定义如下。 收起 自动换行 深色代码主题 复制 enum FrameworkType { CAFFE = 0 , MINDSPORE = 1 , TENSORFLOW = 3 , ANDROID_NN, ONNX, FRAMEWORK_RESERVED, }; |
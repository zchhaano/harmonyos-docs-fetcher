## 函数功能

获取原始shape。

## 函数原型

收起自动换行深色代码主题复制

```
const Shape & GetOriginShape () const
```

## 参数说明

无

## 返回值

原始shape

## 约束说明

无

## 调用示例

收起自动换行深色代码主题复制

```
StorageShape shape ({ 3 , 256 , 256 }, { 256 , 256 , 3 }) ; auto origin_shape = shape. GetOriginShape (); // 3,256,256
```
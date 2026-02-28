## 函数功能

获取dim_num。

## 函数原型

收起自动换行深色代码主题复制

```
size_t GetDimNum () const
```

## 参数说明

无

## 返回值

获取dim_num，即Shape的长度。

## 约束说明

无

## 调用示例

收起自动换行深色代码主题复制

```
Shape shape0 ({ 3 , 256 , 256 }) ; auto dim_num = shape0. GetDimNum (); // 3
```
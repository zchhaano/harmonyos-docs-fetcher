## 函数功能

判断本shape是否为标量，所谓标量，是指GetDimNum()为0。

## 函数原型

收起自动换行深色代码主题复制

```
bool IsScalar () const
```

## 参数说明

无

## 返回值

true为标量，false为非标量。

## 约束说明

无

## 调用示例

收起自动换行深色代码主题复制

```
Shape shape0 ({ 3 , 256 , 256 }) ; Shape shape2; shape0. IsScalar (); // false shape2. IsScalar (); // true
```
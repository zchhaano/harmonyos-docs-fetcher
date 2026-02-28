## 函数功能

设置dim num。

## 函数原型

收起自动换行深色代码主题复制

```
void SetDimNum ( const size_t dim_num)
```

## 参数说明

 展开

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| dim_num | 输入 | 将Shape对象的dim_num_设置为dim_num。 |

## 返回值

无

## 约束说明

无

## 调用示例

收起自动换行深色代码主题复制

```
Shape shape0 ({ 3 , 256 , 256 }) ; shape0. SetDimNum ( 1 ); auto dim_num = shape0. GetDimNum (); // 1
```
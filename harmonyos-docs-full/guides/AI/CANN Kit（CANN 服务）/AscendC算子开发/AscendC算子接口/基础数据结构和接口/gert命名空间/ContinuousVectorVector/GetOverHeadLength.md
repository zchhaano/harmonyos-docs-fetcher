## 函数功能

获取数据描述信息的长度。

## 函数原型

收起自动换行深色代码主题复制

```
static size_t GetOverHeadLength ( const size_t capacity)
```

## 参数说明

 展开

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| capacity | 输入 | 实例的最大容量。 |

## 返回值

数据描述信息的长度。

## 约束说明

无

## 调用示例

收起自动换行深色代码主题复制

```
size_t capacity = 100U ; auto length = ContinuousVectorVector:: GetOverHeadLength (capacity);
```
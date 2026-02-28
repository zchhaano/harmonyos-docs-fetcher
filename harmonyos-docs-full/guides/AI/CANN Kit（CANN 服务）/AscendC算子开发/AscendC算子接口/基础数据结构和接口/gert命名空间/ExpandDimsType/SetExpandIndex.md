## 函数功能

将第index轴设置为补维轴。

## 函数原型

收起自动换行深色代码主题复制

```
void SetExpandIndex ( const AxisIndex index)
```

## 参数说明

 展开

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 第index根轴为补维轴。 收起 自动换行 深色代码主题 复制 using AxisIndex = uint64_t ; |

## 返回值

无

## 约束说明

无

## 调用示例

收起自动换行深色代码主题复制

```
ExpandDimsType type1 ( "1001" ) ; type1. SetExpandIndex ( 1 ); // 补维规则mask_=1101
```
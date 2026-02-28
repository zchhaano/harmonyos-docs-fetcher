## 函数功能

设置Tensor的数据存放的位置。

## 函数原型

收起自动换行深色代码主题复制

```
void SetPlacement (Placement placement) ;
```

## 参数说明

 展开

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| placement | 输入 | 需设置的数据地址的值。 枚举值定义如下。 收起 自动换行 深色代码主题 复制 enum Placement { kPlacementHost = 0 , // host data addr kPlacementDevice = 1 , // device data addr }; |

## 返回值

无

## 异常处理

无

## 约束说明

无
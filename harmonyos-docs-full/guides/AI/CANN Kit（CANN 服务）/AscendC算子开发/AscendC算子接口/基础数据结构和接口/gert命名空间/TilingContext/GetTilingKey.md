## 函数功能

获取tiling key。

## 函数原型

收起自动换行深色代码主题复制

```
uint64_t GetTilingKey () const ;
```

## 参数说明

无

## 返回值

返回tiling key。

## 约束说明

无

## 调用示例

收起自动换行深色代码主题复制

```
ge::graphStatus Tiling4XXX (TilingContext* context) { auto tiling_key = context-> GetTilingKey (); // ... }
```
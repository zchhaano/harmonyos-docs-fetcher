## 函数功能

获取fe::PlatformInfos指针。

## 函数原型

收起自动换行深色代码主题复制

```
fe::PlatFormInfos * GetPlatformInfo () const
```

## 参数说明

无

## 返回值

fe::PlatFormInfos指针。

## 约束说明

无

## 调用示例

收起自动换行深色代码主题复制

```
ge::graphStatus Tiling4XXX (TilingContext* context) { auto platform_info = context-> GetPlatformInfo (); // ... }
```
## 功能说明

用于释放HardEvent（硬件类型同步事件）的TEventID，通常与[AllocEventID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-alloceventid)搭配使用。

## 函数原型

收起自动换行深色代码主题复制

```
template <HardEvent evt> __aicore__ inline void ReleaseEventID (TEventID id)
```

## 参数说明

 展开

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| id | 输入 | TEventID类型，调用 AllocEventID 申请获得的TEventID。 |

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 注意事项

AllocEventID、ReleaseEventID需成对出现，ReleaseEventID传入的TEventID需由对应的AllocEventID申请而来。

## 返回值

无

## 调用示例

收起自动换行深色代码主题复制

```
AscendC::TEventID eventID = GetTPipePtr ()-> AllocEventID <AscendC::HardEvent::V_S>(); // 需要插scalar等vector的同步，申请对应的HardEvent的ID AscendC:: SetFlag <AscendC::HardEvent::V_S>(eventID); // ... AscendC:: WaitFlag <AscendC::HardEvent::V_S>(eventID); GetTPipePtr ()-> ReleaseEventID <AscendC::HardEvent::V_S>(eventID); // 释放scalar等vector的同步HardEvent的ID // ...
```
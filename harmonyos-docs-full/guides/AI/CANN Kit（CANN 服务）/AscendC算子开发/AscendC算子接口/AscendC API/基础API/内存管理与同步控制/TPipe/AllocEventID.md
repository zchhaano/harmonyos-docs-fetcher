## 功能说明

用于申请HardEvent（硬件类型同步事件）的TEventID，必须与[ReleaseEventID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-releaseeventid)搭配使用，调用该接口后，会占用申请的TEventID，直至调用ReleaseEventID释放。

## 函数原型

收起自动换行深色代码主题复制

```
template <HardEvent evt> __aicore__ inline TEventID TPipe::AllocEventID ()
```

## 参数说明

 展开

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| evt | 输入 | HardEvent硬件同步类型。 |

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 注意事项

TEventID有数量限制，使用结束应该立刻调用ReleaseEventID释放，防止TEventID耗尽。

## 返回值

TEventID

## 调用示例

收起自动换行深色代码主题复制

```
AscendC::TEventID eventID = GetTPipePtr ()-> AllocEventID <AscendC::HardEvent::V_S>(); // 需要插scalar等vector的同步，申请对应的HardEvent的ID AscendC:: SetFlag <AscendC::HardEvent::V_S>(eventID); // ... AscendC:: WaitFlag <AscendC::HardEvent::V_S>(eventID); GetTPipePtr ()-> ReleaseEventID <AscendC::HardEvent::V_S>(eventID); // 释放scalar等vector的同步HardEvent的ID // ...
```
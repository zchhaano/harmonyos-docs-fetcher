## 函数功能

设置tensor地址。

## 函数原型

收起自动换行深色代码主题复制

```
ge::graphStatus SetAddr ( const ConstTensorAddressPtr addr, TensorAddrManager manager)
```

## 参数说明

 展开

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| addr | 输入 | tensor地址。 收起 自动换行 深色代码主题 复制 using ConstTensorAddressPtr = const void *; |
| manager | 输入 | tensor的管理函数。 收起 自动换行 深色代码主题 复制 using TensorAddrManager = ge:: graphStatus (*)(TensorAddress addr, TensorOperateType operate_type, void **out); |

## 返回值

成功时返回ge::GRAPH_SUCCESS；失败时返回manager管理函数中定义的错误码。

## 约束说明

无

## 调用示例

收起自动换行深色代码主题复制

```
auto addr = reinterpret_cast < void *>( 0x10 ); TensorData td (addr, nullptr ) ; td. SetAddr (addr, HostAddrManager);
```
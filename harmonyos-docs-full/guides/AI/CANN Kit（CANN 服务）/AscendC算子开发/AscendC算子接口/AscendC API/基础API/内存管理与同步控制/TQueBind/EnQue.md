## 功能说明

将Tensor push到队列。

## 函数原型

收起自动换行深色代码主题复制

```
template < typename T> __aicore__ inline bool EnQue ( const LocalTensor<T>& tensor)
```

## 参数说明

 **表1**bool EnQue(LocalTensor<T>& tensor)原型定义参数说明展开

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| tensor | 输入 | 指定的Tensor。 |

  **图1**将LocalTensor通过EnQue放入A1/B1的Queue中
![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165328.54547904437981718184186122728570:50001231000000:2800:26CD69F60CCCC7271AE8C160E6C112DB35D95AA109CC9C165969BD79EC49DCEA.png)  

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 注意事项

无

## 返回值

- true：表示Tensor加入Queue成功。
- false：表示Queue已满，入队失败。

## 调用示例

收起自动换行深色代码主题复制

```
// 接口: EnQue Tensor AscendC::TPipe pipe; AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 4 > que; int num = 4 ; int len = 1024 ; pipe. InitBuffer (que, num, len); AscendC::LocalTensor<half> tensor1 = que. AllocTensor <half>(); que. EnQue (tensor1); // 将tensor加入VECOUT的Queue中
```
## 功能说明

将Tensor从队列中取出，用于后续处理。

## 函数原型

收起自动换行深色代码主题复制

```
template < typename T> __aicore__ inline LocalTensor<T> DeQue ()
```

 **图1**将LocalTensor通过EnQue放入A1/B1的Queue中后再通过DeQue搬出
![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165328.04776015440374126368514427079495:50001231000000:2800:FACDAE9CFA14DC2EA90B6085B905E9CC969E5BF28E5D48BC8FD1E4D83C571221.png)  

## 参数说明

无

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 注意事项

无

## 返回值

从队列中取出的[LocalTensor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-localtensor)。

## 调用示例

收起自动换行深色代码主题复制

```
// 接口: DeQue Tensor AscendC::TPipe pipe; AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 4 > que; int num = 4 ; int len = 1024 ; pipe. InitBuffer (que, num, len); AscendC::LocalTensor<half> tensor1 = que. AllocTensor <half>(); que. EnQue (tensor1); AscendC::LocalTensor<half> tensor2 = que. DeQue <half>(); // 将tensor从VECOUT的Queue中搬出
```
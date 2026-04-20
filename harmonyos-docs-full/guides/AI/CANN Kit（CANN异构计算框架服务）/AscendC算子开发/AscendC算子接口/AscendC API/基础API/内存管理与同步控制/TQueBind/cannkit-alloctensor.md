# AllocTensor

  

#### 功能说明

从队列中分配Tensor，Tensor所占大小为InitBuffer时设置的每块内存长度。

 ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/JW7dmWC5Q_qLQLJK5AW29A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T191517Z&HW-CC-Expire=86400&HW-CC-Sign=4F0FFE2E8F67E3E74A0DB998E94338D031051331D3D3B855390C40D59501F10E)  

分配的Tensor内容并非全0，可能会是随机值。

   

#### 函数原型

```
template <typename T> 
__aicore__ inline LocalTensor<T> AllocTensor()

```

  

#### 参数说明

无

  

#### 支持的型号

Kirin9020系列处理器

 

KirinX90系列处理器

  

#### 注意事项

无

  

#### 返回值

LocalTensor对象。

  

#### 调用示例

```
// 使用AllocTensor分配Tensor
AscendC::TPipe pipe;
AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 2> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len); // InitBuffer分配内存块数为4，每块大小为1024Bytes
AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>(); // AllocTensor分配Tensor长度为1024Bytes

```
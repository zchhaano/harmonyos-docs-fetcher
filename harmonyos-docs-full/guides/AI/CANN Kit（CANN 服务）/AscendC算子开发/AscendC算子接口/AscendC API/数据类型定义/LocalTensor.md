## 功能说明

用于存放AI Core中Local Memory（内部存储）的数据，支持QuePosition为VECIN、VECOUT、VECCALC、A1、A2、B1、B2、CO1、CO2。

## 定义原型

收起自动换行深色代码主题复制

```
template < typename T> class LocalTensor : public BaseLocalTensor<T> { public : using PrimType = PrimT<T>; __aicore__ inline LocalTensor <T>() {}; # if defined(ASCENDC_CPU_DEBUG) && ASCENDC_CPU_DEBUG == 1 ~ LocalTensor (); explicit LocalTensor <T>(TBuffAddr& address); LocalTensor <T>( const LocalTensor<T>& other); LocalTensor<T> operator = ( const LocalTensor<T>& other); PrimType* GetPhyAddr ( const uint32_t offset) const ; PrimType* GetPhyAddr () const ; __inout_pipe__(S) PrimType GetValue ( const uint32_t offset) const ; __inout_pipe__(S) PrimType& operator () ( const uint32_t offset) const ; template < typename CAST_T> __aicore__ inline LocalTensor<CAST_T> ReinterpretCast () const ; template < typename T1> __inout_pipe__(S) void SetValue ( const uint32_t index, const T1 value) const ; LocalTensor operator []( const uint32_t offset) const ; template < typename T1> void SetAddrWithOffset (LocalTensor<T1> &src, uint32_t offset) ; inline void Print () ; inline void Print ( uint32_t len) ; int32_t ToFile ( const std::string& fileName) const ; # else __aicore__ inline uint64_t GetPhyAddr () const ; __aicore__ inline uint64_t GetPhyAddr ( const uint32_t offset) const ; __aicore__ inline __inout_pipe__(S) PrimType GetValue ( const uint32_t index) const ; __aicore__ inline __inout_pipe__(S) __ubuf__ PrimType& operator () ( const uint32_t offset) const ; template < typename CAST_T> __aicore__ inline LocalTensor<CAST_T> ReinterpretCast () const ; template < typename T1> __aicore__ inline __inout_pipe__(S) void SetValue ( const uint32_t index, const T1 value) const ; __aicore__ inline LocalTensor operator []( const uint32_t offset) const ; template < typename T1> [[ deprecated ( "NOTICE: SetAddrWithOffset has been deprecated and will be removed in the next version. " "Please do not use it!" )]] __aicore__ inline void SetAddrWithOffset (LocalTensor<T1> &src, uint32_t offset) ; # endif __aicore__ inline int32_t GetPosition () const ; __aicore__ inline void SetSize ( const uint32_t size) ; __aicore__ inline uint32_t GetSize () const ; [[ deprecated ( "NOTICE: GetLength has been deprecated and will be removed in the next version. Please do not use " "it!" )]] __aicore__ inline uint32_t GetLength () const ; [[ deprecated ( "NOTICE: SetBufferLen has been deprecated and will be removed in the next version. Please do not use " "it!" )]] __aicore__ inline void SetBufferLen ( uint32_t dataLen) ; __aicore__ inline void SetUserTag ( const TTagType tag) ; __aicore__ inline TTagType GetUserTag () const ; // ... __aicore__ inline void SetShapeInfo ( const ShapeInfo& shapeInfo) ; __aicore__ inline ShapeInfo GetShapeInfo () const ; // ... };
```

## 函数说明

类型T支持基础数据类型，但需要遵循使用此LocalTensor的指令的数据类型支持情况。

 **表1**函数说明展开

| 函数名称 | 入参说明 | 含义 |
| --- | --- | --- |
| GetValue | offset：偏移量，单位为'element' | 获取LocalTensor中的某个值，返回PrimType类型的数值。 该接口仅在LocalTensor的TPosition为VECIN/VECCALC/VECOUT时支持。 |
| SetValue | offset：偏移值，单位为'element' value：设置值，单位为任意类型 | 设置LocalTensor中的某个值。 该接口仅在LocalTensor的TPosition为VECIN/VECCALC/VECOUT时支持。 |
| operator[] | offset：偏移量 | 获取距原LocalTensor起始地址偏移量为offset的新LocalTensor，注意offset不能超过原有LocalTensor的size大小。 |
| operator() | offset:  下标索引 | 获取本LocalTensor的第offset个变量的引用。用于左值，相当于SetValue接口，用于右值，相当于GetValue接口。 |
| GetSize | 无 | 获取当前LocalTensor size大小。单位为元素。 |
| SetSize | size：元素个数，单位为'element' | 设置当前LocalTensor size大小。单位为元素。当开发者重用local tensor变量且使用长度发生变化的时候，需要使用此接口重新设置Size。 |
| SetUserTag | tag：设置的Tag信息，类型TTagType对应为int32_t | 为Tensor添加开发者自定义信息，开发者可以根据需要设置对应的Tag。后续可通过GetUserTag获取指定Tensor的Tag信息，并根据Tag信息对Tensor进行相应操作。 |
| GetUserTag | - | 获取指定Tensor块的Tag信息，开发者可以根据Tag信息对Tensor进行不同操作。 |
| ReinterpretCast | - | 将当前Tensor重解释为开发者指定的新类型，转换后的Tensor与原Tensor地址及内容完全相同，Tensor的大小(字节数)保持不变。 |
| GetPhyAddr | - | 返回LocalTensor的地址，如果传入offset，则表示偏移offset个元素。 |
| GetPosition | - | 获取QuePosition抽象的逻辑位置，支持QuePosition为VECIN、VECOUT、VECCALC、A1、A2、B1、B2、CO1、CO2。 |
| GetLength | 无 | 获取LocalTensor数据长度，单位为Byte。 |
| SetShapeInfo | shapeInfo：ShapeInfo结构体 | 设置LocalTensor的shapeInfo。 |
| GetShapeInfo | 无 | 获取LocalTensor的shapeInfo。 说明 Shape信息没有默认值，只有通过SetShapeInfo设置过Shape信息后，才可以调用该接口获取正确的ShapeInfo。 |
| SetAddrWithOffset | src：基础地址的Tensor，将该Tensor的地址作为基础地址，设置偏移后的Tensor地址 offset：偏移的长度 | 设置带有偏移的Tensor地址。用于快速获取定义一个Tensor，同时指定新Tensor相对于旧Tensor首地址的偏移。偏移的长度为旧Tensor的元素个数。 |
| SetBufferLen | dataLen：buffer长度 | 设置buffer长度。单位为字节。 |
| ToFile | fileName：文件名称 | 只限于CPU调试，将LocalTensor数据Dump到文件中，用于精度调试，文件保存在执行目录。 |
| Print | dataLen：打印元素个数 | 只限于CPU调试，在调试窗口中打印LocalTensor数据用于精度调试，每一行打印一个datablock(32Bytes)的数据。 |

## 注意事项

不要大量使用SetValue对LocalTensor进行赋值，会使性能下降。

## 调用示例

收起自动换行深色代码主题复制

```
```
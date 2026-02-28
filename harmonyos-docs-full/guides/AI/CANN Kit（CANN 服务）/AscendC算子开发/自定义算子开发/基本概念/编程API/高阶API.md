# 高阶API

高阶API一般是基于单核对常见算法的抽象和封装，用于提高编程开发效率，通常会调用多种基础API实现。高阶API当前仅支持Matmul。

如下图所示，实现一个矩阵乘操作，使用基础API需要的步骤较多，需要关注格式转换、数据切分等逻辑；使用高阶API则无需关注这些逻辑，直接传入输入矩阵，调用接口获取输出即可。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165306.80317017100988462320213723263265:50001231000000:2800:6586111588431E03C758FAB75C7A837A2548F6E3CEDB887F9D9A154E5691C666.png)

注意，在程序中调用高阶API的Tiling接口或者使用高阶API的Tiling结构体参数时，需要引入依赖的头文件，示例如下。

 收起自动换行深色代码主题复制

```
# include "register/tilingdata_base.h" # include "lib/tiling_api.h" namespace optiling { BEGIN_TILING_DATA_DEF (MatmulCustomTilingData) TILING_DATA_FIELD_DEF_STRUCT (TCubeTiling, cubeTilingData); END_TILING_DATA_DEF; REGISTER_TILING_DATA_CLASS (MatmulCustom, MatmulCustomTilingData); } // namespace optiling
```
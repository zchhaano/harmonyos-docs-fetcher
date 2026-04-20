# 算子包安装

 

执行算子工程的编译时，编译结果会自动部署到算子包安装目录下。

 

1. 自定义算子包安装。

 

算子编译完成后，会自动将算子交付件安装到DDK指定目录，开发者无需关注。

 ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/REmPDJf1Tj-onFAEOZriXw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T191353Z&HW-CC-Expire=86400&HW-CC-Sign=5978F56D8557D59BD89E153CCA7B4D049799D0F6E8E03C8E7AA48CE641370569)  

自定义算子包默认安装路径为${DDK_INSTALL_PATH}/tools/platform。
2. 安装后的目录结构如下所示：

 

```
platform                            // 平台插件目录
├── kirin9020                       // Kirin AI处理器类型
│   ├── config
│   │   └── npu_custom_opinfo.json  // 算子信息库
│   ├── lib64
│   │   └── libcustom_op.so         // host侧二进制文件
│   ├── ops
│   │   └── impl
│   │       ├── custom              // kernel交付件
│   │       │   ├── add_custom.cpp
│   │       │   ├── add_custom.py
│   │       │   └── op_proto.h
│   │       └── impl
│   └── simulator
└── README.md

```
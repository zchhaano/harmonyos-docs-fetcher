# 环境准备

 

进行环境准备前，你需要了解如下基本概念，以便更好的理解后续操作。

 

- 开发环境：指编译开发代码的环境。
- 运行环境：指运行算子、推理程序等的Linux环境。运行环境必须连接上带有Kirin AI处理器的设备，如手机、平板等。
- 开发环境与运行环境合设场景：开发环境和运行环境在同一台机器上，开发者使用连接上Kirin AI处理器的机器作为运行环境，同时在该环境上进行代码开发与编译。
- 开发环境与运行环境分设场景：开发环境和运行环境不在同一台机器上，开发者使用连接上Kirin AI处理器的机器作为运行环境；使用其他独立机器进行代码开发与编译，作为开发环境。

 ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/7DPF_j7CRhWd4vvQcLnBUg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T191334Z&HW-CC-Expire=86400&HW-CC-Sign=DDD714BA2F1DFC1058F08E847146D4919128007678D5ADEF30492681228C5640)  

开发运行环境需要满足以下要求：

 

  - ubuntu版本大于等于22.04，ubuntu架构为x86_64， python版本在3.7与3.10之间（包含），gcc/g++版本大于等于7.0。
  - 设备连接与调试参考[hdc](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc)。

 

进行自定义算子开发前，需要完成驱动及DDK的安装。

 

1. [下载tools_ascendc](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-preparations#tools下载)，并在Linux环境上解压。

 ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Tqf2IDw3REKfsSv_Pm5bHg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T191334Z&HW-CC-Expire=86400&HW-CC-Sign=945910C9A9B23AF7A99834F7708221F6A2C091EB3498D3BD3BE91263FB6F9E91)  

在Windows平台解压会导致软链接失效。
2. 下载需要的[平台插件包](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-preparations#tools下载)，在linux开发环境上解压，并将需要的平台插件拷贝到${install_path}/ddk/tools/platform下。其中${install_path}为tools包的解压目录。拷贝后的目录结构如下。

 

```
tools
├── platform
│   ├── kirin9020
│   ├── kirinx90

```
3. 进入目录ddk/tools/tools_ascendc，修改安装脚本权限，执行安装脚本进行安装，命令如下。

 

```
cd ddk/tools/tools_ascendc
chmod +x install.sh
source ./install.sh

```
4. 在使用tools工具前，需要先设置环境变量，执行**source ${install_path}/ddk/tools/tools_ascendc/set_ascendc_env.sh**。

 

例如安装目录为/usr/local/：

 

```
source  /usr/local/ddk/tools/tools_ascendc/set_ascendc_env.sh

```
5. python软件依赖，执行步骤3的安装脚本install.sh时会自动安装。若执行ascendebug时提示无对应模块，可执行下表中的命令手动安装。

 

**表1** 第三方软件

 

| 第三方软件 | 用途 | 如何安装 |
| --- | --- | --- |
| toml | 加载和转储TOML文件的功能。 | pip3 install toml |
| jinja2 | CPU调测模板使用。 | pip3 install jinja2 |
| numpy | 精度比对时使用。 | pip3 install numpy |
| torch | 输入、输出数据格式转换使用。 | pip3 install torch |
| sympy | 用于进行符号计算 | pip3 install sympy |
| paramiko | 与远程linux环境连接 | pip3 install paramiko |
| protobuf | 模型解析 | pip3 install protobuf |
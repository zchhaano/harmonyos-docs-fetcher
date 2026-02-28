# ohpm root

在标准输出中打印有效的 oh_modules 目录路径信息。

从ohpm 6.0.2.636版本开始，命令后支持配置log_level和debug参数，用于查看日志级别和指定执行当前命令的日志级别。

## 命令格式

收起自动换行深色代码主题复制

```
ohpm root
```

## 功能描述

可以在模块的任意子目录下执行，用于打印命令工作路径下所在包的有效 oh_modules 目录路径信息。

## Options

### prefix

- 默认值：""
- 类型： string

可以在 root 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件，将会打印该根目录中有效的 oh_modules 目录路径信息。

### log_level

- 默认值：无
- 类型： String

可以在 root 命令后配置--log_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log_level的级别。

### debug

- 默认值：false
- 类型： Boolean

可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log_level的级别。

## 示例

项目结构为：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102137.03443952208295632285275622424629:50001231000000:2800:7FB12BDD599B9A7352C7E9073DFDDB0FF414C32D59743200ABA7C5CE5B19139E.png)

在entry模块的src目录下执行：

 收起自动换行深色代码主题复制

```
ohpm root
```

结果示例：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102137.14331654810682046374446451574585:50001231000000:2800:4C5644B72B5ECEBB383B5D996CAF3EB16B7E48F083BE406FAE50E0F25787DB0E.png)
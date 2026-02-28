# 代码检查工具（codelinter）

codelinter同时支持使用命令行执行代码检查与修复，可将codelinter工具集成到门禁或持续集成环境中。

codelinter命令行格式为：

 收起自动换行深色代码主题复制

```
codelinter [options] [dir]
```

options：可选配置，请参考[表1](/consumer/cn/doc/harmonyos-guides/ide-command-line-codelinter#table25697717185)。

dir：待检查的工程根目录；为可选参数，如不指定，默认为当前上下文目录。

 **表1**codelinter命令行配置展开

| 指令 | 说明 |
| --- | --- |
| --config/-c <filepath> | 指定执行codelinter检查的规则配置文件， <filepath> 指定执行检查的规则配置文件位置。 |
| --fix | 设置codelinter检查同时执行QuickFix。 |
| --format/-f | 设置检查结果的输出格式。目前支持default/json/xml/html四种格式；不指定时，默认是default格式（文本格式）。 |
| --output/-o <filepath> | 指定检查结果保存位置，且命令行窗口不展示检查结果。 <filepath> 指定存放代码检查结果的文件路径，支持使用相对/绝对路径。不使用--output指令时，检查结果默认会显示在命令行窗口中。 |
| --version/-v | 查看codelinter版本。 |
| --product/-p <productName> | 指定当前生效的product。 <productName> 为生效的product名称。 |
| --incremental/-i | 对Git工程中的增量文件（包含新增/修改/重命名的文件）执行Code Linter检查。 |
| --help/-h | 查询codelinter命令行帮助。 |
| --exit-on/-e <levels> | 指定哪些告警级别需要返回非零退出码，告警级别包括：error、warn和suggestion。若需要指定多个告警级别，级别间需要用英文逗号分开。 退出码的计算方式为：用一个3位的二进制数从高到低分别表示error、warn、suggestion告警级别。若在命令行中配置告警级别，并且代码检查结果中也包含该告警级别，则该二进制值为1，否则均为0。将二进制数转换为十进制数，则是退出码。 例如： 命令配置为--exit-on error，代码检查结果包括error、warn、suggestion三类告警，则退出码的二进制数为100，十进制数为4。 命令配置为--exit-on error，代码检查结果包括warn、suggestion两类告警，则退出码的二进制数为000，十进制数为0。 |

1. 进行codelinter代码检查与修复。若您的工程存在多个product，请使用--product/-p指令，指定生效的product和执行检查的工程根目录。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102132.57208399936650796537772825588867:50001231000000:2800:8F052EBB88E2C8F3CD9160E9E53821FAFB5FD87F4D7E69AFB8C2E569D6A9B2A3.png)

  - 在工程根目录下使用命令行工具：

    1. 直接执行**codelinter**指令。此时根据默认codelinter检查规则，对该工程中的TS/ArkTS文件进行代码检查。默认的规则清单可在检查完成后，根据命令行提示，查看相应位置的code-linter.json5文件。收起自动换行深色代码主题复制

```
codelinter // 进行codelinter检查
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102132.73796460376476980424793029572820:50001231000000:2800:A6D957F6C53E48D962C55DC216FCD7FFDF1FD198370B8AB884E72A112AB97244.png)
    2. 执行如下命令，指定codelinter检查所使用的code-linter.json5规则配置文件，并进行代码检查。收起自动换行深色代码主题复制

```
codelinter -c filepath // 指定执行检查的规则配置文件位置
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102132.86711478658966158695305915513040:50001231000000:2800:F914F78A8D01DA7FD4CA82A30C87F6D9ED71893A954EB0BDA7FB8B9B19CC6807.png)
    3. 执行如下命令，对指定工程将根据指定的规则配置文件执行codelinter检查，并对部分支持修复的告警信息进行自动修复。收起自动换行深色代码主题复制

```
codelinter -c filepath --fix // 对工程中的告警进行修复
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102132.00620187540885560062745213772540:50001231000000:2800:E81A0D33214D64D3F9E8456F07DBB3EA3A644326B6A77D3618FEFAB2DA8FE864.png)
  - 在非工程根目录下使用命令行工具：

    1. 执行如下命令，指定需要进行检查的工程目录或文件路径。此时根据默认codelinter检查规则，对该工程中的TS/ArkTS文件进行代码检查。默认的规则清单可在检查完成后，根据命令行提示，查看相应位置的code-linter.json5文件。收起自动换行深色代码主题复制

```
codelinter dir [filepath] [dir1] // 指定执行检查的工程目录或文件路径。支持同时配置多个文件/文件夹路径。 filepath为待检查的文件所在位置，dir、dir1指定待检查的工程目录
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102132.15409639542920704399482958726944:50001231000000:2800:3B3D3FC812A9FE953B5516BF5978E8DAD32B76758F73C5A284002AF7CA16EF83.png)
    2. 在指定的工程目录下，根据指定的codelinter规则配置文件进行代码检查。收起自动换行深色代码主题复制

```
codelinter -c filepath dir // filepath为指定的规则配置文件所在位置， dir 指定执行检查的工程根目录
```
    3. 执行如下命令，对指定工程重新执行codelinter检查，并对部分支持修复的告警进行自动修复。收起自动换行深色代码主题复制

```
codelinter -c filepath dir --fix // 对指定工程中的告警进行修复。支持配置同时多个工程路径
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102132.00118915647435497702286353275526:50001231000000:2800:DB022977A7CFD9AC3C7A590C9B4FF6F794324A320EE52AFA4B0EEB7AAE5E7A36.png)
2. 如需指定检查结果输出格式（以json格式为例），执行如下指令。检查结果将在命令行窗口展示。

收起自动换行深色代码主题复制

```
codelinter [ dir ] -f json  //[ dir ]为待检查的工程根目录
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102132.90885795130439538556869072582948:50001231000000:2800:0D19928B1CB118AC3449231A45D12488D1E0C259356511A4942D039E75AF97F6.png)
3. 执行如下指令，指定代码检查输出格式及结果保存位置。此时将不在命令行窗口中打印检查结果，可在指定的文件存放路径下查看。

收起自动换行深色代码主题复制

```
codelinter [ dir ] -f json -o filepath 2     // [ dir ]为待检查的工程根目录， filepath 2为指定存放代码检查结果的文件路径
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102132.52877434194955560799822050862323:50001231000000:2800:A67BEC667999D7056B3FC92856D2F29F2F198946B05E5212988B85AAA4F7DE29.png)
# ohpm-repo encrypt_password

对键入的密码类型字符串进行加密。

## 命令格式

收起自动换行深色代码主题复制

```
ohpm-repo encrypt_password [options]
```

## 功能描述

使用指定的加密组件加密从标准输入读取的数据，并在标准输出中输出密文。

## 选项

### crypto_path

- 类型：String
- 必填参数

必须在encrypt_password命令后面配置--crypto_path <string>参数，指定加密组件的路径。如果是完整组件，将用该组件对键入的密码内容进行加密。如果是一个空目录，则命令将生成新的加密组件并对键入的密码内容进行加密。

## 示例

执行以下命令：

 收起自动换行深色代码主题复制

```
ohpm-repo encrypt_password --crypto_path D:\encryptPath
```

结果示例：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101918.10454636377194724524797897937939:50001231000000:2800:E04CDC5FF4E092AEBE2B2A34634CD57521BF4B7C3CC6F7200E33C0C03AAED1E7.png)
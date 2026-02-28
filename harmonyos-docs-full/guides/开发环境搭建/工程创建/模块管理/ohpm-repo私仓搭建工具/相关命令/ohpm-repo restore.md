# ohpm-repo restore

将ohpm-repo pack打包产物替换<deploy_root>目录下相应文件，重启服务。

## 前提条件

- 已成功执行[start 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-start)或者[restart 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restart)，ohpm-repo服务启动成功。
- 已获得由[pack 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-pack)打包的.zip 文件。

## 命令格式

收起自动换行深色代码主题复制

```
ohpm - repo restore < file_path >
```

## 功能描述

该命令会停止当前ohpm-repo服务，并用打包文件<file_path>中的内容替换ohpm-repo部署根目录<deploy_root>的相应文件，然后重启ohpm-repo服务。该命令执行前必须已执行过ohpm-repo实例启动命令ohpm-repo start。

 说明

- <file_path>：由ohpm-repo pack命令得到的打包产物。

支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。

- <deploy_root>：ohpm-repo部署根目录 执行install命令后，会创建一个名为OHPM_REPO_DEPLOY_ROOT的环境变量，记录的是[ohpm-repo私仓部署目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-configuration#zh-cn_topic_0000001745376470_关于-deploy_root)。

## 参数

### <file_path>

- 类型：String
- 必填参数

指定待解压的打包文件路径。

## 示例

执行以下命令：

 收起自动换行深色代码主题复制

```
ohpm-repo restore "D:\pack_1702625827995.zip"
```

结果示例：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101921.55213698402338360526439160963348:50001231000000:2800:3F8830E67AE1D12C43432AAF3113605C4F4DCF0E4E1A5D72F489CC8CA7B9F12F.png)
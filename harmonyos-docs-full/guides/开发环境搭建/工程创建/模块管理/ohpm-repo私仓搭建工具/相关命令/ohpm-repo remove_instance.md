# ohpm-repo remove_instance

删除本机实例信息。

## 前提条件

- 已成功执行[start 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-start)或者[restart 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restart)，ohpm-repo服务启动成功。
- 数据存储db模块的类型必须为mysql，文件存储store模块的类型必须为sftp或custom。

## 命令格式

收起自动换行深色代码主题复制

```
ohpm-repo remove_instance
```

## 功能描述

该命令会停止当前运行的ohpm-repo服务，同时删除本机在mysql和sftp中的实例信息。命令要求数据存储db模块必须使用mysql，文件存储store模块必须使用sftp或custom。

## 示例

执行以下命令：

 收起自动换行深色代码主题复制

```
ohpm-repo remove_instance
```

结果示例：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101921.50191107263768518562828609336099:50001231000000:2800:A05B39BABE9D0F30E50598B2BCC67E80766CC042CBCAA329BF24E2E7C58BB3A1.png)
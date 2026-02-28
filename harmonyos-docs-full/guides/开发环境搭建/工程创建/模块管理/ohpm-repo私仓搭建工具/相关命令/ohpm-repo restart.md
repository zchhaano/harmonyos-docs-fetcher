# ohpm-repo restart

重新启动ohpm-repo服务。

## 前提条件

已成功执行[install命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-install)，并按要求刷新环境变量。

## 命令格式

收起自动换行深色代码主题复制

```
ohpm-repo restart
```

## 功能描述

停止当前ohpm-repo服务，重新启动一个新的ohpm-repo服务。

 说明

启动时将ohpm-repo服务的pid存放到<deploy_root>/runtime/.pid文件，其中<deploy_root>为[ohpm-repo私仓部署目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-configuration#zh-cn_topic_0000001745376470_关于-deploy_root)。

## 示例

执行以下命令：

 收起自动换行深色代码主题复制

```
ohpm-repo restart
```

结果示例：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101912.41454555127340145431439801689292:50001231000000:2800:4B9450E03A3649880BE223153C875229E2FC48D6FFA263D13481F26255491329.png)
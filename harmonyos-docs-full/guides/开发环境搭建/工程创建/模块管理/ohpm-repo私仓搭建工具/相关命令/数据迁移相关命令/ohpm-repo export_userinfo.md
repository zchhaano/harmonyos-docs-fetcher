# ohpm-repo export_userinfo

导出用户必要的DB数据。

## 命令格式

收起自动换行深色代码主题复制

```
ohpm-repo export_userinfo
```

## 功能描述

在当前的工作目录导出记录了DB数据的export_userInfo_xxx.zip文件，其中包含加密组件和下面的10张数据表。

- user
- group_member
- public_key
- access_token
- uplink
- uplink_proxy
- repo
- repo_permission
- validation_config
- system_security

## 示例

执行以下命令：

 收起自动换行深色代码主题复制

```
ohpm-repo export_userinfo
```

结果示例：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101929.47642692305992604614540506379270:50001231000000:2800:1B4D45C0DA439C0312C4B7C65534A7AEC4E34C431E9E066690DD5A48DB8AFA21.png)

 收起自动换行深色代码主题复制

```
```

 收起自动换行深色代码主题复制

```
export_userInfo_1754738056722.zip文件结构 |   access_token.json |   group_member.json |   public_key.json |   repo.json |   repo_permission.json |   system_security.json |   uplink.json |   uplink_proxy.json |   user.json |   validation_config.json \ ---meta |   version.txt + ---ac + ---ce \ ---fd
```
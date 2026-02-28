# param工具

param是为开发人员提供用于操作系统参数的工具，该工具只支持标准系统。

## 环境要求

- 获取hdc工具，执行hdc shell。
- 正常连接设备。

## param工具命令列表

 展开

| 选项 | 说明 |
| --- | --- |
| -h | 获取param支持的命令。 |
| ls [-r] [name] | 显示匹配name的系统参数信息。带"-r"则根据参数权限获取信息，不带"-r"则直接获取参数信息。 |
| get [name] | 获取指定name系统参数的值；若不指定任何name，则返回所有系统参数。 |
| set name value | 设置指定name系统参数的值为value。 |
| wait name [value] [timeout] | 同步等待指定name系统参数与指定值value匹配。value支持模糊匹配，如"*"表示任何值，"val*"表示只匹配前三个val字符。timeout为等待时间（单位：s），不设置则默认为30s。 |
| save | 保存persist参数到工作空间。 |

## 获取param支持的命令

- 获取param支持的命令，命令格式如下：

 收起自动换行深色代码主题复制

```
param -h
```

## 获取系统参数信息

- 显示匹配name的系统参数信息，命令格式如下：

 收起自动换行深色代码主题复制

```
param ls [-r] [name]
```

**示例**

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170034.55591173848702240467949432909039:50001231000000:2800:56CD2509E87DE88D53FC16DD749282E840429F86C5148B767844808F9A701ADA.png)

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170034.22826034924196958989047269425238:50001231000000:2800:B91ABC1F3EEBAC8F9E8C7B6706FEF11EF31972F818EDE66CECB86BB2945FD591.png)

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170034.42081443928094895192656748829636:50001231000000:2800:D353317C5674FD6FE14F64582C3B6B5CAE97D171F91BD6125AD4F936E5824A64.png)

## 获取系统参数的值

- 获取指定name系统参数的值，命令格式如下：

 收起自动换行深色代码主题复制

```
param get [name]
```

**示例**

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170034.87878829422691500464923389362579:50001231000000:2800:9D038FA102923A391E4A53280B0D144E3306D2AAB9A1B80657B3D924163D8446.png)

## 设置系统参数的值

- 设置指定name系统参数的值为value，命令格式如下：

 收起自动换行深色代码主题复制

```
param set name value
```

**示例**

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170034.74170326842615333778458731317914:50001231000000:2800:286C9415A7AE8293EAFCADF304C329CA77A80E982C755FA6246ACFEA387EDA90.png)

## 等待系统参数值匹配

- 同步等待指定name系统参数与指定值value匹配，命令格式如下：

 收起自动换行深色代码主题复制

```
param wait name [value] [ timeout ]
```

**示例**

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170034.17128351477306306453394909022412:50001231000000:2800:2F4ECD240ED6BDA2E1CB326A7F0BEF9F939D9F79B19057487524DE9326517423.png)

## 保存persist(可持久化)参数

- 保存persist(可持久化)参数到工作空间，命令格式如下：

 收起自动换行深色代码主题复制

```
param save
```

**示例**

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170034.52134075008154070209474742147792:50001231000000:2800:B952C5C4E49480A87E2FB4B7DC1D3F7D72524AB8CE8777BA0608937887E490C1.png)
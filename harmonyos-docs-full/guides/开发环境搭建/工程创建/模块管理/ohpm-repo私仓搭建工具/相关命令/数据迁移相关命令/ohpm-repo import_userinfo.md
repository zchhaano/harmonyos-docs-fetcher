# ohpm-repo import_userinfo

导入用户DB数据。

## 前提条件

已成功执行[export_userinfo 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-userinfo)。

## 命令格式

收起自动换行深色代码主题复制

```
ohpm - repo import_userinfo < zip_file > [ options ]
```

## 功能描述

根据提供的zip文件导入用户DB数据到ohpm-repo。

## 参数

### <zip_file>

- 类型： String
- 必填参数

必须在import_userinfo命令后面配置<zip_file>参数，指定执行[export_userinfo 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-userinfo)导出的zip文件。

## 选项

### clean-db

- 默认值：false
- 类型：Boolean

可以在import_userinfo命令后面配置--clean-db参数，指定在导入数据前先清空DB数据。

## 示例

执行以下命令：

 收起自动换行深色代码主题复制

```
ohpm - repo import_userinfo < zip_file > -- clean - db
```

结果示例：

 收起自动换行深色代码主题复制

```
```
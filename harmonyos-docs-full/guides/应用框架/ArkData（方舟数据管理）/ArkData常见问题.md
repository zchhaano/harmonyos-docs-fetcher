## 如何查看关系型数据库详细的SQL执行异常信息

可以调用[on('sqliteErrorOccurred')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-rdbstore#onsqliteerroroccurred20)获取SQL执行时出现的异常信息。

## 如何查看关系型数据库生成的SQL语句

可以调用[relationalStore.getInsertSqlInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-f#relationalstoregetinsertsqlinfo20)获取用于插入数据的SQL语句。

可以调用[relationalStore.getUpdateSqlInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-f#relationalstoregetupdatesqlinfo20)获取用于更新数据的SQL语句。

可以调用[relationalStore.getDeleteSqlInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-f#relationalstoregetdeletesqlinfo20)获取用于删除数据的SQL语句。

可以调用[relationalStore.getQuerySqlInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-f#relationalstoregetquerysqlinfo20)获取用于查询数据的SQL语句。
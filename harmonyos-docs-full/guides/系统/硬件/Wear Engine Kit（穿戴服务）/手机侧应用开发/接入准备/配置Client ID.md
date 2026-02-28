# 配置Client ID

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的Client ID。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170116.19491610510960396731934928061513:50001231000000:2800:5C13D33D310979CAC6C36A03C5079654C36C2058876692D5C059FF0B2D7AECB9.png)
2. 在工程中entry模块的module.json5文件中，新增metadata，配置name为client_id，value为上一步获取的Client ID的值，如下所示：收起自动换行深色代码主题复制

```
{ "module" : { "name" : "xxxx" , "type" : "entry" , "description" : "xxxx" , "mainElement" : "xxxx" , "deviceTypes" : [], "pages" : "xxxx" , "abilities" : [], "metadata" : [ // 配置如下信息 { "name" : "client_id" , "value" : "xxxxxx" } ] } }
```
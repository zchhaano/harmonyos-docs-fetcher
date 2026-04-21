# 使用云存储上传文件失败，提示“404:Product does not exist”

 

**问题现象**

 

使用云存储上传文件失败，HiLog提示“404:Product does not exist”。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/hsgm6FDwSiSBfqAOje-Hrw/zh-cn_image_0000002573974801.png?HW-CC-KV=V1&HW-CC-Date=20260420T191224Z&HW-CC-Expire=86400&HW-CC-Sign=1D8A7A06D3690312A4EA46D9912D5D24F31D3F06210A420D123DB2F51E3B1DC5)

 

**解决措施**

 

此错误由云存储服务端返回，原因是云存储服务未开通。请[开通云存储服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-enable-storage)。
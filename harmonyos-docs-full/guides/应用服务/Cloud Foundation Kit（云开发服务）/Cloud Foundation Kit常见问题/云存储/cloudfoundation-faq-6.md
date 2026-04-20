# 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”

 

**问题现象**

 

通过“使用指定的实例”方式初始化云存储实例时，调用业务接口（如调用uploadFile接口上传文件）失败，出现如下错误提示：

 

- app日志提示“"state":65”

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/LmPeK3fwSFCo70GHodwYow/zh-cn_image_0000002573854825.png?HW-CC-KV=V1&HW-CC-Date=20260420T191226Z&HW-CC-Expire=86400&HW-CC-Sign=F0AE8458C606D108C6CDA640421C23A21E19E3DD30D6D9735FA20B364392E1E7)
- upload进程的日志提示“404 Not Found”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/hH41oZ_pRd2jsJKctPSyDg/zh-cn_image_0000002573974803.png?HW-CC-KV=V1&HW-CC-Date=20260420T191226Z&HW-CC-Expire=86400&HW-CC-Sign=DDCF0D802A7B5B2F4447F60597326E5A3C716705AA7A96F1380E10BAD5F2A053)

 

**解决措施**

 

出现此问题，原因是当前云侧不存在该存储实例，或传入的存储实例名称错误。

 

请检查您传入的存储实例名称，确保云侧存在该存储实例，且传入的存储实例名称与云侧存储实例名称完全一致。
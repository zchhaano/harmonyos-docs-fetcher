# ArkTS API错误码

说明 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

## 1002600001 系统内部错误

 支持设备PhonePC/2in1TabletWearable

**错误信息**

System internal error.

**错误描述**

当发生系统内部错误时，将返回该错误码。

**可能原因**

其他未知错误。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600002 应用连接地图服务失败

 支持设备PhonePC/2in1TabletWearable

**错误信息**

Failed to connect to the Map Kit server.

**错误描述**

应用连接地图服务失败。

**可能原因**

1. 设备网络存在问题。

2. 使用自动签名时，未连接上地图服务。

**处理步骤**

1. 检查设备网络状态。

2. 清除旧证书配置后，重新自动签名，并配置client_id和证书指纹；从HarmonyOS 5.0.2(14)版本开始，可参考[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc)进行配置。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170306.77582830301318737022042609016188:50001231000000:2800:84EDBF34D0EA5F401DA7F0CF8108A82CF42B8D24922C9F609AF8FD304ADB22A5.png)

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170306.75560359875219173734214518865619:50001231000000:2800:FCCACB1629C79B9EE94ADA62CF49A63DD060190258A913FEFCA1B57B37CA2E5C.png)

3. 如未解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600003 应用身份校验失败

 支持设备PhonePC/2in1TabletWearable

**错误信息**

App authentication failed.

**错误描述**

应用身份校验失败。

**可能原因**

1. 项目module.json5文件中配置的client_id与AGC上不一致。
2. AGC上公钥指纹为空或错误。
3. 设备网络状态差，身份认证超时。
4. 公钥指纹配置后还未生效。
5. 配置profile文件之前，未开通地图服务开关。
6. 配置自动签名时，重复配置导致AGC上调试证书和本地使用证书不匹配。

**处理步骤**

1. 检查module.json5文件中配置的client_id与AGC上是否一致。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170306.84182181323990159305048394154003:50001231000000:2800:B9D1536B9C79505F71E4E3631E2A3D04C78F52371AE0C37F58F1EE2AC8D20EB6.png)

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170306.06568265204551326014802710592876:50001231000000:2800:CF7F3DA7289F1A5DEF470417424E234EE0539DBE05EE6C373A0F8B652A6F4911.png)

2. 重新生成公钥指纹（[自动生成签名证书指纹](https://developer.huawei.com/consumer/cn/doc/app/agc-help-signature-info-0000001628566748#section958212134217)/[手动生成签名证书指纹](https://developer.huawei.com/consumer/cn/doc/app/agc-help-signature-info-0000001628566748#section2049119231438)），然后在AGC上[配置公钥指纹](https://developer.huawei.com/consumer/cn/doc/app/agc-help-cert-fingerprint-0000002278002933)。

3. 检查设备网络状态后重新尝试。

4. 将设备的系统时间往后调整1天。

5. 请根据[开通地图服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc#section16133115441516)， 先打开地图服务开关，然后重新[申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-add-debugprofile-0000001914423102)，并[手动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)。

6. 自动签名证书不匹配有两种解决方案：

方案一：将本地已生成的csr签名，通过AGC重新生成新的调试证书，然后通过新的调试证书选择生成新的指纹证书。

自动签名默认已生成的csr签名在如下图路径下，马赛克部分为用户名。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170306.69304504305895463318030560692380:50001231000000:2800:5E7880B490E6C42EBE7DCBCE7923E864D68E713F6835E3657D3964D2D0E282A5.png)

在AGC上新增证书，将上述所选csr文件选中并生成新的调试证书。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170306.12331169973410327401883417349477:50001231000000:2800:F0DC7110DB2DC8AD1EB6E17BE43CF549E17BB66B076D6111B0C9D83A2523DD0F.png)

然后添加公钥指纹，选中刚才自己生成调试证书即可。（需注意，配置完成后由于鉴权缓存，可能还是无法马上显示地图，须清除缓存或者将设备的系统时间往后调整1天，才能立刻显示地图。）

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170306.93774286362778207941086799224452:50001231000000:2800:5F7D06449B2FBF2FE93AD7651E75FB6AEB95B42AF13A785F6EE6A47C8B0731C1.png)

方案二：将本地配置自动签名证书和AGC上调试证书全部删除，重新生成新的自动签名，调试证书会自动生成，并用新的调试证书生成公钥指纹。

将build-profile.json5文件下signingConfigs参数删除。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170306.92689321358821080099596818074795:50001231000000:2800:67A0E7DC763FACBE704ABB86D01DE12665854CBADB9D5C21EC79FDBEEE46F36F.png)

将config文件夹下所有内容删除。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170306.17594424890620480036866917709278:50001231000000:2800:8C7F4E4C9BDADD26EC87316FE2F034E0FF08C9C8B00F22C32B190AD6C475D8A0.png)

将AGC上自动签名生成的调试证书删除。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170306.78463573454108349964647288091710:50001231000000:2800:6A53778EE87BA26EA7FE31C4E8EDF66C94C54EFCC403D46621AB2016B4562E86.png)

将旧证书删除后生成新的自动签名，调试证书会被同步创建，然后用新生成的调试证书生成新的指纹即可。（需注意，配置完成后由于鉴权缓存，可能还是无法马上显示地图，须清除缓存或者将设备的系统时间往后调整1天，才能立刻显示地图。）

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170307.56849988573398725646779793700335:50001231000000:2800:2FC257E26D702A9118353DF51F2EF9BBD35AE13B54974CAE7A20B68FF8AA1D2C.png)

7. 如未解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600004 应用没有开通地图服务权限

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The Map permission is not enabled.

**错误描述**

应用没有开通地图服务权限。

**可能原因**

1. 没有开通地图服务权限。

2. client_id未配置。

**处理步骤**

1. [开通地图服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc#section16133115441516)。

2. 配置client_id。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170307.15404264081497186112448631046141:50001231000000:2800:5C0167C800FAE62EDBA0FE24AE778052708B1C3776E8692004C31FCDDE24BB71.png)

3. 如未解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600005 网络不可用

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The network is unavailable.

**错误描述**

网络不可用。

**可能原因**

网络不可用。

**处理步骤**

检查网络后尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600006 API调用量超出配额

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The API call times exceed the quota.

**错误描述**

API调用量超出配额。

**可能原因**

API调用量超出配额。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600007 API的QPS超过配额

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The API QPS exceeds the quota.

**错误描述**

API的QPS超过配额。

**可能原因**

API的QPS超过配额。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600008 接口已经欠费

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The API is in arrears.

**错误描述**

接口欠费。

**可能原因**

接口欠费。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600009 API未订购付费套餐

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The API has not subscribed to any pay-as-you-go package.

**错误描述**

API未订购付费套餐。

**可能原因**

未订购付费套餐。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600010 服务器繁忙，请稍后再试

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The server is busy. Please wait and try again.

**错误描述**

服务器繁忙。

**可能原因**

服务器繁忙。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600011 服务器异常

 支持设备PhonePC/2in1TabletWearable

**错误信息**

Server error.

**错误描述**

当发生系统内部错误时，将返回该错误码。

**可能原因**

1.服务器异常。

2.网络不可用。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600012 国家或地区码异常

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The country code is not supported.

**错误描述**

当传入国家/地区码错误时，将返回该错误码。

**可能原因**

不支持该国家/地区码。

**处理步骤**

更换国家/地区码。

## 1002600013 当前路由地未知，稍后重试

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The current routing location is unknown. Try again later.

**错误描述**

当前路由地未知。

**可能原因**

获取当前设备的路由地失败。

**处理步骤**

1. 检查设备网络是否可用。
2. 尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600014 地图应用启动失败。

 支持设备PhonePC/2in1TabletWearable

**错误信息**

Failed to start the map app.

**错误描述**

地图应用启动失败。

**可能原因**

设备未安装地图应用且拉起应用市场地图下载详情页失败。

**处理步骤**

1. 通过应用市场搜索下载地图应用。
2. 尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600015 热力图ID已存在

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The heatmap ID already exists.

**错误描述**

热力图ID已存在。

**可能原因**

热力图ID已存在。

**处理步骤**

尝试更换ID或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600999 未知错误

 支持设备PhonePC/2in1TabletWearable

**错误信息**

Unknown error.

**错误描述**

当发生系统内部错误时，将返回该错误码。

**可能原因**

其他未知错误。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002601001 要操作的对象已经不存在

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The object to be operated does not exist.

**错误描述**

操作的对象不存在。

**可能原因**

操作的对象不存在。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002601002 自定义地图样式文件不存在

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The custom map style file does not exist.

**错误描述**

自定义地图样式文件不存在。

**可能原因**

1.自定义地图样式文件不存在。

2.设备网络不可用。

**处理步骤**

1.在[Petal Maps Studio](https://developer.petalmaps.com/console/studio/)网站检查样式id是否存在。

2.检查设备网络是否可用。

3.尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002601004 样式内容格式不正确

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The style content format is incorrect.

**错误描述**

样式内容格式不正确。

**可能原因**

样式内容格式不正确。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002601005 生成自定义组件图标失败

 支持设备PhonePC/2in1TabletWearable

**错误信息**

Failed to generate the icon of the custom component.

**错误描述**

生成自定义组件图标失败。

**可能原因**

生成自定义组件图标失败。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002602001 起终点无归属国家，或服务错误

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The start and end points do not have home countries, or a service error occurred.

**错误描述**

起终点无归属国家，或服务错误。

**可能原因**

参数错误。

**处理步骤**

请检查起终点后尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002602002 不支持跨区进行路径规划

 支持设备PhonePC/2in1TabletWearable

**错误信息**

Cross-region route planning is not supported.

**错误描述**

不支持跨区进行路径规划。

**可能原因**

参数错误。

**处理步骤**

检查入参是否涉及跨区。

## 1002602003 起始点或结束点超过100个

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The number of start points or end points exceed 100.

**错误描述**

起始点或结束点超过100个。

**可能原因**

参数错误。

**处理步骤**

检查入参，起点或终点个数是否超限。

## 1002602004 两点直线距离超过限制的距离

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The linear distance between the start point and end point exceeds the upper limit.

**错误描述**

两点直线距离超过限制的距离。

**可能原因**

参数错误。

**处理步骤**

检查入参，两点直线距离是否超过接口限制的距离。

## 1002602005 起点/终点/途经点不支持导航

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The start point, end point, or waypoint does not support navigation.

**错误描述**

起点/终点/途经点不支持导航。

**可能原因**

参数错误。

**处理步骤**

检查入参。

## 1002602006 请求点位映射到道路同一点上

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The request point is mapped to the same point on the road.

**错误描述**

请求点位映射到道路同一点上。

**可能原因**

参数错误。

**处理步骤**

检查入参。

## 1002603001 空结果

 支持设备PhonePC/2in1TabletWearable

**错误信息**

Zero result.

**错误描述**

空结果。

**可能原因**

参数错误。

**处理步骤**

检查入参。

## 1022100001 要操作的地图控制器不存在

 支持设备PhonePC/2in1TabletWearable

**错误信息**

The map controller to be operated does not exist.

**错误描述**

要操作的地图控制器不存在。

**可能原因**

要操作的地图控制器不存在。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 401 入参无效

 支持设备PhonePC/2in1TabletWearable

**错误信息**

Invalid input parameter.

**错误描述**

入参无效。

**可能原因**

入参不符合要求。

**处理步骤**

检查入参。

## 801 功能不支持。设备能力受限，调用接口失败。

 支持设备PhonePC/2in1TabletWearable

**错误信息**

Capability not supported. Failed to call the API due to limited device capabilities.

**错误描述**

功能不支持。设备能力受限，调用接口失败。

**可能原因**

当前设备不支持调用该接口。

**处理步骤**

更换设备或者使用其他接口。
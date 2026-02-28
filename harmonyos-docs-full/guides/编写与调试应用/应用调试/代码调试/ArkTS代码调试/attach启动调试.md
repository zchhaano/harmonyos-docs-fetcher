# attach启动调试

开发者也可以通过将调试程序attach到已运行的应用进行调试。

Attach Debugger和Debug的区别在于，Attach Debugger to Process可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而Debug是直接运行应用/元服务后立即启动调试。

## 前提条件

当前设备上被attach的应用代码和本地代码一致，且已提前进行构建生成必要的sourcemap文件。

## 使用约束

attach不支持的场景：

- 本地无源码。
- bundleName不匹配，将出现提示“The selected process does not match the bundlename of the current project!”，但不阻塞调试过程。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102037.29850664667715832669948191613048:50001231000000:2800:034A9D75B9D888A81D45F39DD4F448C42048E974D2DC4C693E914310A7937E8B.png)

## 操作步骤

1. 在工具栏中，选择调试的设备，并单击**Attach Debugger to Process**![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102038.55177439518964822010233406159199:50001231000000:2800:366A8A941D0254FF452CEA69DACD7AE8BD84C84ADB543D5CB44DBF4BAD3CE46D.png)启动调试。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102038.45913651852638853029250618798065:50001231000000:2800:81AD34CED3A5887D1F8F737963E5B34B8C4F0FD7D5E30FA997F7523BF6D1EF45.png)
2. 选择要调试的应用进程，若应用bundlename与当前工程不一致，则需勾选Show all process。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102038.30203982372239114909832513126017:50001231000000:2800:C76F6E4031AA3DA2BE43A7EB24802DBDFAA0DC1CD02D32DEC584C4E95970B563.png)

 说明

正常情况下，attach调试仅支持debug签名的应用，从DevEco Studio 6.0.2 Beta1版本开始，PC/2in1上的应用，如果使用了release签名并且配置了ohos.permission.kernel.ALLOW_DEBUG权限，也支持被attach调试。
3. 选择需要使用的调试配置，或者使用默认配置。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102038.07119948624516383957535032207154:50001231000000:2800:EA3F1C7A9FE0CDEC856F497B79A469E2A96943069024C68F584292581B48E511.png)
4. 选择需要调试的Debug type，若选择已创建的Run/Debug configuration进行attach调试，此时Debug type不可改变，只可在Run/Debug configuration界面修改。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102038.42755959511775385410745382397772:50001231000000:2800:44706E4C3332F1584A1710A06B0DB9185849EF7EB7D5A14E5D65B0F7D99F1775.png)

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102038.88646236833043302404487855361566:50001231000000:2800:C15DA97E7CA8CEB64EC5ECAD3E0D8CF452E57E7DD0F611AEBD68C98A3CFF1FBC.png)
5. 点击**OK**开始attach调试。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102038.34536029016694165178338434381031:50001231000000:2800:9430BF8D2A10A2BFE326F19A3EB857D0A5E001685BA8725F58872FB3F5C0F7E4.png)
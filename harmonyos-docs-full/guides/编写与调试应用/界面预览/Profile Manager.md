# Profile Manager

由于真机设备有丰富的设备型号，不同设备型号的屏幕分辨率可能不一样。因此，在HarmonyOS应用/元服务开发过程中，由于设备类型繁多，可能需要查看在不同设备上的界面显示效果。对此，DevEco Studio的预览器提供了Profile Manager功能，支持开发者自定义预览设备Profile（包含分辨率和语言），从而可以通过定义不同的预览设备Profile，查看HarmonyOS应用/元服务在不同设备上的预览显示效果。当前支持自定义设备分辨率及系统语言。

定义设备后，可以在Previewer右上角，单击![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102006.14842040028961766882906295999137:50001231000000:2800:8FE5D4E0D3112C84DA6D951EB9EF4164722BA69DCFD04886B474A76BBDFD7449.png)按钮，打开Profile管理器，切换预览设备。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102006.21820749957036626280144483042621:50001231000000:2800:207AB160437D4A78B1FD95F5E7423FF653BDB3914DD6B134D1D74CD188E3CAA3.png)

同时，Profile Manager还支持多设备预览功能，具体请参考[查看多端设备预览效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-multi-profile)。

下面以自定义一款Phone设备为例，介绍设备Profile Manager的使用方法。

1. 在预览器界面，打开Profile Manager界面。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102006.00433751411594954123424450021652:50001231000000:2800:07074DEFB9661E7F5EBD2551FD92716304E1AC0203D7CCD893ED94A3214A2C28.png)
2. 在Profile Manager界面，单击**+ New Profile**按钮，添加设备。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102006.59762432545293162595126980053372:50001231000000:2800:5A8A082BF36952FC3695A8FFEF6327668E6CD656EEB9623C60EC80C20A21FC12.png)
3. 在**Create Profile**界面，填写新增设备的信息，如**Profile ID**（设备型号）、**Device type**（设备类型）、**Resolution**（分辨率）和**Language and region**（语言和区域）等。其中Device type只能选择module.json5中deviceTypes字段已定义的设备。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102006.92830294336966515233570391781844:50001231000000:2800:06437570C8B92B0DD95C88120037D1D1AED7C25FF72BA85AAEB4B8A0FDAA1676.png)
4. 设备信息填写完成后，单击**OK**完成创建。
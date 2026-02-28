# debug启动调试

可以按照如下方式启动调试会话。

1. 如果需要设置断点调试，找到需要暂停的代码片段，点击该代码行的左侧边线，或将光标置于该行上并按Ctrl + F8（macOS为Command+F8）。如果无法添加断点，请查看FAQ[调试过程中无法添加断点](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-1)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102035.51287490304249801244130198878055:50001231000000:2800:3215BB3A428226D5C514821254505B4FE84806B9CBAC736C38A701FBA5AE3323.png)

设置断点后，调试能够在正确的断点处中断，并高亮显示该行。
2. 在设备选择框中，选择调试的设备。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102035.63635114265025557380355250600282:50001231000000:2800:45226FBD047621F214863609F885855EAEF60C6A1A53CE4116BF39FB0677F71A.png)
3. 选择启动调试的配置，在模块选择框中选择需要调试的模块。也可以通过Edit Configurations[配置调试参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-debug-configurations)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102035.16319100570362235653884978435107:50001231000000:2800:03DF32470840E69EBB7C15F317D169F8F358B951C450D4A6074630369210425D.png)
4. 在工具栏中，单击Debug![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102035.68281871278716532121426410342836:50001231000000:2800:41C496E65B4989F24C5EF56C673007A599458E6047B980D719780BF035A84E17.png)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102035.24717837098379006708174962698984:50001231000000:2800:4C71300E55D1DF2A0098A404AA0007446BD115BF9BA53F4593A68B6D910BA0E3.png)

或者在工具栏中Run中选择Debug。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102035.96165833260598756358068693092869:50001231000000:2800:938E708D3B2F83662FB5E6A19A41F9D161F56B8FC3AC9484E7741E3B5F47FDBC.png)
5. 启动调试后，开发者可以通过[调试器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debugger)进行代码调试。

如有断点会在断点处高亮，并展示当前断点处的Frames和Variables。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102035.41207177706243084990607471038195:50001231000000:2800:5277366293282EEB6F13F877DA6847A593C83D4590561ADC5B953E3FC26CA794.png)
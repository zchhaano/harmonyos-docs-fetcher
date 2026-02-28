# 查看ArkUI状态变量

从DevEco Studio 6.0.2 Beta1版本开始，支持在调试时查看ArkUI状态变量的实时变化情况。

在调试窗口中，点击**Layout Settings**![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102031.01731490231679811933441403414534:50001231000000:2800:E497817D950C468370044F7150445739262BD07B3615D47725BE4C4713D52F5F.png)，勾选**ArkUI State**，打开ArkUI状态变量面板。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102031.94170575276377483286385142068715:50001231000000:2800:2D401DF08F10AC19F70505415C32E091CEFF5A435358A12C60D1E1CAD13659C7.png)

状态变量面板分为总览（Summary）和当前值（Current Value）两个子面板：

- 总览面板显示了当前应用运行时，状态变量更新的总体情况，包含了状态变量的名称、更新次数、装饰器类型、所属组件、所属类。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102031.15075402461640001671391555020489:50001231000000:2800:943BD11F105CDB24008F55137B86692A7D417CC46290EB237F008EB12FBCC9C9.png)
- 当前值面板记录了状态变量实时变化的数据，包含了状态变量的更新时间、名称、所属组件、所属类、装饰器类型、当前值、影响的组件数量。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102031.78004327526285084712227433789984:50001231000000:2800:58A164906EF3EFDBC54E53138D00FD27D295B9F10298DF8D1E775A42B35277CD.png)当点击右侧的箭头时，新弹出的面板将显示当前选中状态变量影响的组件列表，包含影响组件的组件名、组件ID、是否为自定义组件。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102031.85682062417216094558896473627195:50001231000000:2800:5404DB970BA46A3911B7B2D47423DAEDF9C5C76DFC4B6410C89AF793E9839F61.png)

 说明

- 打开状态变量面板后才会开始监听状态变量的更新，因此，无法查看面板打开前状态变量的更新情况。
- 同一次调试过程中，关闭状态变量面板不会清空之前的数据，当前值面板最多展示1000条数据，超过限制后，仅展示最新的1000条数据。
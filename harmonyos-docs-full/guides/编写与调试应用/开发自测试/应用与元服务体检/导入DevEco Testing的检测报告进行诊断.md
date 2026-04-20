# 导入DevEco Testing的检测报告进行诊断

 

从DevEco Studio 6.0.0 Beta3版本开始，支持在DevEco Testing中进行性能相关测试生成检测报告后，导入到AppAnalyzer进行诊断和分析，获得可能的故障原因并生成体检报告。

 

#### 前置操作

体检前，请先在DevEco Testing中测试并导出检测报告，具体操作方式请参考[性能基础质量测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/specialized-testing#section12324184817324)或[场景化性能测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/specialized-testing#section8642101711299)。

  

#### 进行体检

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/L9ZAK5IiS0u3x4Kc6KZbSA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194023Z&HW-CC-Expire=86400&HW-CC-Sign=B7B5C73F27BEC4F83084F172A3A36C2205DE16349B482494A93525C5636829AD) 

由于DevEco Testing和AppAnalyzer在检测能力、检测方法以及场景识别上存在差异，所以通过DevEco Testing检测并导入AppAnalyzer诊断和直接通过AppAnalyzer检测并诊断，检测和诊断结果会出现不一致的情况。

   

#### [h2]DevEco Studio 6.0.1 Beta1及以上版本

1. 点击菜单栏**Tools >****AppAnalyzer**，打开AppAnalyzer页面，点击底部**体检历史**按钮，点击右上角的**导入报告**按钮，根据界面提示，确保即将导入的检测报告满足相关要求。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Rea1J_xNTeaM4xYYy2DrbA/zh-cn_image_0000002561752875.png?HW-CC-KV=V1&HW-CC-Date=20260420T194023Z&HW-CC-Expire=86400&HW-CC-Sign=8D5E6D651F528C9B14170290EBC1FA5F8C8306F5B7E45F96622E16200F5C8E8A)
2. 选择从DevEco Testing导出的报告（zip文件），点击**确认**后，等待AppAnalyzer导入数据并对问题进行诊断分析。AppAnalyzer仅支持对DevEco Testing中的部分指标进行诊断，具体请参考[检测指标](#section16156317171913)。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/GwOjF580QnGu7_Lencs6EQ/zh-cn_image_0000002530752944.png?HW-CC-KV=V1&HW-CC-Date=20260420T194023Z&HW-CC-Expire=86400&HW-CC-Sign=261BCF2D8DD676CCF8C0C6E567D613279A0591BE3F75D4370066C8DE07C29F68)
3. 诊断完成后，查看测试报告如下。

  - **源文件、调优文件（包含trace文件和调用栈文件）或snapshot文件、时间戳等**：点击源文件可跳转到问题源码，点击调优文件或snapshot文件支持直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析，点击时间戳可以打开Profiler并定位到问题发生的时间范围。
  - **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
  - **优化建议**：针对可能的故障原因，给出对应的最佳实践，点击链接可跳转至官网文档。

 

从DevEco Studio 6.0.2 Beta1版本开始，如果在体检中遇到问题，可点击报告右上角的**用户反馈**向我们反馈。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/0xilBQAjTUa_bz_pcCCaJg/zh-cn_image_0000002561832869.png?HW-CC-KV=V1&HW-CC-Date=20260420T194023Z&HW-CC-Expire=86400&HW-CC-Sign=2B5399B8564BBBFF08005BA4F84CBDF33F45DDD2600A6BFCCD2CCA070576D737)

  

#### [h2]DevEco Studio 6.0.1 Beta1以下版本

1. 点击菜单栏**Tools >****AppAnalyzer**，打开AppAnalyzer页面，点击底部**历史记录**按钮，进入历史记录页面。
2. 点击右上角的**检测报告导入**按钮，首次测试时，请根据AppAnalyzer的指引，下载Python及三方库，并根据界面提示，确保即将导入的检测报告满足相关要求。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/kjTvnJflRRyQZVL6TJDD0Q/zh-cn_image_0000002561752877.png?HW-CC-KV=V1&HW-CC-Date=20260420T194023Z&HW-CC-Expire=86400&HW-CC-Sign=B46B51693CFD4792F8B7BD89740CA24B9102CB0914FA83ACD231EAFB457C8D18)
3. 选择从DevEco Testing导出的报告（zip文件），点击**确认**后，等待AppAnalyzer导入数据并对问题进行诊断分析。AppAnalyzer仅支持对DevEco Testing中的部分指标进行诊断，具体请参考[检测指标](#section16156317171913)。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/QW7onmsZSKe2tCTGSg9frA/zh-cn_image_0000002530912948.png?HW-CC-KV=V1&HW-CC-Date=20260420T194023Z&HW-CC-Expire=86400&HW-CC-Sign=0F6AF711948EC395603C99EFA3BDD5E17D6EF0D1ADC1002A39981D9D25E5A15C)
4. 诊断完成后，查看测试结果如下。

  - 测试报告：测试结果的汇总信息，点击**详情链接**可跳转到对应场景的详情报告。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/KvnIH5WwQe-yLZ_awOYcmw/zh-cn_image_0000002561752889.png?HW-CC-KV=V1&HW-CC-Date=20260420T194023Z&HW-CC-Expire=86400&HW-CC-Sign=B387AE49CD46BCFAE64C83D7AAB698A245FE1E624BACB8A9C6FED9D7C128523A)
  - 详情报告：给出详细的测试结果、可能的故障原因和对应的优化建议。

    - **开始/结束页面、时间戳、调优文件（包含trace文件和调用栈文件）或snapshot文件等**：点击开始/结束页面可跳转到问题源码，点击时间戳可以打开性能分析工具Profiler并定位到问题发生的时间范围，点击调优文件或snapshot文件支持直接拉起Profiler并导入性能检测的问题数据进行调优分析。
    - **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
    - **优化建议**：针对可能的故障原因，给出对应的最佳实践，点击链接可跳转至官网文档。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/GA3FKSKfRCKzQEYG7JH-tQ/zh-cn_image_0000002530752936.png?HW-CC-KV=V1&HW-CC-Date=20260420T194023Z&HW-CC-Expire=86400&HW-CC-Sign=940ECE689A389A67F840352D6C2EA3E1CE857E34EFEA8FB8B28CF3F625297CE2)

 ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/_j9qy0fRRUqf3hbFwcm1KQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194023Z&HW-CC-Expire=86400&HW-CC-Sign=85D49EDDAD0E41F0DD50857FD2F8018DBF2F3E890E813D3F9D2DF51CB9A74962) 

由于DevEco Testing和AppAnalyzer在检测能力、检测方法以及场景识别上存在差异，所以通过DevEco Testing检测并导入AppAnalyzer诊断和直接通过AppAnalyzer检测并诊断，检测和诊断结果会出现不一致的情况。

  

#### 检测指标

AppAnalyzer会将DevEco Testing测试用例的操作归类为以下场景，仅支持对部分指标进行诊断，具体如下。

 

| 场景 | 检测指标 |
| --- | --- |
| 页面间转场 | 点击响应时延 |
| 点击完成时延 |  |
| 转场卡顿率 |  |
| 页面滑动 | 滑动响应时延 |
| 滑动卡顿率 |  |
| 冷启动 | 完成时延 |
| 页面内转场 | 滑动响应时延 |
| 点击响应时延 |  |
| 点击完成时延 |  |
| 滑动卡顿率 |  |
| 起播时延 |  |
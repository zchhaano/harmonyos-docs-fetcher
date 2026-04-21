# 技能（Skills）配置

 

#### 功能介绍

在日常工作中，我们经常需要处理重复性任务，如调整文档结构、撰写周报告等，每次都需要输入格式要求、偏好、操作流程，这种模式不仅耗时，也容易遗漏关键细节。Skills是一份标准化的教程，会指导CodeGenie面对任务时如何思考、遵循什么步骤、输出什么格式、注意事项是什么。开发者只需要定义一次，CodeGenie便能在后续的每次对话中自动识别并应用，实现“一次定义，长期稳定复用”效果。

 

Skills实际是一个包含SKILL.md文件的文件夹，在SKILL.md文件中以自然语言描述技能的名称、触发条件和执行步骤，让开发者能快速定义自动化工作流。SKILL.md文件写作时，严格遵循业界YAML Frontmatter（元数据） + Markdown Body（正文） 的统一规范，以及要确保内容结构清晰、触发词准确、没有错误处理，提升Skill可维护和可复用性，使Agent能够稳定执行。

 

从DevEco Studio 6.1.0 Release（6.1.0.830）版本开始，CodeGenie支持导入Global Skills（全局技能）和Project Skills（项目技能）两种。其中，Global Skills支持当前用户在本地所有项目中使用，不可跨设备同步；Project Skills适用于当前项目。开发者根据业务需要导入对应的Skills。

  

#### [h2]约束与限制

- 当前自定义Agent和HarmonyOS Act智能体支持使用Skills。
- SKILL.md中name的要求：长度不超过64个字符，由小写字母，数字和-组成，不能以-开头或结尾，不能包含连续的-，与所在文件夹命名一致。
- SKILL.md中description的要求：长度不超过1024个字符。
- SKILL.md中正文指令的要求：长度不超过32768个字符。
- SKILL.md所在文件夹的要求：大小不超过100MB。

  

#### 操作步骤

1. 点击界面右上方![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/W4DH-cQ_RDuJxDqjJhZeeg/zh-cn_image_0000002574920487.png?HW-CC-KV=V1&HW-CC-Date=20260420T193622Z&HW-CC-Expire=86400&HW-CC-Sign=870E266DE668C3D2EB9344C9B57BB7EFEA7B4B3C1AF5EA265AADEE85AAC21DBD)按钮，或者点击界面右上方**Settings**按钮，选择**Skills**，进入配置页面。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/WMAuSmucTpG1DO_60lM4Mw/zh-cn_image_0000002544400266.png?HW-CC-KV=V1&HW-CC-Date=20260420T193622Z&HW-CC-Expire=86400&HW-CC-Sign=71652F082E142D639C926A899C67998299E240CF7F85486565375EB1454C9F77)
2. 在**Global Skills**或**Project Skills**下，首次导入时，点击**Import**导入技能文件；若已存在技能文件，点击![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/f9TjECC4TEWT018cBqggtw/zh-cn_image_0000002575080479.png?HW-CC-KV=V1&HW-CC-Date=20260420T193622Z&HW-CC-Expire=86400&HW-CC-Sign=C4D979CA92CF834A436CA16FB7B8BED19626B8865D0D64E2D9FFF7BE5FBF7EB3)按钮进行导入。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/yFdqkhclR36nEIJw96n-KA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T193622Z&HW-CC-Expire=86400&HW-CC-Sign=2C9E7EEEA67A335C5DBC2E263470574D579C12E4C05C5FF4E565046EAE826FF9) 

  - 若选择的文件夹中存在SKILL.md，则作为单个skill导入。
  - 若选择的文件夹中不存在SKILL.md，则遍历下一级文件夹，检查下一级文件夹中是否包含SKILL.md，遍历到的SKILL.md将作为skill导入。若下一级文件夹遍历出多个SKILL.md，将批量导入。仅支持遍历所选择文件夹的下一级，不支持更深级的遍历。

  

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/nCNmAB32TteaC0TZdbhm6g/zh-cn_image_0000002544240608.png?HW-CC-KV=V1&HW-CC-Date=20260420T193622Z&HW-CC-Expire=86400&HW-CC-Sign=21A1FBFF6F2E5607152A3A854F3784C47E7C6F551BC6E84A01A7E481E3EDC76F)
3. 在**Global Skills**和**Project Skills**列表中，显示已导入的技能信息，包括技能名称（如openharmony-build）、描述信息、启用状态。同时，将鼠标悬浮在技能信息上会显示编辑和删除的操作按钮，点击可在代码编辑区打开SKILL.md文件。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/B9PmRI7XRRupheEiqkojqA/zh-cn_image_0000002574920489.png?HW-CC-KV=V1&HW-CC-Date=20260420T193622Z&HW-CC-Expire=86400&HW-CC-Sign=94A3B5660FF9D1174C4ACA8192F647CF48A249B1A95EA49500368AE9BFFB9C85)
4. 返回CodeGenie对话框调用Skills，在对话框输入时需要带有技能的name（如openharmony-build）。

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/FnBXG-LnRkaFmvk4sH-33w/zh-cn_image_0000002575141233.png?HW-CC-KV=V1&HW-CC-Date=20260420T193622Z&HW-CC-Expire=86400&HW-CC-Sign=766C2F76A8F8FC2F916FF57C9817B2495D4A116253D36DE762B8C0E136EA02D9)
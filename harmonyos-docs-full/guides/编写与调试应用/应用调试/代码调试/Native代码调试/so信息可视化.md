# so信息可视化

在native调试窗口中，点击**Layout Settings**![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102043.57133561832226833500009861688663:50001231000000:2800:FD1C167F7F165FF7ED82CA0FAF04F5A1EDF26C77E405F7B07124FB671C87BE8C.png)，勾选**Modules**，打开模块视图。

在native调试期间，**Modules**窗口会列出并显示有关应用使用的so信息。点击各属性可按升序/降序来排序，；支持字符串匹配搜索。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102043.15624197111838577041672855157142:50001231000000:2800:8FBF2CBD3E5806E5789AD41569DBD6E39A6B0FB4FB3592BBB9E593B766748AB8.png)

- 加载符号表文件

如果符号未加载，可右键点击模块，选择**Load Modules**，加载本地携带符号信息的so文件。加载成功后，Symbol Status列会显示"Symbols Loaded"。

如需将符号恢复为初始状态，可右键点击模块，选择**Reset****Modules**。
- 添加源码地址映射

加载的符号表文件路径默认是编译时的路径，若与本地的源码文件路径不一致时，需要关联源码文件。右键点击模块，选择**Set Source Mapping**，选择本地源码文件路径，映射成功后，Source Root Path列会显示映射后的路径。

如需恢复为默认路径，可右键点击模块，选择**Reset****Source Mapping****s**。
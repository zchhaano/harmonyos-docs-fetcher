# Hot Reload

DevEco Studio提供Hot Reload（热重载）能力，支持开发者在真机或模拟器上运行/调试应用时，修改代码并保存后无需重启应用，在真机或模拟器上即可使用最新的代码，帮助开发者更快速地进行调试。

针对大多数代码修改场景，热重载均能提供支持，但是一些特殊场景需要通过热重载+重启应用后方可生效，因此，DevEco Studio提供基于热重载的增强能力——热重启。[开启开关后](/consumer/cn/doc/harmonyos-guides/ide-hot-reload#section1724105718289)，DevEco Studio在遇到热重载不支持的场景时，将自动切换至热重启以获取更强的支持能力。

从DevEco Studio 5.1.1 Beta1版本开始支持热重启能力。

 说明 

Hot Reload支持Stage模型的ArkTS工程，不支持ArkTS卡片相关工程，不建议在hotReload模式下执行与ArkTS卡片的相关操作。

## 热重载、热重启、完全重启的区别

- **热重载**：不重启应用，可保留应用状态，但整个过程会重新运行入口文件内的逻辑。
- **热重启**：在运行流程上，与热重载相比，主要区别在于会重启应用，不保留应用状态，支持更广泛的ArkTs代码修改快速生效。一旦执行了热重启，后续热重载流程均会被热重启取代。
- **完全重启**：会完全重新运行应用，该任务较为耗时，因为它会重新全量编译代码和资源文件。

## 使用约束

   **表1**热重载/热重启的修改文件支持范围       展开

| 修改文件 | 热重载 | 热重启 | 说明 |
| --- | --- | --- | --- |
| 修改Entry入口模块内ets、ts代码文件 | 支持 | 支持 | - |
| 修改Entry直接或间接依赖的Har模块内代码文件 | 支持 | 支持 | Har模块与Entry模块间无Hsp |
| 修改Entry直接或间接依赖的Hsp模块内代码文件 | 不支持 | 不支持 | - |
| 引入的其他工程Har模块内代码文件 | 支持 | 支持 | Har模块与Entry模块间无Hsp |
| 引入的其他工程Hsp模块内代码文件 | 不支持 | 不支持 | - |
| 修改worker线程文件 | 不支持 | 不支持 | - |
| 修改模块目录下Index文件 | 支持 | 支持 | - |
| 启动应用后新增的代码文件 | 不支持 | 不支持 | - |
| C++、so文件 | 不支持 | 不支持 | - |
| resource资源文件（如修改string.json文件的内容） | 不支持 | 不支持 | 支持对资源引用的修改，例如把$r('app.color.greenColor')改成$r('app.color.redColor') |

    **表2**热重载/热重启的代码元素支持范围       展开

| 代码元素 | 变更行为 | 热重载 | 热重启 | 说明 |
| --- | --- | --- | --- | --- |
| UI代码(如修改字号、颜色等) | 新增、修改、删除 | 支持 | 支持 | - |
| UI响应事件(如添加onClick事件等) | 新增、修改、删除 | 支持 | 支持 | - |
| import | 新增 | 部分支持 | 部分支持 | 不支持从启动应用时未加载的文件中import模块。 |
| 修改、删除 | 支持 | 支持 | - |  |
| export | 新增 | 部分支持 | 部分支持 | 新增export default语句时应同步在调用文件内新增对应import语句，否则将失败。 |
| 修改、删除 | 支持 | 支持 | - |  |
| 装饰器(@State、@Prop等) | 新增、修改、删除 | 部分支持 | 部分支持 | 热重载、热重启：@Entry修饰的文件支持@Styles新增、修改、删除 热重启：@Entry修饰的文件支持@State新增、修改和删除 |
| declare声明变量 | 新增、修改、删除 | 支持 | 支持 | - |
| Struct代码块 | 新增 | 部分支持 | 支持 | @Entry修饰的文件内不支持新增Struct代码块热重载，其他文件支持。 |
| 修改 | 部分支持 | 支持 | @Entry修饰的文件不支持成员变量、成员函数热重载，其他文件支持。 |  |
| 删除 | 支持 | 支持 | - |  |
| 类 | 新增 | 部分支持 | 支持 | @Entry修饰的文件内不支持新增包含成员函数的class，其他文件支持。 |
| 修改 | 部分支持 | 支持 | @Entry修饰的文件内class不支持新增成员函数，其他文件支持。 |  |
| 继承 | 部分支持 | 支持 | @Entry修饰的文件内不支持类继承及被继承场景，其他文件支持。 |  |
| 删除 | 支持 | 支持 | - |  |
| 接口 | 新增、删除 | 支持 | 支持 | - |
| 修改 | 部分支持 | 支持 | @Entry修饰的文件内不支持接口对象修改，其他文件支持。 |  |
| 枚举 | 新增、修改 | 部分支持 | 支持 | @Entry修饰的文件内不支持新增枚举，不支持修改枚举的键和值，其他文件支持。 |
| 删除 | 支持 | 支持 | - |  |
| 匿名函数 | 新增、修改、删除 | 支持 | 支持 | - |
| Lambda函数 | 新增、修改、删除 | 支持 | 支持 | - |
| 闭包函数 | 新增、修改、删除 | 支持 | 支持 | - |
| 闭包变量 | 新增、删除 | 部分支持 | 部分支持 | 热重载仅支持顶层闭包变量（不包括this变量）的新增或删除 从DevEco Studio 6.0.0 Beta3版本开始，热重启不支持首次新增this变量或删除所有this变量。 |
| 修改 | 部分支持 | 支持 | 热重载不支持顶层闭包变量的修改 |  |
| 自定义组件 | 新增、修改、删除 | 部分支持 | 支持 | 热重载：@Entry修饰的文件内仅支持通过import方式引入的自定义组件的新增和修改。 |

    **表3**其他场景       展开

| 场景 | 热重载 | 热重启 | 说明 |
| --- | --- | --- | --- |
| 命中断点时 | 不支持 | 不支持 | 点击 Resume Program 继续执行后再进行热重载/热重启 |
| 修改跳转的其他ability页面 | 不支持 | 支持 | 修改代码并执行热重载后，重新拉起该ability页面可生效 |

## 使能热重启（可选）

如果需要使用热重启的能力，先打开对应开关：点击菜单栏**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**）**>****Build, Execution, Deployment > Hot Reload**，勾选**Enable hot restart****(to hot reload and restart app)**，点击**OK**完成设置。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102030.29420968351651633145814602640809:50001231000000:2800:82E4992832753484B8174172556A141B95FF55FF5B3DA78A1DC234E8E9512C25.png)

## 操作步骤

1. 连接真机设备或模拟器。
2. 在下拉菜单中，将运行/调试配置切换为Hot Reload的配置![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102030.44720006335247584338058854364574:50001231000000:2800:CF2E55315AA7B7BF6B4EB9E26121F0773F32F18A46128998A104559E43F3D10A.png)。 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102030.08206071188391753912548449897836:50001231000000:2800:DE85F2ABC2EA4756B9A2146EF6A83AAB3EE8CDBAC3160EA275DFC4E4F422CAE8.png)
3. 运行/调试应用，请参考[使用本地真机运行应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-device)或[使用模拟器运行应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-emulator)。
4. 修改代码后，可以通过如下操作，查看设备上修改后的显示效果。 

  - 点击Hot Reload![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102030.55497455606174032239990827955726:50001231000000:2800:1DA36DEC4430AB07264F1D1C05D3764B10C8383B46E1F4F829E16340692ABC33.png)按钮：         

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102030.59590412356731724854481259451506:50001231000000:2800:B0FF585A81509E84DE0B50D8592EAB7C4504752FDDD33548CDA002442D5EF66C.png)
  - 通过快捷键方式触发Hot Reload：需要先在菜单栏点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**），选择**Tools > Actions on Save**，勾选**Perform hot reload**，点击**OK**完成设置。修改代码后通过快捷键**Ctrl + S**即可触发Hot Reload。         

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102031.82617306598471759338699806260581:50001231000000:2800:5270DF5364CDEE98CD93A5A9D8CA160A0C92FB543619A7708840D4B660048784.png)

         成功执行热重载后，控制台会打印以下内容：        收起自动换行深色代码主题复制

```
Performing hot reload... Syncing files to device xxx Reloaded 1 files in x s xxx ms.
```

          成功执行热重启后，控制台中会打印以下内容：        收起自动换行深色代码主题复制

```
Performing hot restart... $ hdc shell aa force-stop com.xx.xx Syncing files to device xxx Reloaded 1 files in x s xxx ms. $ hdc shell aa start -a EntryAbility -b com.xxx.xxx in xxx ms
```
5. 点击停止按钮终止运行/调试运行，退出Hot Reload模式。

## 动态配置签名或应用版本号（可选）

在多人协作开发场景中，使用Hot Reload能力时，可以在hvigorfile.ts中动态配置签名或应用版本号，避免每个开发者都需要本地修改。该功能从DevEco Studio 6.0.2 Beta1版本开始支持。

- 可以不使用build-profile.json5中自动生成的签名信息，而是在hvigorfile.ts中配置签名信息，Hot Reload功能仍可正常使用，具体请参考[修改每个hvigorNode中的build-profile.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-config-ohos-sample#section973053620286)。
- 可以不使用app.json5中的versionCode，而是在hvigorfile.ts中动态配置应用版本号，Hot Reload功能仍可正常使用，具体请参考[修改app.json5中的配置信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-config-ohos-sample#section9435132933118)。
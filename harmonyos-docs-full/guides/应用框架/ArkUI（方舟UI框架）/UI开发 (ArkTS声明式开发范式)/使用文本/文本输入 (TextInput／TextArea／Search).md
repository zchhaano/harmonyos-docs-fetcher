# 文本输入 (TextInput/TextArea/Search)

  

TextInput、TextArea是输入框组件，用于响应用户输入，比如评论区的输入、聊天框的输入、表格的输入等，也可以结合其它组件构建功能页面，例如登录注册页面。具体用法请参考[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)和[TextArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea)组件的API文档。Search是特殊的输入框组件，称为搜索框，默认样式包含搜索图标。具体用法请参考[Search](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-search)组件的API文档。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/uj4v739xS1-s27iIaqNuNg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=E0F65C3C1B2AFF1FD2D6B5942A6E461AC1EE01D08DF9440397C2DA44ED360CA1)   

仅支持单文本样式，若需实现富文本样式，建议使用[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)组件。

     

#### 创建输入框

 

TextInput是单行输入框，TextArea是多行输入框，Search是搜索框。通过以下接口创建这些组件。

 

```
TextInput(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextInputController})

```

 

```
TextArea(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextAreaController})

```

 

```
Search(options?:{placeholder?: ResourceStr, value?: ResourceStr, controller?: SearchController, icon?: string})

```

 

- 单行输入框。

 

```
TextInput()

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/xeKnDon-QGWzwZ9LZqiukA/zh-cn_image_0000002543213840.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=B17F864ECF1AA135D7B73BEC5A80D56DEE81743691646A6C9CEC4BF93458331E)
- 多行输入框。

 

```
TextArea()

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/AZsY_ar6QnaYZgzmAzWZ6g/zh-cn_image_0000002573853753.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=740821DEE62A26E68A2F27C3F099A9BA366B31687EB1C728E3848A5AE667C1E9)
- 多行输入框文字超出一行时会自动折行。

 

```
/* 请将$r('app.string.CreatTextInput_textContent')替换为实际资源文件，在本示例中该资源文件的value值为
 * "我是TextArea我是TextArea我是TextArea我是TextArea"
 */
TextArea({ text: $r('app.string.CreatTextInput_textContent') })
  .width(300)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/LHLpgRScQZKvmFxnFse2Cg/zh-cn_image_0000002573973731.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=09CF1D63143B22A7112E132BBE734BA1C7A16E48B1803B11EBDFE652A15E9885)
- 搜索框。

 

```
Search()
  // 请将$r('app.string.Creat_TextInput_Content')替换为实际资源文件，在本示例中该资源文件的value值为"搜索"
  .searchButton($r('app.string.Creat_TextInput_Content'))

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/swJC9MsWQPymE1ciG4bYHA/zh-cn_image_0000002543373504.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=F209F41E9A486A422423BB4A9899AE3AF200FBAD1B0E6D7DF0A337153A791DF4)

    

#### 设置输入框类型

 

TextInput、TextArea和Search都支持设置输入框类型，通过type属性进行设置，但是各组件的枚举值略有不同。下面以单行输入框为例进行说明。

 

TextInput有以下类型可选择：Normal基本输入模式、Password密码输入模式、Email邮箱地址输入模式、Number纯数字输入模式、PhoneNumber电话号码输入模式、USER_NAME用户名输入模式、NEW_PASSWORD新密码输入模式、NUMBER_PASSWORD纯数字密码输入模式、NUMBER_DECIMAL带小数点的数字输入模式、带URL的输入模式。通过[type](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#type)属性进行设置：

    

#### [h2]基本输入模式（默认类型）

 

```
TextInput()
  .type(InputType.Normal)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/hqRU3j6qSTWKEO75OR8X1g/zh-cn_image_0000002543213842.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=5C201833192039FAFC15D067AEE668F2D254545F4E4ECF0BFB418EA48BC26210)

    

#### [h2]密码模式

 

包括Password密码输入模式、NUMBER_PASSWORD纯数字密码模式、NEW_PASSWORD新密码输入模式。

 

以下示例是Password密码输入模式的输入框。

 

```
TextInput()
  .type(InputType.Password)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/sLJsyCPmQSKV1gAW3eLPBg/zh-cn_image_0000002573853755.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=78FD65FE81BFDEFE904BF833B55FC9339EB4E9CDF1E68522D4F9A97F14D21D05)

    

#### [h2]邮箱地址输入模式

 

邮箱地址输入模式的输入框，只能存在一个@符号。

 

```
TextInput()
  .type(InputType.Email)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/ekmW0tc3SeqzpQSPHf2HjQ/zh-cn_image_0000002573973733.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=7A181DD084BCE6816D669C8342C5C6D24C66B4FE82E2D1AB053FFFE9E1F44311)

    

#### [h2]纯数字输入模式

 

纯数字输入模式的输入框，只能输入数字[0-9]。

 

```
TextInput()
  .type(InputType.Number)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/hG-3DP9IR3-KoMKILMbJ3A/zh-cn_image_0000002543373506.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=21BAB568F0DDF2DC0AD95A8D0B6698106CD70EB4445017A56B3A9EE841A23751)

    

#### [h2]电话号码输入模式

 

电话号码输入模式的输入框，支持输入数字、空格、+ 、-、*、#、(、)，长度不限。

 

```
TextInput()
  .type(InputType.PhoneNumber)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/WqnRjMA6RlaFIgzQHS8aSA/zh-cn_image_0000002543213844.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=48C3EA15BE1429941369648A96222D8EBE266FE93D704D0D08A75E6FADAA8FD1)

    

#### [h2]带小数点的数字输入模式

 

带小数点的数字输入模式的输入框，只能输入数字[0-9]和小数点，只能存在一个小数点。

 

```
TextInput()
  .type(InputType.NUMBER_DECIMAL)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/180zRkyUTWqYmfQQ4tK8ow/zh-cn_image_0000002573853757.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=7F122A1583341BF40741C28E2258D76A40C501E390226CBEE93A71A22BE15D3A)

    

#### [h2]带URL的输入模式

 

带URL的输入模式，无特殊限制。

 

```
TextInput()
  .type(InputType.URL)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/afVHJzYcRFaM7vqYg0_mDA/zh-cn_image_0000002573973735.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=750E7CFBD6CC0A3138CA6F91E33E47B8548C8C9E56C98F559E7D0A1A9C273623)

    

#### 设置输入框多态样式

 

TextInput、TextArea支持设置输入框多态样式，通过[style](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#style10)属性进行设置。下面以多行输入框TextArea为例进行说明。

 

TextArea有以下2种类型可选择：默认风格，入参是TextContentStyle.DEFAULT；内联模式，也称内联输入风格，入参是TextContentStyle.INLINE。

    

#### [h2]默认风格

 

默认风格的输入框，在编辑态和非编辑态，样式没有区别。

 

```
TextArea()
  .style(TextContentStyle.DEFAULT)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/rnnuUfTlT2-2KobM_t8SvA/zh-cn_image_0000002543373508.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=59CF3F346B6CE401D5CC9A2D28965C5D91CA41CB1054AE61125B2EB7622B40D0)

    

#### [h2]内联模式

 

内联模式，也称内联输入风格。内联模式的输入框在编辑态和非编辑态样式有明显区分。

 

```
TextArea()
  .style(TextContentStyle.INLINE)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/LmDR5iftSGOpgFLNpP6RdQ/zh-cn_image_0000002543213846.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=C13D840D10F749645FF00BFFB3F40A3B605D5C25DA4C3FED71E7CF7C6ACAD5FD)

    

#### 自定义样式

 

- 设置无输入时的提示文本。

 

```
// 请将$r('app.string.i_am_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
TextInput({ placeholder: $r('app.string.i_am_placeholder') })

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/CuJT2Bo4SHyWRLzQP8ygww/zh-cn_image_0000002573853759.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=654ED7C5D810D1D9BC4536535B5173146D8108962B6FC589F2B2F0EF97076630)
- 设置输入框当前的文本内容。

 

```
TextInput({
  // 请将$r('app.string.i_am_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
  placeholder: $r('app.string.i_am_placeholder'),
  // 请将$r('app.string.i_am_current_text_content')替换为实际资源文件，在本示例中该资源文件的value值为"我是当前文本内容"
  text: $r('app.string.i_am_current_text_content')
})

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/a7fFQ5tTRFOnn80EqKOV7g/zh-cn_image_0000002573973737.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=F2B1E4D485B267134DEFDD595FCDDDBEAA790CFCB954C03CFAE5E37024C311FC)
- 添加backgroundColor改变输入框的背景颜色。

 

```
TextInput({
  // 请将$r('app.string.i_am_placeholder')替换为实际资源文件，在本示例中该资源文件的value值为"我是提示文本"
  placeholder: $r('app.string.i_am_placeholder'),
  // 请将$r('app.string.i_am_current_text_content')替换为实际资源文件，在本示例中该资源文件的value值为"我是当前文本内容"
  text: $r('app.string.i_am_current_text_content')
})
  .backgroundColor(Color.Pink)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/BV92k8dORqax7Nl_kPDYhw/zh-cn_image_0000002543373510.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=EBBE4F146A5BA1FC0457C6FEB0D69438C380F4D150FE257883B4C944D22BC4A5)

 

更丰富的样式可以结合[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)实现。

    

#### 添加事件

 

文本框主要用于获取用户输入的信息，并将信息处理成数据进行上传，绑定[onChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onchange)事件可以获取输入框内改变的文本内容，绑定[onSubmit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onsubmit)事件可以获取回车提交的文本信息，绑定[onTextSelectionChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ontextselectionchange10)事件可以获取文本选中时手柄的位置信息或者编辑时光标的位置信息等等。用户也可以使用通用事件进行相应的交互操作。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/S5ySk8sORtWetxU-PpEvtw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=13752E7396960F40124D4FFCA8C41CD7EE21B5ABCCC35BF9AA967FBD137F5BA7)   

在密码模式下，设置[showPassword](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#showpassword12)属性时，在[onSecurityStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onsecuritystatechange12)回调中，建议增加状态同步，具体详见如下示例。

 

[onWillInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillinsert12)、[onDidInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondidinsert12)、[onWillDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwilldelete12)、[onDidDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondiddelete12)回调仅支持系统输入法的场景。

 

[onWillChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillchange15)的回调时序晚于[onWillInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillinsert12)、[onWillDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwilldelete12)，早于[onDidInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondidinsert12)、[onDidDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondiddelete12)。

   

```
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = '[Sample_Textcomponent]';
const DOMAIN = 0xF811;
const BUNDLE = 'Textcomponent_';

@Entry
@Component
struct TextInputEventAdd {
  @State text: string = '';
  @State textStr1: string = '';
  @State textStr2: string = '';
  @State textStr3: string = '';
  @State textStr4: string = '';
  @State textStr5: string = '';
  @State textStr6: string = '';
  @State textStr7: string = '';
  @State textStr8: string = '';
  @State textStr9: string = '';
  @State passwordState: boolean = false;
  controller: TextInputController = new TextInputController();

  build() {
    Row() {
      Column() {
        Text(`${this.textStr1}\n${this.textStr2}\n${this.textStr3}
          \n${this.textStr4}\n${this.textStr5}\n${this.textStr6}
          \n${this.textStr7}\n${this.textStr8}\n${this.textStr9}`)
          .fontSize(20)
          .width('70%')
        TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
          .type(InputType.Password)
          .showPassword(this.passwordState)
          .onChange((value: string) => {
            // 文本内容发生变化时触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onChange is triggering: ' + value);
            this.textStr1 = `onChange is triggering: ${value}`;
          })
          .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
            // 按下输入法回车键时触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onSubmit is triggering: ' + enterKey + event.text);
            this.textStr2 = `onSubmit is triggering: ${enterKey} ${event.text}`;
          })
          .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
            // 文本选择的位置发生变化或编辑状态下光标位置发生变化时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onTextSelectionChange is triggering: ' + selectionStart + selectionEnd);
            this.textStr3 = `onTextSelectionChange is triggering: ${selectionStart} ${selectionEnd}`;
          })
          .onSecurityStateChange((isShowPassword: boolean) => {
            // 密码显隐状态切换时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onSecurityStateChange is triggering: ' + isShowPassword);
            this.passwordState = isShowPassword;
            this.textStr4 = `onSecurityStateChange is triggering: ${isShowPassword}`;
          })
          .onWillInsert((info: InsertValue) => {
            // 在将要输入时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onWillInsert is triggering: ' + info.insertValue + info.insertOffset);
            this.textStr5 = `onWillInsert is triggering: ${info.insertValue} ${info.insertOffset}`;
            return true;
          })
          .onDidInsert((info: InsertValue) => {
            // 在输入完成时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onDidInsert is triggering: ' + info.insertValue + info.insertOffset);
            this.textStr6 = `onDidInsert is triggering: ${info.insertValue} ${info.insertOffset}`;
          })
          .onWillDelete((info: DeleteValue) => {
            // 在将要删除时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onWillDelete is triggering: ' + info.deleteValue + info.deleteOffset);
            this.textStr7 = `onWillDelete is triggering: ${info.deleteValue} ${info.deleteOffset}`;
            return true;
          })
          .onDidDelete((info: DeleteValue) => {
            // 在删除完成时，触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onDidDelete is triggering: ' + info.deleteValue + info.deleteOffset);
            this.textStr8 = `onDidDelete is triggering: ${info.deleteValue} ${info.deleteOffset}`;
          })
          .onFocus(() => {
            // 绑定通用事件，输入框获焦时触发该回调
            hilog.info(DOMAIN, TAG, BUNDLE + 'onFocus is triggering');
            this.textStr9 = `onFocus is triggering`;
          })
      }.width('100%')
    }
    .height('100%')
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/VmDhaWa4SoWF4XyfBbsLqA/zh-cn_image_0000002543213848.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=647CAD4F7C9F5405C0126C721263645DCB8890EC682BD044A136861AD56E0A54)

    

#### 选中菜单

 

输入框中的文字被选中时会弹出包含剪切、复制、翻译、分享的菜单。

 

TextInput:

 

```
// 请将$r('app.string.show_selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
TextInput({ text: $r('app.string.show_selected_menu') })

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/nu4-lFHGRmqETWI5ubIvYQ/zh-cn_image_0000002573853761.jpg?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=A73FF964BC7941B6D0B775B1933C93F7839F5F95013173572EC2819BFED40873)

 

TextArea:

 

```
// 请将$r('app.string.show_selected_menu')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示选中菜单"
TextArea({ text: $r('app.string.show_selected_menu') })

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/5EB8uooDSYGlGDv-_znIsQ/zh-cn_image_0000002573973739.jpg?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=6BA486B890D7C4CE90D6BE7A2A54CCEC5520CFE2F110DBFEC2E2202C1B90AE9C)

    

#### 禁用系统服务类菜单

 

从API version 20开始，支持使用[disableSystemServiceMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablesystemservicemenuitems20)方法屏蔽文本选择菜单中的所有系统服务菜单项。

 

```
import { TextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct DisableSystemServiceMenuItem {
  aboutToAppear(): void {
    // 禁用所有系统服务菜单项
    TextMenuController.disableSystemServiceMenuItems(true)
  }

  aboutToDisappear(): void {
    // 页面消失时恢复系统服务菜单项
    TextMenuController.disableSystemServiceMenuItems(false)
  }

  build() {
    Row() {
      Column() {
        // 请将$r('app.string.ProhibitSelectMenu_content')替换为实际资源文件，在本示例中该资源文件的value值为"这是一个TextInput，长按弹出文本选择菜单"
        TextInput({ text: $r('app.string.ProhibitSelectMenu_content') })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
              // menuItems不包含被屏蔽的系统菜单项
              return menuItems
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/DLpn0nYjSIeCYueal9EIfw/zh-cn_image_0000002543373512.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=7478EC04157ACA59EA7B5F8390208B736D4F56956EDD2CEA61DAFB6B32120B6B)

 

从API version 20开始，支持使用[disableMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablemenuitems20)方法屏蔽文本选择菜单中指定的系统服务菜单项。

 

```
import { TextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct DisableMenuItem {
  aboutToAppear(): void {
    // 禁用搜索，翻译和AI帮写
    TextMenuController.disableMenuItems([TextMenuItemId.SEARCH, TextMenuItemId.TRANSLATE, TextMenuItemId.AI_WRITER])
  }

  aboutToDisappear(): void {
    // 页面消失时恢复系统服务菜单项
    TextMenuController.disableMenuItems([])
  }

  build() {
    Row() {
      Column() {
        // 请将$r('app.string.ProhibitSelectMenu_content')替换为实际资源文件，在本示例中该资源文件的value值为"这是一个TextInput，长按弹出文本选择菜单"
        TextInput({ text: $r('app.string.ProhibitSelectMenu_content') })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
              // menuItems不包含搜索和翻译
              return menuItems;
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/WUD26GAtSUaPvPVmcAz9Sw/zh-cn_image_0000002543213850.png?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=4EAD92C20171428B6FDADE2723A9F60406B2D8D9B03AAD01E2414CABC8502F5E)

    

#### 自动填充

 

输入框可以通过[contentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#contenttype12)属性设置自动填充类型。

 

支持的类型请参考[ContentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#contenttype12枚举说明)。

 

```
// 请将$r('app.string.Auto_Fill_PlaceHolder')替换为实际资源文件，在本示例中该资源文件的value值为"输入你的邮箱..."
TextInput({ placeholder: $r('app.string.Auto_Fill_PlaceHolder') })
  .width('95%')
  .height(40)
  .margin(20)
  .contentType(ContentType.EMAIL_ADDRESS)

```

    

#### 设置属性

 

- 设置省略属性。

 

输入框可以通过[ellipsisMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ellipsismode18)属性设置省略位置。

 

ellipsisMode属性需要配合[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#textoverflow12)属性设置为TextOverflow.Ellipsis使用，单独设置ellipsisMode属性不生效。

 

```
// 请将$r('app.string.Set_Omission_Property_textContent')替换为实际资源文件，在本示例中该资源文件的value值为"这是一段文本，用来展示省略模式"
TextInput({ text: $r('app.string.Set_Omission_Property_textContent') })
  .textOverflow(TextOverflow.Ellipsis)
  .ellipsisMode(EllipsisMode.END)
  .style(TextInputStyle.Inline)
  .fontSize(30)
  .margin(30)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/hxMffJn8QIaP0wzvjlZUuQ/zh-cn_image_0000002573853763.jpg?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=2BAC5A25924D5AA2F079547D5567D83A6A8EEA23BCDB5F3EA42CECC814F02C2E)
- 设置文本描边属性。

 

从API version 20开始，输入框可以通过[strokeWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#strokewidth20)和[strokeColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#strokecolor20)属性设置文本的描边宽度及颜色。

 

```
TextInput({ text: 'Text with stroke' })
  .width('100%')
  .height(60)
  .borderWidth(1)
  .fontSize(40)
  .strokeWidth(LengthMetrics.px(3.0))
  .strokeColor(Color.Red)

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/2bvJfyjXQcCWm5eca0cotQ/zh-cn_image_0000002573973741.jpg?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=1F6C212D82F09D1556EFAFF27A8592B3E1180043586DCD14B5607AFFAF1F7A37)

    

#### 设置文本行间距

 

从API version 20开始，支持通过[lineSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#linespacing20)设置文本的行间距。如果不配置[LineSpacingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距。如果onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外行间距。

 

```
TextArea({
  text: 'The line spacing of this TextArea is set to 20_px, and the spacing is effective only between the lines.'
})
  .fontSize(22)
  .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/irXoMcb2SHaaVXPMw0XrRw/zh-cn_image_0000002543373514.jpg?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=67CFC2668A6C8C100EC76D7B086380D1A824BC0F209B2EE5976DA0114156AB44)

    

#### 键盘避让

 

键盘抬起后，具有滚动能力的容器组件在横竖屏切换时，才会生效键盘避让，若希望无滚动能力的容器组件也生效键盘避让，建议在组件外嵌套一层具有滚动能力的容器组件，比如[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)、[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)、[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)。

 

```
@Entry
@Component
struct KeyboardAvoid {
  placeHolderArr: string[] = ['1', '2', '3', '4', '5', '6', '7'];

  build() {
    Scroll() {
      Column() {
        ForEach(this.placeHolderArr, (placeholder: string) => {
          TextInput({ placeholder: 'TextInput ' + placeholder })
            .margin(30)
            // ···
        })
      }
    }
    .height('100%')
    .width('100%')
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/j5IYi_rrSZWkXQFfBLFwsw/zh-cn_image_0000002543213852.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=7C908526351C71A51034CA7BFB017D7D0964A1B8BB3D6B6E9C5809EA2B8353B3)

    

#### 光标避让

 

[keyBoardAvoidMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-e#keyboardavoidmode11)枚举中的OFFSET和RESIZE在键盘抬起后，不支持二次避让。如果想要支持光标位置在点击或者通过接口设置变化后发生二次避让，可以考虑使用OFFSET_WITH_CARET和RESIZE_CARET替换原有的OFFSET和RESIZE模式。

 

对于滚动容器更推荐使用RESIZE_WITH_CARET，非滚动容器应该使用OFFSET_WITH_CARET。

 

```
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { KeyboardAvoidMode } from '@kit.ArkUI';

```

 

```
// Used in UIAbility
onWindowStageCreate(windowStage: window.WindowStage): void {
  // Main window is created, set main page for this ability
  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

  windowStage.loadContent('pages/Index', (err, data) => {
    let keyboardAvoidMode = windowStage.getMainWindowSync().getUIContext().getKeyboardAvoidMode();
    windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.OFFSET_WITH_CARET);
    if (err.code) {
      hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
  });
}

```

 

```
@Entry
@Component
struct CursorAvoid {
  @State caretPosition: number = 600;
  areaController: TextAreaController = new TextAreaController();
  text = 'Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot,' +
    ' or someone we hardly know. As a result, what we do remember is anything that makes others happy, ' +
    'anything that makes ourselves unhappy,' +
    ' totally forgetting that there is something happy in our own life.\
    So the best way to destroy happiness is to look at something and focus on even the smallest flaw. ' +
    'It is the smallest flaw that would make us complain. And it is the complaint that leads to us becoming unhappy.\
    If one chooses to be happy, he will be blessed; if he chooses to be unhappy, he will be cursed. ' +
    'Happiness is just what you think will make you happy.' +
    'Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot, ' +
    'or someone we hardly know. As a result, what we do remember is anything that makes others happy, ' +
    'anything that makes ourselves unhappy, totally forgetting that there is something happy in our own life.\
  ';

  build() {
    Scroll() {
      Column() {
        Row() {
          Button('CaretPosition++: ' + this.caretPosition).onClick(() => {
            this.caretPosition += 1;
          }).fontSize(10)
          Button('CaretPosition--: ' + this.caretPosition).onClick(() => {
            this.caretPosition -= 1;
          }).fontSize(10)
          Button('SetCaretPosition: ').onClick(() => {
            this.areaController.caretPosition(this.caretPosition);
          }).fontSize(10)
        }

        TextArea({ text: this.text, controller: this.areaController })
          .width('100%')
          .fontSize('20fp')
      }
    }.width('100%').height('100%')
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/opnrfTgTQpWyebwGZph0dQ/zh-cn_image_0000002573853765.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=F54B91DB3665C03E1A04C48155192CA56998E9E26C5C6B1C94B2BB3F1E257473)

    

#### 常见问题

    

#### [h2]如何设置TextArea的文本最少展示行数并自适应高度

 

**问题现象**

 

设置TextArea的初始高度来控制最少文本展示行数，当输入文本超过初始高度时，TextArea的高度自适应。

 

**解决措施**

 

设置[minLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#minlines20)（从API version 20开始），或者设置height为"auto"，并使用[constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#constraintsize)自行计算高度。

 

```
import { MeasureUtils } from '@kit.ArkUI';

@Entry
@Component
struct TextExample {
  private textAreaPadding = 12;
  private setMaxLines = 3;
  private resourceManager = this.getUIContext().getHostContext()?.resourceManager;
  // 请在resources\base\element\string.json文件中配置name为'NormalQuestion_change'，value为非空字符串的资源
  private changeText = this.resourceManager?.getStringByNameSync('NormalQuestion_change') as string;
  @State fullText: string = this.changeText;
  @State originText: string = this.changeText;
  @State uiContext: UIContext = this.getUIContext();
  @State uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
  textSize: SizeOptions = this.uiContextMeasure.measureTextSize({
    textContent: this.originText,
    fontSize: 18
  });

  build() {
    Column() {
      TextArea({ text: 'minLines: ' + this.fullText })
        .fontSize(18)
        .width(300)
        .minLines(3)

      Blank(50)

      TextArea({ text: 'constraintSize: ' + this.fullText })
        .fontSize(18)
        .padding({ top: this.textAreaPadding, bottom: this.textAreaPadding })
        .width(300)
        .height('auto')
        .constraintSize({
          // 结合padding计算，设置至少显示this.setMaxLines行文本
          // 若涉及适老化字号缩放，需要监听并调整高度
          minHeight: this.textAreaPadding * 2 +
            this.setMaxLines * this.getUIContext().px2vp(Number(this.textSize.height))
        })

      Blank(50)
      // 请将$r('app.string.NormalQuestion_AddInput')替换为实际资源文件，在本示例中该资源文件的value值为"增加输入"
      Button($r('app.string.NormalQuestion_AddInput'))
        .onClick(() => {
          this.fullText += this.changeText;
        })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .padding({ top: 30 })
  }
}

```

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Fnb1a0jETRmrBY_YwtNdfw/zh-cn_image_0000002573973743.gif?HW-CC-KV=V1&HW-CC-Date=20260420T193727Z&HW-CC-Expire=86400&HW-CC-Sign=97879ED4F015FAE387A5506E100F75DC20D94A062396DC2A49FF271668867557)
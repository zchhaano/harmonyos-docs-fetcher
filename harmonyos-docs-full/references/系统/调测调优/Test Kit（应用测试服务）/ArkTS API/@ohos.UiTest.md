# @ohos.UiTest

  

UiTest提供模拟UI操作的能力，供开发者在测试场景使用，主要支持如点击、双击、长按、滑动等UI操作能力。

 

该模块提供以下功能：

 

- [On9+](#on9)：提供控件特征描述能力，用于控件筛选匹配查找。
- [Component9+](#component9)：代表UI界面上的指定控件，提供控件属性获取，控件点击，滑动查找，文本注入等能力。
- [Driver9+](#driver9)：入口类，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。
- [UiWindow9+](#uiwindow9)：入口类，提供窗口属性获取，窗口拖动、调整窗口大小等能力。
- [By(deprecated)](#bydeprecated)：提供控件特征描述能力，用于控件筛选匹配查找。从API version 8开始支持，从API version 9开始废弃，建议使用[On9+](#on9)替代。
- [UiComponent(deprecated)](#uicomponentdeprecated)：代表UI界面上的指定控件，提供控件属性获取，控件点击，滑动查找，文本注入等能力。从API version 8开始支持，从API version 9开始废弃，建议使用[Component9+](#component9)替代。
- [UiDriver(deprecated)](#uidriverdeprecated)：入口类，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。从API version 8开始支持，从API version 9开始废弃，建议使用[Driver9+](#driver9)替代。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/KY_NR0qKSeC1Dw9z0QiHxQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=E9D586961E2986B2DF9ED96AD3CD3FF5AEE929D5D404FDF1EC244754B11FDB61)   

- 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本模块接口在[自动化测试脚本](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uitest-guidelines#使用arkts接口进行ui测试)中使用。
- 本模块接口不支持并发调用。

     

#### 导入模块

 

```
import { Component, Driver, UiWindow, ON, MatchPattern, DisplayRotation, ResizeDirection, WindowMode, PointerMatrix, UiDirection, MouseButton, UIElementInfo, UIEventObserver, UiComponent, UiDriver, BY } from '@kit.TestKit';

```

    

#### MatchPattern

 

控件属性支持的匹配模式。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EQUALS | 0 | 等于给定值。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| CONTAINS | 1 | 包含给定值。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| STARTS_WITH | 2 | 以给定值开始。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| ENDS_WITH | 3 | 以给定值结束。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| REG_EXP 18+ | 4 | 正则表达式匹配。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| REG_EXP_ICASE 18+ | 5 | 正则表达式匹配，忽略大小写。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |

     

#### ResizeDirection 9+

 

窗口调整大小的方向。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 0 | 左方。 |
| RIGHT | 1 | 右方。 |
| UP | 2 | 上方。 |
| DOWN | 3 | 下方。 |
| LEFT_UP | 4 | 左上方。 |
| LEFT_DOWN | 5 | 左下方。 |
| RIGHT_UP | 6 | 右上方。 |
| RIGHT_DOWN | 7 | 右下方。 |

     

#### Point 9+

 

坐标点信息。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 坐标点的横坐标，取值大于0的整数。 说明： 从API version 20开始，该属性不再为只读属性。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| y | number | 否 | 否 | 坐标点的纵坐标，取值大于0的整数。 说明： 从API version 20开始，该属性不再为只读属性。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| displayId 20+ | number | 否 | 是 | 坐标点所属的屏幕ID，取值范围：大于等于0的整数。默认值为设备默认屏幕ID。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

     

#### Rect 9+

 

控件的边框信息。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 控件边框的左上角的X坐标，取值大于0的整数。 说明： 从API version 20开始，该属性不再为只读属性。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| top | number | 否 | 否 | 控件边框的左上角的Y坐标，取值大于0的整数。 说明： 从API version 20开始，该属性不再为只读属性。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| right | number | 否 | 否 | 控件边框的右下角的X坐标，取值大于0的整数。 说明： 从API version 20开始，该属性不再为只读属性。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| bottom | number | 否 | 否 | 控件边框的右下角的Y坐标，取值大于0的整数。 说明： 从API version 20开始，该属性不再为只读属性。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| displayId 20+ | number | 否 | 是 | 控件边框所属的屏幕ID，取值大于或等于0的整数。默认值为设备默认屏幕ID。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

     

#### WindowMode 9+

 

窗口的窗口模式。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FULLSCREEN | 0 | 全屏模式。 |
| PRIMARY | 1 | 主窗口。 |
| SECONDARY | 2 | 第二窗口。 |
| FLOATING | 3 | 浮动窗口。 |

     

#### DisplayRotation 9+

 

设备显示器的显示方向。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ROTATION_0 | 0 | 设备显示器不旋转，初始形态垂直显示。 |
| ROTATION_90 | 1 | 设备显示器顺时针旋转90°，水平显示。 |
| ROTATION_180 | 2 | 设备显示器顺时针旋转180°，逆向垂直显示。 |
| ROTATION_270 | 3 | 设备显示器顺时针旋转270°，逆向水平显示。 |

     

#### WindowFilter 9+

 

窗口的标志属性信息。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 是 | 窗口归属应用的包名，默认值为空。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| title | string | 否 | 是 | 窗口的标题信息，默认值为空。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| focused | boolean | 否 | 是 | 窗口是否处于获焦状态，true：获焦状态，false：未获焦状态，默认值为false。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| actived(deprecated) | boolean | 否 | 是 | 窗口是否正与用户进行交互，true：交互状态，false：未交互状态，默认值为false。 从API version 11开始废弃，建议使用active替代。 |
| active 11+ | boolean | 否 | 是 | 窗口是否正与用户进行交互，true：交互状态，false：未交互状态，默认值为false。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| displayId 20+ | number | 否 | 是 | 窗口所属的屏幕ID。取值大于或等于0的整数。默认值为设备默认屏ID。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

     

#### UiDirection 10+

 

进行抛滑等UI操作时的方向。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 0 | 向左。 |
| RIGHT | 1 | 向右。 |
| UP | 2 | 向上。 |
| DOWN | 3 | 向下。 |

     

#### MouseButton 10+

 

模拟注入的鼠标按钮。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MOUSE_BUTTON_LEFT | 0 | 鼠标左键。 |
| MOUSE_BUTTON_RIGHT | 1 | 鼠标右键。 |
| MOUSE_BUTTON_MIDDLE | 2 | 鼠标中间键。 |

     

#### WindowChangeType 22+

 

支持监听的窗口变化事件类型。

 

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WINDOW_UNDEFINED | 0 | 非窗口变化事件。 说明： 该枚举值仅支持作为返回值，如果作为接口入参会抛出异常。 |
| WINDOW_ADDED | 1 | 窗口出现事件。 |
| WINDOW_REMOVED | 2 | 窗口消失事件。 |
| WINDOW_BOUNDS_CHANGED | 3 | 窗口边框变化事件。 |

     

#### ComponentEventType 22+

 

支持监听的控件操作事件类型。

 

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COMPONENT_UNDEFINED | 0 | 非控件操作事件。 说明： 该枚举值仅支持作为返回值，如果作为接口入参会抛出异常。 |
| COMPONENT_CLICKED | 1 | 控件被点击事件。 |
| COMPONENT_LONG_CLICKED | 2 | 控件被长按事件。 |
| COMPONENT_SCROLL_START | 3 | 控件滚动开始事件。 |
| COMPONENT_SCROLL_END | 4 | 控件滚动结束事件。 |
| COMPONENT_TEXT_CHANGED | 5 | 输入框控件 文本变化事件。 |

     

#### WindowChangeOptions 22+

 

窗口变化事件监听的扩展配置，用于指定监听过程配置及事件筛选条件。

 

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number | 否 | 是 | 监听超时时间，默认值为10000，单位：ms。 |
| bundleName | string | 否 | 是 | 监听窗口对应包名，缺省时默认监听所有窗口。 |

     

#### ComponentEventOptions 22+

 

控件操作事件监听的扩展配置，用于指定监听过程配置及事件筛选条件。

 

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number | 否 | 是 | 监听超时时间，默认值为10000，单位：ms。 |
| on | On | 否 | 是 | 监听目标控件的属性要求，默认监听所有控件。 说明： 仅支持监听指定属性要求的控件，不支持监听指定On.isBefore、On.isAfter、On.within等相对位置的控件。 |

     

#### UIElementInfo 10+

 

UI事件的相关信息。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 是 | 否 | 应用包名。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| type | string | 是 | 否 | 控件/窗口类型。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| text | string | 是 | 否 | 控件/窗口的文本信息。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| windowChangeType 22+ | WindowChangeType | 是 | 是 | 窗口变化事件类型，若非窗口变化事件返回WindowChangeType.WINDOW_UNDEFINED。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| componentEventType 22+ | ComponentEventType | 是 | 是 | 控件操作事件类型，若非控件操作事件返回ComponentEventType.COMPONENT_UNDEFINED。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| windowId 22+ | number | 是 | 是 | 控件所属窗口id。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| componentId 22+ | string | 是 | 是 | 控件id，若非控件操作事件返回空字符串。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| componentRect 22+ | Rect | 是 | 是 | 控件边框信息，若非控件操作事件则返回属性值均为0的Rect对象。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |

     

#### TouchPadSwipeOptions 18+

 

触摸板多指滑动手势选项相关信息。

 

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| stay | boolean | 否 | 是 | 触摸板多指滑动结束是否停留1s后再抬起，默认为false（不停留1s），true：停留，false：不停留。 |
| speed | number | 否 | 是 | 滑动速率，取值范围为200-40000的整数，默认值为2000，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值2000。为负数时抛出参数错误的错误码。 |

     

#### InputTextMode 20+

 

输入文本的方式。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

  

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| paste | boolean | 否 | 是 | 输入文本时是否指定以复制粘贴方式输入。true：指定以复制粘贴方式输入。false：指定以逐字键入方式输入。默认为false。 说明： 当输入文本中包含中文、特殊字符或文本长度超过200字符时，无论该参数取值为何，均以复制粘贴方式输入。 |
| addition | boolean | 否 | 是 | 输入文本时是否以追加的方式进行输入。true：以追加方式输入。false：不以追加方式输入。默认为false。 |

     

#### On 9+

 

UiTest框架从API version 9开始，通过On类提供了丰富的控件特征描述API，用于进行控件筛选来匹配/查找出目标控件。

 

On提供的API能力具有以下几个特点:

 

1、支持单属性匹配和多属性组合匹配，例如同时指定目标控件text和id。

 

2、控件属性支持多种匹配模式。

 

3、支持控件绝对定位，相对定位，可通过[ON.isBefore](#isbefore9)和[ON.isAfter](#isafter9)等API限定邻近控件特征进行辅助定位。

 

On类提供的所有API均为同步接口，建议使用者通过静态构造器ON来链式创建On对象。

 

```
// xxx.test.ets
import { ON } from '@kit.TestKit';

ON.text('123').type('Button');

```

    

#### [h2]text 9+

 

text(txt: string, pattern?: MatchPattern): On

 

指定目标控件文本属性，支持多种匹配模式，返回On对象自身。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/7HhOR1ejQbGUK6AnqwnOng/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=8ED975E6798AF661F44F88D9F8512DC372CA1BE570D49288F49A281BD4D01542)   

如果控件的无障碍属性[accessibilityLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilitylevel)设置为'no'或'no-hide-descendants'，无法使用本接口指定目标控件的文本属性用于查找控件，可以使用[On.originalText()](#originaltext20)接口实现。

   

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| txt | string | 是 | 指定控件文本，用于匹配目标控件文本。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |
| pattern | MatchPattern | 否 | 指定的文本匹配模式，默认为 EQUALS 。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件文本属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.text('123'); // 使用静态构造器ON创建On对象，指定目标控件的text属性。

```

    

#### [h2]id 9+

 

id(id: string): On

 

指定目标控件id属性，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 指定控件的id值。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件id属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.id('123'); // 使用静态构造器ON创建On对象，指定目标控件的id属性。

```

    

#### [h2]id 18+

 

id(id: string, pattern: MatchPattern): On

 

指定目标控件id属性和匹配模式，返回On对象自身。

 

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 指定控件的id值。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |
| pattern | MatchPattern | 是 | 指定的文本匹配模式。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件id属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { MatchPattern, On, ON } from '@kit.TestKit';

let on: On = ON.id('id', MatchPattern.REG_EXP_ICASE); // 忽略大小写匹配控件的id属性值

```

    

#### [h2]type 9+

 

type(tp: string): On

 

指定目标控件的控件类型属性，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tp | string | 是 | 指定控件类型。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件的控件类型属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.type('Button'); // 使用静态构造器ON创建On对象，指定目标控件的控件类型属性。

```

    

#### [h2]type 18+

 

type(tp: string, pattern: MatchPattern): On

 

指定目标控件的控件类型属性和匹配模式，返回On对象自身。

 

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tp | string | 是 | 指定控件类型。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |
| pattern | MatchPattern | 是 | 指定的文本匹配模式。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件的控件类型属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON, MatchPattern } from '@kit.TestKit';

let on: On = ON.type('Button', MatchPattern.EQUALS); // 使用静态构造器ON创建On对象，指定目标控件的控件类型属性。

```

    

#### [h2]clickable 9+

 

clickable(b?: boolean): On

 

指定目标控件的可点击状态属性，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件可点击状态。true：可点击。false：不可点击。默认为true。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件的可点击状态属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.clickable(true); // 使用静态构造器ON创建On对象，指定目标控件的可点击状态属性。

```

    

#### [h2]longClickable 9+

 

longClickable(b?: boolean): On

 

指定目标控件的可长按点击状态属性，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件可长按点击状态。true：可长按点击。false：不可长按点击。默认为true。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件的可长按点击状态属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.longClickable(true); // 使用静态构造器ON创建On对象，指定目标控件的可长按点击状态属性。

```

    

#### [h2]scrollable 9+

 

scrollable(b?: boolean): On

 

指定目标控件的可滑动状态属性，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 控件可滑动状态。true：可滑动。false：不可滑动。默认为true。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件的可滑动状态属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.scrollable(true); // 使用静态构造器ON创建On对象，指定目标控件的可滑动状态属性。

```

    

#### [h2]enabled 9+

 

enabled(b?: boolean): On

 

指定目标控件的使能状态属性，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件使能状态。true：使能。false：未使能。默认为true。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件的使能状态属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.enabled(true); // 使用静态构造器ON创建On对象，指定目标控件的使能状态属性。

```

    

#### [h2]focused 9+

 

focused(b?: boolean): On

 

指定目标控件的获焦状态属性，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 控件获焦状态。true：获焦。false：未获焦。默认为true。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件的获焦状态属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.focused(true); // 使用静态构造器ON创建On对象，指定目标控件的获焦状态属性。

```

    

#### [h2]selected 9+

 

selected(b?: boolean): On

 

指定目标控件的被选中状态属性，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件被选中状态。true：被选中。false：未被选中。默认为true。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件的被选中状态属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.selected(true); // 使用静态构造器ON创建On对象，指定目标控件的被选中状态属性。

```

    

#### [h2]checked 9+

 

checked(b?: boolean): On

 

指定目标控件的被勾选状态属性，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件被勾选状态。true：被勾选。false：未被勾选。默认为true。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件的被勾选状态属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.checked(true); // 使用静态构造器ON创建On对象，指定目标控件的被勾选状态属性

```

    

#### [h2]checkable 9+

 

checkable(b?: boolean): On

 

指定目标控件能否被勾选状态属性，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件能否被勾选状态。true：能被勾选。false：不能被勾选。默认为true。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件能否被勾选状态属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. 1. Incorrect parameter types; 2. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.checkable(true); // 使用静态构造器ON创建On对象，指定目标控件的能否被勾选状态属性。

```

    

#### [h2]isBefore 9+

 

isBefore(on: On): On

 

指定目标控件位于给出的特征属性控件之前，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | On | 是 | 特征控件的属性要求。 可以借助 DevEco Testing 中UiViewer获取控件树，以判断控件间位置关系。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件位于给出的特征属性控件之前的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

// 使用静态构造器ON创建On对象，指定目标控件位于给出的特征属性控件之前。
let on: On = ON.type('Button').isBefore(ON.text('123')); // 查找text为123之前的第一个Button组件

```

    

#### [h2]isAfter 9+

 

isAfter(on: On): On

 

指定目标控件位于给出的特征属性控件之后，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | On | 是 | 特征控件的属性要求。 可以借助 DevEco Testing 中UiViewer获取控件树，以判断控件间位置关系。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件位于给出的特征属性控件之后的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

// 使用静态构造器ON创建On对象，指定目标控件位于给出的特征属性控件之后。
let on: On = ON.type('Text').isAfter(ON.text('123')); // 查找 text为123之后的第一个Text组件

```

    

#### [h2]within 10+

 

within(on: On): On

 

指定目标控件位于给出的特征属性控件之内，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | On | 是 | 特征控件的属性要求。可以借助 DevEco Testing 中UiViewer获取控件树，以判断控件间位置关系。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件位于给出的特征属性控件内的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

// 使用静态构造器ON创建On对象，指定目标控件位于给出的特征属性控件之内。
let on: On = ON.text('java').within(ON.type('Scroll')); // 查找Scroller里面的text为java的子组件

```

    

#### [h2]inWindow 10+

 

inWindow(bundleName: string): On

 

指定目标控件位于给出的应用窗口内，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用窗口的包名。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件位于给出的应用窗口内的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.inWindow('com.uitestScene.acts'); // 使用静态构造器ON创建On对象，指定目标控件位于给出的应用窗口内。

```

    

#### [h2]description 11+

 

description(val: string, pattern?: MatchPattern): On

 

指定目标控件的描述属性，支持多种匹配模式，返回On对象自身。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | string | 是 | 控件的描述属性。 可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |
| pattern | MatchPattern | 否 | 指定的文本匹配模式，默认为 EQUALS 。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件description属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.description('123'); // 使用静态构造器ON创建On对象，指定目标控件的description属性。

```

    

#### [h2]hint 18+

 

hint(val: string, pattern?: MatchPattern): On

 

获取指定提示文本的控件对象，返回On对象自身。

 

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | string | 是 | 指定控件提示文本。 可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |
| pattern | MatchPattern | 否 | 指定的文本匹配模式，默认为 EQUALS 。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定提示文本控件的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { MatchPattern, On, ON } from '@kit.TestKit';

let on: On = ON.hint('welcome', MatchPattern.EQUALS); // 使用静态构造器ON创建On对象，指定目标控件的提示文本属性。

```

    

#### [h2]belongingDisplay 20+

 

belongingDisplay(displayId: number): On

 

获取指定屏幕内的控件对象，返回On对象自身。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 指定控件所属屏幕ID，取值范围：大于等于0的整数。 说明： 传入displayId不存在时，将抛出17000007异常。可通过 getAllDisplays 获取当前所有的display对象，并由display对象获取对应的屏幕ID。可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定控件所属屏幕的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.belongingDisplay(0); // 使用静态构造器ON创建On对象，指定目标控件所属屏幕ID

```

    

#### [h2]originalText 20+

 

originalText(text: string, pattern?: MatchPattern): On

 

指定控件的文本内容和文本匹配模式，返回On对象自身。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/P1iJltktRL6lzzGmxNZKZA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=2761E72B8B7F5F292B8C957A95A36447B489F43875B401E1E5EC435D3CB20090)   

如果控件的无障碍属性[accessibilityLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilitylevel)设置为'no'或'no-hide-descendants'，可以使用本接口指定目标控件的文本属性用于查找控件，使用[On.text()](#text9)接口不生效。

   

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 指定控件文本，用于匹配目标控件文本。 可以借助 DevEco Testing 中UiViewer获取控件节点属性。 |
| pattern | MatchPattern | 否 | 指定的文本匹配模式，默认为 EQUALS 。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| On | 返回指定目标控件文本属性的On对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.originalText('123'); // 使用静态构造器ON创建On对象，指定目标控件的originalText属性

```

    

#### Component 9+

 

UiTest框架在API9中，Component类代表了UI界面上的一个控件，提供控件属性获取，控件点击，滑动查找，文本注入等API。

 

该类提供的所有方法都使用Promise方式作为异步方法，需使用await调用。

    

#### [h2]click 9+

 

click(): Promise<void>

 

控件对象进行点击操作。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, ON, Component } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  await button.click();
}

```

    

#### [h2]doubleClick 9+

 

doubleClick(): Promise<void>

 

控件对象进行双击操作。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  await button.doubleClick();
}

```

    

#### [h2]longClick 9+

 

longClick(): Promise<void>

 

控件对象进行长按操作。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  await button.longClick();
}

```

    

#### [h2]getId 9+

 

getId(): Promise<string>

 

获取控件对象的id值。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的id值。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let id = await button.getId();
}

```

    

#### [h2]getText 9+

 

getText(): Promise<string>

 

获取控件对象的文本信息。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/z7JADoOPSLatVEXYqIFoxQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=26CD105EB00406D337BC8F76079350187B77E8804ECCAD52AAB11267D7113B7F)   

如果控件的无障碍属性[accessibilityLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilitylevel)设置为'no'或'no-hide-descendants'，无法使用本接口获取控件的文本信息，可以使用[Component.getOriginalText()](#getoriginaltext20)获取控件的文本信息。

   

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的文本信息。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let text = await button.getText();
}

```

    

#### [h2]getType 9+

 

getType(): Promise<string>

 

获取控件对象的控件类型。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的类型。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let type = await button.getType();
}

```

    

#### [h2]getBounds 9+

 

getBounds(): Promise<Rect>

 

获取控件对象的边框信息。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< Rect > | Promise对象，返回控件对象的边框信息。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let rect = await button.getBounds();
}

```

    

#### [h2]getBoundsCenter 9+

 

getBoundsCenter(): Promise<Point>

 

获取控件对象所占区域的中心点信息。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< Point > | Promise对象，返回控件对象所占区域的中心点信息。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let point = await button.getBoundsCenter();
}

```

    

#### [h2]isClickable 9+

 

isClickable(): Promise<boolean>

 

获取控件对象可点击属性。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象是否可点击。true：可点击。false：不可点击。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isClickable()) {
    console.info('This button can be Clicked');
  } else {
    console.info('This button can not be Clicked');
  }
}

```

    

#### [h2]isLongClickable 9+

 

isLongClickable(): Promise<boolean>

 

获取控件对象可长按点击属性。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象是否可长按点击。true：可长按点击。false：不可长按点击。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isLongClickable()) {
    console.info('This button can longClick');
  } else {
    console.info('This button can not longClick');
  }
}

```

    

#### [h2]isChecked 9+

 

isChecked(): Promise<boolean>

 

获取控件对象被勾选状态。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象被勾选状态。true：被勾选。false：未被勾选。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let checkBox: Component = await driver.findComponent(ON.type('Checkbox'));
  if (await checkBox.isChecked()) {
    console.info('This checkBox is checked');
  } else {
    console.info('This checkBox is not checked');
  }
}

```

    

#### [h2]isCheckable 9+

 

isCheckable(): Promise<boolean>

 

获取控件对象能否被勾选属性。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象能否可被勾选属性。true：可被勾选。false：不可被勾选。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let checkBox: Component = await driver.findComponent(ON.type('Checkbox'));
  if (await checkBox.isCheckable()) {
    console.info('This checkBox is checkable');
  } else {
    console.info('This checkBox is not checkable');
  }
}

```

    

#### [h2]isScrollable 9+

 

isScrollable(): Promise<boolean>

 

获取控件对象可滑动属性。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象是否可滑动。true：可滑动。false：不可滑动。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.scrollable(true));
  if (await scrollBar.isScrollable()) {
    console.info('This scrollBar can be operated');
  } else {
    console.info('This scrollBar can not be operated');
  }
}

```

    

#### [h2]isEnabled 9+

 

isEnabled(): Promise<boolean>

 

获取控件使能状态。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件使能状态。true：使能。false：未使能。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isEnabled()) {
    console.info('This button can be operated');
  } else {
    console.info('This button can not be operated');
  }
}

```

    

#### [h2]isFocused 9+

 

isFocused(): Promise<boolean>

 

判断控件对象获焦状态。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象获焦状态。true：获焦。false：未获焦。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isFocused()) {
    console.info('This button is focused');
  } else {
    console.info('This button is not focused');
  }
}

```

    

#### [h2]isSelected 9+

 

isSelected(): Promise<boolean>

 

获取控件对象被选中状态。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象被选中状态。true：被选中。false：未被选中。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isSelected()) {
    console.info('This button is selected');
  } else {
    console.info('This button is not selected');
  }
}

```

    

#### [h2]inputText 9+

 

inputText(text: string): Promise<void>

 

清空组件内原有文本并输入指定文本内容，仅针对可编辑的文本组件生效。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 输入的文本信息，当前支持英文、中文和特殊字符。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await text.inputText('123');
}

```

    

#### [h2]inputText 20+

 

inputText(text: string, mode: InputTextMode): Promise<void>

 

向控件中输入文本，并支持指定文本输入方式，仅针对可编辑的文本组件生效。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 输入的文本信息，当前支持英文、中文和特殊字符。 |
| mode | InputTextMode | 是 | 输入文本的方式，取值请参考 InputTextMode 。 说明： InputTextMode.addition取值为true时，在控件已有文本末尾后追加指定文本。取值为false时，指定文本将覆盖控件已有文本。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported, function can not work correctly due to limited device capabilities. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function mode_demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await text.inputText('123', { paste: true, addition: false });
}

```

    

#### [h2]clearText 9+

 

clearText(): Promise<void>

 

清除控件的文本信息，仅针对可编辑的文本组件生效。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await text.clearText();
}

```

    

#### [h2]scrollSearch 9+

 

scrollSearch(on: On): Promise<Component>

 

在控件上滑动查找目标控件（适用支持滑动的控件）。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | On | 是 | 目标控件的属性要求。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< Component > | Promise对象，返回目标控件对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  let button = await scrollBar.scrollSearch(ON.text('next page'));
}

```

    

#### [h2]scrollSearch 18+

 

scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>

 

在控件上滑动查找目标控件（适用支持滑动的控件），支持指定滑动方向和滑动起止点与组件边框的偏移量。使用Promise异步回调。

 

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | On | 是 | 目标控件的属性要求。 |
| vertical | boolean | 否 | 默认为true，表示查找方向是纵向。false表示查找方向为横向。 |
| offset | number | 否 | 滑动起点/终点到组件边框的偏移，默认80，单位：px，取值范围：大于等于0的整数。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< Component > | Promise对象，返回目标控件对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  let button = await scrollBar.scrollSearch(ON.text('next page'));
}

```

    

#### [h2]scrollToTop 9+

 

scrollToTop(speed?: number): Promise<void>

 

在控件上滑动到顶部（适用支持滑动的控件）。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  await scrollBar.scrollToTop();
}

```

    

#### [h2]scrollToBottom 9+

 

scrollToBottom(speed?: number): Promise<void>

 

在控件上滑动到底部（适用支持滑动的控件）。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  await scrollBar.scrollToBottom();
}

```

    

#### [h2]dragTo 9+

 

dragTo(target: Component): Promise<void>

 

将控件拖拽至目标控件处。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | Component | 是 | 目标控件。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await button.dragTo(text);
}

```

    

#### [h2]pinchOut 9+

 

pinchOut(scale: number): Promise<void>

 

将控件按指定的比例进行捏合放大。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | 是 | 指定放大的比例。取值范围大于1。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let image: Component = await driver.findComponent(ON.type('Image'));
  await image.pinchOut(1.5);
}

```

    

#### [h2]pinchIn 9+

 

pinchIn(scale: number): Promise<void>

 

将控件按指定的比例进行捏合缩小。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | 是 | 指定缩小的比例。取值范围为0~1。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let image: Component = await driver.findComponent(ON.type('Image'));
  await image.pinchIn(0.5);
}

```

    

#### [h2]getDescription 11+

 

getDescription(): Promise<string>

 

获取控件对象的描述信息。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的描述信息。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let description = await button.getDescription();
}

```

    

#### [h2]getHint 18+

 

getHint(): Promise<string>

 

获取控件对象的提示文本。使用Promise异步回调。

 

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的提示文本。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('TextInput'));
  let hints = await button.getHint();
}

```

    

#### [h2]getDisplayId 20+

 

getDisplayId(): Promise<number>

 

获取控件对象所属的屏幕ID。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回控件所属的屏幕ID。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('TextInput'));
  let displayId = await button.getDisplayId();
}

```

    

#### [h2]getOriginalText 20+

 

getOriginalText(): Promise<string>

 

获取控件对象的文本信息。使用Promise异步回调。如果控件的无障碍属性[accessibilityLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilitylevel)设置为'no'或'no-hide-descendants'，可以使用本接口获取控件的文本信息，无法使用[Component.getText()](#gettext9)获取控件的文本信息。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的文本信息。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let text = await button.getOriginalText();
}

```

    

#### Driver 9+

 

Driver类为uitest测试框架的总入口，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。

 

该类提供的方法除Driver.create()以外的所有方法都使用Promise方式作为异步方法，需使用await方式调用。

    

#### [h2]create 9+

 

static create(): Driver

 

静态方法，构造一个Driver对象，并返回该对象。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Driver | 返回构造的Driver对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000001 | Initialization failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
}

```

    

#### [h2]delayMs 9+

 

delayMs(duration: number): Promise<void>

 

在给定的时间内延时。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| duration | number | 是 | 给定的时间，单位：ms，取值范围：大于等于0的整数。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.delayMs(1000);
}

```

    

#### [h2]findComponent 9+

 

findComponent(on: On): Promise<Component>

 

根据给出的目标控件属性要求查找目标控件。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | On | 是 | 目标控件的属性要求。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< Component > | Promise对象，返回控件对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.text('next page'));
}

```

    

#### [h2]findComponents 9+

 

findComponents(on: On): Promise<Array<Component>>

 

根据给出的目标控件属性要求查找出所有匹配控件，以列表保存。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | On | 是 | 目标控件的属性要求。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<Array< Component >> | Promise对象，返回控件对象的列表。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let buttonList: Array<Component> = await driver.findComponents(ON.text('next page'));
}

```

    

#### [h2]findWindow 9+

 

findWindow(filter: WindowFilter): Promise<UiWindow>

 

通过指定窗口的属性来查找目标窗口。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | WindowFilter | 是 | 目标窗口的属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< UiWindow > | Promise对象，返回目标窗口对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
}

```

    

#### [h2]waitForComponent 9+

 

waitForComponent(on: On, time: number): Promise<Component>

 

在用户给定的时间内，持续查找满足控件属性要求的目标控件。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | On | 是 | 目标控件的属性要求。 |
| time | number | 是 | 查找目标控件的持续时间。单位ms，取值范围：大于等于0的整数。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< Component > | Promise对象，返回控件对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.waitForComponent(ON.text('next page'), 500);
}

```

    

#### [h2]assertComponentExist 9+

 

assertComponentExist(on: On): Promise<void>

 

断言API，用于断言当前界面是否存在满足给出的目标属性的控件。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | On | 是 | 目标控件的属性要求。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000003 | Assertion failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.assertComponentExist(ON.text('next page'));
}

```

    

#### [h2]pressBack 9+

 

pressBack(): Promise<void>

 

进行点击BACK键的操作。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressBack();
}

```

    

#### [h2]pressBack 20+

 

pressBack(displayId: number): Promise<void>

 

对指定屏幕进行点击BACK键的操作。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 指定的屏幕ID，取值范围：大于等于0的整数。 说明： 传入displayId不存在时，将抛出17000007异常。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressBack(0);
}

```

    

#### [h2]triggerKey 9+

 

triggerKey(keyCode: number): Promise<void>

 

传入key值实现模拟点击对应按键的效果。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyCode | number | 是 | 指定的key值，取值范围：大于等于0的整数。取值范围： KeyCode键码值 。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK); // 返回键
}

```

    

#### [h2]triggerKey 20+

 

triggerKey(keyCode: number, displayId: number): Promise<void>

 

在指定屏幕，传入key值实现模拟点击对应按键的效果。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyCode | number | 是 | 指定的key值，取值范围：大于等于0的整数。取值范围： KeyCode键码值 。 |
| displayId | number | 是 | 指定的屏幕ID，取值范围：大于等于0的整数。 说明： 传入displayId不存在时，将抛出17000007异常。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK, 0); // 返回键
}

```

    

#### [h2]triggerCombineKeys 9+

 

triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>

 

通过给定的key值，找到对应组合键并点击。使用Promise异步回调。例如，Key值为(2072, 2019)时，找到key值对应的组合键并点击，如Ctrl+c。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key0 | number | 是 | 指定的第一个key值，取值大于等于0的整数，取值范围： KeyCode键码值 。 |
| key1 | number | 是 | 指定的第二个key值，取值大于等于0的整数，取值范围： KeyCode键码值 。 |
| key2 | number | 否 | 指定的第三个key值，取值范围：大于等于0的整数。取值范围： KeyCode键码值 ，默认值为0。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerCombineKeys(2072, 2047, 2035);
}

```

    

#### [h2]triggerCombineKeys 20+

 

triggerCombineKeys(key0: number, key1: number, key2?: number, displayId?: number): Promise<void>

 

通过给定的key值，找到对应组合键，并在指定屏幕下进行点击。使用Promise异步回调。例如，Key值为(2072, 2019)时，找到key值对应的组合键并点击，如Ctrl+c。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key0 | number | 是 | 指定的第一个key值，取值大于等于0的整数，取值范围： KeyCode键码值 。 |
| key1 | number | 是 | 指定的第二个key值，取值大于等于0的整数，取值范围： KeyCode键码值 。 |
| key2 | number | 否 | 指定的第三个key值，取值范围：大于等于0的整数，取值范围： KeyCode键码值 ，默认值为0。 |
| displayId | number | 否 | 指定的屏幕ID，取值范围：大于等于0的整数，默认值为设备默认屏幕ID。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerCombineKeys(2072, 2047, 2035, 0);
}

```

    

#### [h2]click 9+

 

click(x: number, y: number): Promise<void>

 

在目标坐标点单击。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.click(100, 100);
}

```

    

#### [h2]clickAt 20+

 

clickAt(point: Point): Promise<void>

 

在目标坐标点进行单击。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | Point | 是 | 以Point对象的形式传入目标点信息。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.clickAt({ x: 100, y: 100, displayId: 0 });
}

```

    

#### [h2]doubleClick 9+

 

doubleClick(x: number, y: number): Promise<void>

 

在目标坐标点双击。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.doubleClick(100, 100);
}

```

    

#### [h2]doubleClickAt 20+

 

doubleClickAt(point: Point): Promise<void>

 

对目标坐标进行双击。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | Point | 是 | 以Point对象的形式传入目标点信息。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.doubleClickAt({ x: 100, y: 100, displayId: 0 });
}

```

    

#### [h2]longClick 9+

 

longClick(x: number, y: number): Promise<void>

 

在目标坐标点长按。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.longClick(100, 100);
}

```

    

#### [h2]longClickAt 20+

 

longClickAt(point: Point, duration?: number): Promise<void>

 

长按目标坐标点，支持指定长按时长。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | Point | 是 | 以Point对象的形式传入目标点信息。 |
| duration | number | 否 | 长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.longClickAt({ x: 100, y: 100, displayId: 0 }, 1500);
}

```

    

#### [h2]swipe 9+

 

swipe(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>

 

从起始坐标点滑向目的坐标点。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startx | number | 是 | 以number的形式传入起始点的横坐标信息，取值范围：大于等于0的整数。 |
| starty | number | 是 | 以number的形式传入起始点的纵坐标信息，取值范围：大于等于0的整数。 |
| endx | number | 是 | 以number的形式传入目的点的横坐标信息，取值范围：大于等于0的整数。 |
| endy | number | 是 | 以number的形式传入目的点的纵坐标信息，取值范围：大于等于0的整数。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.swipe(100, 100, 200, 200, 600);
}

```

    

#### [h2]swipeBetween 20+

 

swipeBetween(from: Point, to: Point, speed?: number): Promise<void>

 

从起始坐标点滑向目标坐标点。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | Point | 是 | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | Point | 是 | 以Point对象的形式传入终止点的坐标信息和所属屏幕ID。 说明： 应与起始点属于同一个屏幕，否则将抛出17000007异常。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.swipeBetween({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, 800);
}

```

    

#### [h2]drag 9+

 

drag(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>

 

从起始坐标点拖拽至目的坐标点。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startx | number | 是 | 以number的形式传入起始点的横坐标信息，取值范围：大于等于0的整数。 |
| starty | number | 是 | 以number的形式传入起始点的纵坐标信息，取值范围：大于等于0的整数。 |
| endx | number | 是 | 以number的形式传入目的点的横坐标信息，取值范围：大于等于0的整数。 |
| endy | number | 是 | 以number的形式传入目的点的纵坐标信息，取值范围：大于等于0的整数。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.drag(100, 100, 200, 200, 600);
}

```

    

#### [h2]dragBetween 20+

 

dragBetween(from: Point, to: Point, speed?: number, duration?: number): Promise<void>

 

从起始坐标点拖拽至目标坐标点，支持指定拖拽速度和拖拽前长按时间。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | Point | 是 | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | Point | 是 | 以Point对象的形式传入终止点的坐标信息和所属屏幕ID。 说明： 应与起始点属于同一个屏幕，否则将抛出17000007异常。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |
| duration | number | 否 | 拖拽前长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.dragBetween({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, 800, 1500);
}

```

    

#### [h2]screenCap 9+

 

screenCap(savePath: string): Promise<boolean>

 

捕获当前屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| savePath | string | 是 | 文件保存路径。路径需为当前应用的 沙箱路径 。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回截图操作是否成功完成。true：完成，false：未完成。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png');
}

```

    

#### [h2]screenCap 20+

 

screenCap(savePath: string, displayId: number): Promise<boolean>

 

捕获指定屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| savePath | string | 是 | 文件保存路径。路径需为当前应用的 沙箱路径 。 |
| displayId | number | 是 | 指定设备屏幕ID。取值范围：大于等于0的整数。 说明： 传入displayId不存在时，将抛出17000007异常。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回截图操作是否成功完成。true：完成。false：未完成。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png', 0);
}

```

    

#### [h2]setDisplayRotation 9+

 

setDisplayRotation(rotation: DisplayRotation): Promise<void>

 

将当前场景的显示方向设置为指定的显示方向。使用Promise异步回调。适用于可旋转的应用场景。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotation | DisplayRotation | 是 | 设备的显示方向。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, DisplayRotation } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.setDisplayRotation(DisplayRotation.ROTATION_180);
}

```

    

#### [h2]getDisplayRotation 9+

 

getDisplayRotation(): Promise<DisplayRotation>

 

获取当前设备的屏幕显示方向。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< DisplayRotation > | Promise对象，返回当前设备的显示方向。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |

  

**示例：**

 

```
// xxx.test.ets
import { DisplayRotation, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let rotation: DisplayRotation = await driver.getDisplayRotation();
}

```

    

#### [h2]getDisplayRotation 20+

 

getDisplayRotation(displayId: number): Promise<DisplayRotation>

 

获取当前设备指定屏幕的显示方向。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 指定设备屏幕ID。取值范围：大于等于0的整数。 说明： 传入displayId不存在时，将抛出17000007异常。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< DisplayRotation > | Promise对象，返回指定屏幕的显示方向。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { DisplayRotation, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let rotation: DisplayRotation = await driver.getDisplayRotation(0);
}

```

    

#### [h2]setDisplayRotationEnabled 9+

 

setDisplayRotationEnabled(enabled: boolean): Promise<void>

 

启用/禁用设备旋转屏幕的功能。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 能否旋转屏幕的标识。true：可以旋转。false：不可以旋转。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.setDisplayRotationEnabled(false);
}

```

    

#### [h2]getDisplaySize 9+

 

getDisplaySize(): Promise<Point>

 

获取当前设备的屏幕大小。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< Point > | Promise对象，返回Point对象，当前设备屏幕的大小为Point.x * Point.y。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let size = await driver.getDisplaySize();
}

```

    

#### [h2]getDisplaySize 20+

 

getDisplaySize(displayId: number): Promise<Point>

 

获取当前设备指定屏幕的大小。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 指定设备屏幕ID。取值范围：大于等于0的整数。 说明： 传入displayId不存在时，将抛出17000007异常。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< Point > | Promise对象，返回Point对象，当前设备指定屏幕的大小为Point.x * Point.y。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let size = await driver.getDisplaySize(0);
}

```

    

#### [h2]getDisplayDensity 9+

 

getDisplayDensity(): Promise<Point>

 

获取当前设备屏幕的分辨率。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< Point > | Promise对象，返回Point对象，当前设备屏幕的分辨率为Point.x*Point.y。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let density = await driver.getDisplayDensity();
}

```

    

#### [h2]getDisplayDensity 20+

 

getDisplayDensity(displayId: number): Promise<Point>

 

获取当前设备指定屏幕的分辨率。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 指定设备屏幕ID。取值范围：大于等于0的整数。 说明： 传入displayId不存在时，将抛出17000007异常。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< Point > | Promise对象，返回Point对象，当前设备指定屏幕的分辨率为Point.x*Point.y。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let density = await driver.getDisplayDensity(0);
}

```

    

#### [h2]wakeUpDisplay 9+

 

wakeUpDisplay(): Promise<void>

 

唤醒当前设备即设备亮屏。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.wakeUpDisplay();
}

```

    

#### [h2]pressHome 9+

 

pressHome(): Promise<void>

 

设备注入返回桌面操作。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressHome();
}

```

    

#### [h2]pressHome 20+

 

pressHome(displayId: number): Promise<void>

 

设备指定屏幕上注入返回桌面操作。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 指定设备屏幕ID。取值范围：大于等于0的整数。 说明： 传入displayId不存在时，将抛出17000007异常。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressHome(0);
}

```

    

#### [h2]waitForIdle 9+

 

waitForIdle(idleTime: number, timeout: number): Promise<boolean>

 

判断当前界面的所有控件是否已经空闲。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| idleTime | number | 是 | 空闲时间的阈值。在这个时间段控件不发生变化，视为该控件空闲，单位：毫秒，取值范围：大于等于0的整数。 |
| timeout | number | 是 | 等待空闲的最大时间，单位：毫秒，取值范围：大于等于0的整数。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回当前界面的所有控件是否已经空闲。true：已经空闲，false：不空闲。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let idled: boolean = await driver.waitForIdle(4000, 5000);
}

```

    

#### [h2]fling 9+

 

fling(from: Point, to: Point, stepLen: number, speed: number): Promise<void>

 

模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | Point | 是 | 手指接触屏幕的起始点坐标。 |
| to | Point | 是 | 手指离开屏幕时的坐标点。 |
| stepLen | number | 是 | 间隔距离，取值大于等于0的整数，单位：px。 |
| speed | number | 是 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数时设为默认值600。为负数时抛出401错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling({ x: 500, y: 480 }, { x: 450, y: 480 }, 5, 600);
}

```

    

#### [h2]injectMultiPointerAction 9+

 

injectMultiPointerAction(pointers: PointerMatrix, speed?: number): Promise<boolean>

 

向设备注入多指操作。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pointers | PointerMatrix | 是 | 滑动轨迹，包括操作手指个数和滑动坐标序列。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回操作是否成功完成。true：完成，false：未完成。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let pointers: PointerMatrix = PointerMatrix.create(2, 5);
  pointers.setPoint(0, 0, { x: 250, y: 480 });
  pointers.setPoint(0, 1, { x: 250, y: 440 });
  pointers.setPoint(0, 2, { x: 250, y: 400 });
  pointers.setPoint(0, 3, { x: 250, y: 360 });
  pointers.setPoint(0, 4, { x: 250, y: 320 });
  pointers.setPoint(1, 0, { x: 250, y: 480 });
  pointers.setPoint(1, 1, { x: 250, y: 440 });
  pointers.setPoint(1, 2, { x: 250, y: 400 });
  pointers.setPoint(1, 3, { x: 250, y: 360 });
  pointers.setPoint(1, 4, { x: 250, y: 320 });
  await driver.injectMultiPointerAction(pointers);
}

```

    

#### [h2]fling 10+

 

fling(direction: UiDirection, speed: number): Promise<void>

 

指定方向和滑动速率，模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | UiDirection | 是 | 进行抛滑的方向。 |
| speed | number | 是 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数时设为默认值600。为负数时抛出401错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling(UiDirection.DOWN, 10000);
}

```

    

#### [h2]fling 20+

 

fling(direction: UiDirection, speed: number, displayId: number): Promise<void>

 

指定方向、滑动速率和操作屏幕，模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | UiDirection | 是 | 进行抛滑的方向。 |
| speed | number | 是 | 滑动速率，取值范围为200-40000，默认值为600，单位：px/s。为不在范围内的非负数时设为默认值600。为负数时抛出401错误码。 |
| displayId | number | 是 | 指定设备屏幕ID。取值范围：大于等于0的整数。 说明： 传入displayId不存在时，将抛出17000007异常。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling(UiDirection.DOWN, 10000, 0);
}

```

    

#### [h2]screenCapture 10+

 

screenCapture(savePath: string, rect?: Rect): Promise<boolean>

 

捕获当前屏幕的指定区域，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| savePath | string | 是 | 文件保存路径。路径需为当前应用的 沙箱路径 。 |
| rect | Rect | 否 | 截图区域，默认为全屏。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回截图操作是否成功完成。true：成功完成，false：未成功完成。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCapture('/data/storage/el2/base/cache/1.png', {
    left: 0,
    top: 0,
    right: 100,
    bottom: 100
  });
}

```

    

#### [h2]mouseClick 10+

 

mouseClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>

 

在指定坐标点注入鼠标点击动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标点击动作。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | Point | 是 | 鼠标点击的坐标。 |
| btnId | MouseButton | 是 | 按下的鼠标按钮。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围： KeyCode键码值 ，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围： KeyCode键码值 ，默认值为0。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
}

```

    

#### [h2]mouseScroll 10+

 

mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>

 

在指定坐标点注入鼠标滚轮滑动动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标滚轮滑动动作。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | Point | 是 | 鼠标点击的坐标。 |
| down | boolean | 是 | 滚轮滑动方向是否向下。true表示向下滑动。false表示向上滚动。 |
| d | number | 是 | 鼠标滚轮滚动的格数，取值大于等于0的整数，每格对应目标点位移120px。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围： KeyCode键码值 ，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围： KeyCode键码值 ，默认值为0。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseScroll({ x: 360, y: 640 }, true, 30, 2072);
}

```

    

#### [h2]mouseMoveTo 10+

 

mouseMoveTo(p: Point): Promise<void>

 

将鼠标光标移到目标点。使用Promise异步回调。

 

**系统能力**：SystemCapability.Test.UiTest

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | Point | 是 | 目标点的坐标。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseMoveTo({ x: 100, y: 100 });
}

```

    

#### [h2]createUIEventObserver 10+

 

createUIEventObserver(): UIEventObserver;

 

创建一个UI事件监听器。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| UIEventObserver | 返回找到的目标窗口对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UIEventObserver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
}

```

    

#### [h2]mouseScroll 11+

 

mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number, speed?: number): Promise<void>

 

在指定坐标点注入鼠标滚轮滑动动作，支持同时按下对应键盘组合键并且指定滑动速度。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | Point | 是 | 鼠标点击的坐标。 |
| down | boolean | 是 | 滚轮滑动方向是否向下。true表示向下滑动。false表示向上滚动。 |
| d | number | 是 | 鼠标滚轮滚动的格数，取值大于等于0的整数，每格对应目标点位移120px。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围： KeyCode键码值 ，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围： KeyCode键码值 ，默认值为0。 |
| speed | number | 否 | 鼠标滚轮滚动的速度，范围：1-500的整数，单位：格/秒。为不在范围内的非负数或为null/undefined时设为默认值20。为负数时抛出401错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseScroll({ x: 360, y: 640 }, true, 30, 2072, 20);
}

```

    

#### [h2]mouseDoubleClick 11+

 

mouseDoubleClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>

 

在指定坐标点注入鼠标双击动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标双击动作。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | Point | 是 | 鼠标双击的坐标。 |
| btnId | MouseButton | 是 | 按下的鼠标按钮。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围： KeyCode键码值 ，默认值0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围： KeyCode键码值 ，默认值0。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDoubleClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
}

```

    

#### [h2]mouseLongClick 11+

 

mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>

 

在指定坐标点注入鼠标长按动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标长按动作。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | Point | 是 | 鼠标长按的坐标。 |
| btnId | MouseButton | 是 | 按下的鼠标按钮。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围： KeyCode键码值 ，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围： KeyCode键码值 ，默认值为0。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseLongClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
}

```

    

#### [h2]mouseLongClick 20+

 

mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number, duration?: number): Promise<void>

 

在指定坐标点注入鼠标长按动作，支持同时按下对应键盘组合键，支持指定长按时长。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标长按动作。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | Point | 是 | 鼠标长按的坐标。 |
| btnId | MouseButton | 是 | 按下的鼠标按钮。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围： KeyCode键码值 ，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围： KeyCode键码值 ，默认值为0。 |
| duration | number | 否 | 长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseLongClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072, 0, 2000);
}

```

    

#### [h2]mouseMoveWithTrack 11+

 

mouseMoveWithTrack(from: Point, to: Point, speed?: number): Promise<void>

 

鼠标从起始坐标点滑向终点坐标点。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | Point | 是 | 起始点坐标。 |
| to | Point | 是 | 终点坐标。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseMoveWithTrack({ x: 100, y: 100 }, { x: 200, y: 200 }, 600);
}

```

    

#### [h2]mouseDrag 11+

 

mouseDrag(from: Point, to: Point, speed?: number): Promise<void>

 

鼠标按住鼠标左键从起始坐标点拖拽至终点坐标点。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | Point | 是 | 起始点坐标。 |
| to | Point | 是 | 终点坐标。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDrag({ x: 100, y: 100 }, { x: 200, y: 200 }, 600);
}

```

    

#### [h2]mouseDrag 20+

 

mouseDrag(from: Point, to: Point, speed?: number, duration?: number): Promise<void>

 

鼠标按住鼠标左键从起始坐标点拖拽至终点坐标点，支持指定拖拽速度和拖拽前长按时间。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | Point | 是 | 起始点坐标。 |
| to | Point | 是 | 终点坐标。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |
| duration | number | 否 | 拖拽前长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDrag({ x: 100, y: 100 }, { x: 200, y: 200 }, 600, 2000);
}

```

    

#### [h2]inputText 11+

 

inputText(p: Point, text: string): Promise<void>

 

在指定坐标点输入文本，不清空组件内原有文本，直接在坐标处追加输入。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | Point | 是 | 输入文本的坐标点。 |
| text | string | 是 | 输入的文本信息，当前支持英文、中文和特殊字符。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  let point = await text.getBoundsCenter();
  await driver.inputText(point, '123');
}

```

    

#### [h2]inputText 20+

 

inputText(p: Point, text: string, mode: InputTextMode): Promise<void>

 

在指定坐标点输入文本，支持指定文本输入方式。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | Point | 是 | 输入文本的坐标点。 |
| text | string | 是 | 输入的文本信息，当前支持英文、中文和特殊字符。 |
| mode | InputTextMode | 是 | 输入文本的方式，取值请参考 InputTextMode 。 说明： InputTextMode.addition取值为true时，将光标移动至文本末尾后输入指定文本。取值为false时，将在坐标点位置输入指定文本。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not support, function can not work correctly due to limited device capabilities. |

  

**示例：**

 

```
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  let point = await text.getBoundsCenter();
  await driver.inputText(point, '123', { paste: true, addition: false });
}

async function demo_Chinese() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  let point = await text.getBoundsCenter();
  await driver.inputText(point, '中文&', { paste: false, addition: true });
  // 以复制粘贴方式输入中文、特殊符号， 指定文本追加到指定坐标所在文本段的末尾。
}

```

    

#### [h2]touchPadMultiFingerSwipe 18+

 

touchPadMultiFingerSwipe(fingers: number, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>

 

模拟触摸板多指滑动手势。使用Promise异步回调。

 

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：该接口在PC/2in1设备中可正常调用，在其他设备中返回17000005错误码。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fingers | number | 是 | 触摸板多指滑动的手指数。取值为3或者4。 |
| direction | UiDirection | 是 | 触摸板多指滑动的方向。 |
| options | TouchPadSwipeOptions | 否 | 触摸板多指滑动手势附加选项，默认取TouchPadSwipeOptions中各属性的默认值。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.touchPadMultiFingerSwipe(3, UiDirection.UP);
}

```

    

#### [h2]touchPadTwoFingersScroll 22+

 

touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: number, speed?: number): Promise<void>

 

模拟触摸板双指滚动手势。使用Promise异步回调。

 

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：该接口在PC/2in1设备中可正常调用，在其他设备中返回17000005错误码。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | Point | 是 | 触摸板双指滚动时鼠标光标的位置。 |
| direction | UiDirection | 是 | 触摸板双指滚动的方向。 |
| d | number | 是 | 触摸板双指滚动的格数，取值为大于等于0的整数，每格对应目标点位移120px。 |
| speed | number | 否 | 触摸板双指滚动的速度，范围：1-500的整数，单位：格/秒。为不在范围内的非负数或为null/undefined时设为默认值20。为负数时抛出17000007错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.touchPadTwoFingersScroll({ x: 100, y: 100 }, UiDirection.UP, 20, 10);
}

```

    

#### [h2]penClick 18+

 

penClick(point: Point): Promise<void>

 

模拟手写笔点击操作。使用Promise异步回调。

 

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | Point | 是 | 点击的坐标点。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penClick({ x: 100, y: 100 });
}

```

    

#### [h2]penLongClick 18+

 

penLongClick(point: Point, pressure?: number): Promise<void>

 

模拟手写笔长按操作。使用Promise异步回调。

 

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | Point | 是 | 长按的坐标点。 |
| pressure | number | 否 | 手写笔滑动操作的压力，默认为1.0，取值范围为0.0到1.0。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penLongClick({ x: 100, y: 100 }, 0.5);
}

```

    

#### [h2]penDoubleClick 18+

 

penDoubleClick(point: Point): Promise<void>

 

模拟手写笔双击操作。使用Promise异步回调。

 

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | Point | 是 | 双击的坐标点。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penDoubleClick({ x: 100, y: 100 });
}

```

    

#### [h2]penSwipe 18+

 

penSwipe(startPoint: Point, endPoint: Point, speed?: number, pressure?: number): Promise<void>

 

模拟手写笔的滑动操作。使用Promise异步回调。

 

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startPoint | Point | 是 | 起始位置的坐标点。 |
| endPoint | Point | 是 | 结束位置的坐标点。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |
| pressure | number | 否 | 手写笔滑动操作的压力，默认为1.0，取值范围为0.0到1.0。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penSwipe({ x: 100, y: 100 }, { x: 100, y: 500 }, 600, 0.5);
}

```

    

#### [h2]injectPenPointerAction 18+

 

injectPenPointerAction(pointers: PointerMatrix, speed?: number, pressure?: number): Promise<void>

 

模拟手写笔多点连续注入操作。使用Promise异步回调。

 

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pointers | PointerMatrix | 是 | 滑动轨迹，包括操作手指个数和滑动坐标序列。 说明 ：当前仅支持单指操作，PointerMatrix中的操作手指个数fingers必须设置为1。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |
| pressure | number | 否 | 手写笔多点连续注入的压力，默认为1.0，取值范围为0.0到1.0。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let pointer = PointerMatrix.create(1, 8);
  for (let step = 0; step < 8; step++) {
    pointer.setPoint(0, step, { x: 500, y: 1100 - 100 * step });
  }
  await driver.injectPenPointerAction(pointer, 600, 0.5);
}

```

    

#### [h2]crownRotate 20+

 

crownRotate(d: number, speed?: number): Promise<void>

 

注入手表表冠旋转事件，可指定旋转速度。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：该接口在Wearable设备中可正常调用，在其他设备中返回801错误码。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | number | 是 | 手表表冠旋转的格数，正值表示顺时针旋转，负值表示逆时针旋转，取值需为整数。 |
| speed | number | 否 | 手表表冠旋转的速度，取值范围：1-500的整数，默认值为20，单位：格/秒。为不在范围内的非负数或为null/undefined时设为默认值20。为负数时抛出17000007错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |
| 801 | Capability not support, function can not work correctly due to limited device capabilities. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 顺时针旋转50格，旋转速度为30格/秒
  await driver.crownRotate(50, 30);
  // 逆时针旋转20格，旋转速度为30格/秒
  await driver.crownRotate(-20, 30);
}

```

    

#### [h2]knuckleKnock 22+

 

knuckleKnock(pointers: Array<Point>, times: number): Promise<void>

 

模拟指关节敲击屏幕操作。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/4ZiItv3vRIOuJ_mrMsRTmQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=2DA47E1FE743097884A5CCB54F6FAE5EA4E589ADD6E8926D18771CFFD2DEA123)   

若设备关闭了指关节手势，则调用本接口返回17000005错误码。

   

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：该接口在支持指关节操作的Phone、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pointers | Array< Point > | 是 | 指关节敲击屏幕坐标点的数组，数组长度取值为1或2。 |
| times | number | 是 | 指关节连续敲击屏幕的次数，取值为1或2。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, Point } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 模拟指关节单指双击手势
  let points: Array<Point> = [{ x: 100, y: 100 }];
  await driver.knuckleKnock(points, 2);
}

```

    

#### [h2]injectKnucklePointerAction 22+

 

injectKnucklePointerAction(pointers: PointerMatrix, speed?: number): Promise<void>

 

模拟指关节多点注入滑动操作。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/M3hjnIYpQwaHxcOKRb5Nag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=3B83D7E812681D8FAD7D4467D1A56B4C484D94A2DDECCC354E0A30C72E1B4F4E)   

若设备关闭了指关节手势，则调用本接口返回17000005错误码。

   

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：该接口在支持指关节操作的Phone、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pointers | PointerMatrix | 是 | 滑动轨迹，包括操作手指个数和滑动坐标序列。 说明 ：当前仅支持单指操作，PointerMatrix中的操作手指个数fingers必须设置为1。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 模拟指关节滑动在屏幕上画'S'
  let pointers: PointerMatrix = PointerMatrix.create(1, 6);
  pointers.setPoint(0, 0, { x: 750, y: 300 });
  pointers.setPoint(0, 1, { x: 500, y: 100 });
  pointers.setPoint(0, 2, { x: 250, y: 300 });
  pointers.setPoint(0, 3, { x: 750, y: 800 });
  pointers.setPoint(0, 4, { x: 500, y: 1000 });
  pointers.setPoint(0, 5, { x: 250, y: 800 });
  await driver.injectKnucklePointerAction(pointers);
}

```

    

#### [h2]isComponentPresentWhenLongClick 22+

 

isComponentPresentWhenLongClick(on: On, point: Point, duration?: number): Promise<boolean>

 

在坐标点长按，并查找目标控件是否存在。使用Promise异步回调。

 

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | On | 是 | 目标控件的属性要求。 |
| point | Point | 是 | 长按的坐标点。 |
| duration | number | 否 | 长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回长按操作期间目标控件是否存在。true：存在。false：不存在。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenLongClick(ON.id('123'), { x: 100, y: 100 }, 2000);
}

```

    

#### [h2]isComponentPresentWhenDrag 22+

 

isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: number, duration?: number): Promise<boolean>

 

从起始点拖拽至终止点，并查找目标控件是否存在。使用Promise异步回调。

 

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | On | 是 | 目标控件的属性要求。 |
| from | Point | 是 | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | Point | 是 | 以Point对象的形式传入终止点的坐标信息和所属屏幕ID。 说明： 应与起始点属于同一个屏幕，否则将抛出17000007异常。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |
| duration | number | 否 | 拖拽前长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回拖拽操作期间目标控件是否存在。true：存在。false：不存在。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenDrag(ON.id('123'), { x: 100, y: 100 }, { x: 200, y: 200 }, 1000, 2000);
}

```

    

#### [h2]isComponentPresentWhenSwipe 22+

 

isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: number): Promise<boolean>

 

从起始点滑向终止点，并查找目标控件是否存在。使用Promise异步回调。

 

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | On | 是 | 目标控件的属性要求。 |
| from | Point | 是 | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | Point | 是 | 以Point对象的形式传入终止点的坐标信息和所属屏幕ID。 说明： 应与起始点属于同一个屏幕，否则将抛出17000007异常。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回滑动操作期间目标控件是否存在。true：存在。false：不存在。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenSwipe(ON.id('123'), { x: 100, y: 100 }, { x: 200, y: 200 }, 1000);
}

```

    

#### PointerMatrix 9+

 

存储多指操作中每根手指每一步动作的坐标点及其行为的二维数组。

    

#### [h2]create 9+

 

static create(fingers: number, steps: number): PointerMatrix

 

静态方法，构造一个PointerMatrix对象，并返回该对象。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fingers | number | 是 | 多指操作中注入的手指数，取值范围：[1,10]的整数。 |
| steps | number | 是 | 每根手指操作的步骤数，取值范围：[1,1000]的整数。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| PointerMatrix | 返回构造的PointerMatrix对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { PointerMatrix } from '@kit.TestKit';

async function demo() {
  let pointerMatrix: PointerMatrix = PointerMatrix.create(2, 3);
}

```

    

#### [h2]setPoint 9+

 

setPoint(finger: number, step: number, point: Point): void

 

设置PointerMatrix对象中指定手指和步骤对应动作的坐标点。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| finger | number | 是 | 手指的序号，取值大于等于0的整数，且不超过构造PointerMatrix对象时设置的手指数。 |
| step | number | 是 | 步骤的序号，取值大于等于0的整数，且不超过构造PointerMatrix对象时设置的操作的步骤数。 |
| point | Point | 是 | 该行为的坐标点。建议相邻的坐标点距离在10px至80px范围内。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { PointerMatrix } from '@kit.TestKit';

async function demo() {
  let pointers: PointerMatrix = PointerMatrix.create(2, 5);
  pointers.setPoint(0, 0, { x: 250, y: 480 });
  pointers.setPoint(0, 1, { x: 250, y: 440 });
  pointers.setPoint(0, 2, { x: 250, y: 400 });
  pointers.setPoint(0, 3, { x: 250, y: 360 });
  pointers.setPoint(0, 4, { x: 250, y: 320 });
  pointers.setPoint(1, 0, { x: 250, y: 480 });
  pointers.setPoint(1, 1, { x: 250, y: 440 });
  pointers.setPoint(1, 2, { x: 250, y: 400 });
  pointers.setPoint(1, 3, { x: 250, y: 360 });
  pointers.setPoint(1, 4, { x: 250, y: 320 });
}

```

    

#### UiWindow 9+

 

UiWindow代表了UI界面上的一个窗口，提供窗口属性获取，窗口拖动、调整窗口大小等能力。

 

该类提供的所有方法都使用Promise方式作为异步方法，需使用await方式调用。

    

#### [h2]getBundleName 9+

 

getBundleName(): Promise<string>

 

获取窗口归属应用的包名信息。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回窗口归属应用的包名信息。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let name: string = await window.getBundleName();
}

```

    

#### [h2]getBounds 9+

 

getBounds(): Promise<Rect>

 

获取窗口的边框信息。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< Rect > | Promise对象，返回窗口的边框信息。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let rect = await window.getBounds();
}

```

    

#### [h2]getTitle 9+

 

getTitle(): Promise<string>

 

获取窗口的标题信息。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回窗口的标题信息。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let title = await window.getTitle();
}

```

    

#### [h2]getWindowMode 9+

 

getWindowMode(): Promise<WindowMode>

 

获取窗口的窗口模式信息。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< WindowMode > | Promise对象，返回窗口的窗口模式信息。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let mode = await window.getWindowMode();
}

```

    

#### [h2]isFocused 9+

 

isFocused(): Promise<boolean>

 

判断窗口是否处于获焦状态。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回窗口对象是否获取获焦状态。true：获焦。false：未获焦。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let focused = await window.isFocused();
}

```

    

#### [h2]isActived (deprecated)

 

isActived(): Promise<boolean>

 

判断窗口是否为用户正在交互窗口。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/c2LLgmqASpS0WwBDPJVDVQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=AEFF0263C17B3609E85ED7E0953859BC56C4208960A5A5A620FCC9D11686093E)   

从API version 9开始支持，从API version 11开始废弃，建议使用[isActive11+](#isactive11)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回窗口对象是否为用户正在交互窗口。true表示是交互窗口。false表示非交互窗口。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let focused = await window.isActived();
}

```

    

#### [h2]focus 9+

 

focus(): Promise<void>

 

让窗口获焦。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.focus();
}

```

    

#### [h2]moveTo 9+

 

moveTo(x: number, y: number): Promise<void>

 

将窗口移动到目标点。使用Promise异步回调。适用于支持移动的窗口。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.moveTo(100, 100);
}

```

    

#### [h2]resize 9+

 

resize(wide: number, height: number, direction: ResizeDirection): Promise<void>

 

根据传入的宽、高和调整方向来调整窗口的大小。使用Promise异步回调。适用于支持调整大小的窗口。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wide | number | 是 | 以number的形式传入调整后窗口的宽度，取值范围：大于等于0的整数。 |
| height | number | 是 | 以number的形式传入调整后窗口的高度，取值范围：大于等于0的整数。 |
| direction | ResizeDirection | 是 | 以 ResizeDirection 的形式传入窗口调整的方向。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, ResizeDirection, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.resize(100, 100, ResizeDirection.LEFT);
}

```

    

#### [h2]split 9+

 

split(): Promise<void>

 

将窗口模式切换成分屏模式。使用Promise异步回调。适用于支持切换分屏模式的窗口。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.split();
}

```

    

#### [h2]maximize 9+

 

maximize(): Promise<void>

 

将窗口最大化。使用Promise异步回调。适用于支持窗口最大化操作的窗口。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.maximize();
}

```

    

#### [h2]minimize 9+

 

minimize(): Promise<void>

 

将窗口最小化。使用Promise异步回调。适用于支持窗口最小化操作的窗口。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.minimize();
}

```

    

#### [h2]resume 9+

 

resume(): Promise<void>

 

将窗口恢复到之前的窗口模式。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.resume();
}

```

    

#### [h2]close 9+

 

close(): Promise<void>

 

将窗口关闭。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.close();
}

```

    

#### [h2]isActive 11+

 

isActive(): Promise<boolean>

 

判断窗口是否为用户正在交互窗口。使用Promise异步回调。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回窗口对象是否为用户正在交互窗口。true：交互窗口。false：非交互窗口。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  let focused = await window.isActive();
}

```

    

#### [h2]getDisplayId 20+

 

getDisplayId(): Promise<number>

 

获取窗口所属的屏幕ID。使用Promise异步回调。

 

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回窗口所属的屏幕ID。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

  

**示例：**

 

```
// xxx.test.ets
import { UiWindow, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  let id = await window.getDisplayId();
}

```

    

#### UIEventObserver 10+

 

UI事件监听器。

    

#### [h2]once('toastShow') 10+

 

once(type: 'toastShow', callback: Callback<UIElementInfo>): void

 

开始监听toast控件出现的事件，使用callback的形式返回结果。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型，取值为'toastShow'。 |
| callback | Callback< UIElementInfo > | 是 | 事件发生时执行的回调函数。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
  }
  observer.once('toastShow', callback);
}

```

    

#### [h2]once('dialogShow') 10+

 

once(type: 'dialogShow', callback: Callback<UIElementInfo>): void

 

开始监听dialog控件出现的事件，使用callback的形式返回结果。

 

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型，取值为'dialogShow'。 |
| callback | Callback< UIElementInfo > | 是 | 事件发生时执行的回调函数。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
  }
  observer.once('dialogShow', callback);
}

```

    

#### [h2]once('windowChange') 22+

 

once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void

 

开始监听指定类型的窗口变化事件，支持设置事件监听的扩展配置，监听到指定窗口变化事件时触发callback回调。仅支持[自由多窗模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由多窗模式)的窗口监听。

 

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型，支持的事件为'windowChange'。当监听到窗口变化时，触发该事件。 |
| windowChangeType | WindowChangeType | 是 | 窗口变化事件类型。 |
| options | WindowChangeOptions | 是 | 窗口变化事件监听的扩展配置，包括监听超时时间和监听窗口对应包名。 |
| callback | Callback< UIElementInfo > | 是 | 事件发生时执行的回调函数，返回事件的相关信息。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver, WindowChangeOptions, WindowChangeType } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let options: WindowChangeOptions = {
    timeout: 20000,
    bundleName: 'com.example.myapplication'  // 请开发者替换为实际包名
  }
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
    console.info(UIElementInfo.windowChangeType?.toString());
    console.info(UIElementInfo.windowId?.toString());
  }
  observer.once('windowChange', WindowChangeType.WINDOW_ADDED, options, callback);
}

```

    

#### [h2]once('componentEventOccur') 22+

 

once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void

 

开始监听指定类型的控件操作事件，支持设置事件监听的扩展配置，监听到指定控件操作事件时触发callback回调。

 

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型，支持的事件为'componentEventOccur'。当监听到控件操作时，触发该事件。 |
| componentEventType | ComponentEventType | 是 | 控件操作事件类型。 |
| options | ComponentEventOptions | 是 | 控件操作事件监听的扩展配置，包括监听超时时间和监听控件匹配条件。 |
| callback | Callback< UIElementInfo > | 是 | 事件发生时执行的回调函数。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver, ComponentEventOptions, ComponentEventType, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let option: ComponentEventOptions = {
    timeout: 20000,
    on: ON.id('123')  // 请开发者替换为实际存在的控件id值
  };
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
    console.info(UIElementInfo.componentEventType?.toString());
    console.info(UIElementInfo.windowId?.toString());
    console.info(UIElementInfo.componentId);
    console.info(UIElementInfo.componentRect?.left.toString());
    console.info(UIElementInfo.componentRect?.left.toString());
    console.info(UIElementInfo.componentRect?.left.toString());
    console.info(UIElementInfo.componentRect?.left.toString());
  };
  observer.once('componentEventOccur', ComponentEventType.COMPONENT_CLICKED, option, callback);
}

```

    

#### By (deprecated)

 

UiTest框架通过By类提供了丰富的控件特征描述API，用于进行控件筛选来匹配/查找出目标控件。

 

By提供的API能力具有以下几个特点:

 

1、支持单属性匹配和多属性组合匹配，例如同时指定目标控件text和id。

 

2、控件属性支持多种匹配模式。

 

3、支持控件绝对定位，相对定位，可通过[By.isBefore(deprecated)](#isbeforedeprecated)和[By.isAfter(deprecated)](#isafterdeprecated)等API限定邻近控件特征进行辅助定位。

 

By类提供的所有API均为同步接口，建议使用者通过静态构造器BY来链式创建By对象。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/vGancozJTTK59HlPlW4gZg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=E9A7F76C953479E4EA84E7DAD8A47BACA9A49B45A30FEB5B2694794282F4007E)   

从API version 8开始支持，从API version 9开始废弃，建议使用[On9+](#on9)替代。

   

```
// xxx.test.ets
import { BY } from '@kit.TestKit';

BY.text('123').type('Button');

```

    

#### [h2]text (deprecated)

 

text(txt: string, pattern?: MatchPattern): By

 

指定目标控件文本属性，支持多种匹配模式，返回By对象自身。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/ny1ykhtLR5qLIGKIGRVRJw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=401005A84B6EC3DDE39BD2A9512650E6BF5F2C1EED0BBC3ABA6B7D665D50E634)   

从API version 8开始支持，从API version 9开始废弃，建议使用[text9+](#text9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| txt | string | 是 | 指定控件文本，用于匹配目标控件文本。 |
| pattern | MatchPattern | 否 | 指定的文本匹配模式，默认为 EQUALS 。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| By | 返回指定目标控件文本属性的By对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { BY, By } from '@kit.TestKit';

let by: By = BY.text('123'); // 使用静态构造器BY创建by对象，指定目标控件的text属性。

```

    

#### [h2]key (deprecated)

 

key(key: string): By

 

指定目标控件key值属性，返回By对象自身。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/OX5vwLpLSl2u0DrAm8kUgA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=630BCDFDAD3526F7A8545985FBF6BAEB54DF814D33B851B66DCAC5A91C96ADF5)   

从API version 8开始支持，从API version 9开始废弃，建议使用[id9+](#id9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 指定控件的Key值。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| By | 返回指定目标控件key值属性的By对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.key('123'); // 使用静态构造器BY创建by对象，指定目标控件的key值属性。

```

    

#### [h2]id (deprecated)

 

id(id: number): By

 

指定目标控件id属性，返回By对象自身。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/oHK9fM-bTyKNjek13ql39A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=3C1D8469AEB787B2EEA31977CD32D08D4113ACFA7D9FF15ACA0981925E3F597A)   

从API version 8开始支持，从API version 9开始废弃，建议使用[id9+](#id9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 指定控件的id值。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| By | 返回指定目标控件id属性的By对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.id(123); // 使用静态构造器BY创建by对象，指定目标控件的id属性。

```

    

#### [h2]type (deprecated)

 

type(tp: string): By

 

指定目标控件的控件类型属性，返回By对象自身。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/AuJHYMUyTL-EZc0sbbxRxw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=9E9381DA99108F173A215E021FBAC6C2124BA644B208AFF24E0EB383D5300998)   

从API version 8开始支持，从API version 9开始废弃，建议使用[type9+](#type9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tp | string | 是 | 指定控件类型。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| By | 返回指定目标控件的控件类型属性的By对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.type('Button'); // 使用静态构造器BY创建by对象，指定目标控件的控件类型属性。

```

    

#### [h2]clickable (deprecated)

 

clickable(b?: boolean): By

 

指定目标控件的可点击状态属性，返回By对象自身。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/-AA6VN_6Q_ip4XXli8oQew/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=76D7844B3D69F7796B39B114E087C27F6D2BA51774FE918A58D3784DE4491E62)   

从API version 8开始支持，从API version 9开始废弃，建议使用[clickable9+](#clickable9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件可点击状态。true：可点击。false：不可点击。默认为true。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| By | 返回指定目标控件的可点击状态属性的By对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.clickable(true); // 使用静态构造器BY创建by对象，指定目标控件的可点击状态属性。

```

    

#### [h2]scrollable (deprecated)

 

scrollable(b?: boolean): By

 

指定目标控件的可滑动状态属性，返回By对象自身。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/QD_uehdcRj2zih7s5s_khA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=6435EAC03E93E90FC82D0703810546EAB86C871EFCEB8DE087918D5D4505B8B4)   

从API version 8开始支持，从API version 9开始废弃，建议使用[scrollable9+](#scrollable9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 控件可滑动状态。true：可滑动。false：不可滑动。默认为true。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| By | 返回指定目标控件的可滑动状态属性的By对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.scrollable(true); // 使用静态构造器BY创建by对象，指定目标控件的可滑动状态属性。

```

    

#### [h2]enabled (deprecated)

 

enabled(b?: boolean): By

 

指定目标控件的使能状态属性，返回By对象自身。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/RzzElfRSSw68v8FKnZyQMA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=DCC0757C1FA6315BDCB80DC4D7F895936B9D3A0E7B7334E878DF872C99D7542F)   

从API version 8开始支持，从API version 9开始废弃，建议使用[enabled9+](#enabled9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件使能状态。true：使能。false：未使能。默认为true。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| By | 返回指定目标控件的使能状态属性的By对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.enabled(true); // 使用静态构造器BY创建by对象，指定目标控件的使能状态属性。

```

    

#### [h2]focused (deprecated)

 

focused(b?: boolean): By

 

指定目标控件的获焦状态属性，返回By对象自身。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/3EXHZ_laQOaCddwqT9kYhg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=4BB8B9EF7B9A31BDC078CC537CA9339E78DB39E855B777652F44B5A839982E2E)   

从API version 8开始支持，从API version 9开始废弃，建议使用[focused9+](#focused9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 控件获焦状态。true：获焦。false：未获焦。默认为true。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| By | 返回指定目标控件的获焦状态属性的By对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.focused(true); // 使用静态构造器BY创建by对象，指定目标控件的获焦状态属性。

```

    

#### [h2]selected (deprecated)

 

selected(b?: boolean): By

 

指定目标控件的被选中状态属性，返回By对象自身。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/qX-7bptRS6Gp4adgDa2mUQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=EB7126871A4EA807536FA30ED4EBA58C6E6C41EB65AC5177A75A7C0960F7E35E)   

从API version 8开始支持，从API version 9开始废弃，建议使用[selected9+](#selected9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件被选中状态。true：被选中。false：未被选中。默认为true。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| By | 返回指定目标控件的被选中状态属性的By对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.selected(true); // 使用静态构造器BY创建by对象，指定目标控件的被选中状态属性。

```

    

#### [h2]isBefore (deprecated)

 

isBefore(by: By): By

 

指定目标控件位于给出的特征属性控件之前，返回By对象自身。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/wULwQBLDTECDpu9dfm9MIA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=D88AF288D37D99BDDA49E2475072C9A5676418D1FA87BA91CE5FD42319AA95DC)   

从API version 8开始支持，从API version 9开始废弃，建议使用[isBefore9+](#isbefore9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| by | By | 是 | 特征控件的属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| By | 返回指定目标控件位于给出的特征属性控件之前的By对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

// 使用静态构造器BY创建by对象，指定目标控件位于给出的特征属性控件之前。
let by: By = BY.type('Button').isBefore(BY.text('123')); // 查找text为123之前的第一个Button组件

```

    

#### [h2]isAfter (deprecated)

 

isAfter(by: By): By

 

指定目标控件位于给出的特征属性控件之后，返回By对象自身。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/aCaDOIi_T-q988NQPOylOw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=002378143FE24B9ADE22B2694D1A64DFBA7D824EB8C32E39455E5D119EC6A2A4)   

从API version 8开始支持，从API version 9开始废弃，建议使用[isAfter9+](#isafter9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| by | By | 是 | 特征控件的属性。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| By | 返回指定目标控件位于给出的特征属性控件之后的By对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

// 使用静态构造器BY创建by对象，指定目标控件位于给出的特征属性控件之后。
let by: By = BY.type('Text').isAfter(BY.text('123')); // 查找 text为123之后的第一个Text组件

```

    

#### UiComponent (deprecated)

 

UiTest中，UiComponent类代表了UI界面上的一个控件，提供控件属性获取，控件点击，滑动查找，文本注入等API。

 

该类提供的所有方法都使用Promise方式作为异步方法，需使用await调用。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/CBwIwobcTmyerlEDHrvvSA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=23E309F99DDBAD53E4D9CCA37A439C13D0BD8B88A3AF3B866055E4651D8C9760)   

从API version 8开始支持，从API version 9开始废弃，建议使用[Component9+](#component9)替代。

      

#### [h2]click (deprecated)

 

click(): Promise<void>

 

控件对象进行点击操作。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/L4y47tIYRw28U_6xy03JKw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=15FC5C6E1C539538C04EE2046E0C40859097A2D94815102C09F889FD5ED7EAF5)   

从API version 8开始支持，从API version 9开始废弃，建议使用[click9+](#click9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, Driver, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.click();
}

```

    

#### [h2]doubleClick (deprecated)

 

doubleClick(): Promise<void>

 

控件对象进行双击操作。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/5xoQ8g2oShqF6twaCmPNAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=3854263A2F8FF0B95C44F6678F4A745EC014132726BA941957666C96E30C0219)   

从API version 8开始支持，从API version 9开始废弃，建议使用[doubleClick9+](#doubleclick9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.doubleClick();
}

```

    

#### [h2]longClick (deprecated)

 

longClick(): Promise<void>

 

控件对象进行长按操作。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/xFVpyDtNRL6OJO3p3uIPfA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=781B47DC2C7E611C8DF17D0BE208A9DDAD69B3ABE379B8307C412D5EF23C0678)   

从API version 8开始支持，从API version 9开始废弃，建议使用[longClick9+](#longclick9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.longClick();
}

```

    

#### [h2]getId (deprecated)

 

getId(): Promise<number>

 

获取控件对象的id值。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/-YFQVGceTEus3Yrp2VYq4Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=C2C00484061666E9AC9B449A5998C2ED0047F4608644C6A53C5EAF9D2F5733A7)   

从API version 8开始支持，从API version 9开始废弃，建议使用[getId9+](#getid9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回控件的id值。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let id = await button.getId();
}

```

    

#### [h2]getKey (deprecated)

 

getKey(): Promise<string>

 

获取控件对象的key值。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/1OE-GN09RKuyaSTgWFSvrw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=BAFDE8DE7C39A6333A8F57FAB9C087EDD1A44D2CE767805A945100B6B1967EEB)   

从API version 8开始支持，从API version 9开始废弃，建议使用[getId9+](#getid9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的key值。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let str_key = await button.getKey();
}

```

    

#### [h2]getText (deprecated)

 

getText(): Promise<string>

 

获取控件对象的文本信息。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/l-xM4nmPRqerySDmZiP96A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=AC6EC390E86436C0D53DE6E81048D03F79D6044453A69342073E6FA97F99C5EB)   

从API version 8开始支持，从API version 9开始废弃，建议使用[getText9+](#gettext9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的文本信息。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let text = await button.getText();
}

```

    

#### [h2]getType (deprecated)

 

getType(): Promise<string>

 

获取控件对象的控件类型。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/_3hDhexIRhum1ze3L0ipCg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=59D954D54BADD8E6A248A2756EC6C0B5FCBE7CD283050B1451E73D66E4C928FD)   

从API version 8开始支持，从API version 9开始废弃，建议使用[getType9+](#gettype9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的类型。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let type = await button.getType();
}

```

    

#### [h2]isClickable (deprecated)

 

isClickable(): Promise<boolean>

 

获取控件对象可点击状态。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/pKgwKEB-RCSGy_M7Q7x_kg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=4CF3AD98806C341B971DBBCC40C518D0DD73F6C9C08EC5D97B1C948454F4AEAA)   

从API version 8开始支持，从API version 9开始废弃，建议使用[isClickable9+](#isclickable9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象可点击状态。true：可点击。false：不可点击。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isClickable()) {
    console.info('This button can be Clicked');
  } else {
    console.info('This button can not be Clicked');
  }
}

```

    

#### [h2]isScrollable (deprecated)

 

isScrollable(): Promise<boolean>

 

获取控件对象可滑动状态。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/3c6cDjIjTpiDFKMI4-mBdA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=75BA6140F6C871695316FE6D0AE5CC74703DB255DC7ABF741CBF95B510219A34)   

从API version 8开始支持，从API version 9开始废弃，建议使用[isScrollable9+](#isscrollable9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象可滑动状态。true：可滑动。false：不可滑动。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let scrollBar: UiComponent = await driver.findComponent(BY.scrollable(true));
  if (await scrollBar.isScrollable()) {
    console.info('This scrollBar can be operated');
  } else {
    console.info('This scrollBar can not be operated');
  }
}

```

    

#### [h2]isEnabled (deprecated)

 

isEnabled(): Promise<boolean>

 

获取控件使能状态。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/99W1J-17S963rc-jtla6Ng/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=869E8CC551CC907DAA9A02FC83DBB452649B87251EE5DA2486A97D3D60844C13)   

从API version 8开始支持，从API version 9开始废弃，建议使用[isEnabled9+](#isenabled9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件使能状态。true：使能。false：未使能。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isEnabled()) {
    console.info('This button can be operated');
  } else {
    console.info('This button can not be operated');
  }
}

```

    

#### [h2]isFocused (deprecated)

 

isFocused(): Promise<boolean>

 

判断控件对象是否获焦。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/v3lJhDJuSdCTsk5P2wGJSw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=ECA7C689EBDCFC3215265FE8FDC348BABAF401627266985669754A12B9F30752)   

从API version 8开始支持，从API version 9开始废弃，建议使用[isFocused9+](#isfocused9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象是否获焦。true：获焦。false：未获焦。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isFocused()) {
    console.info('This button is focused');
  } else {
    console.info('This button is not focused');
  }
}

```

    

#### [h2]isSelected (deprecated)

 

isSelected(): Promise<boolean>

 

获取控件对象被选中状态。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/DSsbYKv3SI64sMRLuTY17A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=A4523399932D3124FC563FDC2153C9541BFF1AD82D8F7CAFAD466BB0C92DE22E)   

从API version 8开始支持，从API version 9开始废弃，建议使用[isSelected9+](#isselected9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象被选中的状态。true：被选中。false：未被选中。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isSelected()) {
    console.info('This button is selected');
  } else {
    console.info('This button is not selected');
  }
}

```

    

#### [h2]inputText (deprecated)

 

inputText(text: string): Promise<void>

 

向控件中输入文本，仅针对可编辑的文本组件生效。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/uczaHyH3TmuXcgKtnxG4PQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=86C303F0BBC21AAB375A3F8AEBBE9A4F6A4AAC2E9658E39B296C097D7E2FEB73)   

从API version 8开始支持，从API version 9开始废弃，建议使用[inputText9+](#inputtext9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 输入的文本信息。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let text: UiComponent = await driver.findComponent(BY.text('hello world'));
  await text.inputText('123');
}

```

    

#### [h2]scrollSearch (deprecated)

 

scrollSearch(by: By): Promise<UiComponent>

 

在控件上滑动查找目标控件（适用于List等支持滑动的控件）。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/fTDWBr3TSjaqAZ8UOE1K9A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=7AF42B8DC2371BEB81E3B3C4A86A5BEDB021A565E86DD4F2A350AB0E3422FA52)   

从API version 8开始支持，从API version 9开始废弃，建议使用[scrollSearch9+](#scrollsearch9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| by | By | 是 | 目标控件的属性要求。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< UiComponent > | Promise对象，返回目标控件对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let scrollBar: UiComponent = await driver.findComponent(BY.type('Scroll'));
  let button = await scrollBar.scrollSearch(BY.text('next page'));
}

```

    

#### UiDriver (deprecated)

 

UiDriver类为uitest测试框架的总入口，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等API。

 

该类提供的方法除UiDriver.create()以外的所有方法都使用Promise方式作为异步方法，需使用await调用。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/KVmpiSL3SIe9VmIqyPr3YA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=1098218759A3837C1B9B91D096C1C0615FA9AD11F1D4C661B96512ADC8398A84)   

从API version 8开始支持，从API version 9开始废弃，建议使用[Driver9+](#driver9)替代。

      

#### [h2]create (deprecated)

 

static create(): UiDriver

 

静态方法，构造一个UiDriver对象，并返回该对象。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/brhGitBoR8KDpyAqSRi-lw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=6F5633E3B9ACD5AFCDA33C2FB05EA40FB563E7EF992016D8B113E311576F4AEA)   

从API version 8开始支持，从API version 9开始废弃，建议使用[create9+](#create9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| UiDriver | 返回构造的UiDriver对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
}

```

    

#### [h2]delayMs (deprecated)

 

delayMs(duration: number): Promise<void>

 

UiDriver对象在给定的时间内延时。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/iMSDjceRSXSVSygNlVnG9w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=64763C409B74CC9740975C3E856FE63579E5CFC8AF83B3F7C5865ABEECE1FBAC)   

从API version 8开始支持，从API version 9开始废弃，建议使用[delayMs9+](#delayms9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| duration | number | 是 | 给定的时间。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.delayMs(1000);
}

```

    

#### [h2]findComponent (deprecated)

 

findComponent(by: By): Promise<UiComponent>

 

在UiDriver对象中，根据给出的目标控件属性要求查找目标控件。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/3xO3NuwkQWiIrQXBvnSqLQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=C2A4436F97A215676B7FE85FC6893F5CFEE63B9021CD1BAB6B732A6B43948D9A)   

从API version 8开始支持，从API version 9开始废弃，建议使用[findComponent9+](#findcomponent9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| by | By | 是 | 目标控件的属性要求。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise< UiComponent > | Promise对象，返回控件对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.text('next page'));
}

```

    

#### [h2]findComponents (deprecated)

 

findComponents(by: By): Promise<Array<UiComponent>>

 

在UiDriver对象中，根据给出的目标控件属性要求查找出所有匹配控件，以列表保存。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/CB9X4vSeTs6AB5jcsNV37g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=EF7BB83042FF9834352136253B27B3A64A85D0682464FEBC1095E99A186ABE3A)   

从API version 8开始支持，从API version 9开始废弃，建议使用[findComponents9+](#findcomponents9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| by | By | 是 | 目标控件的属性要求。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<Array< UiComponent >> | Promise对象，返回控件对象的列表。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let buttonList: Array<UiComponent> = await driver.findComponents(BY.text('next page'));
}

```

    

#### [h2]assertComponentExist (deprecated)

 

assertComponentExist(by: By): Promise<void>

 

断言API，用于断言当前界面存在满足给出的目标控件属性的控件; 如果控件不存在，该API将抛出JS异常，使当前测试用例失败。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/dttvx3hcSA2J6XGR1Km5XQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=3C22234F1411375928E9110A4307DB1E9DE27953EB652B104E78EA7DE0691DF5)   

从API version 8开始支持，从API version 9开始废弃，建议使用[assertComponentExist9+](#assertcomponentexist9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| by | By | 是 | 目标控件的属性要求。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**错误码：**

 

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

  

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | if the input parameters are invalid. |
| 17000002 | if the async function was not called with await. |
| 17000003 | if the assertion failed. |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver, BY } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.assertComponentExist(BY.text('next page'));
}

```

    

#### [h2]pressBack (deprecated)

 

pressBack(): Promise<void>

 

UiDriver对象进行点击BACK键的操作。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/WHn_8lS7SnuSIFk9r9iUuA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=078CF3DA6353EA3C0C38F6A40811974C31E0859BD6382AF679178A2829AB07FF)   

从API version 8开始支持，从API version 9开始废弃，建议使用[pressBack9+](#pressback9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.pressBack();
}

```

    

#### [h2]triggerKey (deprecated)

 

triggerKey(keyCode: number): Promise<void>

 

UiDriver对象采取如下操作：通过key值找到对应键并点击。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/uu-_3WnLRy22IaJfVotZjA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=598832297543B7CD8D25DB19DD475FC6D10C6B053325C9B429F134B637070A7C)   

从API version 8开始支持，从API version 9开始废弃，建议使用[triggerKey9+](#triggerkey9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyCode | number | 是 | 指定的key值，取值大于等于0的整数，取值范围： KeyCode键码值 。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { Driver, UiDriver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK); // 返回键
}

```

    

#### [h2]click (deprecated)

 

click(x: number, y: number): Promise<void>

 

UiDriver对象采取如下操作：在目标坐标点单击。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/ZnrNkqf9SYei9DVLDkSgDg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=7D2B3D6DDCCF85C912AE68463B875EDCCE93B06C41D91B0033D7561A24F6F8F0)   

从API version 8开始支持，从API version 9开始废弃，建议使用[click9+](#click9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.click(100, 100);
}

```

    

#### [h2]doubleClick (deprecated)

 

doubleClick(x: number, y: number): Promise<void>

 

UiDriver对象采取如下操作：在目标坐标点双击。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/vHAQh-kBTMi09c7qPPNY-Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=AB4AA3F89AAED82DC23730E54E888980DA7A5A471CB10616F05A94F5B45C1AC4)   

从API version 8开始支持，从API version 9开始废弃，建议使用[doubleClick9+](#doubleclick9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.doubleClick(100, 100);
}

```

    

#### [h2]longClick (deprecated)

 

longClick(x: number, y: number): Promise<void>

 

UiDriver对象采取如下操作：在目标坐标点长按下鼠标左键。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/Cbsjv6hfTlSCWw5anCGlrg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=DD9712C91BA2137B296B2BE5ECA82A572EB4898C061E172DA8F21564012CBB28)   

从API version 8开始支持，从API version 9开始废弃，建议使用[longClick9+](#longclick9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.longClick(100, 100);
}

```

    

#### [h2]swipe (deprecated)

 

swipe(startx: number, starty: number, endx: number, endy: number): Promise<void>

 

UiDriver对象采取如下操作：从给出的起始坐标点滑向给出的目的坐标点。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/9ioOkNs8SUKdsaFWdY6__A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=EEF557FE56DADA4DCF9EBE367289D29DB2314E516802F3938AA39EB7987DBBE6)   

从API version 8开始支持，从API version 9开始废弃，建议使用[swipe9+](#swipe9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startx | number | 是 | 以number的形式传入起始点的横坐标信息，取值范围：大于等于0的整数。 |
| starty | number | 是 | 以number的形式传入起始点的纵坐标信息，取值范围：大于等于0的整数。 |
| endx | number | 是 | 以number的形式传入目的点的横坐标信息，取值范围：大于等于0的整数。 |
| endy | number | 是 | 以number的形式传入目的点的纵坐标信息，取值范围：大于等于0的整数。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.swipe(100, 100, 200, 200);
}

```

    

#### [h2]screenCap (deprecated)

 

screenCap(savePath: string): Promise<boolean>

 

UiDriver对象采取如下操作：捕获当前屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/zeWUtDzGTsOtScKKMyz7rg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194359Z&HW-CC-Expire=86400&HW-CC-Sign=2C02C2588215A19E37D79A64677280D635501B1E0A5BFB23AD130F54B3FBDDDB)   

从API version 8开始支持，从API version 9开始废弃，建议使用[screenCap9+](#screencap9)替代。

   

**系统能力**：SystemCapability.Test.UiTest

 

**参数：**

  

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| savePath | string | 是 | 文件保存路径。 |

  

**返回值：**

  

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回截图操作是否成功完成。true：成功完成，false：未成功完成。 |

  

**示例：**

 

```
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png');
}

```
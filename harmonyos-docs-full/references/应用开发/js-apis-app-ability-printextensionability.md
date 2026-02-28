# @ohos.app.ability.PrintExtensionAbility (打印扩展能力)

该模块为打印扩展能力的操作API，提供调用打印扩展能力的接口。

 说明 

本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

 支持设备PhonePC/2in1Tablet

```
import { PrintExtensionAbility } from '@kit.BasicServicesKit';
```

## PrintExtensionAbility

 支持设备PhonePC/2in1Tablet  

### onCreate

 支持设备PhonePC/2in1Tablet

onCreate(want: Want): void

初始化扩展能力，会在系统首次连接打印扩展时调用。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 表示调用打印页面需要参数。 |

**示例：**

```
import { PrintExtensionAbility } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

export default class HWPrintExtension extends PrintExtensionAbility {
    onCreate(want: Want): void {
        console.info('onCreate');
        // ...
    }
}
```

### onStartDiscoverPrinter

 支持设备PhonePC/2in1Tablet

onStartDiscoverPrinter(): void

开始发现与设备连接的打印机时调用。

**系统能力：** SystemCapability.Print.PrintFramework

**示例：**

```
import { PrintExtensionAbility } from '@kit.BasicServicesKit';

export default class HWPrintExtension extends PrintExtensionAbility {
    onStartDiscoverPrinter(): void {
        console.info('onStartDiscoverPrinter enter');
        // ...
    }
}
```

### onStopDiscoverPrinter

 支持设备PhonePC/2in1Tablet

onStopDiscoverPrinter(): void

停止发现打印机时调用。

**系统能力：** SystemCapability.Print.PrintFramework

**示例：**

```
import { PrintExtensionAbility } from '@kit.BasicServicesKit';

export default class HWPrintExtension extends PrintExtensionAbility {
    onStopDiscoverPrinter(): void {
        console.info('onStopDiscoverPrinter enter');
        // ...
    }
}
```

### onConnectPrinter

 支持设备PhonePC/2in1Tablet

onConnectPrinter(printerId: number): void

连接到特定打印机时调用。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerId | number | 是 | 表示打印机ID。 |

**示例：**

```
import { PrintExtensionAbility } from '@kit.BasicServicesKit';

export default class HWPrintExtension extends PrintExtensionAbility {
    onConnectPrinter(printerId: number): void {
        console.info('onConnectPrinter enter');
        // ...
    }
}
```

### onDisconnectPrinter

 支持设备PhonePC/2in1Tablet

onDisconnectPrinter(printerId: number): void

断开与特定打印机的连接时调用。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerId | number | 是 | 表示打印机ID。 |

**示例：**

```
import { PrintExtensionAbility } from '@kit.BasicServicesKit';

export default class HWPrintExtension extends PrintExtensionAbility {
    onDisconnectPrinter(printerId: number): void {
        console.info('onDisconnectPrinter enter');
        // ...
    }
}
```

### onDestroy

 支持设备PhonePC/2in1Tablet

onDestroy(): void

结束打印扩展时调用。

**系统能力：** SystemCapability.Print.PrintFramework

**示例：**

```
import { PrintExtensionAbility } from '@kit.BasicServicesKit';

export default class HWPrintExtension extends PrintExtensionAbility {
    onDestroy(): void {
        console.info('onDestroy');
    }
}
```
# @ohos.WorkSchedulerExtensionAbility (延迟任务调度回调)

本模块提供延迟任务回调能力。开发者可重写模块接口，在延迟任务触发时，系统可通过本模块接口回调应用，在回调里处理任务逻辑。

 说明 

- 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本模块接口仅可在Stage模型下使用。

## 导入模块

支持设备PhonePC/2in1TabletTVWearable

```
import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';
```

## WorkSchedulerExtensionContext 10+

支持设备PhonePC/2in1TabletTVWearable

type WorkSchedulerExtensionContext = _WorkSchedulerExtensionContext

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

 展开

| 类型 | 说明 |
| --- | --- |
| _WorkSchedulerExtensionContext | WorkSchedulerExtension的上下文环境。 |

## WorkSchedulerExtensionAbility

支持设备PhonePC/2in1TabletTVWearable 

### 属性

支持设备PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

 展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context 10+ | WorkSchedulerExtensionContext | 否 | 否 | WorkSchedulerExtension的上下文环境，继承自ExtensionContext。 |

### onWorkStart

支持设备PhonePC/2in1TabletTVWearable

onWorkStart(work: workScheduler.WorkInfo): void

开始延迟任务调度回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数**：

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| work | workScheduler.WorkInfo | 是 | 要添加到执行队列的任务。 |

**示例：**

```
import { workScheduler } from '@kit.BackgroundTasksKit';
import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';

export default class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
  onWorkStart(workInfo: workScheduler.WorkInfo) {
      console.info(`MyWorkSchedulerExtensionAbility onWorkStart, workId: ${workInfo.workId},
          bundleName: ${workInfo.bundleName}, abilityName: ${workInfo.abilityName}.`);
  }
}
```

### onWorkStop

支持设备PhonePC/2in1TabletTVWearable

onWorkStop(work: workScheduler.WorkInfo): void

结束延迟任务调度回调。当延迟任务2分钟超时或应用调用[stopWork](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-workscheduler#workschedulerstopwork)接口取消任务时，触发该回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数**：

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| work | workScheduler.WorkInfo | 是 | 执行队列中要结束回调的任务。 |

**示例：**

```
import { workScheduler } from '@kit.BackgroundTasksKit';
import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';

export default class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
  onWorkStop(workInfo: workScheduler.WorkInfo) {
      console.info(`MyWorkSchedulerExtensionAbility onWorkStop, workId: ${workInfo.workId},
          bundleName: ${workInfo.bundleName}, abilityName: ${workInfo.abilityName}.`);
  }
}
```
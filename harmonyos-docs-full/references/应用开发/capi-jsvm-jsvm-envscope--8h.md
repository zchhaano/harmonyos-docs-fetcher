# JSVM_EnvScope__*

```
typedef struct JSVM_EnvScope__* JSVM_EnvScope
```

## 概述

支持设备PhonePC/2in1TabletWearable

表示用于控制附加到当前虚拟机实例的环境。只有当线程通过OH_JSVM_OpenEnvScope进入该环境的JSVM_EnvScope后，该环境才对线程的虚拟机实例可用。

**起始版本：** 11

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)
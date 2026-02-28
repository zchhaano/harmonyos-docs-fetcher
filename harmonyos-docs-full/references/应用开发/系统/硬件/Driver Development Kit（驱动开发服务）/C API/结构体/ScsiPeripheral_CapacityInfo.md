# ScsiPeripheral_CapacityInfo

```
typedef struct ScsiPeripheral_CapacityInfo {...} ScsiPeripheral_CapacityInfo
```

## 概述

支持设备PC/2in1

SCSI read capacity 数据。

**起始版本：** 18

**相关模块：** [SCSIPeripheralDDK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk)

**所在头文件：** [scsi_peripheral_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h)

## 汇总

支持设备PC/2in1 

### 成员变量

 支持设备PC/2in1展开

| 名称 | 描述 |
| --- | --- |
| uint32_t lbAddress | 返回的逻辑单元地址。 |
| uint32_t lbLength | 单个逻辑单元长度，单位：字节。 |
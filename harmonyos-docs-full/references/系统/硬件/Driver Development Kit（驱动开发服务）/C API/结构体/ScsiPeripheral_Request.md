# ScsiPeripheral_Request

```
typedef struct ScsiPeripheral_Request {...} ScsiPeripheral_Request
```

## 概述

支持设备PC/2in1

请求参数结构体。

**起始版本：** 18

**相关模块：** [SCSIPeripheralDDK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk)

**所在头文件：** [scsi_peripheral_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h)

## 汇总

支持设备PC/2in1 

### 成员变量

 支持设备PC/2in1展开

| 名称 | 描述 |
| --- | --- |
| uint8_t commandDescriptorBlock[SCSIPERIPHERAL_MAX_CMD_DESC_BLOCK_LEN] | 命令描述符块。 |
| uint8_t cdbLength | 命令描述符块的长度。 |
| int8_t dataTransferDirection | 数据传输方向。 |
| ScsiPeripheral_DeviceMemMap* data | 数据传输的缓冲区。 |
| uint32_t timeout | 超时时间（单位：毫秒）。 |
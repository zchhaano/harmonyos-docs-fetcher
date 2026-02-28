# @ohos.document (文件交互)

说明 

- 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本模块接口从API version 9开始废弃。不建议使用以下接口，调用以下接口将抛出异常。

## 导入模块

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
import document from '@ohos.document' ;
```

## document.choose (deprecated)

支持设备PhonePC/2in1TabletTV

choose(types?: string[]): Promise<string>

通过文件管理器选择文件，异步返回文件URI，使用promise形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | string[] | 否 | 限定文件选择的类型 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 异步返回文件URI（注：当前返回错误码） |

**示例：**

 收起自动换行深色代码主题复制

```
let types : Array < string > = []; document . choose (types);
```

## document.choose (deprecated)

支持设备PhonePC/2in1TabletTV

choose(callback:AsyncCallback<string>): void

通过文件管理器选择文件，异步返回文件URI，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 异步获取对应文件URI（注：当前返回错误码） |

**示例：**

 收起自动换行深色代码主题复制

```
let uri : string = "" ; document . choose ( ( err: TypeError , uri: string ) => { //do something with uri });
```

## document.choose (deprecated)

支持设备PhonePC/2in1TabletTV

choose(types:string[], callback:AsyncCallback<string>): void

通过文件管理器选择文件，异步返回文件URI，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | string[] | 是 | 限定选择文件的类型 |
| callback | AsyncCallback<string> | 是 | 异步获取对应文件URI（注：当前返回错误码） |

**示例：**

 收起自动换行深色代码主题复制

```
let types : Array < string > = []; let uri : string = "" ; document . choose (types, ( err: TypeError , uri: string ) => { //do something with uri });
```

## document.show (deprecated)

支持设备PhonePC/2in1TabletTV

show(uri:string, type:string):Promise<void>

异步打开URI对应的文件，使用promise形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待打开的文件URI |
| type | string | 是 | 待打开文件的类型 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise回调返回void表示成功打开文件（注：当前返回错误码） |

**示例：**

 收起自动换行深色代码主题复制

```
let type : string = "" ; let uri : string = "" ; document . show (uri, type );
```

## document.show (deprecated)

支持设备PhonePC/2in1TabletTV

show(uri:string, type:string, callback:AsyncCallback<void>): void

异步打开URI对应的文件，使用callback形式返回结果。

**系统能力**：SystemCapability.FileManagement.UserFileService

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待打开的文件URI |
| type | string | 是 | 待打开文件的类型 |
| callback | AsyncCallback<void> | 是 | 异步打开uri对应文件（注：当前返回错误码） |

**示例：**

 收起自动换行深色代码主题复制

```
let type : string = "" ; let uri : string = "" ; document . show (uri, type , ( err: TypeError ) => { //do something });
```
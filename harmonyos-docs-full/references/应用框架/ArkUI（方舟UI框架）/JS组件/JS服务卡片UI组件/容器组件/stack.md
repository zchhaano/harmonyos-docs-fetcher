# stack

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

 说明 

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

支持设备PhonePC/2in1TabletTVWearable

支持。

## 属性

支持设备PhonePC/2in1TabletTVWearable

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-attributes)。

## 样式

支持设备PhonePC/2in1TabletTVWearable

支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-styles)。

## 事件

支持设备PhonePC/2in1TabletTVWearable

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-events)。

## 示例

支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<stack class="stack-parent">
  <div class="back-child bd-radius"></div>
  <div class="positioned-child bd-radius"></div>
  <div class="front-child bd-radius"></div>
</stack>
```

```
/* xxx.css */
.stack-parent {
  width: 400px;
  height: 400px;
  margin: 50px;
  background-color: #ffffff;
  border-width: 1px;
  border-style: solid;
}
.back-child {
  width: 300px;
  height: 300px;
  background-color: #3f56ea;
}
.front-child {
  width: 100px;
  height: 100px;
  background-color: #00bfc9;
}
.positioned-child {
  width: 100px;
  height: 100px;
  left: 50px;
  top: 50px;
  background-color: #47cc47;
}
.bd-radius {
  border-radius: 16px;
}
```

**4×4卡片**

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170900.07598667358215404243827422055161:50001231000000:2800:59A8F943F98173CAD46D6D6182B77146E41FA111D3A19AEC6F8B2C27F82509DE.png)
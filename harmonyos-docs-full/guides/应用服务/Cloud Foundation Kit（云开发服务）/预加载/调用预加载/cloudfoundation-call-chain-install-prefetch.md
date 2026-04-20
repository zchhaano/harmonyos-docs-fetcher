# 调用跳链安装预加载

  

在项目的EntryAbility.ets文件中导入预加载实现类[PrefetchWrapper](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-implementation-class#prefetchwrapper)，并在onCreate中调用PrefetchWrapper的doLinkPrefetch方法。方法内部会先调用[popDeferredLink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/applinking-deferredlink-api#popdeferredlink)接口获取延迟链接，再调用[getPrefetchResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cloudfoundation-cloudresprefetch#getprefetchresult)获取跳链安装预加载缓存数据。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/KfFQtriuQPGiwPRo5DGYLQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T191223Z&HW-CC-Expire=86400&HW-CC-Sign=BB973CC0D609EA5F0162B7B9387D793E3A8343B7FF37F7223E5772FD93580B39)   

跳链安装预加载缓存的是应用详情页数据，仅允许调用一次，被调用后将被销毁。

   

```
import { GlobalContext } from '../common/GlobalContext';
import { PrefetchWrapper } from '../prefetchUtil/PrefetchWrapper';

onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  GlobalContext.initContext(this.context); // 初始化全局上下文
  PrefetchWrapper.getInstance().doLinkPrefetch();
}

```
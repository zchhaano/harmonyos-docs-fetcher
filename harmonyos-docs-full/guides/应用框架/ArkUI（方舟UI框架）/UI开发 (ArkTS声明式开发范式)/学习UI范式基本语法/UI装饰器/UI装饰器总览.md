# UI装饰器总览

ArkUI包含的V2状态管理装饰器列表如下：

 展开

| V2状态管理装饰器 | 装饰器说明 |
| --- | --- |
| @ComponentV2 | 创建自定义组件。 |
| @Local | 组件内部状态。 |
| @Param | 组件外部输入。 |
| @Once | 初始化同步一次。 |
| @Event | 规范组件输出。 |
| @Provider | 与后代状态双向同步。 |
| @Consumer | 与祖先状态双向同步。 |
| @Monitor | 状态变量变化监听。 |
| @Computed | 计算属性。 |
| @ObservedV2 | 标记类可观察 |
| @Trace | 标记类属性可观察。 |
| @Type | 标记类属性的类型。 |
| @ReusableV2 | 标记组件可复用。 |

ArkUI包含的V1状态管理装饰器列表如下：

 展开

| V1状态管理装饰器 | 装饰器说明 |
| --- | --- |
| @Component | 创建自定义组件。 |
| @State | 基础状态变量。 |
| @Prop | 建立父子状态单向同步。 |
| @Link | 建立父子状态双向同步。 |
| @ObjectLink | 嵌套类对象属性变化观察。 |
| @Provide | 与后代状态双向同步。 |
| @Consume | 与祖先状态双向同步。 |
| @Watch | 状态变量变化监听。 |
| @StorageLink | 与AppStorage中对应的属性建立双向数据同步。 |
| @StorageProp | 与AppStorage中对应的属性建立单向数据同步。 |
| @LocalStorageLink | 与LocalStorage中对应的属性建立双向数据同步。 |
| @LocalStorageProp | 与LocalStorage中对应的属性建立单向数据同步。 |
| @Observed | 标记类可观察。 |
| @Track | 类对象属性级更新。 |
| @Reusable | 标记组件可复用。 |

ArkUI包含的通用UI装饰器列表如下：

 展开

| 通用装饰器 | 装饰器说明 |
| --- | --- |
| @Builder | 自定义构建函数。 |
| @LocalBuilder | 维持组件关系。 |
| @BuilderParam | 引用@Builder函数。 |
| @Styles | 定义组件重用样式。 |
| @Extend | 定义扩展组件样式。 |
| @AnimatableExtend | 定义可动画属性。 |
| @Require | 校验构造传参。 |
| @Env | 环境变量。 |
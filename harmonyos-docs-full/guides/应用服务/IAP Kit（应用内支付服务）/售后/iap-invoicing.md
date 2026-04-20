# 开票

    

#### 用户申请开发票

 

从6.1.0（23）开始，支持开发票功能。若用户购买应用内数字商品后需要申请开发票，可选择需要申请开票的订单后根据页面指引，提交开发票信息。

 

用户可按照以下步骤：

 

1. 选择“手机设置 > 华为账号 > 付款与账单 > 发票中心”，点击“开发票”，在需要开发票的订单后，点击“下一步”，进入“开发票”页面。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/yWrKSrw-Sc6-h3UfilV-aQ/zh-cn_image_0000002543214976.png?HW-CC-KV=V1&HW-CC-Date=20260420T191238Z&HW-CC-Expire=86400&HW-CC-Sign=D1E42D50F1A51B3ACB6E657505EDBBE6421A6BC2C4C6A1DE25621F27B7A60257)![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/63FaIE-hRpSkOsjSMbx31w/zh-cn_image_0000002573854891.png?HW-CC-KV=V1&HW-CC-Date=20260420T191238Z&HW-CC-Expire=86400&HW-CC-Sign=EE3029F84CF0BD5B1B8467F521A71D49256477A7F008ADBC00D602685804A810)
2. 在“开发票”页面，选择发票类型、抬头类型，输入发票抬头、税号和电子邮箱，然后提交开发票申请，提交后等待即可。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/jVXv8RLkSFKZ8Y2SCYmjlw/zh-cn_image_0000002573974869.png?HW-CC-KV=V1&HW-CC-Date=20260420T191238Z&HW-CC-Expire=86400&HW-CC-Sign=388D7F161695C49BDBA8EE900B810EABB3D4C3CA28B0C4973BDCC3273A454843)

 

用户提交开发票申请后，返回“发票中心”页面，在“我的发票”中查看所有订单的开发票状态。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/MW67iWWRRi6lmGPBmwtm6w/zh-cn_image_0000002543374640.png?HW-CC-KV=V1&HW-CC-Date=20260420T191238Z&HW-CC-Expire=86400&HW-CC-Sign=112C17E60DEAC0F0DC2E6F337EE4C6889C3AC753353C21BB36850BC83556F8DA)

    

#### 应用内接入开发票入口

 

**拉起开发票页面**

 

用户发起申请开发票后，应用客户端向IAP Kit发送[showManagedInvoices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-iap#iapshowmanagedinvoices)请求拉起开发票页面，请求中需携带待开发票的订单号（purchaseOrderId）。

 

**代码示例**

 

```
import { iap } from '@kit.IAPKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct IapTest {
  /**
   * 拉起开发票界面
   */
  showManagedInvoices() {
    const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // 调用iap.showManagedInvoices拉起开发票页面，传入context和purchaseOrderId
    let purchaseOrderId = '';
    iap.showManagedInvoices(context, purchaseOrderId).then(() => {
      // 请求成功
      console.info('Succeeded in showing invoice page.');
      // ...
    }).catch((err: BusinessError) => {
      // 请求失败
      console.error(`Failed to show invoice page. Code is ${err.code}, message is ${err.message}`);
      // ...
    });
  }
  build() {
  }
}

```
# 退款

  

当[用户申请退款](#用户申请退款)时，对于非游戏类应用，开发者可以在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上审核退款订单，实现用户的退款。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/CXiofUekTT29Gy3osdNT0w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=91955BC9442AD281EDDB11235B8A9186279C58F03B122F794982830F19DED084)   

- 退款只能由用户发起，具体参见[用户申请退款](#用户申请退款)。
- 对于游戏类应用，[用户申请退款](#用户申请退款)后，由华为游戏运营人员审核退款，开发者可跳过此章节。

     

#### 开发者审核退款订单

 

开发者使用退款管理功能，需要拥有至少一个具备退款权限的角色：账号持有者、管理员、App管理员、财务。具体可查看[添加成员账号](https://developer.huawei.com/consumer/cn/doc/app/agc-help-manageaccount-0000001099996700#section151241455193313)。

 

添加完账号后，开发者可按照以下步骤审核用户的退款订单：

 

1. 开发者登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“APP”。 在应用列表中点击待处理退款订单的应用。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/3wXJV7zyQuqwVJ7fwk6x5g/zh-cn_image_0000002543214970.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=6712DFAC29D75580203242E29E620138E5997F465D340619E804705A581722BA)
2. 在“运营”页签下，点击“产品运营 > 退款管理”，查看用户提交的退款申请，处理退款订单。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/QEUUlgA-TvaEbjnjQh0t8A/zh-cn_image_0000002573854885.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=514B51C0C26FAF3EA27BD2B968776920DAAD291B699FD2124E3A573EEE56C430)
3. 审核或查询退款订单。

 

**同意退款**：如果开发者同意退款，可在 “退款金额“下输入可退款金额，点击“同意”。在弹窗中点击“确认”，即可完成退款。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/zFzeVSyzQwiAXC5TsakWmw/zh-cn_image_0000002573974863.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=98AC99A5CFEE4427B54249A976CDA1A869A8259F3444B014C8BF24B8D9260938)

 

**驳回退款**：开发者不同意退款，可点击“驳回”，输入驳回原因，点击“确认”。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/DqLZxkPiQkepK780G1VKYQ/zh-cn_image_0000002543374634.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=E7B864389CFFEB36A1CD9F22784D617C54F317EC682F084CED9E747171796A2E)

 

**退款详情页面审核退款**：开发者也可以在退款详情页面审核退款，输入退款金额后选择“同意”或“驳回”，点击提交，完成审核。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/tFB9KMXvT5W4tRk0RbRRmg/zh-cn_image_0000002543214972.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=A30C61E32BAD5E6A312D4BDE2D21B28C00468B6915633F53B0727D4A56E6A87A)

 

**查询退款订单**：点击“已完成”页签，开发者可以查看所有已处理的退款订单。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/YilfJO3pRaegW0PLxiGLxQ/zh-cn_image_0000002573854887.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=FDF8C303BD6C959349F80AB6C211FA1F6634D800AC3BDE7BF664171611053893)

 

退款订单状态如下：

  

| 序号 | 退款订单状态 | 说明 |
| --- | --- | --- |
| 1 | 申请已拒绝 | 开发者驳回退款订单。 |
| 2 | 申请已通过 | 开发者同意退款订单。 |
| 3 | 退款成功 | 开发者同意退款，且华为操作退款成功。 |
| 4 | 退款失败 | 开发者同意退款，且华为操作退款失败。 |
| 5 | 超期未处理 | 开发者未按规定时间处理退款订单时，退款订单由华为运营进行审核。 |

    

#### 用户申请退款

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/VEjS4jQVTH-snYzvZwR48Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=634C0B59494BBF94923FB57239E15FD3EFCC72548392E6DCFF4AE08D794EBA69)   

- 生态应用订单退款最低系统版本要求为6.16.10（检查版本可参考以下路径“系统设置-华为账号-付款与账单-更多设置-关于”）。
- 退款申请后到退款完成非实时，一般从发起申请退款到完成需要7个工作日左右。

   

若用户购买应用内数字商品后需要申请退款，可选择某笔订单后根据页面指引，提交退款信息。开发者审核完成后，用户可收到退款金额。

 

用户可按照以下步骤申请订单退款：

 

1. 在“手机设置 > 华为账号 > 付款与账单 > 购买记录”中点击待退款的订单，跳转至详情页面，点击“对订单有疑问”。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/gXcktTs-QFidUotVPnAQEA/zh-cn_image_0000002573974865.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=7F6958249451B6696B72F2331D35B874D8561AB6CD32BF1A9F80D77E70E7BD84)![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/sNksFncZS-OSP0o3FabD8Q/zh-cn_image_0000002543374636.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=70EE3CD0627FCA3B04540994D2244A14877D3A0FC8EB79042954337B67055CB1)
2. 在“对订单有疑问”页面，点击“申请退款”，选择退款原因后，提交退款申请，提交后等待应用审核。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/txzKlfTRRpyK6nFNuYScTQ/zh-cn_image_0000002543214974.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=3E4618A4AF6BFBF4D52EC5DEC7B1F20C9AB121142351AC0BB1C2D591F8F035EF)![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/j-DNEKlvT0-dcD8SPJaFnA/zh-cn_image_0000002573854889.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=D978EBCB28D5137FDF7DC2E37FFAF3FC9B1621B6FD24FB955BEEF6CFACDA961E)

 

用户提交退款后，可点击“查看退款记录”，在“退款记录”查看所有退款订单的退款状态。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/LkQHf0xkRtyLPJUwJ7BL_A/zh-cn_image_0000002573974867.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=831DBEF1B90FC00E62F3EB8EC52AD2ED1ABF965495BE82751130C4240DD46315)![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/6JQ4j6xYRI2wRaSBCc9q9Q/zh-cn_image_0000002543374638.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=463138C606830758CBC52A45B9D2B29D71847D3E411BB4FA7572D6269A53C0F2)

    

#### 应用内接入退款入口

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/TBPO75TFTkWzuPJscRHVJA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T191236Z&HW-CC-Expire=86400&HW-CC-Sign=BDE1B91E9AE3FB27B997C8DBF1561116E5E4369DB4BE4464041200BDAF63124F)   

- 仅支持非游戏类应用接入。
- 该退款入口仅支持应用本身所产生的订单的退款。

   

**拉起退款**

 

用户发起退款后，应用客户端向IAP Kit发送[createRefundRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-iap#iapcreaterefundrequest)请求拉起退款页面，请求中需携带待退款的订单号（purchaseOrderId）。

 

**代码示例**

 

```
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {

  /**
   * 拉起退款界面
   */
  createRefundRequest(context: common.UIAbilityContext) {
    // 调用iap.createRefundRequest拉起退款，传入context和purchaseOrderId
    let purchaseOrderId = '';
    iap.createRefundRequest(context, purchaseOrderId).then(() => {
      // 退款成功
      console.info('Succeeded in creating refund request.');
      // ...
    }).catch((err: BusinessError) => {
      // 退款失败
      console.error(`Failed to create refund request. Code is ${err.code}, message is ${err.message}`);
      // ...
    });
  }

  build() {}
}

```
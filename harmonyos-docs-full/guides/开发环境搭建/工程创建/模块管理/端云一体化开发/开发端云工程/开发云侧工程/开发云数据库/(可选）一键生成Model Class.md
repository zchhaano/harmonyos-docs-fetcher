# (可选）一键生成Model Class

云数据库支持从端侧或者云侧云函数（含云对象）访问云数据库，代码涉及调用云数据库时，需引入对应云数据库对象类型的Model Class。当前支持为对象类型一键生成Server Model与Client Model，供您在端侧及云侧云函数（含云对象）开发时引用。

## 生成Server Model

1. 右击需要调用的对象类型文件（以“Post.json”为例），选择“Generate Server Model”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101936.87570849272403942922110362930070:50001231000000:2800:F65E4EEFD7E9E7CD0FFB0AF5DC539600493ADD7B1C873BDEA7B282AC81FCC5BF.png)
2. 选择生成的Server Model文件存放的云函数（或云对象）目录，以“id-generator”为例。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101936.22216459832529504276650921048097:50001231000000:2800:34BDEF02E48119434A9C8CF7A59E03CE23D8FF9D1711118A5F1B513AA5DB662A.png)
3. 点击“OK”。

指定目录下生成对应对象类型的Server Model文件，后续您便可以在代码中方便地引用该Server Model 。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101936.28287066711475170545037632470918:50001231000000:2800:4B5BDD29483F1FAD41024CC67078DAE086F09D042D458AC5469C098BB0F304D8.png)
4. 在云对象“id-generator”目录的package.json文件中引入@hw-agconnect/cloud-server依赖。收起自动换行深色代码主题复制

```
"dependencies" : { "@hw-agconnect/cloud-server" : "latest" }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101936.68299494947127302024652125918022:50001231000000:2800:F733095B503D7BCF441D4D87B5B18676D8CCED76DA6F22D6BD5C58C44A0BB7F2.png)
5. 在云对象文件idGenerator.ts中添加如下代码，实现云函数访问云数据库。收起自动换行深色代码主题复制

```
import { cloud } from '@hw-agconnect/cloud-server' ; import { Post } from './Post' ; // Post是Server Model // Demo是Post对象类型使用的存储区名 const collection = cloud. database ({ zoneName : 'Demo' }). collection ( Post ); // IdGenerator云对象，实现了对Post对象类型的查询和更新 export class IdGenerator { query ( ) { return collection. query (). get (); } upsert ( posts: Post[] ) { return new Promise ( ( resolve, reject ) => { collection. upsert (posts. map ( post => Post . parseFrom (post))) . then ( result => resolve ({ result })) . catch ( err => reject (err)) }); } }
```

 注意

如果定义的云数据库表字段中包含ByteArray或Date类型的字段，在插入或者更新云数据库时需要使用Server Model的parseFrom方法将入参转化成API识别的类型，例如上述示例中的Post.parseFrom方法。

## 生成Client Model

1. 右击需要调用的对象类型文件（以“Post.json”为例），选择“Generate Client Model”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101936.95966583020035901513380137979663:50001231000000:2800:298F7121392F289467C0D7437B97EE05836673629FE77A45FA8DE1CC57391BEA.png)
2. 选择生成的Client Model文件存放的端侧目录。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101936.86423000791244131442995143528381:50001231000000:2800:915AB08F08E9C4D45844D62294A4CC79D93B2ACC393B73ED41C764B3CBDE008E.png)
3. 点击“OK”。

指定目录下生成对应对象类型的Client Model文件，后续您便可以在端侧代码中方便地引用该Client Model，具体可参考端云一体化工程初始化代码中的Client Model示例（“ets/pages/CloudDb/Post.ts”）在CloudDb.ets以及DbInset.ets中的引用。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226101936.75833111076283881232129404539028:50001231000000:2800:C60A93B51B4ED35012827E37C918209071715F6C418030756C7B7FA5E7F66010.png)
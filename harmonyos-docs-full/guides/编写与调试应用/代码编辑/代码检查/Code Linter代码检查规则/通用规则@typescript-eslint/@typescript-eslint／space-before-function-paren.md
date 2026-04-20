# @typescript-eslint/space-before-function-paren

 

强制在函数名和括号之间保持一致的空格风格。

 ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/zjJv9UcoQGOHhnqawA5bAg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194015Z&HW-CC-Expire=86400&HW-CC-Sign=98A81753AD39DFA4ED0F37C3A063C271D22A848934ED6094D5813F7559062642) 

- 该规则默认要求函数名和括号间有空格。如需修改请参考[选项](#section182418564158)。
- 该规则建议在对.ts文件进行检查时使用。如需检查.ets文件，建议使用[@hw-stylistic/space-before-function-paren](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-space-before-function-paren-stylistic)。

  

#### 规则配置

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/space-before-function-paren": "error"
  }
}

```

  

#### 选项

详情请参考[@typescript-eslint/space-before-function-paren选项](https://eslint.nodejs.cn/docs/rules/space-before-function-paren#选项)。

  

#### 正例

```
// 默认foo和(之间需要一个空格
export function foo () {
  // ...
}

```

  

#### 反例

```
// 默认foo和(之间需要一个空格
export function foo() {
  // ...
}

```

  

#### 规则集

```
plugin:@typescript-eslint/all

```

 

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
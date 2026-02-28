# @typescript-eslint/init-declarations

禁止或者要求在变量声明中进行初始化。

## 规则配置

收起自动换行深色代码主题复制

```
// code-linter.json5 { "rules" : { "@typescript-eslint/init-declarations" : "error" } }
```

## 选项

详情请参考[@typescript-eslint/init-declarations选项](https://eslint.nodejs.cn/docs/rules/init-declarations#选项)。

## 正例

收起自动换行深色代码主题复制

```
// 默认变量必须在声明时初始化 export function foo ( ) { console . info ( 'hello' ); } export let bar = 1 ; export let qux = 3 ;
```

## 反例

收起自动换行深色代码主题复制

```
// 默认变量必须在声明时初始化 export function foo ( ) { console . info ( 'hello' ); } export let bar : string ; export let qux : number ;
```

## 规则集

收起自动换行深色代码主题复制

```
plugin :@ typescript - eslint / all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
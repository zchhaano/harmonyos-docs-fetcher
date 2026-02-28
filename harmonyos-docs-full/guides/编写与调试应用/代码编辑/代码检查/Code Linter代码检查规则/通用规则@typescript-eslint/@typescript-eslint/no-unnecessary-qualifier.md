# @typescript-eslint/no-unnecessary-qualifier

禁止不必要的命名空间限定符。

## 规则配置

收起自动换行深色代码主题复制

```
// code-linter.json5 { "rules" : { "@typescript-eslint/no-unnecessary-qualifier" : "error" } }
```

## 选项

该规则无需配置额外选项。

## 正例

收起自动换行深色代码主题复制

```
export enum A { b = 'x' , c = b } export namespace B { export type C = number ; export const x : C = 3 ; }
```

## 反例

收起自动换行深色代码主题复制

```
export enum A { b = 'x' , c = A. b } export namespace B { export type C = number ; export const x : B. C = 3 ; }
```

## 规则集

收起自动换行深色代码主题复制

```
plugin :@ typescript - eslint / all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
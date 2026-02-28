# @typescript-eslint/no-loss-of-precision

禁止使用失去精度的字面数字。

## 规则配置

收起自动换行深色代码主题复制

```
// code-linter.json5 { "rules" : { "@typescript-eslint/no-loss-of-precision" : "error" } }
```

## 选项

该规则无需配置额外选项。

## 正例

收起自动换行深色代码主题复制

```
export const a = 12345 ; export const b = 123.456 ; export const c = 123e34 ; export const d = 12300000000000000000000000 ; export const e = 0x1FFFFFFFFFFFFF ; export const f = 9007199254740991 ; export const g = 9007 _1992547409_91;
```

## 反例

收起自动换行深色代码主题复制

```
export const a = 9007199254740993 ; export const b = 5123000000000000000000000000001 ; export const c = 1230000000000000000000000.0 ; export const d = .1230000000000000000000000 ; export const e = 0X20000000000001 ; export const f = 0X2 _000000000_0001;
```

## 规则集

收起自动换行深色代码主题复制

```
plugin :@ typescript - eslint / all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
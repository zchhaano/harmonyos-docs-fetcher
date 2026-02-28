# @security/no-cycle

该规则禁止使用循环依赖。

## 规则配置

收起自动换行深色代码主题复制

```
// code-linter.json5 { "rules" : { "@security/no-cycle" : "error" } }
```

## 选项

该规则无需配置额外选项。

## 正例

收起自动换行深色代码主题复制

```
// foo.ets import {} from './bar' ; // bar.ets import {} from './index' ;
```

## 反例

收起自动换行深色代码主题复制

```
// foo.ets import {} from './bar' ; // bar.ets import {} from './foo' ;
```

 说明

反例中foo.ets文件依赖了bar.ets文件，bar.ets文件同时依赖了foo.ets文件，造成了循环依赖。

## 规则集

收起自动换行深色代码主题复制

```
plugin: @security / all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
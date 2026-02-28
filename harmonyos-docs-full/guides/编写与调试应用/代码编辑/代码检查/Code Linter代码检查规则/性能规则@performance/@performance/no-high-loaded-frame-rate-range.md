# @performance/no-high-loaded-frame-rate-range

不允许锁定最高帧率运行。

## 规则配置

收起自动换行深色代码主题复制

```
// code-linter.json5 { "rules" : { "@performance/no-high-loaded-frame-rate-range" : "warn" , } }
```

## 选项

该规则无需配置额外选项。

## 正例

收起自动换行深色代码主题复制

```
import { displaySync } from '@kit.ArkGraphics2D' ; let sync = displaySync. create (); sync. setExpectedFrameRateRange ({ expected : 60 , min : 45 , max : 60 , });
```

## 反例

收起自动换行深色代码主题复制

```
import { displaySync } from '@kit.ArkGraphics2D' ; let sync = displaySync. create (); sync. setExpectedFrameRateRange ({ expected : 120 , min : 120 , max : 120 , });
```

## 规则集

收起自动换行深色代码主题复制

```
plugin:@performance/ all plugin : @performance /recommended
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
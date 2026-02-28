# @performance/dark-color-mode-check

通过启用深色模式，可以进一步实现能耗的降低。应用需要根据当前设备状态来适配深色模式。

## 规则配置

```
// code-linter.json5
{
  "rules": {
    "@performance/dark-color-mode-check": "suggestion",
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```
src
├── main  
│   ├── ets    
│   └── resources
│       └── dark    
│           └── element
│               └── color.json     
│           
├── mock
│   └── mock-config.json5
```

## 反例

```
src
├── main  
│   ├── ets    
│   └── resources
│       └── dark    
│           └── element
│           
├── mock
│   └── mock-config.json5
```

## 规则集

```
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
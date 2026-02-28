## 场景介绍

开发者通过createJsCore方法来创建一个新的JS运行时环境，并通过该方法获得一个CoreID。然后，通过evaluateJS方法使用CoreID对应的运行环境来运行JS代码，在JS代码中创建promise并异步执行函数。最后，使用releaseJsCore方法来销毁CoreID对应的运行环境。

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-process)，本文仅对接口对应C++相关代码进行展示。

创建多个JS运行时环境并运行JS代码

 收起自动换行深色代码主题复制

```
```

预计的输出结果：

 收起自动换行深色代码主题复制

```
JSVM CreateJsCore START JSVM CreateJsCore END TEST coreId: 0 JSVM EvaluateJS START JSVM API TEST: hello World JSVM API TEST: CreatePromise start JSVM API TEST: CreatePromise end JSVM API TEST type: 4 JSVM API TEST: CreatePromise 0 JSVM API TEST RESULT: PASS JSVM EvaluateJS END TEST evaluateJS: hello World JSVM CreateJsCore START JSVM CreateJsCore END TEST coreId: 1 JSVM EvaluateJS START JSVM API TEST: second hello JSVM API TEST RESULT: PASS JSVM API TEST RESULT: PASS JSVM API TEST: CreatePromise start JSVM API TEST: CreatePromise end JSVM API TEST type: 4 JSVM API TEST: CreatePromise 1 JSVM API TEST RESULT: PASS JSVM EvaluateJS END TEST evaluateJS: second hello JSVM ReleaseJsCore START JSVM ReleaseJsCore END JSVM ReleaseJsCore START JSVM ReleaseJsCore END Test NAPI end
```
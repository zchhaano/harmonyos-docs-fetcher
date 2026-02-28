## 功能介绍

使用工具进行算子调测时，支持printf/PRINTF功能，可以打印Scalar数据。

 说明

- CPU调测场景支持printf和PRINTF打印，其中printf采用C++自身打印功能，不受dump-mode参数控制。

- simulator调测场景支持printf和PRINTF打印，受dump mode参数控制。

- 固定为每个核分配的打印数据的最大可使用空间为1M，目前该大小不支持修改，若打印超过1M，打印内容不再显示，请开发者控制待打印的数据量。

## 使用方法（命令行）

1. 在核函数代码中按需在目标位置加上printf或PRINTF语句，接口说明参见表1，以PRINTF打印为例：

收起自动换行深色代码主题复制

```
PRINTF ( "1 fmt string d %d\n" , 6666 ); PRINTF ( "1 fmt string lf %lf\n" , float ( 61.556 ));
```
2. simulator调测场景执行如下命令，使能Dump开关。

收起自动换行深色代码主题复制

```
ascendebug kernel --backend simulator --dump-mode normal ... {其他simulator调测参数}
```

--dump-mode取normal，开启通用打印Scalar模式，其他参数参考[NPU调测参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-cli-parameters#section1351011652416)按需配置。
3. 查看屏显打印结果，示例如下。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165310.49128559517997249612952796104384:50001231000000:2800:A2E79151509335DF6A20B28F138E8770FEA3FFC09FDAF821C4684A675FF49309.png)

## 接口说明

 **表1**printf/PRINTF接口说明表

| 函数原型 | template <class... Args> void printf(__gm__ const char* fmt, Args&&... args); void PRINTF(__gm__ const char* fmt, Args&&... args); |
| --- | --- |
| 函数功能 | 打印Scalar数据。 |
| 参数(IN) | fmt |
| args | 附加参数，个数和类型可变的输出列表：根据不同的fmt字符串，函数可能需要一系列的附加参数，每个参数包含了一个要被插入的值，替换了fmt参数中指定的每个%标签。参数的个数应与%标签的个数相同。 |
| 参数(OUT) | NA |
| 返回值 | NA |
| 使用约束 | 不支持转义字符打印。 当前支持的打印类型： %d / %i：输出十进制数。 %f：输出实数。 %x：输出十六进制整数。 %s：输出字符串。 %u：输出unsigned类型数据。 %p：输出指针地址。 |
| 调用示例 | 收起 自动换行 深色代码主题 复制 // 整型打印： printf ( "fmt string %d" , 0x123 ); PRINTF ( "fmt string %d" , 0x123 ); // 指针打印： int *a; printf ( "TEST %p" , a); PRINTF ( "TEST %p" , a); |
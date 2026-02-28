## 函数功能

封装算子的InferShape函数。

该函数传入的OpType为基于Operator类派生出来的子类，会自动生成一个类型为此子类的对象op，可以使用子类的成员函数获取输入输出描述的方法，从而进行InferShape的实现。

基于OpType派生出来的子类op的成员函数如下。

- op.set_input_*x*(Operator &v, const string &srcName)：将网络中算子v的输出srcName设置为当前算子的输入x。
- op.get_input_desc_*x*()：获取该算子的输入x的描述信息，返回对象为TensorDesc类型。

op.update_input_desc_*x*(const TensorDesc& tensorDesc)：更新输入x的描述信息，包括shape、datatype与format。
- op.get_output_desc_*y*()：获取该算子的输出y的描述信息，返回对象TensorDesc类型。
- op.update_output_desc_*y*(const TensorDesc& tensorDesc)：更新输出y的描述信息，包括shape、datatype与format。
- op.get_attr_*attr1*(AscendString &val)：获取算子属性attr1的值val。

## 函数原型

收起自动换行深色代码主题复制

```
IMPLEMT_INFERFUNC (op_name, func_name)
```

## 约束说明

无

## 参数说明

 展开

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| op_name | 输入 | 算子类型。 |
| func_name | 输入 | InferShape函数名，开发者自定义。 |

## 返回值

无
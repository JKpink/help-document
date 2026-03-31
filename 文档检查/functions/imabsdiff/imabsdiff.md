## imabsdiff
计算两幅图像的绝对差值

## 简介
[`Z = imabsdiff(X, Y)`](#function1)

## 用法
<a id="function1"></a>
[Z](#Q3) = imabsdiff([X](#Q1), [Y](#Q2)) 将数组 `X` 中每个元素减去数组 `Y` 中对应位置的元素，并将差值的绝对值返回至输出数组 `Z` 的对应位置。

## 参数说明
### 输入参数
**<a id="Q1"></a> X — 输入图像**  
数值数组

输入图像：指定为任意维度的数值数组。

**数据类型**：`single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`

**<a id="Q2"></a> Y — 输入图像**  

数值数组

输入图像：指定为数值数组。`Y` 必须与 `X` 尺寸和数据类型完全相同。

数据类型：`single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`

### 输出参数
**<a id="Q3"></a> Z — 差值图像**  
数值数组

差值图像：返回为数值数组。`Z` 与 `X`、`Y` 尺寸和数据类型相同。若 `X` 和 `Y` 为整数数组，则 `imabsdiff` 会截断输出中超出该整数类型数值范围的元素。

## 提示
- 如果 `X` 属于 double 类，则使用表达式 abs(X-Y) 而不是此函数。
- 如果 `X` 属于 logical 类，则使用表达式 XOR(X,Y) 而不是此函数。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imadd/imadd.html">imadd</a> | <a 
href="../imcomplement/imcomplement.html">imcomplement</a> | <a 
href="../imdivide/imdivide.html">imdivide</a> | <a 
href="../imlincomb/imlincomb.html">imlincomb</a> | <a 
href="../immultiply/immultiply.html">immultiply</a> | <a 
href="../imsubtract/imsubtract.html">imsubtract</a> 

## imadd
两幅图像相加或者向图像叠加常数

## 简介
[`Z = imadd(X, Y)`](#function1)

## 用法
<a id="function1"></a>
[Z](#Q3) = imadd([X](#Q1), [Y](#Q2)) 将数组 `X` 中每个元素与数组 `Y` 中对应位置的元素相加，并将求和结果返回至输出数组 `Z` 的对应位置。

## 参数说明c
### 输入参数
**<a id="Q1"></a> X — 第一个数组**  
数值数组 | 逻辑数组

第一个数组：指定为任意维度的数值数组或逻辑数组。

**<a id="Q2"></a> Y — 第二个数组**  
数值标量 | 数值数组 | 逻辑数组

要与 `X` 相加的第二个数组：指定为与 `X` 尺寸和数据类型相同的数值 / 逻辑数组，或 `double` 类型的数值标量。

### 输出参数
**<a id="Q3"></a> Z — 求和结果**  
数值数组

求和结果：返回为与 `X` 尺寸相同的数值数组。`Z` 的数据类型与 `X` 一致，除非 `X` 为逻辑类型（此时 `Z` 为 `double` 类型）。若 `X` 为整数数组，输出中超出该整数类型数值范围的元素会被截断，小数部分会被四舍五入。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imabsdiff/imabsdiff.html">imabsdiff</a> | <a 
href="../imcomplement/imcomplement.html">imcomplement</a> | <a 
href="../imdivide/imdivide.html">imdivide</a> | <a 
href="../imlincomb/imlincomb.html">imlincomb</a> | <a 
href="../immultiply/immultiply.html">immultiply</a> | <a 
href="../imsubtract/imsubtract.html">imsubtract</a> 

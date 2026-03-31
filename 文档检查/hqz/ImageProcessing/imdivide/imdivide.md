## imdivide
一幅图像除以另一幅图像或者图像除以常数

## 简介
[`Z = imdivide(X, Y)`](#function1)

## 用法
<a id="function1"></a>
[Z](#Q3) = imdivide([X](#Q1), [Y](#Q2)) 将数组 `X` 中的每个元素除以数组 `Y` 中对应位置的元素，并将商返回至输出数组 `Z` 的对应位置。

## 输入参数
**<a id="Q1"></a> X — 第一个数组**  
数值数组 | 逻辑数组

第一个数组（被除数）：指定为任意维度的数值数组或逻辑数组。

**<a id="Q2"></a> Y — 第二个数组**  
数值标量 | 数值数组 | 逻辑数组

要除以 `X` 的第二个数组（除数）：指定为与 `X` 尺寸和数据类型相同的数值 / 逻辑数组，或 `double` 类型的数值标量。

### 输出参数
**<a id="Q3"></a> Z — 商**  
数值数组

商：返回为与 `X` 尺寸相同的数值数组。`Z` 的数据类型与 `X` 一致，除非 `X` 为逻辑类型（此时 `Z` 为 `double` 类型）。若 `X` 为整数数组，输出中超出该整数类型数值范围的元素会被截断，小数部分会被四舍五入。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
 <a href="../imabsdiff/imabsdiff.html">imabsdiff</a> | <a 
href="../imadd/imadd.html">imadd</a> | <a 
href="../imcomplement/imcomplement.html">imcomplement</a> | <a 
href="../imlincomb/imlincomb.html">imlincomb</a> | <a 
href="../immultiply/immultiply.html">immultiply</a> | <a 
href="../imsubtract/imsubtract.html">imsubtract</a>


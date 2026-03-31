## imsubtract
图像的减运算

## 简介
[`Z = imsubtract(X, Y)`](#function1)

## 用法
<a id="function1"></a>
[Z](#Q3) = imsubtract([X](#Q1), [Y](#Q2))  将数组 `X`（被减数）中每个元素减去数组 `Y`（减数）中对应位置的元素，差值结果存储在输出数组 `Z` 的对应位置：

- 若 `Y` 为标量，则 `X` 中所有元素均减去该标量；
- 若输入为整数数组，运算结果中**负数会被截断为 0**，小数部分会被舍入；
- 若 `X` 为逻辑数组，输出 `Z` 自动转为 `double` 类型（`true=1`，`false=0`）。

## 参数说明
### 输入参数
**<a id="Q1"></a> X — 第一个数组**  
数值数组 | 逻辑数组

被减数数组：指定为任意维度的数值数组（如灰度图像）或逻辑数组。

**<a id="Q2"></a> Y — 第二个数组**  
数值标量 | 数值数组 | 逻辑数组

减数数组，需满足以下规则：

- 与 `X` 尺寸、数据类型完全相同的数值 / 逻辑数组；
- 或 `double` 类型的数值标量（如常数 50）。

### 输出参数
**<a id="Q3"></a> Z — 差**  
数值数组

差值结果，返回为与 `X` 尺寸相同的数值数组：

- 若 `X` 为数值类型（如 `uint8`/`double`），`Z` 与 `X` 数据类型相同；
- 若 `X` 为逻辑类型，`Z` 为 `double` 类型；
- 若 `X` 为整数数组，超出该类型范围的元素会被截断（如负数→0），小数部分舍入。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
 <a href="../imabsdiff/imabsdiff.html">imabsdiff</a> | <a 
href="../imadd/imadd.html">imadd</a> | <a 
href="../imcomplement/imcomplement.html">imcomplement</a> | <a 
href="../imdivide/imdivide.html">imdivide</a> | <a 
href="../imlincomb/imlincomb.html">imlincomb</a> | <a 
href="../immultiply/immultiply.html">immultiply</a> 


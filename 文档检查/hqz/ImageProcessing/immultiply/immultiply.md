## immultiply
图像逐元素相乘

## 简介
[`Z = immultiply(X, Y)`](#function1)

## 用法
<a id="function1"></a>
[Z](#Q3) = immultiply([X](#Q1), [Y](#Q2)) 将数组 `X` 中的每个元素与数组 `Y` 中对应位置的元素相乘，乘积结果存储在输出数组 `Z` 的对应位置。

- 若 `Y` 为标量，则 `X` 中所有元素均与该标量相乘；
- 运算时先以双精度浮点数逐元素计算，若输入为整数类型，最终结果会截断超出类型范围的元素并舍入小数部分。

## 参数说明
### 输入参数
**<a id="Q1"></a> X — 第一个数组**  
数值数组 | 逻辑数组

第一个输入数组，指定为任意维度的数值数组或逻辑数组。

**<a id="Q2"></a> Y — 第二个数组**  
数值标量 | 数值数组 | 逻辑数组

与 `X` 相乘的第二个数组，指定为数值标量、数值数组或逻辑数组，需满足以下规则：
- 如果 `X` 是数值数组，则 `Y` 的大小和类可以是以下值之一：

  - `Y` 与 `X` 的大小和类相同。
  - `Y` 与 `X` 的大小相同，并且为逻辑数组。
  - `Y` 是双精度浮点类型的标量。
- 如果 `X` 是逻辑数组，则 `Y` 必须与 `X` 具有相同的大小。`Y` 可以是任何类。

### 输出参数
**<a id="Q3"></a> Z — 乘积**  
数值数组

乘积结果，返回为数值数组：

- 若 `X` 为数值类型，`Z` 与 `X` 尺寸、类型均相同；
- 若 `X` 为逻辑类型，`Z` 与 `Y` 尺寸、类型均相同。
  -  注：`immultiply` 先以双精度浮点数逐元素计算乘积，若输入为整数数组，最终会截断超出该整数类型范围的元素，并对小数部分舍入。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
 <a href="../imadd/imadd.html">imadd</a> | <a 
href="../imcomplement/imcomplement.html">imcomplement</a> | <a 
href="../imdivide/imdivide.html">imdivide</a> | <a 
href="../immultiply/immultiply.html">immultiply</a> | <a 
href="../imsubtract/imsubtract.html">imsubtract</a>




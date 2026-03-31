## imlincomb
图像的线性组合运算

## 简介
[`Z = imlincomb(K1, A1, K2, A2, …, Kn, An)`](#function1)  
[`Z = imlincomb(K1, A1, K2, A2, …, Kn, An, K)`](#function2)

## 用法
<a id="function1"></a>
[Z](#Q4) = imlincomb([K1](#Q1), [A1](#Q2), [K2](#Q1), [A2](#Q2), …, [Kn](#Q1), [An](#Q2)) 计算多张图像 `A1, A2, …, An` 的线性组合，其中 `K1, K2, …, Kn` 为对应图像的权重系数，运算公式为：
$$
Z = K_1 \times A_1 + K_2 \times A_2 + \dots + K_n \times A_n
$$
<a id="function2"></a>
[Z](#Q4)  = imlincomb([K1](#Q1), [A1](#Q2), [K2](#Q1), [A2](#Q2), …, [Kn](#Q1), [An](#Q2), [K](#Q3)) 在上述线性组合基础上增加偏移量 `K`，运算公式为：
$$
Z = K_1 \times A_1 + K_2 \times A_2 + \dots + K_n \times A_n+K
$$

## 参数说明
### 输入参数
**<a id="Q1"></a> K1， K2， Kn — 图像系数**  
数值标量

图像的权重系数，指定为数值标量。

**数据类型：**  `double` 

**<a id="Q2"></a> A1， A2， An — 输入图像**  
数值数组

输入图像，指定为尺寸和数据类型完全相同的数值数组。

**<a id="Q3"></a> K — 偏移**  
数值标量

线性组合的偏移量，指定为数值标量。

**数据类型：**  `double` 

### 输出参数
**<a id="Q4"></a> Z — 线性组合图像**  
数值数组

线性组合后的图像，返回为与 `A1` 尺寸相同的数值数组：

- 若 `A1` 为逻辑类型，`Z` 为 `double` 类型；否则 `Z` 与 `A1` 数据类型相同。

## 提示
对多张图像执行连续算术运算时，使用 `imlincomb` 比嵌套调用 <a href="../imadd/imadd.html">imadd</a>/<a 
href="../imdivide/imdivide.html">imdivide</a> 等单个算术函数能获得更高精度：

- 嵌套调用时，若输入为整数类型，每个函数都会先截断 / 舍入结果再传递给下一个函数，导致精度损失；
- `imlincomb` 先以双精度浮点数逐元素完成所有运算，仅在最终输出时（若为整数类型）裁剪超出范围的元素、舍入小数部分，最大程度保留精度。

## 版本历史
在北太天元图像处理工具箱 V1.1 推出

## 相关主题
 <a href="../imadd/imadd.html">imadd</a> | <a 
href="../imcomplement/imcomplement.html">imcomplement</a> | <a 
href="../imdivide/imdivide.html">imdivide</a> | <a 
href="../immultiply/immultiply.html">immultiply</a> | <a 
href="../imsubtract/imsubtract.html">imsubtract</a>


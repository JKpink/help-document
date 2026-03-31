## houghpeaks
计算 Hough 变换中的峰值

## 简介
[`peaks = houghpeaks(H, numpeaks)`](#function1)  
[`peaks = houghpeaks(H, numpeaks, Name, Value)`](#function2)

## 用法
<a id="function1"></a>
[peaks](#Q1) = houghpeaks([H](#Q2), [numpeaks](#Q3)) 定位由 <a href="../hough/hough.html">hough</a> 函数生成的霍夫变换矩阵 H （行和列对应于 `rho` 和 `theta` 值）中的峰值。`numpeaks` 指定要识别的最大峰值个数。该函数返回 `peaks`，即一个保留峰值的行和列坐标的矩阵。  
<a id="function1"></a>
[peaks](#Q1) = houghpeaks([H](#Q2), [numpeaks](#Q3), [Name, Value](#Q4)) 使用名称-值对组参量控制运算的各个方面。

## 参数说明
### 输入参数
**<a id="Q2"></a> H — 霍夫变换矩阵**  
数值数组

霍夫变换矩阵，指定为数值数组。行和列对应于 `rho` 和 `theta` 值，使用 `hough` 函数创建一个霍夫变换矩阵。

**数据类型：** `double`

**<a id="Q3"></a> numpeaks — 要识别的最大峰值个数**  
1 (默认) | 正整数

要识别的最大峰值个数，指定为正整数。

**数据类型：** `double`

**<a id="Q4"></a> 名称-值参数**  

将可选的参量对组指定为 Name1，Value1,...,NameN，ValueN，其中 Name 是参量名称，Value 是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。

**Threshold — 被视为峰值的最小值**  
0.5*max(H(:\)) (默认) | 非负数

被视为峰值的最小值，指定为非负数。

**数据类型：** `double`

**NHoodSize — 隐藏邻域的大小**  
由正奇数组成的二元素向量

隐藏邻域的大小，指定为由正奇数组成的二元素向量。隐藏邻域是每个峰值周围的邻域，在识别出峰值后，该值设置为零。`NHoodSize` 的默认值为大于或等于size(H)/50 的最小奇数值。`NHoodSize` 的维数必须小于霍夫变换矩阵 H 的大小。

**数据类型**: `double`

**Theta — 霍夫变换 theta 值**  
-90:89 (默认) | 数值向量

霍夫变换 `theta` 值，指定为由`hough` 函数返回的数值向量。向量的每个元素指定输出矩阵H的对应列的 `theta` 值。`houghpeaks` 使用为峰值隐藏指定的 `theta` 值。使用 `hough` 函数创建一个霍夫变换矩阵。

**数据类型：** `double`

### 输出参量
**<a id="Q1"></a> peaks — 找到的峰值的行和列坐标**  
Q×2 矩阵

找到的峰值的行和列坐标，以 `Q×2` 矩阵形式返回。值 `Q` 的范围可以从 0 到[numpeaks](#Q3)。

## 版本历史
在北太天元图像处理工具箱 V1.1 推出

## 相关主题
<a href="../hough/hough.html">hough</a> | <a 
href="../houghlines/houghlines.html">houghlines</a> 

## imapplymatrix
颜色通道的线性组合

## 简介
[`Y = imapplymatrix(M, X)`](#function1)  
[`Y = imapplymatrix(M, X, C)`](#function2)

## 用法
<a id="function1"></a>
[Y](#Q4) = imapplymatrix([M](#Q1), [X](#Q2)) 计算矩阵 `M` 的行与 `X` 的颜色通道的线性组合。

<a id="function2"></a>
[Y](#Q4)  = imapplymatrix([M](#Q1), [X](#Q2), [C](#Q3)) 计算矩阵 `M` 的行与 `X` 的颜色通道的线性组合，并且向每个组合添加相应的常数 C 。

## 参数说明
### 输入参数
**<a id="Q1"></a> M — 每个颜色通道的加权系数**  
q×p 数值数组

每个颜色通道的加权系数，指定为 q×p 数值数组。p 是 [X](#Q2) 的第三维的长度。换句话说，p=size(X,3)。q 在 [1,p] 范围内。

**<a id="Q2"></a> X — 输入图像**  
m×n×p 数值数组

输入图像，指定为 m×n×p 数值数组。

**<a id="Q3"></a> C — 要添加到每个通道的常数**  
q 元素数值向量

线性组合期间添加到每个通道的常量，指定为 q 元素数字向量，其中 q 是 [M](#Q1) 中的行数。

**数据类型：**  `double` 

### 输出参数
**<a id="Q4"></a> Y — 输出图像**  
数值数组

输出图像由 `M` 行与 `X` 颜色通道的线性组合组成，以数值数组形式返回。如果未指定 `output_type`  ，则 `Y` 的数据类型与 `X` 的数据类型相同。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imlincomb/imlincomb.html">imlincomb</a> | <a 
href="../immultiply/immultiply.html">immultiply</a> 

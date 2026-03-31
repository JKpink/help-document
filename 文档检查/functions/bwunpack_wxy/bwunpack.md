## bwunpack  
解包打包后的二值图像

## 简介  
[ `BW = bwunpack(BWP, m)`](#function1)

## 用法  
<a id="function1"></a>
[BW](#Q1) = bwunpack([BWP](#Q2), [m](#Q3))将打包后的二值图像 [`BWP`](#Q2) 解包为具有 [`m`](#Q3) 行的二维逻辑二值图像 [`BW`](#Q1) ，还原 bwpack 函数的打包操作，恢复原始二值图像的像素分布。解包逻辑为将 [`BWP`](#Q2) 中每个 uint32 元素的比特位反向映射为单个像素（最低有效位对应 [`BW`](#Q1) 首行像素，最高有效位对应 [`BW`](#Q1) 第 32 行像素），最终输出指定行数的逻辑矩阵。

## 参数说明  
### 输入参数  
**<a id="Q2"></a>BWP — 打包后的二值图像**
二维数值数组

仅支持二维的 uint32 类型数值数组；
为 bwpack 函数输出的打包二进制图像，每个元素的比特位映射原始二值图像的 32 个像素。

**数据类型：** `uint32`

**<a id="Q3"></a>m — 输出图像的行数**
正整数

需指定为正整数，对应解包后二值图像 BW 的行数；
默认值为 32*size(BWP,1)（即打包前原始图像的默认行数）。

**数据类型：** `uint32`

## 输出参数  
**<a id="Q1"></a>BW — 解包后的二值图像**
m 行 n 列逻辑矩阵

解包后的二维二值图像，以 logical 类型矩阵形式返回，行数为指定的 m，列数与输入 BWP 的列数一致；矩阵中每个元素为逻辑值（true/false），对应原始二值图像的像素状态（1/0）。

**数据类型：** `logical`

## 版本历史  
在北太天元图像处理工具箱 V3.0 推出

## 相关主题  
<a href="../bwpack/bwpack.html">bwpack</a> | <a
href="../imdilate/imdilate.html">imdilate</a> | <a
ref="../imerode/imerode.html">imerode</a> | <a
href="../bwarea/bwarea.html">bwarea</a>
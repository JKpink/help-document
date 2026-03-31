## superpixels

2-D 图像的超像素过分割处理

## 简介

[[L, numLabels] = superpixels(A, N)](#functions)

[[L, numLabels] = superpixels(A, N, Name, Value)](#function2)

## 用法

<a id="function1"></a>

[[L](#Q4), [numLabels](#Q5)] = superpixels([A](#Q2), [N](#Q2))计算二维灰度或 RGB 图像的超像素。参数N指定想要创建的超像素数量。函数返回标签矩阵L以及实际计算出的超像素数量numLabels。

该函数采用简单线性迭代聚类（SLIC）算法 [[1]](#1)，将像素分组为具有相似值的区域。在分割等图像处理操作中使用这些区域，可降低操作的复杂度。

<a id="function2"></a>

[[L](#Q4), [numLabels](#Q5)] = superpixels([A](#Q2), [N](#Q2), Name,Value) 通过名称 - 值参数控制分割的相关特性，计算图像A的超像素。

## 参数说明

### 输入参数

<a id="Q2"></a> A — 待分割图像

二维灰度图像 | 二维真彩色图像

待分割的图像，指定为二维灰度图像或二维真彩色图像。当 `IsInputLab` 为 `true` 且数据类型为 `int16` 时，`A` 必须是灰度图像；当 `IsInputLab` 为 `true` 时，输入图像的数据类型必须为 `single` 或 `double`。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16`

<a id="Q3"></a> N — 期望的超像素数量

正整数

期望创建的超像素数量，指定为正整数。

**数据类型：** `double`

### 输出参数

**<a id="Q4"></a>L — 标签矩阵**

正整数数组

标签矩阵，以正整数数组形式返回。其中数值 1 表示第一个超像素区域，数值 2 表示第二个超像素区域，依此类推，覆盖图像中所有超像素区域。

**数据类型：** `double`

<a id="Q5"></a>**numLabels — 实际计算的超像素数量**

正整数

实际计算出的超像素数量，以正整数形式返回。

**数据类型：** `double`

## 参考文献

<a id="1"></a>[1] Radhakrishna Achanta, Appu Shaji, Kevin Smith, Aurelien Lucchi, Pascal Fua, and Sabine Susstrunk, SLIC Superpixels Compared to State-of-the-art Superpixel Methods. IEEE Transactions on Pattern Analysis and Machine Intelligence, Volume 34, Issue 11, pp. 2274-2282, May 2012

## 版本历史

在北太天元图像处理工具箱 V3.0 推出

## 相关主题

 <a href="../boundarymask/boundarymask.html">boundarymask</a> | <a href="../imoverlay/imoverlay.html">imoverlay</a> | <a href="../label2idx/label2idx.html">label2idx</a> | <a href="../label2rgb/label2rgb.html">label2rgb</a> | <a href="../hyperslic/hyperslic.html">hyperslic</a>
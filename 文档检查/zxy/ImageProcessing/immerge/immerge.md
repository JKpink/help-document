## immerge
将多个单通道图像合并为多通道图像

## 简介
[`out = immerge(c1, c2, c3, ..., ck)`](#function1)

## 用法
<a id="function1"></a>
[out](#P1) = immerge[(c1, c2, c3, ..., ck)](#Q1) 将 k 个通道图像进行合并，组成多通道图像。

## 参数说明
### 输入参数
**<a id="Q1"></a> c1, c2, c3, ..., ck — 输入每个通道的图像**  
每个通道的数值矩阵

输入图像，以 k 个单独的数字矩阵形式输入，其中 k 是通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数
**<a id="P1"></a> I — 输出图像**  
m×n×k 数值数组

输出图像，以 m×n×k 数值数组形式返回，其中 k 是输入图像中的通道数。输出图像与输入图像是同一数据类型。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../im2gray/im2gray.html">im2gray</a> | <a
href="../imsplit/imsplit.html">imsplit </a>

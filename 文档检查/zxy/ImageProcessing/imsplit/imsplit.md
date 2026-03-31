## imsplit
将多通道图像拆分为独立的单通道图像

## 简介
[`[c1, c2, c3, ..., ck] = imsplit(I)`](#function1)  

## 用法
<a id="function1"></a>
[[c1, c2, c3, ..., ck]](#P1) = imsplit([I](#Q1)) 将多通道图像 `I` 拆分为 k 个独立的单通道图像，其中 c1 对应第 1 通道、c2 对应第 2 通道，……，ck 对应第 k 通道。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
m×n×k 数值数组

输入的多通道图像，指定为 m×n×k 数值数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数
**<a id="P1"></a> c1, c2, c3, ..., ck — 输出每个通道的图像**  
每个通道的数值矩阵

输出图像，以 k 个单独的数字矩阵形式返回，其中 k 是输入图像中的通道数。输出图像与输入图像是数据类型一致。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../cat/cat.html">cat</a> | <a
href="../im2gray/im2gray.html">im2gray </a>

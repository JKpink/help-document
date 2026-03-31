## grayconnected
确定相似的灰度区域

## 简介
[`BW = grayconnected(I, row, column)`](#function1)  
[`BW = grayconnected(I, row, column, tolerance)`](#function2)

## 用法
<a id="function1"></a> [BW](#Q2) = grayconnected([I](#Q1), [row](#Q3), [column](#Q4)) 在灰度图像 `I` 中找到相似强度的连接区域。指定起点（种子像素）的行和列索引。该函数返回一个二进制掩码 BW，该二进制掩码指示哪些像素以相似的强度 8 连接到种子像素。  
<a id="function2"></a> [BW](#Q2) = grayconnected([I](#Q1), [row](#Q3), [column](#Q4), [tolerance](#Q5)) 指定要包括在掩码中的强度值的范围，如 [(seedvalue-tolerance), (seedvalue+tolerance)]。

## 参数说明
### 输入参数
**<a id="Q1"></a> I —— 灰度图像**  
二维数值矩阵

灰度图像，指定为数值矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

**<a id="Q3"></a> row —— 种子像素的行索引**  
正整数

种子像素的行索引，指定为正整数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

**<a id="Q4"></a> column —— 种子像素的列索引**  
正整数

种子像素的列索引，指定为正整数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

**<a id="Q5"></a> tolerance —— 强度值的容差**  
数值标量

掩码中包含的强度值的容差，指定为数值标量。掩码包括所有值在范围 `[(seedvalue-tolerance),(seedvalue+tolerance)]` 内的像素。默认情况下，容差为整数图像的 32 和浮点数图像的 0.1。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出参数
**<a id="Q2"></a> BW —— 二值掩码**  
逻辑矩阵

连接区域的二进制掩码，以与 `I` 相同大小的逻辑数组形式返回。所有前景像素都表示与种子像素具有相似强度的 8 连接图像像素。

**数据类型：** `logical`

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imfill/imfill.html">imfill</a> | <a 
href="../bwselect/bwselect.html">bwselect</a> | <a 
href="../Image Segmenter/Image Segmenter.html">Image Segmenter</a> 


## medfilt2
二维中位数滤波

## 简介
[ `J = medfilt2(I)`](#function1)  
[ `J = medfilt2(I, [m n])`](#function2)  
[ `J = medfilt2(___, padopt)`](#function3)

## 用法
<a id="function1"></a>
[J](#Q4) = medfilt2([I](#Q1)) 对图像 `I` 执行二维中位数滤波，每个输出像素包含输入图像中对应像素周围 3×3 邻域的中位数值。  
<a id="function2"></a>
[J](#Q4) = medfilt2([I](#Q1), [[m n]](#Q2)) 执行中位数滤波，其中每个输出像素包含输入图像中对应像素周围的 m×n 邻域中的中位数值。  
<a id="function3"></a>
[J](#Q4) = medfilt2(___, [padopt](#Q3)) 控制 `medfilt2` 如何填充图像边界。

## 参数说明
### 输入参数
**<a id="Q1"></a>I — 输入图像**  
二维灰度图像 | 二维二值图像

输入图像，指定为二维灰度图像或二值图像。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`

**<a id="Q2"></a>[m n] — 邻域大小**  
[3 3]（默认）| 二元数值向量

邻域大小，指定为由正整数组成的二元向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q3"></a>padopt — 填充选项**  
"zeros"（默认）| "symmetric"

填充选项，指定为下列值之一：

| **值** | **描述** |
|:--|:--|
| "zeros"（默认值） |用 0 填充图像。|
| "symmetric" |在边界处对称延伸图像。|  
**数据类型：** `char` | `string`

### 输出参数
**<a id="Q4"></a>J — 输出图像**  
数值矩阵

含噪图像，以与输入图像 [`I`](#Q1) 具有相同数据类型的数值矩阵形式返回。

## 参考文献
[1] Lim Jae S. Two-Dimensional Signal and Image Processing. Englewood Cliffs, NJ: Prentice Hall, 1990: 469-476.

## 版本历史
在北太天元图像处理工具箱 V1.0 推出 

##相关主题
<a href="../ordfilt2/ordfilt2.html">ordfilt2</a> | <a 
href="../wiener2/wiener2.html">wiener2</a> | <a 
href="../medfilt3/medfilt3.html">medfilt3</a> 
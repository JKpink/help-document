## wiener2
二维自适应去噪滤波

## 简介
[ `J = wiener2(I）`](#function1)  
[ `J = wiener2(I, [m n], noise)`](#function1)

## 用法
<a id="function1"></a>
[J](#Q4) = wiener2([I](#Q1), [[m n]](#Q2), [noise](#Q3)) 使用像素级自适应低通 Wiener 滤波器对灰度图像 `I` 进行滤波，`[m n]` 指定用于估计局部图像均值和标准差的邻域的大小 (m×n)，加性噪声（高斯白噪声）功率假定为 `noise`。

输入图像的质量已被恒定功率加性噪声降低。`wiener2` 基于从每个像素的局部邻域估计的统计量使用像素级自适应 Wiener 方法。

## 参数说明
### 输入参数
**<a id="Q1"></a>I — 输入图像**  
二维数值数组

输入图像，指定为二维数值数组。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16`

**<a id="Q2"></a>[m n] — 邻域大小**  
[3 3]（默认）| 二元数值向量

邻域大小，指定为 [m n] 形式的二元向量，其中 m 是行数，n 是列数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q3"></a>noise — 加性噪声**  
数值数组

加性噪声，指定为数值数组。如果不指定噪声，则 `wiener2` 使用局部方差的均值，即 mean2(localVar)。

**数据类型：** `double`

### 输出参数
**<a id="Q4"></a>J — 滤波后的图像**  
数值数组

滤波后的图像，以与输入图像 [`I`](#Q1) 大小和数据类型相同的数值数组形式返回。

## 参考文献
[1] Lim Jae S. Two-Dimensional Signal and Image Processing. Englewood Cliffs, NJ: Prentice Hall, 1990.

## 版本历史
在北太天元图像处理工具箱 V1.0 推出 

##相关主题
<a href="../medfilt2/medfilt2.html">medfilt2</a> | <a 
href="../deconvwnr/deconvwnr.html">deconvwnr</a>

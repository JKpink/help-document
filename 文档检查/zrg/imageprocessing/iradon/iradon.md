## iradon 
逆 Radon 变换

## 简介
[ `I = iradon(R, theta)`](#function1)

[ `I = iradon(R, theta, interp, filter, frequencyScaling, outputSize)`](#function2)

## 用法
<a id="function1"></a>
[I](#Q1) = iradon([R](#Q2), [theta](#Q3)) 从在投影角度 `θ` 处捕获的投影数据中重建图像。
<a id="function2"></a>
[I](#Q1) = iradon([R](#Q2), [theta](#Q3), [interp](#Q4), [filter](#Q5), [frequencyScaling](#Q6), [outputSize](#Q7)) 指定用于逆 `Radon` 变换的附加参数，可以指定最后四个参数的任意组合。

## 参数说明
### 输入参数

**<a id="Q2"></a>R — 平行束投影数据**  
数值列向量 | 数值矩阵

平行束投影数据，指定为以下之一：
 - 如果 [`theta`](#Q3)是标量，则将 `R` 指定为包含 `theta` 度的 `Radon` 变换的数值列向量。
 - 如果 `theta` 是向量，则将 `R` 指定为二维矩阵，其中每一列是 `theta` 中一个角度的 `Radon` 变换。

**数据类型：** `single` | `double`

**<a id="Q3"></a>theta — 投影角度**  
数值向量 | 数值标量 | []

投影角度（以度为单位），指定为以下之一：

| **值** | **描述** |
|:-|:-|
| 数值向量 | 投影角度，角度之间必须有相等的间距。 |
| 数值标量 | 投影之间的增量角度。投影在角度m*theta处获取，其中m = 0,1,2,...,size([R](#Q2),2)-1。 |
| [] | 自动将投影之间的增量角度设置为180/size(R,2) |

**数据类型：** `single` | `double` 

**<a id="Q4"></a>interp — 插值类型**  
"linear"（默认）| "nearest" | "spline" | "pchip" | "v5cubic" 

在反投影中使用的插值类型，指定为以下值之一，这些值按精度和计算复杂度递增的顺序列出。

| **值** | **描述** |
|:-|:-|
| "nearest" | 最近邻插值 |
| "linear" | 线性插值 |
| "spline" | 样条插值 |
| "pchip" | 保形分段三次插值 |
| "v5cubic" | 立方卷积 | 

**数据类型：** `char` | `string`

**<a id="Q5"></a>filter — 滤波器**  
"Ram-Lak"（默认）| "Shepp-Logan" | "Cosine" | "Hamming" | "Hann" | "None"

用于频率域滤波的滤波器，指定为以下值之一：

| **值** | **描述** |
|:-|:-|
| "Ram-Lak" | 截断的Ram-Lak或斜坡滤波器。该滤波器的频率响应为f。由于此滤波器对投影中的噪声敏感，因此下面列出的滤波器之一可能更为合适。这些滤波器将Ram-Lak滤波器与一个削弱高频的窗口相乘。 |
| "Shepp-Logan" | 将Ram-Lak滤波器与sinc函数相乘 |
| "Cosine" | 将Ram-Lak滤波器与余弦函数相乘 |
| "Hamming" | 将Ram-Lak滤波器与汉明窗相乘 |
| "Hann" | 将Ram-Lak滤波器与汉宁窗相乘 | 
| "None" | 未应用滤波。iradon 返回未滤波的反投影数据。|

**<a id="Q6"></a>frequencyScaling — 缩放因子**  
1（默认）| 范围 (0, 1] 内的正数

用于重新缩放频率轴的缩放因子，指定为范围 (0, 1] 内的正数。
如果 `frequencyScaling` 小于 1，则滤波器会被压缩以适应频率范围 [0, frequencyScaling]（归一化频率）。此外，所有高于 `frequencyScaling` 的频率将被设置为 0。

**<a id="Q7"></a>outputSize — 重建图像的行数和列数**  
正整数

重建图像中的行数和列数，指定为正整数。如果你不指定 `outputSize` ，那么 `iradon` 会根据投影的长度计算尺寸，如果你指定 `outputSize` ，那么 `iradon` 会重建图像的较小或较大部分，但不会更改数据的比例尺。 如果投影是使用 `radon` 函数计算的，则重建的图像大小可能与原始图像不同。

### 输出参量
**<a id="Q1"></a>I — 灰度图像**  
数值矩阵

灰度图像，以数值矩阵形式返回。`I` 的数据类型与 [`R`](#Q2) 的数据类型相同。

**数据类型：** `single` | `double`


## 参考文献
 [1] Kak A C, Slaney M. Principles of Computerized Tomographic Imaging. New York, NY: IEEE Press, 1988.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../radon/radon.html">radon</a> | <a 
href="../phantom/phantom.html">phantom</a> 
## radon 
radon 变换

## 简介
[ `R = radon(I)`](#function1)  
[ `R = radon(I, theta)`](#function2)  
[ `[R, xp] = radon(___)`](#function3)

## 用法
<a id="function1"></a>
[R](#Q1) = radon([I](#Q3)) 返回二维灰度图像 `I` 的拉东变换，角度范围为 [0, 179] 度。拉东变换是图像强度沿特定角度的径向线的投影。  
<a id="function2"></a>
[R](#Q1) = radon([I](#Q3), [theta](#Q4)) 返回基于 `theta` 所指定角度的拉东变换。  
<a id="function3"></a>
[[R](#Q1), [xp](#Q2)] = radon(\___) 返回向量 `xp`，其中包含与图像的每行对应的径向坐标。径向坐标是沿 x' 轴的值，该值与 x 轴呈逆时针方向 `theta` 度角。  

## 参数说明
### 输入参数
**<a id="Q3"></a>I — 灰度图像**  
二维数值矩阵

灰度图像，指定为二维数值矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` |  `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q4"></a>theta — 投影角度**   
0:179（默认）| 数值标量 | 数值向量

投影角度（以度为单位），指定为数值标量或数值向量。

**数据类型：** `double`

### 输出参数
**<a id="Q1"></a>R — 拉东变换**  
数值列向量 | 数值矩阵

图像 [`I`](#Q3) 的拉东变换，返回为下列项之一：
 - 如果 [`theta`](#Q4) 是标量，则 `R` 是数值列向量，其中包含基于 `theta` 度的拉东变换。
 - 如果 `theta` 是向量，则 `R` 是矩阵，其中每列是基于 `theta` 中某一角度的拉东变换。

**<a id="Q2"></a>xp — 径向坐标**  
数值向量

对应于 [`R`](#Q1) 的每行的径向坐标，以数值向量形式返回。径向坐标是沿 x' 轴的值，该值与 x 轴呈逆时针方向 [`theta`](#Q4) 度角。两个轴的原点均为图像的中心像素，定义为
floor((size(I)+1)/2)

例如，在 20×30 的图像中，中心像素是 (10, 15)。


## 参考文献
Bracewell, Ronald N. Two-Dimensional Imaging. Englewood Cliffs, NJ: Prentice Hall, 1995: 505-537.
Lim, Jae S. Two-Dimensional Signal and Image Processing. Englewood Cliffs, NJ: Prentice Hall, 1990: 42-45.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../iradon/iradon.html">iradon</a> | <a 
href="../phantom/phantom.html">phantom</a> 
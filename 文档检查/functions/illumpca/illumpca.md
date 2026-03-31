## illumpca
使用主成分分析 (PCA) 估计场景光源

## 简介
[`illuminant = illumpca(A)`](#function1)  
[`illuminant = illumpca(A, percentage)`](#function2)  
[`illuminant = illumpca(___, 'Mask', mask)`](#function3)

## 用法
<a id="function1"></a>
[illuminant](#P1) = illumpca([A](#Q1)) 使用主成分分析 (PCA) 基于图像中较大的颜色差异，估计 RGB 图像 A 的场景光照。

<a id="function2"></a>
[illuminant](#P1) = illumpca([A](#Q1), [percentage](#Q2)) 使用指定比例的最暗像素与最亮像素参与估计，从而得到场景光照的估计值。

<a id="function3"></a>
[illuminant](#P1) = illumpca(___, 'Mask', [mask](#Q3)) 仅使用二值掩膜所定义的 ROI 内的像素进行估计，从而得到场景光照的估计值。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — RGB 图像**  
m×n×3 数值数组

RGB 图像，指定为 m×n×3 的数值数组。

**数据类型：** `single` | `double` | `uint8` | `uint16`

**<a id="Q2"></a> percentage — 参与估计的像素比例**  
3.5(默认) | 数值标量

用于光源估计的像素保留比例，指定为位于 (0, 50] 范围内的数值标量。该比例用于确定参与估计的最暗像素与最亮像素子集。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` |  `uint64`

**<a id="Q3"></a> mask — 图像掩膜 k**  
m×n 逻辑或数值矩阵

图像掩膜，指定为 m×n 的逻辑矩阵或数值矩阵。该掩膜用于指示在估计光源时应使用输入图像 A 中的哪些像素：掩膜值为 0 的位置对应像素将被排除，掩膜值非 0 的位置对应像素将被纳入计算。默认情况下，掩膜所有元素均为 1，即使用 A 的全部像素参与估计。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` |  `uint64` | `logical`

### 输出参数
**<a id="P1"></a> illuminant — 场景光照估计值**  
3 元素数值行向量

场景光照的估计值，返回为包含三个元素的数值行向量。三个元素分别对应光源在红、绿、蓝三个通道上的分量。

**数据类型：** `double`

## 算法
算法将每个像素的颜色表示为 RGB 空间中的向量。首先，以图像的平均颜色向量为参考，计算每个像素颜色在该参考方向上的投影，并依据投影的亮度对颜色进行排序。随后，按照该排序仅保留最暗与最亮的颜色。最后，在这一子集上执行主成分分析，其中第一主成分对应的方向用于给出光源的估计。

## 参考
[1] Cheng, Dongliang, Dilip K. Prasad, and Michael S. Brown. Illuminant Estimation for Color Constancy: Why spatial-domain methods work and the role of the color distribution. Journal of the Optical Society of America A. Vol. 31, Number 5, 2014, pp. 1049–1058.

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../chromadapt/chromadapt.html">chromadapt</a> | <a
href="../illumgray/illumgray.html">illumgray</a> | <a
href="../illumwhite/illumwhite.html">illumwhite</a> | <a
href="../lin2rgb/lin2rgb.html">lin2rgb</a> | <a
href="../rgb2lin/rgb2lin.html">rgb2lin</a>

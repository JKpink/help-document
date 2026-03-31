## imgradient
梯度幅值和方向

## 简介
[`[Gmag, Gdir] = imgradient(I)`](#function1)  
[`[Gmag, Gdir] = imgradient(I, method)`](#function2)  
[`[Gmag, Gdir] = imgradient(Gx, Gy)`](#function3)

## 用法
<a id="function1"></a>
[[Gmag](#Q1), [Gdir](#Q2)] = imgradient([I](#Q3)) 返回二维灰度图像或二值图像 `I` 的梯度幅值 Gmag 和梯度方向 Gdir。  
<a id="function2"></a>
[[Gmag](#Q1), [Gdir](#Q2)] = imgradient([I](#Q3), [method](#Q4)) 使用指定的 method 返回梯度幅值和方向。  
<a id="function3"></a>
[[Gmag](#Q1), [Gdir](#Q2)] = imgradient([Gx](#Q5), [Gy](#Q6)) 分别从 x 和 y 方向的定向梯度 Gx 和 Gy 返回梯度幅值和方向。

## 参数说明
### 输入参数
**<a id="Q3"></a> I — 输入图像**  
二维灰度图像 | 二维二值图像

输入图像，指定为二维灰度图像或二维二值图像。

**数据类型：** `single` | `double` | `int8` | `int32` |  `uint8` | `uint16` | `uint32` | `logical`

**<a id="Q4"></a> method — 梯度算子**  
"sobel" (默认) | "prewitt" | "central" | "intermediate" | "roberts"

梯度算子，指定为下列值之一。

| **方法** | **描述** |
|:-|:-|
| "sobel" | 索贝尔梯度算子。像素的梯度是 3×3 邻域内像素的加权和。 |
| "prewitt" | 普瑞维特梯度算子。像素的梯度是 3×3 邻域内像素的加权和。 |
| "central" | 中心差分梯度。一个像素的梯度是相邻像素的加权差。在 y 方向为 dI/dy = (I(y+1) - I(y-1))/2 |
| "intermediate" | 中间差分梯度。一个像素的梯度是相邻像素和当前像素之间的差。在 y 方向为 dI/dy = I(y+1) - I(y)。 |
| "roberts" | 罗伯茨梯度算子。一个像素的梯度是对角相邻像素之间的差。 |
| | |

**数据类型**:`char` | `string`

**<a id="Q5"></a> Gx — 水平梯度**  
数值矩阵

水平梯度，指定为数值矩阵。水平 (x) 轴指向列下标递增的方向。您可以使用 <a 
href="../imgradientxy/imgradientxy.html">imgradientxy</a> 函数来计算 Gx。

**数据类型：** `single` | `double` | `int8` | `int32` |  `uint8` | `uint16` | `uint32`

**<a id="Q6"></a> Gy — 垂直梯度**  
数值矩阵

垂直梯度，指定为与 [Gx](#Q5) 大小相同的数值矩阵。垂直 (y) 轴指向行下标递增的方向。您可以使用 <a href="../imgradientxy/imgradientxy.html">imgradientxy</a> 函数来计算 Gy。

**数据类型：** `single` | `double` | `int8` | `int32` |  `uint8` | `uint16` | `uint32`

### 输出参量
**<a id="Q1"></a> Gmag — 梯度幅值**  
数值矩阵

梯度幅值，以数值矩阵形式返回，其大小与图像 [I](#Q3) 或定向梯度 [Gx](#Q5) 和 [Gy](#Q6) 相同。Gmag 的数据类型为 double。如果输入图像或定向梯度的数据类型为 single，则 Gmag 的数据类型为 single。

**数据类型：** `double`

**<a id="Q2"></a> Gdir — 梯度方向**  
数值矩阵

梯度方向，以数值矩阵形式返回，其大小与梯度幅值 [Gmag](#Q1) 相同。Gdir 包含与正 x 轴的 [-180, 180] 范围内的逆时针夹角，以度为单位（x 轴指向列下标递增的方向），Gdir 的数据类型为 double。如果输入图像或定向梯度的数据类型为single，则 Gdir 的数据类型为single。

**数据类型：** `double`

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
 <a href="../edge/edge.html">edge</a> | <a 
href="../fspecial/fspecial.html">fspecial</a> | <a 
href="../imgradientxyz/imgradientxyz.html">imgradientxyz</a> | <a 
href="../imgradientxy/imgradientxy.html">imgradientxy</a> | <a 
href="../imgradient3/imgradient3.html">imgradient3</a> 


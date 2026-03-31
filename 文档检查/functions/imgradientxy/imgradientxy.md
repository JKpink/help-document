## imgradientxy
梯度

## 简介
[`[Gx, Gy] = imgradientxy(I)`](#function1)  
[`[Gx, Gy] = imgradientxy(I, method)`](#function2)

## 用法
<a id="function1"></a>
[[Gx](#Q1), [Gy](#Q2)] = imgradientxy([I](#Q3)) 返回灰度或二值图像 `I` 的定向梯度 Gx 和 Gy。   
<a id="function1"></a>
[[Gx](#Q1), [Gy](#Q2)] = imgradientxy([I](#Q3), [method](#Q4)) 使用指定的 method 返回定向梯度。

## 参数说明
### 输入参数
**<a id="Q3"></a> I — 输入图像**  
二维灰度图像 | 二维二值图像

输入图像，指定为二维灰度图像或二维二值图像。

**数据类型：** `single` | `double` | `int8` | `int32` |  `uint8` | `uint16` | `uint32` | `logical`

**<a id="Q4"></a> method — 梯度算子**  
"sobel" (默认) | "prewitt" | "central" | "intermediate"

梯度算子，指定为下列值之一。

| **方法** | **描述** |
|:-|:-|
| "sobel" | sobel 梯度算子。像素的梯度是 3×3 邻域内像素的加权和。 |
| "prewitt" | prewitt 梯度算子。像素的梯度是 3×3 邻域内像素的加权和。|
| "central" | 中心差分梯度。一个像素的梯度是相邻像素的加权差。在 y 方向为 dI/dy = (I(y+1) - I(y-1))/2 |
| "intermediate" | 中间差分梯度。一个像素的梯度是相邻像素和当前像素之间的差。在 y 方向为 dI/dy = I(y+1) - I(y)。 |

**数据类型**: `char` | `string`
### 输出参量
**<a id="Q1"></a> Gx — 水平梯度**  
数值矩阵

水平梯度，以与图像 `I` 大小相同的数值矩阵形式返回。水平 (x) 轴指向列下标递增的方向。`Gx` 的数据类型为 double。如果输入图像 `I` 的数据类型为`single`，则`Gx`的数据类型为`single`。

**数据类型：** `double` | `single`

**<a id="Q2"></a> Gy — 垂直梯度**  
数值矩阵

垂直梯度，以与图像 `I` 大小相同的数值矩阵形式返回。垂直 (y) 轴指向行下标递增的方向。Gy 的数据类型为 double。如果输入图像 `I` 的数据类型为`single`，则`Gy`的数据类型为`single`。

**数据类型：** `double` | `single`

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
 <a href="../edge/edge.html">edge</a> | <a 
href="../fspecial/fspecial.html">fspecial</a> | <a 
href="../imgradientxyz/imgradientxyz.html">imgradientxyz</a> | <a 
href="../imgradient/imgradient.html">imgradient</a> | <a 
href="../imgradient3/imgradient3.html">imgradient3</a> 


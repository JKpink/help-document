## imgradient3
查找3-D图像的梯度幅值和方向

## 简介
[[Gmag, Gazimuth, Gelevation] = imgradient3(I)](#function1)
[[Gmag, Gazimuth, Gelevation] = imgradient3(I, method)](#function2)
[[Gmag, Gazimuth, Gelevation] = imgradient3(Gx, Gy, Gz)](#function3)

## 用法
<a id="function1"></a>

[Gmag](#Q11), [Gazimuth](#Q12), [Gelevation](#Q13) = imgradient3([I](#Q1)) 返回3-D灰度或二值图像I的梯度幅值 `Gmag` 、梯度方位角 `Gazimuth` 和梯度仰角 `Gelevation` 。

<a id="function2"></a>

[Gmag](#Q11), [Gazimuth](#Q12), [Gelevation](#Q13) = imgradient3([I](#Q1), [method](#Q4)) 使用指定的方法计算梯度幅值、方位角和仰角。

<a id="function3"></a>

[Gmag](#Q11), [Gazimuth](#Q12), [Gelevation](#Q13) = imgradient3([Gx](#Q5), [Gy](#Q6), [Gz](#Q7)) 分别根据 `x`、 `y` 和 `z` 方向的方向梯度 `Gx` 、 `Gy` 和 `Gz` 计算梯度幅值、方位角和仰角。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
3-D灰度图像 | 3-D二值图像  

输入图像，指定为3-D灰度图像或3-D二值图像。  

**数据类型：**  `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`  

**<a id="Q4"></a> method — 梯度算子**  
"sobel"（默认） | "prewitt" | "central" | "intermediate"  

梯度算子，指定为以下值之一：  

| 值             | 含义                                                         |
| -------------- | ------------------------------------------------------------ |
| "sobel"        | Sobel梯度算子。像素的梯度是 3×3×3 邻域内像素的加权和。例如，在深度（z）方向，三个平面的权重为：<br>plane z-1：<br>[ 1  3  1 <br>  3  6  3 <br>  1  3  1 ]<br>plane z：<br>[ 0  0  0 <br>  0  0  0 <br>  0  0  0 ]<br>plane z+1：<br>[ -1  -3  -1 <br>  -3  -6  -3 <br>  -1  -3  -1 ] |
| "prewitt"      | Prewitt梯度算子。像素的梯度是 3×3×3 邻域内像素的加权和。例如，在深度（z）方向，三个平面的权重为：<br>plane z-1：<br>[ 1  1  1 <br>  1  1  1 <br>  1  1  1 ]<br>plane z：<br>[ 0  0  0 <br>  0  0  0 <br>  0  0  0 ]<br>plane z+1：<br>[ -1  -1  -1 <br>  -1  -1  -1 <br>  -1  -1  -1 ] |
| "central"      | 中心差分梯度。像素的梯度是相邻像素的加权差。例如，在深度（z）方向，dI/dz = (I(z+1) - I(z-1))/2。 |
| "intermediate" | 中间差分梯度。像素的梯度是相邻像素与当前像素的差。例如，在深度（z）方向，dI/dz = I(z+1) - I(z)。 |

在图像边界应用梯度算子时，imgradient3假设图像边界外的值等于最近的图像边界值。此行为类似于imfilter中的"replicate"边界选项。  

**数据类型：**  `char` | `string`  

**<a id="Q5"></a> Gx — 水平梯度**  
3-D数值数组  

水平梯度，指定为3-D数值数组。水平（x）轴指向列下标增加的方向。可使用imgradientxyz函数计算Gx。  

**数据类型：**  `double` | `single`  

**<a id="Q6"></a> Gy — 垂直梯度**  
3-D数值数组  

垂直梯度，指定为与Gx大小相同的3-D数值数组。垂直（y）轴指向行下标增加的方向。可使用imgradientxyz函数计算Gy。  

**数据类型：**  `double` | `single`  

**<a id="Q7"></a> Gz — 深度梯度**  
3-D数值数组  

深度梯度，指定为与Gx大小相同的3-D数值数组。深度（z）轴指向平面下标增加的方向。可使用imgradientxyz函数计算Gz。  

**数据类型：**  `double` | `single`  

### 输出参数
**<a id="Q11"></a> Gmag — 梯度向量的幅值**  
3-D数值数组  

梯度向量的幅值，返回为与图像I或方向梯度 `Gx` 、 `Gy` 、 `Gz` 大小相同的3-D数值数组。  

 `Gmag` 的数据类型为 `double` ，除非输入图像或任一方向梯度的数据类型为 `single` ，此时Gmag的数据类型为 `single` 。  

**<a id="Q12"></a> Gazimuth — 方位角**  
3-D数值数组  

方位角，返回为与梯度幅值 `Gmag` 大小相同的3-D数值数组。 `Gazimuth` 包含的角度以度为单位，范围为[-180, 180]，测量基准为x轴正方向与该点在x-y平面上的投影之间的夹角。  

`Gazimuth` 的数据类型为 `double` ，除非输入图像或任一方向梯度的数据类型为 `single` ，此时其数据类型为 `single` 。  

**<a id="Q13"></a> Gelevation — 梯度仰角**  
3-D数值数组  

梯度仰角，返回为与梯度幅值 `Gmag` 大小相同的3-D数值数组。 `Gelevation` 包含的角度以度为单位，范围为[-90, 90]，测量基准为径向线与x-y平面之间的夹角。  

 `Gelevation` 的数据类型为 `double` ，除非输入图像或任一方向梯度的数据类型为 `single` ，此时其数据类型为 `single` 。  

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../imgradientxyz/imgradientxyz.html">imgradientxyz</a> | <a href="../imgradient/imgradient.html">imgradient</a> | <a href="../imgradientxy/imgradientxy.html">imgradientxy</a>
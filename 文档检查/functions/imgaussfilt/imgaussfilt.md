## imgaussfilt
图像的二维高斯滤波

## 简介
[ `B = imgaussfilt(A)`](#function1)  
[ `B = imgaussfilt(A, sigma)`](#function2)  
[ `B = imgaussfilt(___, Padding)`](#function3)

## 用法
<a id="function1"></a>
[B](#Q4) = imgaussfilt([A](#Q1)) 使用标准差为 0.5 的二维高斯平滑核对图像 `A` 进行滤波，并在 `B` 中返回滤波后的图像。  
<a id="function2"></a>
[B](#Q4) = imgaussfilt([A](#Q1), [sigma](#Q2)) 使用由 `sigma` 指定标准差的二维高斯平滑核对图像 `A` 进行滤波。  
<a id="function3"></a>
[B](#Q4) = imgaussfilt(___, [Padding](#Q3)) 使用 `Padding` 参量来控制 `imgaussfilt` 如何填充图像边界。

## 参数说明
### 输入参数
**<a id="Q1"></a>A — 要滤波的图像**  
数值数组

要滤波的图像，指定为任意维度的数值数组。

**数据类型：**  `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` 

**<a id="Q2"></a>sigma — 高斯分布的标准差**  
0.5（默认）| 正数

高斯分布的标准差，指定为正数。如果指定标量，则 `imgaussfilt` 使用方高斯核。

**数据类型：** `double`

**<a id="Q3"></a>Padding — 图像填充**  
"replicate" | "symmetric" | "circular"

图像填充，指定为下表中的值之一：

| **值** | **描述** |
|:--|:--|
| "symmetric" |数组边界之外的输入数组值是通过沿数组边界对数组进行镜面反射得到。|
| "replicate" |数组边界之外的输入数组值假定为等于最近的数组边界值。|
| "circular"  |数组边界之外的输入数组值是通过隐式假设输入数组具有周期性来计算的。|

**数据类型：** `char` | `string`

### 输出参数
**<a id="Q4"></a>B — 滤波后的图像**  
数值数组

滤波后的图像，以与输入图像 [`A`](#Q1) 大小和数据类型相同的数值数组形式返回。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出 

## 相关主题
<a href="../imgaussfilt3/imgaussfilt3.html">imgaussfilt3</a> | <a 
href="../imfilter/imfilter.html">imfilter</a> | <a 
href="../fspecial/fspecial.html">fspecial</a>
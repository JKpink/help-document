## ssim  
结构相似性

## 简介  
[ `ssimval = ssim(A, ref)`](#function1)  
[ `[ssimval, ssimmap] = ssim(___)`](#function2)

## 用法  
<a id="function1"></a>
[ssimval](#Q1) = ssim([A](#Q2), [ref](#Q3)) 使用 [`ref`](#Q3) 作为参考图像，计算灰度图像 [`A`](#Q2) 的结构相似性 (SSIM) 索引，值越接近 1 表示图像质量越好。
<a id="function2"></a>  
[[ssimval](#Q1), [ssimmap](#Q4)] = ssim(\___) 还返回 [`A`](#Q2) 中每个像素或体素的局部 SSIM 值。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>A — 用于质量度量的图像**  
数值数组

用于质量度量的图像，指定为任意维数值数组对象，[A](#Q2)与[ref](#Q3)必须在维度与各维度长度上完全一致。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16`

**<a id="Q3"></a>ref — 参考图像**  
数值数组

用于测量质量的参考图像，指定为数值数组，[A](#Q2)与[ref](#Q3)必须在维度与各维度长度上完全一致。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16`

### 输出参数  
**<a id="Q1"></a>ssimval — SSIM 索引**  
数值标量

SSIM 索引，返回具有单 SSIM 测量的数值标量。`ssimval` 的值通常在 [0, 1] 范围内。值 1 表示最高质量，当 `A` 和 `ref` 相同时出现，`ssimval` 的值越小，质量越差。

**数据类型：** `double`

**<a id="Q4"></a>ssimmap — SSIM 索引的局部值**  
数值数组

SSIM 索引的局部值，返回与输入图像大小相同的数值数组。输入图像中的每个元素都有一个对应的 SSIM 测量值。

**数据类型：** `double`

## 详细信息  
### 结构相似性索引  
一种图像质量度量，用于评估图像三个特性的视觉效果：亮度、对比度和结构。
该指标由 Wang 等人提出，完整理论与实现方法参考经典论文 [[1]](#Q5)。

## 参考文献  
<a id="Q5"></a>[1] Zhou Wang, Bovik A C, Sheikh H R, et al. Image quality assessment: From error visibility to structural similarity[J] . IEEE Transactions on Image Processing, 2004, 13(4): 600-612.
## 版本历史
在北太天元图像处理工具箱 V1.1 推出

## 相关主题  
<a href="../immse/immse.html">immse</a> | <a 
href="../psnr/psnr.html">psnr</a>


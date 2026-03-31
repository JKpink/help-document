# edgetaper
弱化图像边缘的不连续性

## 简介
[`J = edgetaper(I, PSF)`](#function1)

## 用法
<a id="function1"></a>
[J](#Q3) = edgetaper([I](#Q1), [PSF](#Q2)) 使用点扩散函数 `PSF` 对输入图像 `I` 的边缘进行模糊处理。

输出图像 `J` 是原始图像 `I` 与其模糊版本的加权和。加权数组由 `PSF` 的自相关函数确定，使得 `J` 在中心区域与 `I` 完全一致，在边缘区域则与 `I` 的模糊版本一致。

`edgetaper` 函数可减轻使用离散傅里叶变换的图像去模糊方法（如<a href="../deconvwnr/deconvwnr.html">deconvwnr</a> , <a href="../deconvreg/deconvreg.html">deconvreg</a> 和 <a 
href="../deconvlucy/deconvlucy.html">deconvlucy</a> ）中出现的振铃效应。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
数值数组

输入图像：指定为数值数组。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16`

**<a id="Q2"></a> PSF — 点分布函数**  
数值数组

点扩散函数：指定为数值数组。`PSF` 在任意维度上的尺寸均不得超过图像对应维度尺寸的一半。

**数据类型：** `double` 

### 输出参数
**<a id="Q3"></a> J — 原始图像与其模糊版本的加权和**  
数值数组

原始图像与其模糊版本的加权和：返回为与 `I` 尺寸和数据类型均相同的数值数组。加权数组由 `PSF` 的自相关函数确定，使得 `J` 在中心区域与 `I` 完全一致，在边缘区域则与 `I` 的模糊版本一致。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../deconvlucy/deconvlucy.html">deconvlucy</a> | <a 
href="../deconvreg/deconvreg.html">deconvreg</a> | <a 
href="../deconvwnr/deconvwnr.html">deconvwnr</a> | <a 
href="../otf2psf/otf2psf.html">otf2psf</a> | <a 
href="../padarray/padarray.html">padarray</a> | <a 
href="../psf2otf/psf2otf.html">psf2otf</a> 


## psnr  
峰值信噪比

## 简介  
[ `peaksnr = psnr(A, ref)`](#function1)  
[ `peaksnr = psnr(A, ref, peakval)`](#function2)  
[ `[peaksnr, snr] = psnr(___)`](#function3)

## 用法  
<a id="function1"></a>
[peaksnr](#Q1) = psnr([A](#Q2), [ref](#Q3)) 以图像 [`ref`](#Q3) 为参考，计算图像 [`A`](#Q2) 的峰值信噪比 (PSNR)。PSNR 值越大，表示图像质量越好。
<a id="function2"></a>  
[peaksnr](#Q1) = psnr([A](#Q2), [ref](#Q3), [peakval](#Q4)) 使用峰值信号值 [`peakval`](#Q4) 计算图像 [`A`](#Q2) 的 PSNR 。
<a id="function3"></a>  
[[peaksnr](#Q1), [snr](#Q5)] = psnr(___) 还返回简单信噪比 [snr](#Q5) 。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>A — 要分析的图像**  
数值数组 

要分析的图像，指定为任意维度的数值数组，[A](#Q2)与[ref](#Q3)必须在维度与各维度长度上完全一致。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16`

**<a id="Q3"></a>ref — 参考图像**  
数值数组 

参考图像，指定为数值数组，[A](#Q2)与[ref](#Q3)必须在维度与各维度长度上完全一致。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16`

**<a id="Q4"></a>peakval — 峰值信号级别**  
非负数

峰值信号级别，指定为非负数，如果未指定，则 `peakval` 的默认值取决于 [`A`](#Q2) 和 [`ref`](#Q3) 的类：
 - 如果图像的数据类型为 `double` 或 `single`，则图像数据在范围 [0, 1] 内，`peakval` 的默认值为 1。
 - 如果图像是整数数据类型，则 `peakval` 的默认值是该类的范围所允许的最大值。对于 `uint8` 数据，`peakval` 的默认值为 255。对于 `uint16` 或 `int16`，默认值为 65535。

### 输出参数  
**<a id="Q1"></a>peaksnr — PSNR**  
数值标量

以分贝为单位的 PSNR，返回具有单一 PSNR 测量值的数值标量。

**数据类型：** `double`

**<a id="Q5"></a>snr — 信噪比**  
数值标量

以分贝为单位的信噪比，返回具有单一SNR测量值的数值标量。

**数据类型：** `double`

## 版本历史  
在北太天元图像处理工具箱 V1.1 推出

## 相关主题  
<a href="../immse/immse.html">immse</a> | <a 
href="../ssim/ssim.html">ssim</a>
## applylut  
使用查找表对二值图像执行邻域运算

## 简介  
[ `A = applylut(BW, lut)`](#function1)

## 用法  
<a id="function1"></a>
[A](#Q1) = applylut([BW](#Q2), [lut](#Q3))  
对二值图像 [`BW`](#Q2) 执行 2×2 或 3×3 邻域运算，运算规则由查找表 [`lut`](#Q3) 定义。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 输入图像**  
二维数值数组 | 二维逻辑数组  

输入的二维二值图像，若为数值型数组，所有非零像素均被视为 1（真）。  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`  

**<a id="Q3"></a>lut — 输出像素值的查找表**  
16 元素数值向量 | 512 元素数值向量  

定义邻域运算输出值的查找表，必须为16元素或512元素的行向量或列向量，有如下对应：  

- 若为 2×2 邻域运算，则输入 16 元素向量（对应 2⁴ = 16 种邻域像素排列）；  
- 若为 3×3 邻域运算，则输入 512 元素向量（对应 2⁹ = 512 种邻域像素排列）。  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`  

**<a id="Q1"></a>A — 输出图像**  
二维数值数组 | 二维逻辑数组  

邻域运算后的输出图像，尺寸与输入图像 BW 完全一致。  

**数据类型：** `double`| `uint8` | `logical`  

## 版本历史  
在北太天元图像处理工具箱 V3.0 推出  

## 相关主题  
<a href="../makelut/makelut.html;">makelut</a> | <a
href="../bwlookup/bwlookup.html">bwlookup</a> | <a
href="../imdilate/imdilate.html">imdilate</a> | <a
href="../imerode/imerode.html">imerode</a>
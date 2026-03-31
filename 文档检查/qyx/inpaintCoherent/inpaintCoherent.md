## inpaintCoherent 
使用基于相干传输的图像修复来复原特定图像区域

## 简介
[`J = inpaintCoherent(I, mask)`](#function1)  
[`J = inpaintCoherent(I, mask, Name, Value)`](#function2)

## 用法
<a id="function1"></a>
[J](#Q4) = inpaintCoherent([I](#Q1), [mask](#Q2)) 使用基于相干传输的图像修复方法[[1]](#R1)，复原输入图像中指定区域的缺失部分。`mask` 是一个二值图像，用于标记需要通过修复填充的目标区域。  
<a id="function2"></a>
[J](#Q4) = inpaintCoherent([I](#Q1), [mask](#Q2), [Name, Value](#Q3)) 通过一个或多个名称 — 值参量指定额外的修复选项，其中 `SmoothingFactor` 用于指定 `Gaussian` 滤波的标准差，`Radius` 用于指定修复的半径。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 修复图像**  
灰度图像 | RGB 彩色图像

要修复的图像，指定为大小为 m×n 的灰度图像或大小为 m×n×3 的 RGB 彩色图像。

**数据类型**: `single` | `double` | `uint8` | `uint16` | `int8` | `int16` 

**<a id="Q2"></a> mask — 目标区域的空间掩码**  
2-D 二进制图像

目标区域的空间掩码，指定为大小为 m×n 的二维二进制图像，其中 m 和 n 是输入图像 `I` 的尺寸。`mask` 中的非零像素构成了要通过修复填充的目标区域。

**数据类型**: `logical`

**<a id="Q3"></a> 名称 — 值参数**  
将可选的参量对组指定为 Name1, Value1, ..., NameN, ValueN，其中 Name 是参量名称，Value 是对应的值。名称 — 值参量必须出现在其他参量之后，但参量对组的顺序无关紧要。

**SmoothingFactor — 高斯滤波器的标准差**  
2 (默认) | 正数

高斯滤波器的标准差，指定为正数。该值用于计算高斯滤波器的尺度，同时估计相干方向。

**Radius — 修复半径**  
5 (默认) | 正整数

修复半径，指定为正整数。修复半径表示以要进行修复的像素为中心的圆形邻域区域的半径。

### 输出参数
**<a id="Q4"></a> J — 修复图像**  
灰度图像 | RGB 彩色图像

已修复图像，以相同大小的灰度图像或 RGB 彩色图像形式返回。
数据类型与输入图像 `I` 相同。

## <a id="R1"></a> 参考文献  
[1] Bornemann F, März T. Fast image inpainting based on coherence transport. Journal of Mathematical Imaging and Vision, 2007, 28(3): 259-278. 

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../imfill/imfill.html">imfill</a> | <a 
href="../inpaintExemplar/inpaintExemplar.html">inpaintExemplar</a> 
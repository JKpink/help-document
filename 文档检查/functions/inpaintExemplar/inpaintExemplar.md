## inpaintExemplar 
使用基于样本块的图像修复来复原特定图像区域

## 简介
[`J = inpaintExemplar(I, mask)`](#function1)  
[`J = inpaintExemplar(I, mask, Name, Value) `](#function2)

## 用法
<a id="function1"></a>
[J](#Q4) = inpaintExemplar([I](#Q1), [mask](#Q2))  使用基于样本的图像修复方法填充输入图像中的指定区域[[1]](#R1)。`mask` 是一个二值图像，用于标记需要通过修复填充的目标区域。  
<a id="function2"></a>
[J](#Q4) = inpaintExemplar([I](#Q1), [mask](#Q2), [Name, Value](#Q3) ) 通过一个或多个名称 — 值参量指定额外的修复选项，其中 `PatchSize` 用于指定图像补丁的大小。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 修复图像**  
灰度图像 | RGB 彩色图像

要修复的图像，指定为大小为 m×n 的灰度图像或大小为 m×n×3 的 RGB 彩色图像。

**数据类型**：`single` | `double` | `uint8` | `uint16` |`uint32`| `int8` | `int16` 

**<a id="Q2"></a> mask — 目标区域的空间掩码**  
2-D 二进制图像

目标区域的空间掩码，指定为大小为 m×n 的二维二进制图像，其中 m 和 n 是输入图像 `I` 的尺寸。`mask` 中的非零像素构成了要通过修复填充的目标区域。

**数据类型**： `logical`

**<a id="Q3"></a> 名称 — 值参数**  
将可选的参量对组指定为 Name1, Value1, ..., NameN, ValueN，其中 Name 是参量名称，Value 是对应的值。名称 — 值参量必须出现在其他参量之后，但参量对组的顺序无关紧要。

**PatchSize — 图像补丁的大小**  
[9,  9]  (默认) | 标量 | 向量

图像图块的大小，指定为以下值之一。


- 标量 s — 图像块是一个方形区域 大小为 s×s。


- 形式为 [p s] 的向量 — 图像块是正方形或矩形区域 尺寸为 p×s。

默认图像块大小为 9×9。图像补丁是指考虑用于补丁匹配和修复的图像区域。

**注意**  
图像补丁的大小必须至少为 3×3 且始终小于输入图像的尺寸。

**数据类型**： `double` 

### 输出参数
**<a id="Q4"></a> J — 修复图像**  
灰度图像 | RGB 彩色图像

已修复图像，以相同大小的灰度图像或 RGB 彩色图像形式返回。
数据类型与输入图像 `I` 相同。

## 参考文献
[1] Criminisi A, Pérez P, Toyama K. Region filling and object removal by exemplar-based image inpainting. IEEE Transactions on image processing, 2004, 13(9): 1200-1212.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../imfill/imfill.html">imfill</a> | <a 
href="../inpaintCoherent/inpaintCoherent.html">inpaintCoherent</a> 
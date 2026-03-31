## imadjust
调整图像亮度值或颜色表

## 简介
[ `J = imadjust(I)`](#function1)  
[ `J = imadjust(I, [low_in high_in])`](#function2)  
[ `J = imadjust(I, [low_in high_in], [low_out high_out])`](#function3)  
[ `J = imadjust(I, [low_in high_in], [low_out high_out], gamma)`](#function4)  
[`J = imadjust(RGB,[low_in high_in],___)`](#function5)  

## 用法
<a id="function1"></a>
[J](#Q6) = imadjust([I](#Q1))  将灰度图像 `I` 中的强度值映射到 `J` 中的新值。使用此语法时，`imadjust` 对所有像素值中最低的 1%  和最高的 1% 进行饱和处理。该函数将饱和界限之间的像素值线性映射到 0 和 1 之间的值。此运算可提高输出图像 `J` 的对比度。
此语法等效于 imadjust(I,stretchlim(I))。  
<a id="function2"></a>
[J](#Q6)  = imadjust([I](#Q1), [[low_in high_in]](#Q3)) 将 `I` 中的强度值映射到 `J` 中的新值，以使 low_in 和 high_in 之间的值线性映射到 0 到 1 之间的值。  
<a id="function3"></a>
[J](#Q6)  = imadjust([I](#Q1), [[low_in high_in]](#Q3),[ [low_out high_out]](#Q4))  将 `I` 中的强度值映射到 `J` 中的新值，以使low_in和high_in之间的值线性映射到 low_out到high_out 之间的值。  
<a id="function4"></a>
[J](#Q6)  = imadjust([I](#Q1), [[low_in high_in]](#Q3), [ [low_out high_out]](#Q4), [gamma](#Q5)) 将 `I` 中的强度值映射到 `J` 中的新值，其中 `gamma` 指定描述 `I` 和 `J` 中的值之间关系的曲线形状。  
<a id="function5"></a>
[J](#Q6)  = imadjust([RGB](#Q2), [[low_in high_in]](#Q3),___) 将真彩色图像 `RGB` 中的值映射到 `J` 中的新值。您可以为每个颜色通道应用相同的映射或互不相同的映射。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 灰度图像**    
m×n 数值矩阵  

灰度图像，指定为 m×n 数值矩阵。如果 `I` 是整数数据类型，则 `imadjust` 先使用 `im2double` 将像素值重新缩放到范围 [0, 1]。在通过映射输入和输出对比度范围之间的值来调整对比度后，该函数会将输出图像转换回 `I` 的原始数据类型。

**数据类型:** `uint8`


**<a id="Q2"></a> RGB — 真彩色图像**  
m×n×3 数值数组  

真彩色图像，指定为 m×n×3 数值数组。如果 RGB 是整数数据类型，则 `imadjust` 先使用 `im2double` 将像素值重新缩放到范围 [0, 1]。在通过映射输入和输出对比度范围之间的值来调整对比度后，该函数会将输出图像转换回 RGB 的原始数据类型。  

**数据类型:** `double` | `uint8` | `logical`

**<a id="Q3"></a>[low_in high_in] — 输入图像的对比度范围**  
二元素数值向量 | 2×3 数值矩阵  

输入图像的对比度范围，指定为下表中的值之一。

| **输入类型** | **值** | **描述** |
|:---|:---|:---|
| 灰度图像 |[low_in high_in] 形式的 1×2 向量 | 指定要映射到输出图像中的值的输入灰度图像的对比度范围。值必须在 [0, 1.0] 范围内。值 low_in 必须小于值 high_in。 |
| 灰度图像 | 未指定 | 如果使用语法 imadjust(I) 仅指定一个输入参量，则该函数将根据输入图像值设置 low_in 和 high_in，以便对所有像素值中最低的 1% 和最高的 1% 进行饱和处理。 |
| RGB 图像或颜色图 | 	[low_RGB_triplet; high_RGB_triplet] 形式的 2×3 矩阵 | 指定要映射到输出图像或颜色图中的值的输入 RGB 图像或颜色图的对比度范围。数组中的每行均为一个 RGB 颜色三元组。值必须在 [0, 1] 范围内。值 low_RGB_triplet 必须小于值 high_RGB_triplet。 |
| RGB 图像或颜色图 | [low_in high_in] 形式的 1×2 向量 | 指定要映射到输出图像中的值的输入 `RGB` 图像的对比度范围。每个值必须在 [0, 1.0] 范围内。值 low_in 必须小于值 high_in。如果您对 `RGB` 图像或颜色图指定 1×2 向量，则 imadjust 会对每个颜色平面或通道应用相同的调整。 |
| 所有类型 | []  | 如果您指定空矩阵 ([])，则 `imadjust` 使用范围 [0, 1]。 |

`imadjust` 函数裁剪低于 low_in 和高于 high_in 的值。低于 low_in 的值映射到 low_out，高于 high_in 的值映射到 high_out。

**数据类型:** `single` | `double`
  
**<a id="Q4"></a> [low_out high_out] — 输出图像的对比度范围**  
[0 1] (默认) | 二元素数值向量 | 2×3 数值矩阵

| **输入类型** | **值** | **描述** |
|:---|:---|:---|
| 灰度图像 |[low_in high_in] 形式的 1×2 向量 |指定输出灰度图像的对比度范围。每个值必须在 [0, 1] 范围内。 |
| RGB 图像或颜色图 | 	[low_RGB_triplet; high_RGB_triplet] 形式的 2×3 矩阵 | 指定输出 RGB 图像或颜色图的对比度范围。数组中的每行均为一个 RGB 颜色三元组。值必须在 [0, 1] 范围内。 |
| RGB 图像或颜色图 | [low_in high_in] 形式的 1×2 向量 | 指定输出图像中的对比度范围。每个值必须在 [0, 1] 范围内。如果您对 RGB 图像或颜色图指定 1×2 向量，则 imadjust 会对每个平面或通道应用相同的调整。 |
| 所有类型 | 未指定或 [] | 如果不指定输出对比度范围，或指定了空矩阵 ([])，则 imadjust 使用默认范围 [0, 1]。|

如果 high_out 小于 low_out，则 `imadjust` 反转输出图像，就像照片底片一样。

**数据类型:** `single` | `double`


**<a id="Q5"></a> gamma — 描述输入和输出值关系的曲线形状**  
1 (默认) | 非负标量 | 1×3 数值向量  

描述输入和输出值关系的曲线形状，指定为非负标量或 1×3 数值向量。

如果 `gamma` 小于 1，则 `imadjust` 会对映射加权，使之偏向更高（更亮）输出值。

如果 `gamma` 大于 1，则 `imadjust` 会对映射加权，使之偏向更低（更暗）输出值。

如果 `gamma` 是 1×3 向量，则 `imadjust` 会对每个颜色分量或通道分别应用不同的 `gamma`。

如果省略该参量，则 `gamma` 取默认值 1（线性映射）。
此图说明了在 `gamma` 小于 1、等于 1 和大于 1 时变换曲线的形状。在每个图中，x 轴表示输入图像中的强度值，y 轴表示输出图像中的强度值。  

  
**数据类型:** `double`

### 输出参数
**<a id="Q6"></a>J — 调整后的图像**  
灰度图像 | RGB 图像  

调整后的图像，以灰度或 RGB 图像形式返回。`J` 的大小和类与输入灰度图像 `I` 或真彩色图像 RGB 相同。

**数据类型:** `single` | `double` | `uint8` 
## 版本历史
在北太天元图像处理工具箱 V1.0 推出
## 相关主题

<a href="../brighten/brighten.html">brighten</a> | <a
href="../histeq/histeq.html">histeq</a> | <a 
href="../stretchlim/stretchlim.html">stretchlim</a> | <a 
href="../lin2rgb/lin2rgb.html">lin2rgb</a> | <a 
href="../rgb2lin/rgb2lin.html">rgb2lin</a> 
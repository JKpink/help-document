## imcrop
裁剪图像

## 简介
[`Icropped = imcrop(I, rect)`](#function1)

## 用法  
<a id="function1"></a> [Icropped](#P1) = imcrop([I](#Q1), [rect](#Q2)) 根据裁剪矩形 `rect` 指定的位置和大小裁剪图像 `I`。输出图像包含输入图像中与该矩形区域存在交集的所有像素。例如，在默认空间坐标系下，假设 `rect` 是 [10 10 20 30]，即指定矩形的左上角是空间 (x, y) 坐标为 (10, 10) 的像素的中心，矩形的右下角是空间 (x, y) 坐标为 (30, 40) 的像素的中心，生成的输出图像大小为 20×30 像素。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 要裁剪的图像**  
数值矩阵 | 数值数组 | 逻辑矩阵

要裁剪的图像，指定为下列项之一：

- 表示灰度图像的 m×n 数值矩阵。
- 表示真彩色图像的 m×n×3 数值数组。
- 表示二值掩膜的 m×n 逻辑矩阵。

**数据类型：**`single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `logical`

**<a id="Q2"></a> rect — 裁剪矩形的大小和位置**  
4 元数值向量

裁剪矩形在空间坐标中的大小和位置，指定为 [xmin ymin width height] 形式的 4 元数值向量。

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出参数

**<a id="P1"></a> Icropped — 裁剪后的图像**  
数值数组 | 数值矩阵 | 逻辑矩阵

裁剪后的图像，以数值数组、数值矩阵或逻辑矩阵形式返回。如果指定输入图像 `I`，则输出图像与输入图像具有相同的数据类型。如果未指定输入图像，则输出图像通常与输入图像具有相同的数据类型。但是，如果输入图像是 `int16` 或 `single` 数据类型，则输出图像是 `double` 数据类型。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<!-- <a href="../zoom/zoom.html">zoom</a> |  -->
<a 
href="../imcrop3/imcrop3.html">imcrop3</a> | <a 
href="../drawrectangle/drawrectangle.html">drawrectangle</a> 
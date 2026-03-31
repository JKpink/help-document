## im2gray
将 RGB 图像转换为灰度图像

## 简介
[ `I = im2gray(RGB)`](#function1)

## 用法
<a id="function1"></a>
[I](#P1) = im2gray[(RGB)](#Q1) 将指定的真彩色图像 `RGB` 转换为灰度图像 `I`。若输入为灰度图像，则函数直接原样返回该图像。im2gray 函数通过消除色调和饱和度信息，同时保留亮度，来将 RGB 图像转换为灰度图像。

## 参数说明
### 输入参数
**<a id="Q1"></a> RGB — 真彩色图像**  
m×n×3 数值数组 | m×n 数值数组

真彩色图像，指定为 m×n×3 数值数组。im2gray 还接受 m×n 数值数组（灰度图像）并原样返回它们。im2gray 函数要求数据类型为 `double` 和 `single` 的真彩色图像的值在范围 [0, 1] 内。如果一个图像的值超出范围 [0, 1]，则可以使用 <a href="../rescale/rescale.html">rescale</a> 函数将值重新缩放到需要的范围。

**数据类型：** `single` | `double` | `uint8` | `uint16`

### 输出参数
**<a id="P1"></a> I — 灰度图像**  

灰度图像，以 m×n 数值数组形式返回。如果 im2gray 的输入是灰度图像，则输出图像 [I](#P1) 与输入图像相同。

## 提示
- im2gray 函数与 <a href="../rgb2gray/rgb2gray.html">rgb2gray</a> 基本相同，不同之处是它可以接受灰度图像作为输入并原样返回它们。如果输入图像是灰度图像，则 rgb2gray 函数返回错误。  
- 与 rgb2gray 函数不同，im2gray 函数不接受颜色图作为输入。要将颜色图转换为灰度图，请使用 <a href="../cmap2gray/cmap2gray.html">cmap2gray</a> 函数。

## 算法
im2gray 通过计算 R、G 和 B 分量的加权和，将 RGB 值转换为灰度值：  
0.298936021293775 \* R + 0.587043074451121 \* G + 0.114020904255103 \* B 

在舍入到小数点后 3 位之后，im2gray 函数中用来计算灰度值的系数与 Rec.ITU-R BT.601-7 中用来计算亮度 (E'y) 的系数相同。Rec.ITU-R BT.601-7 使用以下公式计算 E'y：  
0.299 \* R + 0.587 \* G + 0.114 \* B

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../ind2gray/ind2gray.html">ind2gray</a> | <a
href="../rgb2gray/rgb2gray.html">rgb2gray</a> | <a 
href="../mat2gray/mat2gray.html">mat2gray</a> | <a 
href="../ntsc2rgb/ntsc2rgb.html">ntsc2rgb</a> | <a 
href="../rgb2ind/rgb2ind.html">rgb2ind</a> | <a 
href="../rgb2ntsc/rgb2ntsc.html">rgb2ntsc</a> | <a 
href="../cmap2gray/cmap2gray.html">cmap2gray </a>

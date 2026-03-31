## rgb2gray
将 RGB 图像（颜色表）转换为灰度图像（颜色表）

## 简介
[ `I = rgb2gray(RGB)`](#function1)  
[`newmap = rgb2gray(map)`](#function2)
## 用法
<a id="function1"></a>
[I](#P1) = rgb2gray[(RGB)](#Q1) 将真彩色图像 `RGB` 转换为灰度图像 `I`。`rgb2gray` 函数通过消除色调和饱和度信息，同时保留亮度，来将 RGB 图像转换为灰度图。  
<a id="function1"></a>
[newmap](#P2) = rgb2gray([map](#Q2))返回与 `map` 等效的灰度颜色映射表。
## 参数说明
### 输入参数
**<a id="Q1"></a> RGB — 真彩色图像**  
m×n×3 数值数组

真彩色图像，指定为 m×n×3 数值数组。
`rgb2gray` 函数要求数据类型为 `double` 和 `single` 的真彩色图像的值在范围 [0, 1] 内。如果一个图像的值超出范围 [0, 1]，则可以使用 <a href="../rescale/rescale.html">rescale</a> 函数将值重新缩放到需要的范围。

**数据类型：** `single` | `double` | `uint8` | `uint16`  

**<a id="Q2"></a> map — 颜色映射表**  
c×3 数值矩阵  

颜色映射表，指定为一个 c×3 数值矩阵，矩阵中所有值的范围为 [0, 1]。颜色映射表 map 的每一行都是一个三元 RGB 色值组，用于指定该颜色映射表中一种颜色的红、绿、蓝分量。  

**数据类型：** `double`  

### 输出参数
**<a id="P1"></a> I — 灰度图像**  
m×n 数值数组

灰度图像，以 m×n 数值数组形式返回。  

**<a id="P2"></a> newmap — 灰度颜色映射表**   
c×3 数值矩阵  

灰度颜色映射表，以 c×3 数值矩阵的形式返回，矩阵中所有值的范围为 [0, 1]。newmap 的三列数值完全相同，因此该颜色映射表的每一行仅表示一个单一的灰度值。  

**数据类型：**`double`

## 提示
- 如果输入图像是灰度图像，则 `rgb2gray` 函数返回错误。为了避免错误，可以改用 `im2gray` 函数。`im2gray` 与 `rgb2gray` 基本相同，不同之处是它可以接受灰度图像作为输入并原样返回它们。如果使用 `im2gray` 函数，就不再需要类似如下条件语句的代码。

```
	if ndims(I) == 3
    		I = rgb2gray(I);
	end
```

## 算法
`rgb2gray` 通过计算 R、G 和 B 分量的加权和，将 RGB 值转换为灰度值：  
0.298936021293775 \* R + 0.587043074451121 \* G + 0.114020904255103 \* B 

在舍入到小数点后 3 位之后，`rgb2gray` 函数中用来计算灰度值的系数与 Rec.ITU-R BT.601-7 中用来计算亮度 (E'y) 的系数相同。Rec.ITU-R BT.601-7 使用以下公式计算 E'y：  
0.299 \* R + 0.587 \* G + 0.114 \* B

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../im2gray/im2gray.html">im2gray</a> | <a
href="../cmap2gray/cmap2gray.html">cmap2gray</a> | <a 
href="../mat2gray/mat2gray.html">mat2gray</a> | <a 
href="../ind2gray/ind2gray.html">ind2gray</a> | <a 
href="../rgb2ind/rgb2ind.html">rgb2ind</a> | <a 
href="../rgb2ntsc/rgb2ntsc.html">rgb2ntsc </a>

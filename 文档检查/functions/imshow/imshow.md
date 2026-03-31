## imshow
显示图像

## 简介
[`imshow(I)`](#function1)   
[`imshow(I, [])`](#function7)  
[`imshow(RGB)`](#function2)  
[`imshow(BW)`](#function3)  
[`imshow(X, map)`](#function4)  
<!-- [`imshow(filename)`](#function5)   -->

## 用法
<a id="function1"></a> imshow([I](#Q1)) 以数据类型的默认值域显示灰度图像 `I`，并自动优化图窗、坐标轴及图像对象的可视化属性。  
<a id="function7"></a> imshow([I](#Q1), []) 显示灰度图像 `I`，根据 `I` 中的像素值范围缩放灰度显示。  
<a id="function2"></a> imshow([RGB](#Q2)) 显示三通道真彩色图像，通道值按原始数据渲染。  
<a id="function3"></a> imshow([BW](#Q3)) 显示二值图像，将逻辑值 0 渲染为黑色，1 渲染为白色。  
<a id="function4"></a> imshow([X](#Q4), [map](#Q5)) 结合颜色映射表 `map` 显示索引图像 `X`。  
<!-- <a id="function5"></a> imshow([filename](#Q6)) 显示存储在由 `filename` 指定的图形文件中的图像。 -->

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 灰度图像**  
矩阵

灰度图像，指定为矩阵。

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q7"></a> [low high] — 灰度图像显示范围**  
二元向量

灰度图像显示范围，指定为二元向量。  
**示例：** [50 200]

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` 

**<a id="Q2"></a> RGB — 真彩色图像**  
m×n×3 数组

真彩色图像，指定为 m×n×3 数组。

若真彩色图像的数据类型为 `single` 或 `double`，则值应在 [0, 1] 范围内。如果像素值超出此范围，则可以使用 <a href="../rescale/rescale.html">rescale</a> 函数将像素值缩放到范围 [0, 1] 内。

**数据类型：**`single` | `double` | `uint8` | `uint16`

**<a id="Q3"></a> BW — 二值图像**  
矩阵

二值图像，指定为矩阵。

**数据类型：**`logical`

**<a id="Q4"></a> X — 索引图像**  
由正整数组成的二维矩阵

索引图像，指定为由正整数组成的二维矩阵。`X` 中的值是指向 `map` 指定的颜色图的索引。

**数据类型：**`single` | `double` | `uint8` | `logical`

**<a id="Q5"></a> map — 颜色图**  
c×3 矩阵

与索引图像 `X` 关联的颜色图，指定为 c×3 矩阵。`map` 的每行都是一个三元素 RGB，指定颜色图的单种颜色的红、绿和蓝分量。当 `map` 的数据类型为 `single` 或 `double` 时，矩阵的值必须在 [0, 1] 范围内。

**数据类型：**`single` | `double` | `uint8`

<!-- **<a id="Q6"></a> filename — 文件名**  
字符串标量 | 字符向量

文件名，指定为字符串标量或字符向量。图像可由 <a href="../imread/imread.html">imread</a> 函数读取。`imshow` 函数显示图像，但不将图像数据存储在工作区中。如果该文件包含多个图像，则 `imshow` 显示文件中的第一个图像。

**示例：**"peppers.png"

**数据类型：**`string` | `char` -->

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imread/imread.html">imread</a> | <a 
href="../image/image.html">image</a> | <a 
href="../imwrite/imwrite.html">imwrite</a> | <a 
href="../imfinfo/imfinfo.html">imfinfo</a> 
<!-- | <a 
href="../colormap/colormap.html">colormap</a> | <a 
href="../imagesc/imagesc.html">imagesc</a>  -->
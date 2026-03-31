## imfill
填充

## 简介
[ `BW2 = imfill(BW, locations)`](#function1)  
[ `BW2 = imfill(BW, locations, conn)`](#function2)  
[ `BW2 = imfill(BW, "holes")`](#function3)  
[ `BW2 = imfill(BW, "holes")`](#function4)   
[ `I2 = imfill(I)`](#function5)   
[ `I2 = imfill(I, conn)`](#function6) 

## 用法
<a id="function1"></a>
[BW2](#Q5) = imfill([BW](#Q1), [locations](#Q2)) 从 `locations` 中指定的点开始，对输入二值图像 `BW` 的背景像素执行泛洪填充运算。  
<a id="function2"></a>
[BW2](#Q5)  = imfill([BW](#Q1), [locations](#Q2), [conn](#Q4)) 填充由 `locations` 定义的区域，其中 `conn` 指定连通性。  
<a id="function3"></a>
[BW2](#Q5)  = imfill([BW](#Q1), "holes") 填充输入二值图像 `BW` 中的孔。在此语法中，孔是无法通过从图像边缘填充背景来到达的一组背景像素。  
<a id="function4"></a>
[BW2](#Q5)  = imfill([BW](#Q1), [conn](#Q4), "holes")  填充二值图像 `BW` 中的孔，其中 `conn` 指定连通性。  
<a id="function5"></a>
[I2](#Q6) = imfill([I](#Q3)) 填充灰度图像I中的孔。在此语法中，孔定义为由较亮像素包围的一个暗像素区域。  
<a id="function6"></a>
[I2](#Q6) = imfill([I](#Q3), [conn](#Q4)) 填充灰度图像 `I` 中的孔，其中 `conn` 指定连通性。

## 参数说明
### 输入参数
**<a id="Q1"></a> BW — 二值图像**  
逻辑数组

二值图像，指定为任意维度的逻辑数组。

**数据类型**： `logical`

**<a id="Q2"></a> locations — 标识像素位置的线性索引**  
p×ndims(BW) 正整数矩阵 | p 元素正整数列向量

标识像素位置的索引，指定为以下选项之一。
- 要使用下标索引指定 p 个位置，请指定一个 p × ndims(BW) 正整数矩阵。此处，ndims(BW) 是输入图像的维数，每行包含一个位置的下标索引。
- 要使用线性索引指定 p 个位置，请指定一个 p 元素正整数列向量。

**示例**：  [3 4] 指定二维输入图像内的一个位置，其行和列索引为 (3, 4)。  
**示例**：  2 指定对应于线性索引 2 的单个位置。  
**示例**：  [2; 8; 16] 指定对应于线性索引 2、8 和 16 的三个位置。

**数据类型**： `double` 

**<a id="Q3"></a> I — 灰度图像**  
数值数组

灰度图像，指定为任意维度的数值数组。

**数据类型**： `single` | `double` | `uint8` | `uint16` | `int8` | `int16` | `logical`

**<a id="Q4"></a> conn — 像素连通性**  
4 | 8 

像素连通性，指定为下表中的值之一。对于二维图像，默认连通性是 4。

<table><tr><td>值</td> <td colspan="2">意义</td></tr><tr><td colspan="3">二维连通</td></tr><tr><td>4</td><td>如果像素的边缘相互接触，则这些像素具有连通性。像素的邻域是水平或垂直方向上的相邻像素。</br></td></tr><tr><td>8</td><td>如果像素的边缘或角相互接触，则这些像素具有连通性。像素的邻域是水平、垂直或对角线方向上的相邻像素。</br> </br></td></tr></table>

**数据类型**：  `double` | `logical`

### 输出参数
**<a id="Q5"></a> BW2 — 填充的二值图像**   
逻辑数组

填充的二值图像，以逻辑数组形式返回。

**<a id="Q6"></a> I2 — 填充的灰度图像**  
数值数组

填充的灰度图像，以数值数组形式返回。

## 算法
`imfill` 使用基于形态学重新构造的算法 [[1]](#R1)。

## <a id="R1"></a> 参考文献  
[1] Soille P. Morphological image analysis: principles and applications. Berlin: Springer, 1999.

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../conndef/conndef.html">conndef</a> | <a 
href="../bwselect/bwselect.html">bwselect</a> | <a 
href="../imreconstruct/imreconstruct.html">imreconstruct</a> 





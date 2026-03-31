## bwareafilt  
按面积从二值图像中提取对象

## 简介  
[ `BW2 = bwareafilt(BW, range)`](#function1)  
[ `BW2 = bwareafilt(BW, n)`](#function2)  
[ `BW2 = bwareafilt(BW, n, keep)`](#function3)  
[ `BW2 = bwareafilt(___, conn)`](#function4)

## 用法  
<a id="function1"></a>
[BW2](#Q1) = bwareafilt([BW](#Q2), [range](#Q3)) 从二值图像 [`BW`](#Q2) 中提取对象面积在指定 [`range`](#Q3) 内的所有连通分量（对象），并生成另一个二值图像 [`BW2`](#Q1) ，`bwareafilt` 返回仅包含符合条件的那些对象的二值图像 [`BW2`](#Q1) 。
<a id="function2"></a>  
[BW2](#Q1) = bwareafilt([BW](#Q2), [n](#Q4)) 保留 [`n`](#Q4) 个最大对象。如果第 [`n`](#Q4) 个位置出现面积相等（平局 /tie），则 [`BW2`](#Q1) 中仅包含前 [`n`](#Q4) 个对象。
<a id="function3"></a>  
[BW2](#Q1) = bwareafilt([BW](#Q2), [n](#Q4), [keep](#Q5)) 指定是保留 [`n`](#Q4) 个最大对象还是 [`n`](#Q4) 个最小对象。
<a id="function4"></a>  
[BW2](#Q1) = bwareafilt(___, [conn](#Q6)) 指定定义对象的像素连通性。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 要滤波的图像**  
逻辑矩阵

要滤波的图像，指定为二值图像。

**数据类型：** `logical`

**<a id="Q3"></a>range — 最小和最大面积**  
二元数值向量

面积的最小值和最大值，指定为 [low high] 形式的数值向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q4"></a>n — 要包含的对象数量**  
正整数

按大小对图像对象进行滤波时要包含的对象数量，指定为数值标量。

**数据类型：** `double`

**<a id="Q5"></a>keep — 要包含的对象的大小**  
"largest"（默认）| "smallest"

要包含在输出图像中的对象的大小，指定为 "largest" 或 "smallest"，如果第 n 个位置出现结值，则 `bwareafilt` 仅包括前 n 个对象。

**数据类型：** `char` | `string`

**<a id="Q6"></a>conn — 像素连通性**  
8（默认）| 4

像素连通性，指定为下列值之一：

| **值** | **意义** | **图示** |
|:--|:--|:--|
| <th colspan=3 align="left">二维连通</th> |
| 4 |如果像素的边缘相互接触，则这些像素具有连通性，如果两个相邻像素都为 on 并在水平或垂直方向上连通，则它们是同一对象的一部分。|<img src="4_neighborhood.png" alt="Jet Color Map" style="width:50%;"> <br>当前像素以灰色显示。|
| 8 |如果像素的边缘或角相互接触，则这些像素具有连通性，如果两个相邻像素都为 on 并在水平、垂直或对角线方向上连通，则它们是同一对象的一部分。|<img src="8_neighborhood.png" alt="Jet Color Map" style="width:50%;"> <br>当前像素以灰色显示。|

**数据类型：** `double` | `logical`

### 输出参数  
**<a id="Q1"></a>BW2 — 滤波后的图像**  
逻辑矩阵

滤波后的图像，以与输入图像 [`BW`](#Q2) 大小和类型相同的二值图像形式返回。

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../bwareaopen/bwareaopen.html">bwareaopen</a> | <a 
href="../bwconncomp/bwconncomp.html">bwconncomp</a> | <a 
href="../conndef/conndef.html">conndef</a> | <a 
href="../regionprops/regionprops.html">regionprops</a>
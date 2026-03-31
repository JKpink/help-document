## bwconvhull 
从二值图像生成凸包图像

## 简介
[ `CH = bwconvhull(BW)`](#function1)   
[ `CH = bwconvhull(BW, method)`](#function2)   
[ `CH = bwconvhull(BW, 'objects', conn)`](#function3)

## 用法
<a id="function1"></a>
[CH](#Q1) = bwconvhull([BW](#Q2)) 计算 `BW` 中所有物体的凸包，并返回 `CH`，一个二值凸包图像。 

<a id="function2"></a>
[CH](#Q1) = bwconvhull([BW](#Q2), [method](#Q3)) 指定计算凸包图像的所需方法。

<a id="function3"></a>
[CH](#Q1) = bwconvhull([BW](#Q2), 'objects', [conn](#Q4)) 指定所需的连接在定义单个前景对象时使用。

## 参数说明
### 输入参数
**<a id="Q2"></a>BW — 输入二值图像**  
二维逻辑矩阵

输入二值图像，指定为二维逻辑矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q3"></a>method — 用于计算凸包的方法**  
'union'(默认) | 'objects'

用于计算凸包的方法，指定为以下之一：

| **值** | **描述** |
|:-|:-|
| 'union' | 计算所有前景对象的凸包，将它们视为一个对象 |
| 'objects' | 分别计算二值图像 `BW` 每个连通分量的凸包。`CH` 包含每个连通分量的凸包。

**数据类型：** `char` | `string`

**<a id="Q4"></a>conn — 像素连通性**  
8（默认）| 4 

像素连通性，指定为以下值之一。`conn` 参数仅在 [`method`](#Q3) 为 'objects' 时有效。

| **值** | **意义** |
|:--|:--|
| 二维连通 |
| 4 |如果像素的边缘相互接触，则这些像素具有连通性。像素的邻域是水平或垂直方向上的相邻像素。||
| 8 |如果像素的边缘或角相互接触，则这些像素具有连通性。像素的邻域是水平、垂直或对角线方向上的相邻像素。||

连通性也可以通过指定一个由 0 和 1 组成的 3×3 矩阵来更一般地定义。其中值为 1 的元素定义了相对于 conn 中心元素的邻域位置。该矩阵必须关于其中心元素对称。

**数据类型：** `double`

### 输出参数
**<a id="Q1"></a>CH — 输入图像中所有前景对象的凸包的二值掩模**  
二维逻辑矩阵

输入图像中所有前景对象的凸包的二值掩模，以二维逻辑矩阵的形式返回。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../bwconncomp/bwconncomp.html">bwconncomp</a> | <a
href="../bwlabel/bwlabel.html">bwlabel</a> | <a 
href="../labelmatrix/labelmatrix.html">labelmatrix</a> | <a 
href="../regionprops/regionprops.html">regionprops</a> 
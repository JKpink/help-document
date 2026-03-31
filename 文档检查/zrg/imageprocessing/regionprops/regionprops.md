## regionprops 
测量图像区域的属性

## 简介
[ `stats = regionprops(BW, properties)`](#function1)  
[ `stats = regionprops(L, properties)`](#function2)  
[ `stats = regionprops(CC, properties)`](#function3)  

## 用法
<a id="function1"></a>
[stats](#Q1) = regionprops([BW](#Q2), [properties](#Q3)) 测量二值图像 `BW` 中每个对象的属性。  
<a id="function2"></a>
[stats](#Q1) = regionprops([L](#Q4), [properties](#Q3)) 测量标注图像 `L` 中每个标注区域的属性。  
<a id="function3"></a>
[stats](#Q1) = regionprops([CC](#Q5), [properties](#Q3)) 测量每个连通分量 `CC` 的属性。

## 参数说明
### 输入参数

**<a id="Q2"></a>BW — 二值图像**  
逻辑数组

二值图像，指定为任意维度的逻辑数组。

`regionprops` 根据每个分量的 top-left 极值，从左到右对二值图像中的对象进行排序。当多个对象具有相同的水平位置时，该函数从上到下对这些对象进行排序，然后再沿任何更高的维度进行排序。`regionprops` 返回测量的属性 [`stats`](#Q1)，顺序与排序的对象相同。

**数据类型:** `logical`

**<a id="Q4"></a>L — 标注图像**  
数值数组 | 分类数组

标注图像，指定为下列项之一：
 - 任意维数的数值数组，标注为 0 的像素构成背景。标注为 1 的像素构成一个对象；标注为 2 的像素构成第二个对象；以此类推。`regionprops` 将负值像素视为背景，并向下舍入非整数的输入像素。您可以通过 <a href="../watershed/watershed.html">watershed</a> 或 <a href="../labelmatrix/labelmatrix.html">labelmatrix</a> 等标注函数得到一个数值标注图像。
 - 分类数组。每个类别对应一个不同区域。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` 

**<a id="Q5"></a>CC — 连通分量**  
结构体

连通分量，指定为具有四个字段的结构体。您可以通过使用 <a href="../bwconncomp/bwconncomp.html">`bwconncomp`</a> 或 <a href="../bwpropfilt/bwpropfilt.html">`bwpropfilt`</a> 函数来获得连通分量结构体。 

| **字段** | **描述** |
|:-|:-|
| Connectivity | 连通分量（对象）的连通性 |
| ImageSize | 二值图像的大小 |
| NumObjects |  二值图像中连通分量（对象）的数量 |
| PixelIdxList |  1xNumObjects 的单元数组，其中单元数组中的第 k 个元素是一个向量，包含第 k 个对象中像素的线性索引。 |

**数据类型：** `struct`

**<a id="Q3"></a>properties — 测量的类型**  
"basic"（默认） | 字符串标量或字符向量的逗号分隔列表 | 字符串标量数组 | 字符向量的元胞数组 | "all"

测量的类型，指定为字符串标量或字符向量的逗号分隔列表、字符串标量数组、字符向量的元胞数组，或者指定为 "all" 或 "basic"。
 - 如果指定 "all"，则 `regionprops` 会计算所有形状测量值，对于灰度图像，还会计算像素值测量值。
 - 如果指定 "basic"，则 `regionprops` 仅计算 "Area"、"Centroid" 和 "BoundingBox" 测量值。

下列各表列出了提供形状测量值的所有属性，表中列出的属性仅在指定灰度图像时有效。

**形状测量值**

| **属性名称** | **描述** |
|:-:|:-|
| "BoundingBox" | 包含区域的最小外接框的位置和大小，以 1×(2*Q) 向量形式返回，其中 Q 是图像维度。前 Q 个元素是边界框最小边角的坐标。接下来的 Q 个元素是外接框沿每个维度的大小。 |
|"Centroid" |区域的质心，以 1×Q 向量形式返回，其中 Q 是图像维度。Centroid 的第一个元素是质心的水平坐标（即 x 坐标），第二个元素是垂直坐标（即 y 坐标），Centroid 的所有其他元素均按维度顺序排列。|
|"Circularity"|对象的圆度，以具有字段 Circularity 的结构体形式返回。该结构体包含输入图像中每个对象的圆度值。|
|"ConvexArea"|ConvexImage 中的像素数，以标量形式返回。|
|"ConvexHull" | 可以包含区域的最小凸多边形，以 p×2 矩阵形式返回。矩阵的每一行包含多边形一个顶点的 x 和 y 坐标。|
|"ConvexImage" |指定凸包的图像，凸包内的所有像素均被填充（设置为 on），以二值图像形式返回。图像大小与区域边界框的大小相同。 |
| "Eccentricity" |与区域具有相同二阶矩的椭圆的偏心率，以标量形式返回。偏心率是椭圆焦距与其长轴的比值，该值介于 0 和 1 之间。（0 和 1 是特例。偏心率为 0 的椭圆其实是圆，偏心率为 1 的椭圆是线段。） |
| "EulerNumber"	| 区域中的对象数减去这些对象中的孔洞数，以标量形式返回。仅二维标签矩阵支持此属性。regionprops 使用 8 连通计算欧拉数（也称为欧拉示性数）。|
|"Extent"	| 区域中的像素数与边界框中总像素数的比率，以标量形式返回。计算方法为 Area 除以边界框的面积。|
|"Extrema"	|区域中的极值点，以 8×2 矩阵形式返回。矩阵的每一行都包含其中一个点的 x 和 y 坐标。向量的形式为[top-left top-right right-top right-bottom bottom-right bottom-left left-bottom left-top]。对于某些形状，多个极值点可以具有相同的坐标。|
|"FilledArea"| FilledImage 中 on 像素的数量，以标量形式返回。|
|"FilledImage"	|与区域的边界框大小相同的图像，以二值数组形式返回，on 像素对应于该区域，所有孔洞都已填充。| 
|"Image"|与区域的边界框大小相同的图像，以二值数组形式返回。on 像素对应于该区域，所有其他像素为 off。|
|"MajorAxisLength"	| 与区域具有相同归一化二阶中心矩的椭圆长轴的长度（以像素为单位），以标量形式返回。|
| "MinorAxisLength" | 与区域具有相同归一化二阶中心矩的椭圆短轴的长度（以像素为单位），以标量形式返回。|
|"Orientation" | x轴与椭圆长轴（该椭圆与区域具有相同的二阶矩）之间的角度，以标量形式返回。该值以度为单位，范围从 -90 度到 90 度。|
| "Perimeter" | 围绕区域边界的距离，以标量形式返回。regionprops 通过计算围绕区域边界的相邻像素对之间的距离来计算周长。如果图像包含不连续区域，regionprops 将返回意外结果。 |
| "PixelIdxList" | 区域中像素的线性索引，以包含 p 个元素的向量形式返回。 |
| "PixelList" | 区域中像素的位置，以 p×Q 矩阵形式返回。矩阵的每一行都具有 [x y z ...] 形式，指定区域中一个像素的坐标。 |
| "Solidity" | 凸包中区域内像素所占的比例，以标量形式返回。实度计算为 Area/ConvexArea。|

### 输出参量
**<a id="Q1"></a>stats — 测量值**  
字符串数组

测量值，以字符串数组形式返回。每行对应一个区域，包含由 `properties` 指定的属性文本表示。数组长度等于区域数，顺序与输入图像中区域排列顺序一致。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../bwconncomp/bwconncomp.html">bwconncomp</a> | <a 
href="../watershed/watershed.html">watershed</a> | <a 
href="../labelmatrix/labelmatrix.html">labelmatrix</a> 
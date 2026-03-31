## bwpropfilt  
按照属性从二值图像中提取对象

## 简介  
[`BW2 = bwpropfilt(BW,prop,range)`](#function1)  
[`BW2 = bwpropfilt(BW,prop,n)`](#function2)  
[`BW2 = bwpropfilt(BW,prop,n,keep)`](#function3)   
[`BW2 = bwpropfilt(___,conn)`](#function5)  

[`CC2 = bwpropfilt(CC,prop,range)`](#function6)  
[`CC2 = bwpropfilt(CC,prop,n)`](#function7)  
[`CC2 = bwpropfilt(CC,prop,n,keep)`](#function8)  

## 用法  
<a id="function1"></a>  
[BW2](#Q1) = bwpropfilt([BW](#Q2), [prop](#Q3), [range](#Q4))  保留属性 `prop` 值在 `range` 范围内的所有对象。  
<a id="function2"></a>  
[BW2](#Q1) = bwpropfilt([BW](#Q2), [prop](#Q3), [n](#Q5))  保留按 `prop` 排序后最大的 `n` 个对象；并列时取前 `n` 个。  
<a id="function3"></a>  
[BW2](#Q1) = bwpropfilt([BW](#Q2), [prop](#Q3), [n](#Q5), [keep](#Q6))  选择保留最大或最小：`keep = "largest"`（默认）或 `"smallest"`。  
<a id="function5"></a>  
[BW2](#Q1) = bwpropfilt(___, [conn](#Q8))  指定像素连通度 `conn`。  
<a id="function6"></a>  
[CC2](#Q9) = bwpropfilt([CC](#Q10), [prop](#Q3), [range](#Q4))  对连通域结构 `CC` 进行区间过滤，返回新的连通域结构。  
<a id="function7"></a>  
[CC2](#Q9) = bwpropfilt([CC](#Q10), [prop](#Q3), [n](#Q5))  返回最大的 `n` 个连通域。  
<a id="function8"></a>  
[CC2](#Q9) = bwpropfilt([CC](#Q10), [prop](#Q3), [n](#Q5), [keep](#Q6))  选择最大或最小 `n` 个连通域。  

## 参数说明  
### 输入参数  
**<a id="Q2"></a> BW — 二值图像**  
逻辑矩阵  

待过滤的二值图像，指定为逻辑矩阵。 `bwpropfilt` 通过调用 `bwconncomp` 函数在图像内部查找连通分量。

**数据类型：** `logical`

**<a id="Q10"></a> CC — 连通组件**  
结构体  

待过滤的连通分量，指定为结构体。  
您可通过对二值图像调用 `bwconncomp` 函数来获得连通分量结构体。

**数据类型：** `struct`

**<a id="Q3"></a> prop — 属性名称**  
字符向量 | 字符串标量  

过滤所用属性的名称，指定为下列值之一:
| 名称 | 描述 |
|-------|-------|
| "Area" | 图像中的像素个数 |
| "EulerNumber" | 欧拉数（又称欧拉特征），计算为 1 减去区域中孔洞的数量。 |
|"Circularity" |物体的圆度。


**数据类型：** `char` | `string`

**<a id="Q4"></a> range — 最小/最大属性值**  
二元素数值向量  

形式 `[low high]`；可写单值 `n` 退化到 `>=n`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q5"></a> n — 对象数量**  
正整数  

要返回的对象数量，指定为正整数。

**数据类型：** `double`

**<a id="Q6"></a> keep — 保留方向**  
`"largest"` (默认) | `"smallest"`  

要保留的对象，指定为 "largest"（最大）或 "smallest"（最小）。

**数据类型：** `char` | `string`

**<a id="Q8"></a> conn — 像素连通性**  
`8` (默认) | `4` | `3×3` 矩阵  

像素连通性，指定为 4 或 8。


| 值 | 意义 |
| :----------- | :----------- | 
| 二维连通 |  
| 4 | 如果像素的边缘相互接触，则这些像素具有连通性。像素的邻域是水平或垂直方向上的相邻像素。 |  |
| 8 | 如果像素的边缘或角相互接触，则这些像素具有连通性。像素的邻域是水平、垂直或对角线方向上的相邻像素。 | 

连通性还可以通过指定一个 3×3 的 0 和 1 的矩阵来以更一般的方式定义。矩阵中值为 1 的元素表示相对于 `conn` 中心元素的邻域位置，该矩阵必须关于其中心元素对称。

**数据类型：** `double` | `logical`

### 输出参数  
**<a id="Q1"></a> BW2 — 过滤后的二值图像**  
逻辑矩阵  

过滤后的二值图像，以与输入 BW 相同尺寸的逻辑矩阵形式返回。

**数据类型：** `logical`

**<a id="Q9"></a> CC2 — 过滤后的连通组件**  
结构体  

过滤后的连通分量，以结构体形式返回。

**数据类型：** `struct`

## 版本历史  
北太天元图像处理工具箱 V3.0 引入


## 相关主题
<a href="../regionprops/regionprops.html">regionprops</a> | <a href="../bwareafilt/bwareafilt.html">bwareafilt</a> |
<a href="../bwareaopen/bwareaopen.html">bwareaopen</a> |
<a href="../bwconncomp/bwconncomp.html">bwconncomp</a> | <a href="../conndef/conndef.html">conndef</a> | <a href="../cc2bw/cc2bw.html">cc2bw</a>
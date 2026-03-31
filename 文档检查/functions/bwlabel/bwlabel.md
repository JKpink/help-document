## bwlabel  
标记 2 维二值图像中的连通分量

## 简介  
[ `L = bwlabel(BW)`](#function1)  
[ `L = bwlabel(BW, conn)`](#function2)  
[ `[L, n] = bwlabel(___)`](#function3)

## 用法  
<a id="function1"></a>
[L](#Q1) = bwlabel([BW](#Q2)) 返回标签矩阵 [`L`](#Q1)，其中包含在 [`BW`](#Q2) 中找到的 8 连通对象的标签。
<a id="function2"></a>  
[L](#Q1) = bwlabel([BW](#Q2), [conn](#Q3)) 返回标签矩阵，其中 [`conn`](#Q3) 指定连通性。
<a id="function3"></a>  
[[L](#Q1), [n](#Q4)] = bwlabel(\___) 还返回 [`n`](#Q4)，即在 [`BW`](#Q2) 中找到的连通对象的数量。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 二值图像**  
二维数值矩阵 | 二维逻辑矩阵

- 仅支持二维的逻辑数组或数值数组；
- 若为逻辑数组，true 表示目标像素，false 表示背景像素；
- 若为数值数组，非零元素视为目标像素，零元素视为背景像素。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q3"></a>conn — 像素连通性**  
8（默认）| 4

像素连通性，指定为下表中的值之一。默认连通性是8

| **值** | **意义** | **图示** |
|:--|:--|:--|
| <th colspan=3 align="left">二维连通</th> |
| 4 |如果像素的边缘相互接触，则这些像素具有连通性，如果两个相邻像素都为 on 并在水平或垂直方向上连通，则它们是同一对象的一部分。|<img src="4_neighborhood.png" alt="Jet Color Map" style="width:50%;"> <br>当前像素以灰色显示。|
| 8 |如果像素的边缘或角相互接触，则这些像素具有连通性，如果两个相邻像素都为 on 并在水平、垂直或对角线方向上连通，则它们是同一对象的一部分。|<img src="8_neighborhood.png" alt="Jet Color Map" style="width:50%;"> <br>当前像素以灰色显示。|

**数据类型：** `double` | `logical`

### 输出参数  
**<a id="Q1"></a>L — 标签矩阵**  
由非负整数组成的矩阵

由连续区域组成的标签矩阵，以与 [`BW`](#Q2) 大小相同的非负整数矩阵形式返回。标签为 0 的像素构成背景；标签为 1 的像素构成一个对象；标签为 2 的像素构成另一个对象，以此类推。

**数据类型：** `double`

**<a id="Q4"></a>n — 连通对象的数量**  
非负整数

[`BW`](#Q2) 中连通对象的数量，以非负整数形式返回。

**数据类型：** `double`

## 算法  
bwlabel 使用参考文献 [[1]](#Q5)（第 40-48 页）中概述的通用过程：
 1. 对输入图像进行行程长度编码。
 2. 扫描各次运行，从而分配初步标签并在本地等效表中记录标签等效性。
 3. 解析等效类。
 4. 基于解析的等效类重新对各次运行进行标注。

## 参考文献  
<a id="Q5"></a>[1] Haralick R M, Shapiro L G. Computer and Robot Vision, Volume I[M]. Addison-Wesley, 1992: 28-48.

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../bwconncomp/bwconncomp.html">bwconncomp</a> | <a 
href="../bwlabeln/bwlabeln.html">bwlabeln</a> | <a 
href="../bwselect/bwselect.html">bwselect</a> | <a 
href="../labelmatrix/labelmatrix.html">labelmatrix</a> | <a 
href="../label2rgb/label2rgb.html">label2rgb</a> | <a 
href="../regionprops/regionprops.html">regionprops</a> 

## bwlabeln  
标记二值图像中的连通分量

## 简介  
[ `L = bwlabeln(BW)`](#function1)  
[ `L = bwlabeln(BW, conn)`](#function2)  
[ `[L, n] = bwlabeln(___)`](#function3)  

## 用法  
<a id="function1"></a>
[L](#Q1) = bwlabeln([BW](#Q2)) 返回标签矩阵 [`L`](#Q1)，其中包含 [`BW`](#Q2) 中的连通分量的标签。  
<a id="function2"></a>
[L](#Q1) = bwlabeln([BW](#Q2), [conn](#Q3)) 返回标签矩阵，其中 [`conn`](#Q3) 指定连通性。  
<a id="function3"></a>
[[L](#Q1), [n](#Q4)] = bwlabeln(\___) 还返回 [`n`](#Q4)，即在 [`BW`](#Q2) 中找到的连通目标的数量。  

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 二值图像**  
数值数组 | 逻辑数组

二值图像，指定为任意维度的数值或逻辑数组。

- 若为逻辑数组，true 表示目标像素，false 表示背景像素；
- 若为数值数组，非零元素视为目标像素，零元素视为背景像素。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q3"></a>conn — 像素连通性**  
4 | 8 | 6 | 18 | 26

像素连通性，指定为下表中的值之一。

| **值** | **意义** | **图示** |
|:--|:--|:--|
| <th colspan=3 align="left">二维连通</th> |
| 4 |如果像素的边缘相互接触，则这些像素具有连通性，如果两个相邻像素都为 on 并在水平或垂直方向上连通，则它们是同一对象的一部分。|<img src="4_neighborhood.png" alt="Jet Color Map" style="width:50%;"> <br>当前像素以灰色显示。|
| 8 |如果像素的边缘或角相互接触，则这些像素具有连通性，如果两个相邻像素都为 on 并在水平、垂直或对角线方向上连通，则它们是同一对象的一部分。|<img src="8_neighborhood.png" alt="Jet Color Map" style="width:50%;"> <br>当前像素以灰色显示。|
| <th colspan=3 align="left">三维连通</th> |
| 6 | 如果像素的面接触，则这些像素具有连通性。如果两个相邻像素都为 on 并以如下方式连通，则它们是同一目标的一部分：<br>在所列方向之一上连通：内、外、左、右、上、下<br>|<img src="6_neighborhood.png" alt="Jet Color Map" style="width:50%;"> <br>当前像素是立方体的中心。|
| 18 |如果像素的面或边缘接触，则这些像素具有连通性。如果两个相邻像素都为 on 并以如下方式连通，则它们是同一目标的一部分：<br>在所列方向之一上连通：内、外、左、右、上、下<br>在两个方向的组合上连通，如右下或内上|<img src="18_neighborhood.png" alt="Jet Color Map" style="width:50%;"> <br>当前像素是立方体的中心。|
| 26 | 如果像素的面、边缘或角接触，则这些像素具有连通性。如果两个相邻像素都为 on 并以如下方式连通，则它们是同一目标的一部分：<br>在所列方向之一上连通：内、外、左、右、上、下<br>在两个方向的组合上连通，如右下或内上<br>在三个方向的组合上连通，如内右上或内左下 | <img src="26_neighborhood.png" alt="Jet Color Map" style="width:50%;"> <br>当前像素是立方体的中心。|

**数据类型：** `double` | `logical`

### 输出参数  
**<a id="Q1"></a>L — 标签矩阵**  
由非负整数组成的数组

标签矩阵，以非负整数数组形式返回，其大小与 [`BW`](#Q2) 相同。标签为 0 的像素构成背景；标签为 1 的像素构成一个对象；标签为 2 的像素构成另一个对象，等等。

**数据类型：** `double`

**<a id="Q4"></a>n — 连通对象的数量**  
非负整数

[`BW`](#Q2) 中连通对象的数量，以非负整数形式返回。

**数据类型：** `double`

## 算法  
bwlabeln 使用以下一般过程：
 1. 扫描所有图像像素，为非零像素分配初步标签，并将标签等效项记录在一个并查集表中。
 2. 使用并查集算法 [[1]](#Q5) 解析等效类。
 3. 基于解析的等效类重新对像素进行标注。

## 参考文献  
<a id="Q5"></a>[1] Sedgewick R. Algorithms in C[M]. 3rd ed. Addison-Wesley, 1998: 11-20.
## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../bwconncomp/bwconncomp.html">bwconncomp</a> | <a 
href="../bwlabel/bwlabel.html">bwlabel</a> | <a 
href="../labelmatrix/labelmatrix.html">labelmatrix</a> | <a 
href="../label2rgb/label2rgb.html">label2rgb</a> | <a 
href="../regionprops/regionprops.html">regionprops</a> 
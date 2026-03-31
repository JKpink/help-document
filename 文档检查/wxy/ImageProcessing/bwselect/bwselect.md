## bwselect  
在二值图像中选择对象

## 简介  
[ `BW2 = bwselect(BW, c, r)`](#function1)  
[ `BW2 = bwselect(BW, c, r, conn)`](#function2)

## 用法  
<a id="function1"></a>
[BW2](#Q1) = bwselect([BW](#Q2), [c](#Q3), [r](#Q4)) 返回一个二值图像，其中包含与像素 ([`c`](#Q3), [`r`](#Q4)) 重叠的对象，对象是由连通的像素组成的集合，即值为 1 的像素。  
<a id="function2"></a>
[BW2](#Q1) = bwselect([BW](#Q2), [c](#Q3), [r](#Q4), [conn](#Q5)) 还指定了对象的连通性 [`conn`](#Q5) ，为 4 连通或 8 连通。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 二值图像**  
二维数值矩阵 | 二维逻辑矩阵

二值图像，指定为二维数值矩阵或二维逻辑矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`
 
**<a id="Q3"></a>c — 列索引**  
数值标量 | 数值向量

列索引，指定为数值标量或数值向量，且指定为正整数，需要小于BW的列数。如果 `r` 和 `c` 是等长的向量，则 `BW2` 包含与任何像素 (r(k),c(k) )重叠的对象集合。

**示例：** c = [43 185 212];
**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q4"></a>r — 行索引**  
数值标量 | 数值向量

行索引，指定为数值标量或数值向量，且指定为正整数，需要小于BW的行数。如果 `r` 和 `c` 是等长的向量，则 `BW2` 包含与任何像素 (r(k),c(k)) 重叠的对象集合。

**示例：** r = [38 68 181];
**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q5"></a>conn — 像素连通性**  
8（默认）| 4 

像素连通性，指定为下表中的值之一：

| **值** | **描述** |
|:-|:-|
| 4 | 四连通对象 |
| 8 | 八连通对象 |

### 输出参数  
**<a id="Q1"></a>BW2 — 包含重叠指定像素的对象的二值图像**  
逻辑数组

返回一个包含与指定像素重叠的对象的二值图像，形式为逻辑数组。`BW2` 包含与由 `r` 和 `c` 指定的任何像素重叠的对象集合。
如果不指定输出参数，则 `bwselect` 会在新图形中显示输出图像。

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../bwlabel/bwlabel.html">bwlabel</a> | <a 
href="../imfill/imfill.html">imfill</a> | <a 
href="../grayconnected/grayconnected.html">grayconnected</a> | <a 
href="../roipoly/roipoly.html">roipoly</a> 

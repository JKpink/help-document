## graydist  
灰度图像的灰度加权距离变换

## 简介  
[ `T = graydist(I, mask)`](#function1)  
[ `T = graydist(I, ind)`](#function2)  
[ `T = graydist(___, method)`](#function3)  

## 用法  
<a id="function1"></a>
[T](#Q1) = graydist([I](#Q2), [mask](#Q3))   
计算灰度图像 [`I`](#Q2) 的灰度加权距离变换，核心是将图像灰度值作为权重因子，计算非种子像素到最近种子像素的加权距离，输出与原图像尺寸一致的距离变换矩阵。掩码为真的位置是种子位置。  

<a id="function2"></a>
[T](#Q1) = graydist([I](#Q2), [ind](#Q6))   
指定种子位置的线性索引 [`ind`](#Q6) 。  

<a id="function3"></a>
[T](#Q1) = graydist(___, [method](#Q5))   
使用指定的距离度量方法。  

## 参数说明  
### 输入参数  

**<a id="Q2"></a>I — 灰度图像**  
数值数组 | 逻辑数组

灰度图像，指定为数值或逻辑数组。

**<a id="Q3"></a>mask — 二值图像**  
逻辑数组

指定种子位置的二值掩模，表示为与 [`I`](#Q2) 大小相同的逻辑数组。

**<a id="Q6"></a>ind — 索引**  
正整数向量

种子位置的索引，指定为正整数的向量。

**<a id="Q3"></a>method — 距离度量**  
'euclidean'（默认）| 'chessboard' | 'cityblock' | 'quasi-euclidean'

距离度量，指定为下列值之一:

| **方法** | **描述** |
|:-|:-|
| 'chessboard' | 在二维空间中，(x, y) 和 (a, b) 之间的棋盘距离是 $\max(\|x-a\|,\|y-b\|)$ |
| 'cityblock' | 在二维空间中，(x, y)和 (a, b) 之间的城市街区距离（曼哈顿距离）是 $\|x-a\|-\|y-b\|$ |
| 'euclidean' | 在二维空间中，(x, y)和 (a, b) 之间的欧几里得距离是 $\sqrt{(x-a)^2+(y-a)^2}$ |
| 'quasi-euclidean' | 在二维空间中，(x, y) 和 (a, b) 之间的准欧几里得距离为，如果$\|x-a\|>\|y-b\|$,则距离为$\|x-a\|+(\sqrt2-1)\|y-b\|$，否则为$(\sqrt2-1)\|x-a\|+\|y-b\|$ |

### 输出参数  
**<a id="Q1"></a>T — 灰度加权距离变换**  
数值数组

灰度加权距离变换，以与 [`I`](#Q2) 相同大小的数值数组形式返回。

**数据类型：** `double`

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../bwdist/bwdist.html">bwdist</a> | <a 
href="../bwdistgeodesic/bwdistgeodesic.html">bwdistgeodesic</a> | <a 
href="../watershed/watershed.html">watershed</a>

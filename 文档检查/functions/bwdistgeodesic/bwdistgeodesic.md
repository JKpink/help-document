## bwdistgeodesic  
二值图像的测地距离变换

## 简介  
[ `D = bwdistgeodesic(BW, mask)`](#function1)  
[ `D = bwdistgeodesic(BW, idx)`](#function3)  
[ `D = bwdistgeodesic(___, method)`](#function4)

## 用法  
<a id="function1"></a>
[D](#Q1) = bwdistgeodesic([BW](#Q2), [mask](#Q3)) 计算给定二值图像 [`BW`](#Q2) 和由 [`mask`](#Q3) 指定的种子位置的测地距离变换。逻辑值为 false 的区域视为障碍区域（Obstacle Region），测地距离计算中不可穿越；逻辑值为 true 的区域为可行域（Feasible Region），仅在该区域内计算最短路径。对于 [`BW`](#Q2) 中的每个 true 像素，测地距离变换分配一个数字，表示该像素与 [`mask`](#Q3) 中最邻近的 true 像素之间的测地距离。输出矩阵 [`D`](#Q1) 包含测地距离。  
<a id="function3"></a> 
[D](#Q1) = bwdistgeodesic([BW](#Q2), [idx](#Q7)) 计算二值图像 [`BW`](#Q2) 的测地距离变换。[`idx`](#Q7) 是种子位置的线性索引向量。
<a id="function4"></a>  
[D](#Q1) = bwdistgeodesic(___, [method](#Q6)) 使用方法指定的替代距离度量计算测地距离变换。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 二值图像**  
数值数组 | 逻辑数组

- 仅支持二维的逻辑数组或数值数组；
- 若为逻辑数组，true 表示目标像素，false 表示背景像素；
- 若为数值数组，非零元素视为目标像素，零元素视为背景像素。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q3"></a>mask — 种子位置**  
数值数组 | 逻辑数组

种子位置，指定为与 [`BW`](#Q2) 大小相同的逻辑数组。

- mask 中true的位置为种子点，false为非种子点；
- mask 若输入数值数组，种子位置必须为非负整数；
- mask 的维度和大小必须与 BW 完全一致。

**数据类型：** `uint8` | `logical`

**<a id="Q7"></a>idx — 种子位置的线性索引**  
正整数向量

种子位置的线性索引，指定为正整数向量。

**<a id="Q3"></a>method — 距离度量**  
'euclidean'（默认）| 'chessboard' | 'cityblock' | 'quasi-euclidean'

距离度量，指定为下列值之一:

| **方法** | **描述** |
|:-|:-|
| 'chessboard' | 在二维空间中，(x, y) 和 (a, b) 之间的棋盘距离是 $\max(\|x-a\|,\|y-b\|)$ |
| 'cityblock' | 在二维空间中，(x, y)和 (a, b) 之间的城市街区距离（曼哈顿距离）是 $\|x-a\|-\|y-b\|$ |
| 'euclidean' | 在二维空间中，(x, y)和 (a, b) 之间的欧几里得距离是 $\sqrt{(x-a)^2+(y-a)^2}$ |
| 'quasi-euclidean' | 在二维空间中，(x, y) 和 (a, b) 之间的准欧几里得距离为，如果$\|x-a\|>\|y-b\|$,则距离为$\|x-a\|+(\sqrt2-1)\|y-b\|$，否则为$(\sqrt2-1)\|x-a\|+\|y-b\|$ |

**数据类型：** `char` | `string`

### 输出参数  
**<a id="Q1"></a>D — 测地距离**  
数值数组

测地距离，以与[ `BW` ](#Q1)大小相同的数值数组形式返回。

- BW 为 false（障碍区域）的像素，D 中值为NaN（不可达）；
- BW 为 true 且是种子点的像素，D 中值为 0；
- BW 为 true 且不是种子点的像素，若所在可行域中不存在种子，D 中值为NaN；若所在可行域中存在种子，D 中值为可行域内到最近种子点的测地距离

**数据类型：** `double`

## 算法  
`bwdistgeodesic` 使用 Soille, P. 在《形态图像分析：原理与应用》（第二版）中描述的测地距离算法，该书由施普林格出版社于 2003 年出版，出版地为美国新泽西州锡考克斯，第 219–221 页。

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../bwdist/bwdist.html">bwdist</a> | <a 
href="../graydist/graydist.html">graydist</a>



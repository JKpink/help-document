## bwtraceboundary 
在二值图像中跟踪对象边界

## 简介
[`B = bwtraceboundary(BW, P, fstep)`](#function1)  
[`B = bwtraceboundary(BW, P, fstep, conn)`](#function2)  
[`B = bwtraceboundary(BW, P, fstep, conn, m, dir)`](#function3)

## 用法
<a id="function1"></a>
[B](#Q1) = bwtraceboundary([BW](#Q2), [P](#Q3), [fstep](#Q4)) 跟踪二进制图像 `BW` 中对象的轮廓。非零像素属于对象，零值像素构成背景。`P` 指定对象边界上要开始跟踪的点的行和列坐标。`fstep` 指定连接到 `P` 的下一个对象像素的初始搜索方向。`B` 保留该区域的边界像素的行和列坐标。  
<a id="function2"></a>
[B](#Q1) = bwtraceboundary([BW](#Q2), [P](#Q3), [fstep](#Q4), [conn](#Q5)) 跟踪边界，其中 `conn` 指定所需的连通性。  
<a id="function3"></a>
[B](#Q1) = bwtraceboundary([BW](#Q2), [P](#Q3), [fstep](#Q4), [conn](#Q5), [m](#Q6), [dir](#Q7)) 指定 `m` （要提取的最大边界像素数）和 `dir` （跟踪边界的方向）。默认情况下，`bwtraceboundary` 标识边界上的所有像素。  

## 参数说明
### 输入参数
**<a id="Q2"></a> BW — 二值图像**  
二维数值 | 逻辑矩阵

二值图像，指定为二维数值或逻辑矩阵。

**<a id="Q3"></a> P — 起点坐标**  
二元素向量

对象边界上您希望开始追踪的起点坐标，指定为格式为 [行 列] 的二元素向量。

**数据类型：** `double`

**<a id="Q4"></a> fstep — 初始搜索方向**  
"N" | "NE" | "E" | "SE" | "S" | "SW" | "W" | "NW"

下一个与 [P](#Q3) 相连的对象像素的初始搜索方向，指定为字符向量或字符串标量。

**数据类型：** `char` | `string`

**<a id="Q5"></a> conn — 像素连通性**  
8 (默认) | 4

像素连通性，指定为 4 或 8。


| 值 | 意义 | 
| :----------- | :----------- |
| 二维连通 |  
| 4 | 如果像素的边缘相互接触，则这些像素具有连通性。像素的邻域是水平或垂直方向上的相邻像素。 |  |
| 8 | 如果像素的边缘或角相互接触，则这些像素具有连通性。像素的邻域是水平、垂直或对角线方向上的相邻像素。 | 

**数据类型**： `double` 

**<a id="Q6"></a> m — 要提取的边界像素的最大数量**  
Inf (默认) | 正整数

要提取的边界像素的最大数量，指定为正整数。默认情况下，m 为 Inf，`bwtraceboundary` 会识别出所有边界上的像素。

**数据类型：** `double`

**<a id="Q7"></a> dir — 追踪边界的方向**  
"clockwise"（顺时针，默认）| "counterclockwise"(逆时针)

顺时针或逆时针方向追踪边界的方向。

**数据类型：** `char` | `string`

### 输出参量
**<a id="Q1"></a> B — 边界像素的行和列坐标**  
q×2 矩阵

区域的边界像素的行和列坐标，以 q×2 矩阵的形式返回，`B` 的每一行具有[行 列]的形式。

## 参考
 [1] Gonzalez R C, Woods R E, Eddins S L.Digital image processing using MATLAB. New Jersey: Pearson Prentice Hall, 2004.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../bwboundaries/bwboundaries.html">bwboundaries</a> | <a 
href="../bwperim/bwperim.html">bwperim</a> 

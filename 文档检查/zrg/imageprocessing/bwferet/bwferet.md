## bwferet
图像中对象的Feret属性

## 简介
[`out = bwferet(BW,properties)`](#function1)  
[`out = bwferet(CC,properties)`](#function2)  
[`out = bwferet(L,properties)`](#function3)  
[`out = bwferet(input)`](#function4)


## 用法
<a id="function1"></a>
[out](#Q1) = bwferet([BW](#Q2), [properties](#Q3)) 测量图像中目标对象的 Feret 属性，并将测量结果以表格形式返回。输入参数`properties`指定需为输入二值图像`BW`中每个目标对象测量的 Feret 属性。所测量的Feret属性包括 Feret 最小直径， Feret 最大直径， Feret 角，以及 Feret 直径的端点坐标。

<a id="function2"></a>
[out](#Q1) = bwferet([CC](Q4), [properties](#Q3)) 对CC结构中的每个连通分量都计算Feret属性。

<a id="function3"></a>
[out](#Q1) = bwferet([L](#Q5), [properties](#Q3)) 测量输入标签矩阵`L`中每个对象的Feret属性。

<a id="function4"></a>
[out](#Q1) = bwferet([input](#Q6)) 测量输入的最大 Feret 直径、其相对方位角以及对应的坐标值，并以表格形式返回测量结果。输入可以是二值图像`BW`、连通分量`CC`或标签矩阵`L`。



## 参数说明
### 输入参数
**<a id="Q2"></a> BW —— 二值图像**
逻辑矩阵 | 数值矩阵

二值图像，被指定为逻辑型或数值型矩阵。对于数值型输入，所有非零像素均被视作 1（true）。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`

**<a id="Q4"></a> CC —— 连通分量**
结构体

连通分量，被指定为一个结构体，该结构体包含以下表格中四个字段。
| 字段 | 说明 |
|-------|-------|
|Connectivity| 连通分量的连通方式 |
| ImageSize | 输入二值图像的尺寸|
|NumObjects | 输入二值图像中连通分量的数量       |
|PixelIdxList| `1×NumObjects`元胞数组，其中第`k`个元素为一个向量，包含第`k`个目标对象中所有像素的线性索引|

可以使用<a href="../ bwconncomp / bwconncomp .html"> bwconncomp </a>函数从二值图像中生成连通分量。

**数据类型：**`struct`

**<a id="Q5"></a> L —— 标签数组**
非负整数矩阵

连续区域的标签矩阵，被指定为一个由非负整数构成的矩阵。标记为 0 的像素属于背景；标记为 1 的像素构成第一个目标；标记为 2 的像素构成第二个目标，依此类推。`L` 所表示的目标数量等于 `L` 的最大值。可使用<a href="../ bwlabel / bwlabel .html"> bwlabel </a>函数由二值图像生成标签矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`

**<a id="Q3"></a> properties —— Feret属性标签**
"MaxFeretProperties" | "MinFeretProperties" | "all"

Feret属性标签，被指定为`MaxFeretProperties`（含最大直径，对应角度，端点坐标），`MinFeretProperties`（含最小直径，对应角度，端点坐标）或者`all`（所有Feret属性，默认取值）。

**数据类型：**`char` | `string` 

**<a id="Q6"></a> input —— 通用输入**
数值矩阵 | 逻辑矩阵 | 结构体 | 非负整数矩阵

通用输入，被指定为以下值：

  • 数值矩阵或逻辑矩阵 —— 当输入为二值图像(BW)。
  • 结构体 —— 当输入为连通分量(CC)。
  • 非负整数矩阵 —— 当输入是标签矩阵(L)。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical` | `struct`

### 输出参数
**<a id="Q1"></a> out —— Feret属性表**
m×n表格

Feret属性表，返回m×n形式的表格。其中`m`为待测算Feret属性的目标对象数量,`n`的取值为 3 或 6，具体取决于输入的属性参数。

  • 若属性参数输入为 `MaxFeretProperties`，则输出表格为 m×3 规格，包含三列，分别为最大直径、最大角度和最大坐标。
  • 若属性参数输入为 `MinFeretProperties`，则输出表格为 m×3 规格，包含三列，分别为最小直径、最小角度和最小坐标。
  • 若属性参数输入为`all`，则输出表格为 m×6 规格，包含本表格所列的全部列。

| 列名 | 描述 |
|-------|-------|
| MaxDiameter | 目标对象的最大Feret直径，定义为包围该对象的凸包对跖顶点上任意两个边界点之间的最大距离 |
| MaxAngle | 最大Feret直径相对于图像水平轴的方向角，取值为角度制，范围为 [–180°, 180°] |
|MaxCoordinates|最大费雷特直径的端点坐标，以 $\begin{pmatrix}x_1 & y_1 \\ x_2 & y_2\end{pmatrix}$ 形式返回 |
|MinDiameter|目标对象的最小费雷特直径，定义为包围该对象的凸包对跖顶点上任意两个边界点之间的最小距离|
|MinAngle|最小费雷特直径相对于图像水平轴的方向角，取值为角度制，范围为 [–180°, 180°] |
|MinCoordinates	|最小费雷特直径的端点坐标，以 $\begin{pmatrix}x_1 & y_1 \\ x_2 & y_2\end{pmatrix}$ 形式返回 |


**数据类型：** `uint8`


## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../bwconncomp/bwconncomp.html">bwconncomp</a> | <a href="../bwlabel/bwlabel.html">bwlabel</a> | <a href="../labelmatrix/labelmatrix.html">labelmatrix</a> | <a 
href="../bwlabeln/bwlabeln.html">bwlabeln</a> | <a href="../regionprops/regionprops.html">regionprops</a>






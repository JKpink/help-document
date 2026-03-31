## strel
形态学结构元

## 简介
[`SE = strel(nhood)`](#function1)  
[`SE = strel("diamond", r)`](#function2)  
[`SE = strel("disk", r)`](#function3)  
[`SE = strel("disk", r, n)`](#function4)  
[`SE = strel("octagon", r)`](#function5)  
[`SE = strel("line", len, deg)`](#function6)  
[`SE = strel("rectangle", [m n])`](#function7)  
[`SE = strel("square", w)`](#function8)  
[`SE = strel("cube", w)`](#function9)  
[`SE = strel("cuboid", [m n p]`](#function10)  
[`SE = strel("sphere", r)`](#function11) 

## 用法
<a id="function1"></a>
SE = strel([nhood](#Q1))  创建一个具有指定邻域 `nhood` 的平面结构元素。
<a id="function2"></a>
SE = strel("diamond", [r](#Q2)) 创建一个菱形结构元素，其中 `r` 指定从结构元素原点到菱形各点的距离。
<a id="function3"></a>
SE = strel("disk", [r](#Q2)) 创建一个盘形结构元素，其中 `r` 指定半径。
<a id="function4"></a>
SE = strel("disk", [r](#Q2), [n](#Q3)) 创建一个盘形结构元素，其中 `r` 指定半径，`n` 指定用于逼近盘形的线条结构元素的数量。当结构元素使用逼近时，使用盘形逼近的形态学运算的运行速度要快得多。
<a id="function5"></a>
SE = strel("octagon", [r](#Q2)) 创建一个八边形结构元素，其中 `r` 指定从结构元素原点到八边形边的距离，沿水平和垂直轴测量。`r` 必须为 3 的非负倍数。
<a id="function6"></a>
SE = strel("line", [len](#Q4), [deg](#Q5)) 创建一个关于邻域中心对称的线性结构元素，长度约为 `len`，角度约为 `deg`。
<a id="function7"></a>
SE = strel("rectangle", [ [m n] ](#Q6)) 创建一个大小为 m×n 的矩形结构元素。
<a id="function8"></a>
SE = strel("square", [w](#Q7)) 创建一个宽度为 `w` 个像素的正方形结构元素。
<a id="function9"></a>
SE = strel("cube", [w](#Q7)) 创建一个宽度为 `w` 个像素的三维立方体结构元素。
<a id="function10"></a>
SE = strel("cuboid", [[m n p]](#Q8)) 创建一个大小为 `m×n×p` 像素的三维立方体结构元素。
<a id="function11"></a>
SE = strel("sphere", [r](#Q2)) 创建一个半径为 `r` 个像素的三维球面结构元素。

## 参数说明
### 输入参数
**<a id="Q1"></a> nhood — 邻域**  
数值数组
邻域，指定为任意维度的数值数组。`nhood` 的所有非零像素都属于形态学运算的邻域。`nhood` 的中心（或原点）是其中心元素，由 `floor((size(nhood) + 1) / 2)` 给出。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `int8` | `int16`

**<a id="Q2"></a> r — 结构元素的半径**  
正整数

结构元素的半径，指定为正整数。
- 对于盘形，`r` 是从原点到盘边的距离。
- 对于菱形，`r` 是从结构元素原点到菱形各点的距离。
- 对于八边形，`r` 是从结构元素原点到八边形边的距离，沿水平和垂直轴测量。`r` 必须为 3 的倍数。
- 对于球面形状，`r` 是从原点到球面的距离。

**数据类型：** `double`

**<a id="Q3"></a> n — 用于逼近形状的循环线条结构元素的数量**  
4 (默认) | 0 | 6 | 8

用于逼近形状的循环线条结构元素的数量，指定为 0、4、6 或 8。当结构元素使用逼近 (n > 0) 时，使用盘形逼近的形态学运算的运行速度快得多。

|n 的值|行为|
|:-|:-|
|n > 0|strel 使用包含 n 个循环线条形结构元素的序列来逼近形状。有时 strel 必须在逼近中使用两个额外的线条结构元素，在这种情况下，分解结构元素的实际数量是 n+2。|
|n = 0|strel 不使用任何逼近。结构元素成员包括中心距原点不大于 r 的所有像素。|

**数据类型：** `double`

**<a id="Q4"></a> len — 线性结构元素的长度**  
正数

线性结构元素的长度，指定为正数。`len` 大约是线条两端的结构元素成员中心之间的距离。

**数据类型：** `double`

**<a id="Q5"></a> deg — 线性结构元素的角度**  
数值标量

线性结构元素的角度，以度为单位，指定为数值标量。该角度是从水平轴按逆时针方向测量的。

**数据类型：** `double`

**<a id="Q6"></a> [m n] — 矩形结构元素的大小**  
由正整数组成的二元素向量

矩形结构元素的大小，指定为由正整数组成的二元素向量。结构元素有 `m` 行和 `n `列。

**数据类型：** `double`

**<a id="Q7"></a> w — 正方形或立方体结构元素的宽度**  
正整数

正方形或立方体结构元素的宽度，指定为正整数。

**数据类型：** `double`

**<a id="Q8"></a> [m n p] — 立方体结构元素的大小**  
由正整数组成的二元素向量

立方体结构元素的大小，指定为由正整数组成的三元素向量。结构元素具有 `m` 行、`n` 列和 `p` 个平面。

**数据类型：** `double`

## 属性
**Neighborhood — 结构元素邻域**  
逻辑数组

结构元素邻域，指定为逻辑数组。

**数据类型：** `logical` 

**Dimensionality — 结构元素的维数**  
非负标量

结构元素的维数，指定为非负标量。

**数据类型：** `logical` 

## 对象函数

| 函数                                             | 简述                   |
| :----------------------------------------------- | :--------------------- |
| <a href="../imdilate/imdilate.html">imdilate</a> | 膨胀图像               |
| <a href="../imerode/imerode.html">imerode</a>    | 腐蚀图像               |
| <a href="../imclose/imclose.html">imclose</a>    | 对图像执行形态学闭运算 |
| <a href="../imopen/imopen.html">imopen</a>       | 对图像执行形态学开运算 |
| <a href="../imbothat/imbothat.html">imbothat</a> | 底帽滤波               |
| <a href="../imtophat/imtophat.html">imtophat</a> | 顶帽滤波               |

## 提示
- 不使用逼近 (n = 0) 的结构元素不适合计算粒度。

## 算法
对于所有几何形状，都使用统称为结构元素分解的一系列方法构造结构元素。其原理是：通过一些大的结构元素实现的膨胀可以通过用较小的结构元素序列实现的膨胀来更快地计算。例如，要实现 11×11 正方形结构元素的膨胀，可以首先用 1×11 结构元素进行膨胀，然后用 11×1 结构元素进行膨胀。这在理论上可使性能提高 5.5 倍，尽管实际上性能的提升要稍低于此值。用于 "disk" 形状的结构元素分解是一种逼近 - 所有其他分解都是精确的。

## 参考文献
van den Boomgard R, R. van Balen。 Methods for Fast Morphological Image Transforms Using Bitmapped Images. Computer Vision, Graphics, and Image Processing: Graphical Models and Image Processing, 1992, 54(3): 252–254.  
Adams R. Radial Decomposition of Discs and Spheres, Computer Vision, Graphics, and Image Processing: Graphical Models and Image Processing, 1993, 55(5): 325–332.  
Jones R, P. Soille. Periodic lines: Definition, cascades, and application to granulometrie. Pattern Recognition Letters, 1996, 17:1057–1063.

## 版本历史
在北太天元图像处理工具箱 V1.0 推出








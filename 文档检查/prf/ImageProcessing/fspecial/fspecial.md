## fspecial
创建预定义的2维滤波器

## 简介
[ `h = fspecial(type)`](#function1)\
[ `h = fspecial('average', hsize)`](#function2)\
[ `h = fspecial('gaussian', hsize, sigma)`](#function3)\
[ `h = fspecial('laplacian', alpha)`](#function4)\
[ `h = fspecial('motion', len, theta)`](#function5)\
[ `h = fspecial('prewitt')`](#function6)\
[ `h = fspecial('sobel')`](#function7)

## 用法
<a id="function1"></a>
[h](#Q7) = fspecial([type](#Q1)) 创建具有指定 `type` 的二维滤波器 `h` 。一些滤波器类型具有可选的附加参数，如以下语法所示。`fspecial` 以相关性核形式返回 `h` ，该形式适用于 `imfilter` 。  
<a id="function2"></a>
[h](#Q7) = fspecial('average', [hsize](#Q2)) 返回大小为 `hsize` 的均值滤波器 `h`。  
<a id="function3"></a>
[h](#Q7) = fspecial('gaussian', [hsize](#Q2), [sigma](#Q3)) 返回大小为 `hsize` 的旋转对称高斯低通滤波器，标准差为 `sigma`。不推荐。请改用 `imgaussfilt` 或 `imgaussfilt3`。  
<a id="function4"></a>
[h](#Q7)  = fspecial('laplacian', [alpha](#Q4)) 返回逼近二维拉普拉斯算子形状的 3×3 滤波器，`alpha` 控制拉普拉斯算子的形状。  
<a id="function5"></a>
[h](#Q7)  = fspecial('motion', [len](#Q5), [theta](#Q6)) 返回与图像卷积后逼近相机线性运动的滤波器。`len` 指定运动的长度，`theta` 以逆时针方向度数指定运动的角度。滤波器成为一个水平和垂直运动的向量。默认 `len` 是 9，默认 `theta` 是 0，对应于 9 个像素的水平运动。  
<a id="function6"></a>
[h](#Q7)  = fspecial('prewitt') 返回一个 3×3 滤波器，该滤波器通过逼近垂直梯度来强调水平边缘。要强调垂直边缘，请转置滤波器 `h`。
<a id="function7"></a>
[h](#Q7)  = fspecial('sobel') 返回一个 3×3 滤波器，该滤波器通过逼近垂直梯度来使用平滑效应强调水平边缘。要强调垂直边缘，请转置滤波器 `h`。

## 参数说明
### 输入参数
**<a id="Q1"></a> type — 滤波器的类型**  
"average" | "disk" | "gaussian" | "laplacian" | "log" | "motion" | "prewitt" | "sobel"

滤波器的类型，指定为下列值之一：

|值|描述|
|:-|:-|
|"average"|平均值滤波器|
|"disk"|圆形平均值滤波器 (pillbox)|
|"gaussian"|高斯低通滤波器。不推荐。请改用 `imgaussfilt` 或 `imgaussfilt3`。|
|"laplacian"|逼近二维拉普拉斯算子|
|"log"|高斯拉普拉斯滤波器|
|"motion"|逼近相机的线性运动|
|"prewitt"|普瑞维特水平边缘强调滤波器|
|"sobel"|索贝尔水平边缘强调滤波器|

**数据类型：**  `char` | `string`

**<a id="Q2"></a> hsize — 滤波器的大小**  
正整数 | 由正整数组成的二元素向量

滤波器的大小，指定为正整数或由正整数组成的二元素向量。使用向量指定 h 中的行数和列数。如果您指定标量，则 h 是方阵。
当与 `"average"` 滤波器类型结合使用时，默认滤波器大小为 [3 3]。当与高斯拉普拉斯 (`"log"`) 滤波器类型结合使用时，默认滤波器大小为 [5 5]。

**数据类型：**  `double`

**<a id="Q3"></a> sigma — 标准差**  
0.5 (默认) | 正数

标准差，指定为正数。

**数据类型：**  `double`

**<a id="Q4"></a> alpha — 拉普拉斯算子的形状**  
0.2 (默认) | [0, 1] 范围内的数值

拉普拉斯算子的形状，指定为范围 [0, 1] 内的数值。指定 `alpha` 为 0 以获得 4 邻点拉普拉斯滤波器。

**数据类型：**  `double`

**<a id="Q5"></a> len — 相机的线性移动**  
9 (默认) | 数值标量

相机的线性移动，指定为数值标量，以像素为单位测量。

**数据类型：**  `double`

**<a id="Q6"></a> theta — 相机移动的角度**  
0 (默认) | 数值标量

相机移动的角度，以度为单位，指定为数值标量。角度是从水平方向逆时针方向测量的。

**数据类型：**  `double`

### 输出参数
**<a id="Q7"></a> h — 相关性核**  
矩阵

相关性核，以矩阵形式返回。

**数据类型：**  `double`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../imfilter/imfilter.html">imfilter</a>
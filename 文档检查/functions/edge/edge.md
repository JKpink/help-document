## edge
边缘提取

## 简介
[`BW = edge(I)`](#function1)  
[`BW = edge(I, method)`](#function2)  
[`BW = edge(I, method, threshold)`](#function3)  
[`BW = edge(I, method, threshold, direction)`](#function4)  
[`BW = edge(___, "thinning")`](#function5)  
[`BW = edge(I, method, threshold, sigma)`](#function6)  
[`BW = edge(I, method, threshold, h)`](#function7)

## 用法
<a id="function1"></a>
[BW](#Q1) = edge([I](#Q2)) 返回二值图像 `BW`，其中的值 1 对应于二维灰度图像或二值图像 `I` 中函数找到边缘的位置，值 0 对应于其他位置。  
<a id="function2"></a>
[BW](#Q1) = edge([I](#Q2), [method](#Q3)) 使用 method 指定的边缘检测算法检测图像 `I` 中的边缘。  
<a id="function3"></a>
[BW](#Q1) = edge([I](#Q2), [method](#Q3), [threshold](#Q4)) 返回强度高于 `threshold` 的所有边缘。  
<a id="function4"></a>
[BW](#Q1) = edge([I](#Q2), [method](#Q3), [threshold](#Q4), [direction](#Q5)) 指定要检测的边缘的方向， "Sobel"、"Prewitt" 方法可以检测垂直方向和 / 或水平方向的边缘，"Roberts" 方法可以检测与水平方向成 45 度角和 / 或 135 度角的边缘。  
<a id="function5"></a>
[BW](#Q1) = edge(___, "thinning") 开启边缘细化阶段。  
<a id="function6"></a>
[BW](#Q1) = edge([I](#Q2), [method](#Q3), [threshold](#Q4), [sigma](#Q6)) 指定 `sigma`，即滤波器的标准差。  
<a id="function7"></a> [BW](#Q1) = edge([I](#Q2),[method](#Q3),[threshold](#Q4),[h](#Q7)) 使用 "zerocross" 方法和指定的滤波器 h 检测边缘。仅当 method 是 "zerocross" 时，此语法才有效。

## 参数说明
### 输入参数
**<a id="Q2"></a> I — 输入图像**  
二维灰度图像 | 二维二值图像

输入图像，指定为二维灰度图像或二维二值图像。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` |  `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q3"></a> method — 边缘检测方法**  
"Sobel" (默认) | "Prewitt" | "Roberts" | "log" | "zerocross" | "Canny" 

边缘检测方法，指定为下列方法之一。

| **方法** | **描述** |
|:-:|:-:|
| "Sobel"| 使用导数的索贝尔逼近，通过寻找图像 `I` 的梯度最大的那些点来查找边缘。 |
| "Prewitt" | 使用导数的普瑞维特逼近，通过寻找 `I` 的梯度最大的那些点来查找边缘。 |
| "Roberts" | 使用导数的罗伯茨逼近，通过寻找I的梯度最大的那些点来查找边缘。 |
| "log" | 使用高斯拉普拉斯 (LoG) 滤波器对I进行滤波后，通过寻找过零点来查找边缘。 |
|"Canny"	| 通过寻找 `I` 的梯度的局部最大值来查找边缘。`edge` 函数使用高斯滤波器的导数计算梯度。此方法使用双阈值来检测强边缘和弱边缘，如果弱边缘与强边缘连通，则将弱边缘包含到输出中。通过使用双阈值，坎尼方法相对其他方法不易受噪声干扰，更可能检测到真正的弱边缘。|
| | |
|"zerocross" | 使用指定的滤波器 `h` 对 `I` 进行滤波后，通过寻找过零点来查找边缘。|

**<a id="Q4"></a> threshold — 敏感度阈值**  
非负标量 | 二元素向量 | [ ]

敏感度阈值，指定为非负标量（对于一般 method）或二元素向量（对于 "Canny" 方法）。edge 忽略所有强度不大于 threshold 的边缘。
- 如果不指定 threshold 或指定空数组 ([])，则 edge 会自动根据输入数据通过启发式方法选择一个或多个值。更改阈值的最佳方法是运行一次函数，将计算出的阈值作为 `threshOut` 参量输出。然后，从计算出的阈值开始，分别增大或减小阈值以检测更少或更多边缘像素。
- 对于 "Sobel"、"Prewitt" 和 "Roberts" 方法，该函数使用阈值来确定要被视为边缘的梯度幅值。使用阈值 0 会选择图像中的所有边缘，即使其强度非常低也是如此。
- 对于 "log" 方法，该函数使用阈值来确定要被视为边缘的过零的幅值。换言之，当采用高阈值时，较大的过零跳跃被视为边缘，而较小的过零跳跃不是。如果指定阈值为 0，则输出图像具有闭合轮廓，因为它包括输入图像中的每个过零点。
- "Canny" 方法使用两个梯度阈值：具有低边缘敏感度的上阈值和具有高边缘敏感度的下阈值。边缘检测在低敏感度结果的基础上进行扩展，以包含高敏感度结果中连通的边缘像素。这有助于填补检测到的边缘中的间断。函数忽略边缘强度低于下阈值的所有边缘，保留边缘强度高于上阈值的所有边缘。您可以将 threshold 指定为 [low high] 形式的二元素向量，其中 low 和 high 值在范围 [0, 1] 内。您还可以将 threshold 指定为数值标量，edge 将其作为上阈值赋值。在这种情况下，edge 将下阈值计算为 threshold*0.4。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q5"></a> direction — 要检测的边缘的方向**  

要检测的边缘的方向，指定为"horizontal"、"vertical"或"both"。仅当method是 "Sobel"、"Prewitt"或"Roberts"时，direction参量才有效。

**数据类型：** `char` | `string`

**<a id="Q7"></a> h —— 滤波器**
数值矩阵
滤波器，指定为数值矩阵。仅 "zerocross" 方法支持 h 参量。

**数据类型**:`double`

**<a id="Q6"></a> sigma — 滤波器的标准差**  
数值标量

滤波器的标准差，指定为数值标量。仅 "Canny" 和 "log" 方法支持 sigma 参量。

| **方法** | **描述** |
|:-:|:-:|
| "Canny" | 标量值，指定高斯滤波器标准差。默认值为 sqrt(2)。edge 根据 sigma 自动选择滤波器的大小。|
| "log"（高斯拉普拉斯）| 标量值，指定高斯拉普拉斯滤波器标准差。默认值为 2。滤波器的大小为 n×n，其中 n=ceil(sigma*3)*2+1。|

**数据类型：** `double`

### 输出参量
**<a id="Q1"></a> BW — 输出二值图像**  
逻辑数组

输出二值图像，以与 [I](#Q2) 大小相同的逻辑数组形式返回，值 1 对应于 `I` 中函数找到边缘的位置，值 0 对应于其他位置。

**<a id="Q8"></a> threshOut —— 计算的阈值**
数值标量 | 二元素向量 

在运算中使用的计算的阈值，以二元素向量形式（对于 "Canny" 方法）或数值标量形式（对于所有其他边缘检测方法）返回。

## 参考
[1] Canny J. A computational approach to edge detection. IEEE Transactions on Pattern Analysis and Machine Intelligence, 1986, 8(6): 679-698.

[2] Lim J S. Two-dimensional signal and image processing. Englewood Cliffs, NJ: Prentice Hall, 1990: 478-488.

[3] Parker J R. Algorithms for image processing and computer vision. New York: John Wiley & Sons, Inc., 1997: 23-29.

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
 <a href="../edge3/edge3.html">edge3</a> | <a 
href="../fspecial/fspecial.html">fspecial</a> | <a 
href="../imgradient/imgradient.html">imgradient</a> | <a 
href="../imgradientxy/imgradientxy.html">imgradientxy</a> 


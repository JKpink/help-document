## imfindcircles
使用 Hough 变换查找圆

## 简介
[`centers = imfindcircles(A, radius)`](#function1)  
[`[centers, radii] = imfindcircles(A, radiusRange)`](#function2)  
[`[centers, radii] = imfindcircles(A, radiusRange, Name,Value)` ](#function3)

## 用法
<a id="function1"></a>
[centers](#Q1) = imfindcircles([A](#Q3), [radius](#Q4)) 查找图像 `A` 中半径约等于 radius 的圆。输出 centers 是一个两列矩阵，其中包含图像中各圆中心的 (x,y) 坐标。  
<a id="function2"></a>
[[centers](#Q1), [radii](#Q2)] = imfindcircles([A](#Q3), [radiusRange](#Q5)) 查找半径在 radiusRange 指定范围内的圆。附加输出参量 radii 包含与 centers 中每个圆心对应的估计半径。  
<a id="function3"></a>
[[centers](#Q1), [radii](#Q2)] = imfindcircles([A](#Q3),[radiusRange](#Q5), [Name, Value](#Q6))支持任何上述语法，且可使用一个或多个名称-值参量指定其他选项。

## 参数说明
### 输入参数
**<a id="Q3"></a> A — 输入图像**  
灰度图像 | 彩色图像 | 二值图像

输入图像是在其中检测圆形目标的图像，指定为灰度图像、彩色 (RGB) 图像或二值图像。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` | `logical`

**<a id="Q4"></a> radius — 圆半径**  
正数

圆半径活要检测的圆形目标的近似半径，指定为正数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q5"></a> radiusRange — 半径范围**  
由正整数组成的二元素向量

要检测的圆形目标的半径范围，指定为 [rmin rmax] 形式的由正整数组成的二元素向量，其中 rmin 小于 rmax。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`


**<a id="Q6"></a> 名称-值参数**

将可选的参量对组指定为 Name1,Value1,...,NameN,ValueN，其中 Name 是参量名称，Value 是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。

**示例：**  
centers = imfindcircles(A, radius, "ObjectPolarity", "bright") 在深色背景上指定亮色圆形目标。

**ObjectPolarity — 目标极性**  
"bright" (默认) | "dark"

目标极性，指定为下表中的值之一。

| | |
|:-|:-|
| "bright" | 圆形目标比背景亮。 |
| "dark" | 圆形目标比背景暗。 |
| | |

**Sensitivity — 敏感度因子**  
0.85 (默认) | [0, 1] 范围内的数值

圆形霍夫变换累加器数组的敏感度因子，指定为范围 [0, 1] 内的数值。随着敏感度因子的增大，`imfindcircles` 会检测到更多圆形目标，包括弱圆形和部分模糊圆形。更高的敏感度值也会增加错误检测的风险。

**EdgeThreshold — 边缘梯度阈值**  
[0, 1] 范围内的数值

用于确定图像中边缘像素的边缘梯度阈值，指定为范围 [0, 1] 内的数字。指定 0 可将阈值设置为零梯度幅值。指定 1 可将阈值设置为最大梯度幅值。阈值设置得越低，`imfindcircles` 检测到的圆形目标（具有弱边缘和强边缘）越多，随着阈值的增大，它会检测到较少的具有弱边缘的圆形。默认情况下，`imfindcircles` 使用函数 <a href="../graythresh/graythresh.html">graythresh</a> 自动选择边缘梯度阈值。

### 输出参数
**<a id="Q1"></a> centers — 圆心坐标**  
P×2 矩阵

圆心坐标，返回为 P×2 矩阵，第一列中包含圆心的 x 坐标，第二列中包含 y 坐标。行数 P 是检测到的圆形的个数。centers 根据圆形的强度（从最强到最弱）排序。

**数据类型：** `double`

**<a id="Q2"></a> radii — 估计半径**  

各圆心对应的估计半径，以列向量形式返回，`radii(j)` 处的半径值对应于以 `centers(j,:)` 为中心的圆形。

**数据类型：** `double`

## 参考
[1] Atherton T J, Kerbyson D J. Size invariant circle detection. Image and Vision Computing, 1999, 17(11): 795-803.

[2] Yuen H K, Princen J, Illingworth J, et al. Comparative study of Hough transform methods for circle finding. Image and Vision Computing, 1990, 8(1): 71-77.

[3] Davies E R. Machine vision: theory, algorithms, practicalities. 3rd ed. Chapter 10. San Francisco: Morgan Kaufmann Publishers, 2005.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../circles2mask/circles2mask.html">circles2mask</a> | <a 
href="../hough/hough.html">hough</a> | <a 
href="../houghpeaks/houghpeaks.html">houghpeaks</a> | <a 
href="../houghlines/houghlines.html">houghlines</a> | <a
href="../viscircles/viscircles.html">viscircles</a> 

### 主题
 <a href="../检测和测量图像中的圆形目标/检测和测量图像中的圆形目标.html">检测和测量图像中的圆形目标</a> 

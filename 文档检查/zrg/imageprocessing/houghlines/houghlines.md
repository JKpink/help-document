## houghlines
基于 Hough 变换检测线段

## 简介
[`lines = houghlines(BW, theta, rho, peaks)`](#function1)  
[`lines = houghlines(BW, theta, rho, peaks, Name, Value)`](#function2)

## 用法
<a id="function1"></a>
[lines](#Q1) = houghlines([BW](#Q2), [theta](#Q3), [rho](#Q4), [peaks](#Q5)) 提取图像 `BW` 中与霍夫变换中的特定 `bin` 相关联的线段。`theta` 和 `rho` 是函数 `hough` 返回的向量。`peaks` 是由 `houghpeaks` 函数返回的矩阵，其中包含霍夫变换 `bin` 的行和列坐标，用于搜索线段。返回值 `lines` 包含有关提取的线段的信息。  
<a id="function2"></a>
[lines](#Q1) = houghlines([BW](#Q2), [theta](#Q3), [rho](#Q4), [peaks](#Q5), [Name, Value](#Q6)) 使用名称-值对组参量来控制线条提取的各个方面。

## 参数说明
### 输入参数
**<a id="Q2"></a> BW — 二值图像**  
二维逻辑矩阵 | 二维数值矩阵

二值图像，指定为二维逻辑矩阵或二维数值矩阵。对于数值输入，任何非零像素都被视为 1 (true)。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` |  `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q3"></a> theta — 线条旋转角度**  
数值矩阵

线条旋转角度，以度为单位，指定为数值矩阵。角度是在 x 轴和 rho 向量之间测量的角度。

**数据类型：** `double`

**<a id="Q4"></a> rho — 从原点到线条的距离**  
数值矩阵

距坐标原点的距离，指定为数值矩阵，坐标原点是图像的左上角 (0,0)。

**数据类型：** `double`

**<a id="Q5"></a> peaks — 霍夫变换 bin 的行和列坐标**  
数值矩阵

霍夫变换 `bin` 的行和列坐标，指定为数值矩阵。

**数据类型：** `double`

**<a id="Q6"></a> 名称-值参数**  

将可选的参量对组指定为 Name1,Value1,...,NameN,ValueN，其中 Name 是参量名称，Value 是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。

**FillGap — 与同一霍夫变换 bi 相关联的两个线段之间的距离**  
20 (默认) | 正数

与同一个霍夫变换 bin 相关联的两个线段之间的距离，指定为正数。当线段之间的距离小于指定值时，`houghlines` 函数会将这些线段合并为一条线段。

**数据类型：** `double`

**MinLength — 最小线条长度**  
40 (默认) | 正数

最小线条长度，指定为正数。`houghlines` 丢弃短于指定值的线条。

**数据类型：** `double`

### 输出参量
**<a id="Q1"></a> lines — 检测到的线条**  
结构体数组

检测到的线条，以结构体数组形式返回，其长度等于找到的合并线段数。结构体数组的每个元素都有以下字段：

| **字段** | **描述** |
|:-|:-|
| point1 | 指定线段端点坐标的二元素向量 [X Y] |
| point2 | 指定线段端点坐标的二元素向量 [X Y] |
| theta | 霍夫变换 bin 的角度（以度为单位）|
| rho | 霍夫变换 bin 的 rho 轴位置 |
| | |

## 版本历史
在北太天元图像处理工具箱 V1.1 推出

## 相关主题
<a href="../hough/hough.html">hough</a> | <a 
href="../houghpeaks/houghpeaks.html">houghpeaks</a> 



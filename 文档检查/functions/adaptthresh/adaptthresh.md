## adaptthresh
基于局部一阶统计量计算自适应图像阈值

## 简介
[T = adaptthresh(I)](#function1)  
[T = adaptthresh(I, sensitivity)](#function2)  
[T = adaptthresh(___, Name, Value)](#function3)

## 用法
<a id="function1"></a>
[T](#Q1) = adaptthresh([I](#Q2)) 计算二维灰度图像 `I` 的局部自适应阈值。`adaptthresh` 函数基于每个像素邻域的局部均值强度（一阶统计量）选择阈值。阈值 T 可与 `imbinarize` 函数结合使用以将灰度图像转换为二值图像。

<a id="function2"></a>
[T](#Q1) = adaptthresh([I](#Q2), [sensitivity](#Q3)) 使用灵敏度因子计算局部自适应阈值，通过阈值化处理将更多像素归为前景。

<a id="function3"></a>
T = adaptthresh(___, [Name, Value](#Q4)) 使用名称-值对组计算局部自适应阈值，以控制阈值的各个方面。

## 参数说明
### 输入参数
**<a id="Q2"></a> I — 灰度图像**  
二维数值矩阵 | 三维数值矩阵

灰度图像或图像体，指定为二维数值矩阵或三维数值数组。
`adaptthresh` 需要数据类型为 double 和 single 的图像的值在 [0, 1] 的范围内。如果 `I` 的值超出范围 [0, 1]，则可以使用 `rescale` 函数将值重新缩放到需要的范围。
如果图像包含 Inf 或 NaN 值，则说明 `adaptthresh` 的行为未定义。 Inf 或 NaN 值的传播可能不会局限于 Inf 或 NaN 像素周围的邻域。

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` 

**<a id="Q3"></a> sensitivity — 确定哪些像素被阈值化为前景像素**
默认值为0.5 | `[0,1]`范围内的数值

确定哪些像素被阈值化为前景像素，指定为 [0, 1] 范围内的数字,一般默认为 0.5。高敏感度值导致更多的像素通过阈值化处理归为前景，但这会存在将一些背景像素也归为前景的风险。

**<a id="Q4"></a> 名称-值参数**  
将可选的参量对组指定为 Name1, Value1,..., NameN, ValueN，其中 Name 是参量名称，Value 是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。

**示例：** `T = adaptthresh(I, 0.4, "ForegroundPolarity", "dark")`; 指定前景比背景暗。

**NeighborhoodSize — 用于计算每个像素周围局部统计量的邻域大小**
2*floor(size(I)/16)+1(默认) | 正数 | 由正数组成的二元素向量

用于计算每个像素周围局部统计量的邻域大小，指定为正奇数或由正奇数组成的二元素向量，一般默认为 2*floor(size(I)/16)+1。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**ForegroundPolarity — 确定哪些像素被视为前景像素**
"bright"(默认) | "dark"

确定哪些像素被视为前景像素，使用以下项之一进行指定：

| **值** | **意义** |
|:-|:-|
| "bright" | 前景比背景亮 |
| "dark" | 前景比背景暗 |

**数据类型：** `char` | `string`

**Statistic — 用于计算局部阈值的统计量**
"mean"(默认) | "median" 

用于计算每个像素的局部阈值的统计量，指定为下列值之一：

| **值** | **意义** |
|:-|:-|
| "mean" | 邻域中的局部均值强度。这种方法也称为布拉德利方法[[1]](#ref1) |
| "median" | 邻域中的局部中位数，此统计量的计算可能会很慢，请考虑使用较小的邻域大小来更快地获得结果 |


**数据类型：** `char` | `string`

### 输出参数
**<a id="Q1"></a> T — 归一化的强度值** 
 
归一化的强度值，以与输入图像或图像体 `I` 大小相同的数值矩阵或数值数组形式返回。值被缩放到 [0, 1] 的范围内。

**数据类型：** `double`

## 参考
<a id="ref1"></a>
[1] D. Bradley and G. Roth,  
"Adapting thresholding using the integral image,"  
*Journal of Graphics Tools*, vol. 12, no. 2, pp. 13–21, 2007.

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imbinarize/imbinarize.html">imbinarize</a> | <a 
href="../otsuthresh/otsuthresh.html">otsuthresh</a> | <a 
href="../graythresh/graythresh.html">graythresh</a> 



## grabcut
使用图割算法将图像分割为前景和背景

## 简介
[`BW = grabcut(A, L, ROI)`](#function1)  
[`BW = grabcut(A, L, ROI, foremask, backmask)`](#function2)  
[`BW = grabcut(A, L, ROI, foreind, backind)`](#function3)  
[`BW = grabcut(___,Name,Value)`](#function4)

## 用法
<a id="function1"></a>
[BW](#P1)  = grabcut([A](#Q1), [L](#Q2), [ROI](#Q3)) 将图像 `A` 分割为前景和背景区域。标签矩阵 `L` 指定图像的子区域。`ROI` 是用于指定初始感兴趣区域的逻辑掩膜。

<a id="function2"></a>
[BW](#P1)  = grabcut([A](#Q1), [L](#Q2), [ROI](#Q3), [foremask](Q4), [backmask](#Q5)) 对图像 `A` 进行分割，其中 `foremask` 和 `backmask` 分别为指定图像中前景和背景像素的掩膜。

<a id="function4"></a>
[BW](#P4) = grabcut(___, Name, Value) 使用名称-值参数控制分割的各个方面。

## 参数说明
### 输入参数

**<a id="Q1"></a> A — 待分割图像**  
2-D 灰度图像 | 2-D 真彩色图像 | 3-D 灰度体数据

输入图像或体数据，指定为 2-D 灰度图像、2-D 真彩色图像或 3-D 灰度体数据。仅灰度图像可为 `int16` 数据类型。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16`

**<a id="Q2"></a> L — 标签矩阵**  
数值数组

标签矩阵，指定为数值数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q3"></a> ROI — 感兴趣区域**  
逻辑数组

感兴趣区域，指定为逻辑数组。所有定义感兴趣区域的像素值为 `true`。

**数据类型：** `logical`

**<a id="Q4"></a> foremask — 前景掩膜**  
逻辑数组

前景掩膜，指定为逻辑数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q5"></a> backmask — 背景掩膜**  
逻辑数组

背景掩膜，指定为逻辑数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 名称-值参数
使用名称-值参数指定可选的参数对。参数名必须为字符向量，参数值为对应值。名称-值参数必须出现在其他参数之后，但各对的顺序不限。

**<a id="Q8"></a> Connectivity — 连通组件的连通性**  
`4` | `8` | `6` | `18` | `26`

连通组件的连通性，指定为以下值之一。对于 2-D 图像，默认连通性为 `8`；

| 值   | 含义                                                         |
| ---- | ------------------------------------------------------------ |
| `4`  | 像素若边缘相接则视为连通。两个相邻像素若水平或垂直方向相连，则属于同一对象。 |
| `8`  | 像素若边缘或角点相接则视为连通。两个相邻像素若水平、垂直或对角线方向相连，则属于同一对象。 |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q9"></a> MaximumIterations — 最大迭代次数**  
`5` （默认） | 正标量

算法执行的最大迭代次数。算法可能在达到最大迭代次数之前收敛到解。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出参数

**<a id="P1"></a> BW — 分割图像**  
逻辑数组

分割后的图像，以与标签矩阵 `L` 相同大小的二值图像形式返回。

## 提示
- 对于 `double` 和 `single` 类型图像，`grabcut` 假定图像值范围为 [0, 1]。对于 `uint16`、`int16` 和 `uint8` 类型图像，假定范围为该数据类型对应的完整范围。
- 对于灰度图像，`L`、`foremask` 和 `backmask` 的大小必须与图像 `A` 的大小一致。对于彩色图像和多通道图像，`L`、`foremask` 和 `backmask` 必须是 2-D 数组，其前两维与图像 `A` 的前两维相同。

## 算法
- 算法将 ROI 掩膜外部的所有子区域视为背景。为获得最优分割，需确保待分割对象完全包含在 ROI 内，并由少量背景像素包围。
- 标签矩阵中的同一子区域不可同时标记为前景和背景。若某子区域同时包含前景和背景像素，算法将该区域视为未标记。
- 算法假定感兴趣区域外部的所有子区域属于背景。将这些子区域标记为前景或背景对最终分割结果无影响。

## 参考文献
[1] Rother C, Kolmogorov V, Blake A. GrabCut - Interactive Foreground Extraction using Iterated Graph Cuts. ACM Transactions on Graphics (SIGGRAPH). 2004;23(3):309–314.

## 版本历史
在北太天元图像处理工具箱 V3.0 推出  

## 相关主题
<a href="../imagesegmenter/imagesegmenter.html">Image Segmenter</a> | <a href="../segmentAnythingModel/segmentAnythingModel.html">segmentAnythingModel</a> | <a href="../superpixels/superpixels.html">superpixels</a> | <a href="../lazysnapping/lazysnapping.html">lazysnapping</a> | <a href="../watershed/watershed.html">watershed</a>
## lazysnapping
使用基于图的分割将图像分割为前景和背景

## 简介
[`BW = lazysnapping(A, L, foremask, backmask)`](#function1)  
[`BW = lazysnapping(A, L, foreind, backind)`](#function2)  

## 用法
<a id="function1"></a>
[BW](#P1) = lazysnapping([A](#Q1), [L](#Q2), [foremask](#Q3), [backmask](#Q4)) 使用 lazy snapping 将图像 `A` 分割为前景和背景区域。标签矩阵 `L` 指定图像的子区域。`foremask` 和 `backmask` 分别为指定图像中前景和背景像素的掩膜。

<a id="function2"></a>

[BW](#P1) = lazysnapping([A](#Q1), [L](#Q2), [foreind](#Q5), [backind](#Q6)) 将图像 `A` 分割为前景和背景区域。`foreind` 和 `backind` 分别指定标记为前景和背景的像素的线性索引。

## 参数说明
### 输入参数

**<a id="Q1"></a> A — 待分割图像**  
2-D 灰度图像 | 2-D 真彩色图像 | 2-D 多光谱图像 

待分割图像，指定为 2-D 灰度图像、真彩色图像、多光谱图像。对于 `double` 和 `single` 类型图像，`lazysnapping` 假定图像值范围为 [0, 1]。对于 `uint16`、`int16` 和 `uint8` 类型图像，假定范围为该数据类型对应的完整范围。若图像值不符合基于数据类型的预期范围，可缩放图像至预期范围或调整 `EdgeWeightScaleFactor` 以改善结果。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16`

**<a id="Q2"></a> L — 标签矩阵**  
数值数组

输入图像或体数据的标签矩阵，指定为数值数组。对于 2-D 灰度图像，`L` 的大小必须与输入图像 `A` 的大小一致。对于彩色图像和多通道图像，`L` 必须是 2-D 数组，其前两维与输入图像 `A` 的前两维匹配。

标签矩阵中的同一子区域不可同时标记为前景和背景。若某子区域同时包含前景和背景像素，`lazysnapping` 将该区域分割为背景。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q3"></a> foremask — 定义前景的掩膜图像**  
逻辑数组

定义前景的掩膜图像，指定为逻辑数组。对于 2-D 灰度图像，`foremask` 的大小必须与输入图像 `A` 的大小一致。对于彩色图像和多通道图像，`foremask` 必须是 2-D 数组，其前两维与输入图像 `A` 的前两维匹配。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q4"></a> backmask — 定义背景的掩膜图像**  
逻辑数组

定义背景的掩膜图像，指定为逻辑数组。对于 2-D 灰度图像，`backmask` 的大小必须与输入图像 `A` 的大小一致。对于彩色图像和多通道图像，`backmask` 必须是 2-D 数组，其前两维与输入图像 `A` 的前两维匹配。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q5"></a> foreind — 前景像素的线性索引**  
数值向量

标签矩阵中前景像素的线性索引，指定为数值向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q6"></a> backind — 背景像素的线性索引**  
数值向量

标签矩阵中背景像素的线性索引，指定为数值向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 名称-值参数
使用名称-值参数指定可选的参数对。参数名必须为字符向量，参数值为对应值。名称-值参数必须出现在其他参数之后，但各对的顺序不限。

**<a id="Q7"></a> Connectivity — 连通组件的连通性**  
`8`（2-D 图像默认）| `4` 

连通组件的连通性，指定为 `'Connectivity'` 和以下值之一：对于 2-D 图像，可取 `4` 或 `8`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q8"></a> EdgeWeightScaleFactor — 边权重的缩放因子**  
`500` （默认） | 正数

标签矩阵子区域间边权重的缩放因子，指定为 `'EdgeWeightScaleFactor'` 和一个正数。典型取值范围为 [10, 1000]。增大该值可提高 `lazysnapping` 将相邻子区域一同标记为前景或背景的可能性。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出参数
**<a id="P1"></a> BW — 分割图像**  
逻辑数组

分割后的图像，以与标签矩阵 `L` 相同大小的逻辑数组形式返回。

**数据类型：** `logical`

## 算法
Lazy snapping 是一种基于图割的交互式图像分割算法。该算法首先将图像过分割为若干超像素（由标签矩阵 `L` 表示），构建图模型，其中节点为超像素，边连接相邻超像素。边的权重基于超像素间的颜色相似性计算。用户通过指定前景和背景种子点（通过掩膜或线性索引提供）来标记部分节点。算法通过求解最小割问题，将剩余节点标记为前景或背景，从而实现分割。

## 参考文献
Li Y, Sun J, Tang CK, Shum HY. Lazy Snapping. In: Proceedings of the 31st International Conference on Computer Graphics and Interactive Techniques (SIGGRAPH); 2004.

## 版本历史
在北太天元图像处理工具箱 V3.0 推出  
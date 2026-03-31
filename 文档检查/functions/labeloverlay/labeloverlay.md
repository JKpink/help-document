## labeloverlay
在2维图像上叠加标记矩阵区域

## 简介

[`B = labeloverlay(A, BW)`](#function1)  
[`B = labeloverlay(A, L)`](#function2)  
[`B = labeloverlay(A, C)`](#function4)  
[`B = labeloverlay(___, Name, Value)`](#function3)

## 用法
<a id="function1"></a>
[B](#Q1) = labeloverlay([A](#Q2), [BW](#Q3)) 将输入图像与掩码 BW 为真处的颜色融合。`labeloverlay` 函数不会将背景像素（标记为假）与颜色融合。

<a id="function2"></a>
[B](#Q1) = labeloverlay([A](#Q2), [L](#Q4)) 将输入图像 `A` 与标签矩阵 `L` 中每个非零标签的不同颜色进行融合。`labeloverlay` 函数不会将背景像素与颜色融合。

<a id="function4"></a>
[B](#Q1) = labeloverlay([A](#Q2), [C](#Q6)) 将输入图像 `A` 与分类矩阵 `C` 中每个非零标签的不同颜色进行融合。

<a id="function3"></a>[B](#Q1) = labeloverlay(___, [Name, Value](#Q5)) 使用“名称，值”对来控制融合方面的图像 `B`，以控制计算的各个方面。

## 参数说明
### 输入参数
**<a id="Q2"></a> A — 输入图像**  
二维灰度 | 彩色图像

输入图像，指定为二维灰度或彩色图像。

**数据类型：** `uint8` | `single` | `int16` | `int8` | `uint16` | `double`

**<a id="Q3"></a> BW — 掩码**  
逻辑矩阵

掩码，指定为逻辑矩阵。

**数据类型：** `logical`

**<a id="Q4"></a> L — 标签**  
非负整数的矩阵

标签，指定为非负整数的矩阵。

**数据类型：** `uint8` | `single` | `int16` | `int8` | `uint16` | `double` | `int32` | `uint32`

**<a id="Q6"></a> C- 分类标签**
数值数组

分类标签，指定为一个数值数组。

**数据类型**:`double` | `int`

**<a id="Q5"></a> 名称-值参数**  
将可选的参量对组指定为 Name1,Value1,...,NameN,ValueN，其中 Name 是参量名称，Value 是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。

**示例：** labeloverlay (A, L, "Colormap", "hot") 会使用 “hot”（热图）色彩映射表中的颜色来显示标签。

**ColorAssignment — 颜色分配**  
"auto"（默认值）| "noshuffle" | "shuffle" | "contrasting-neighbors"

颜色分配参数，需指定为下表中的某个值。

| **颜色分配参数** | **说明** |
|:-|:-|
| "noshuffle" | 按数值顺序将色彩映射表颜色分配给标签矩阵区域。每个区域具有唯一颜色。 | |
| "shuffle" | 以伪随机方式分配色彩映射表颜色。每个区域具有唯一颜色。 | |
| "auto" | 据色彩映射表（Colormap）的格式分配颜色。默认情况下，当通过名称指定色彩映射表时，labeloverlay 函数会打乱颜色顺序；当将色彩映射表指定为数值矩阵时，则保留颜色顺序。 | |
| "contrasting-neighbors" | 分配色彩映射表的一个子集颜色，以最大化相邻区域之间的对比度。一种颜色可对应多个标签。 |  |

**Colormap — 颜色图**  
"jet"（默认值）| l×3 色彩映射表 | 字符串 | 字符向量

颜色图，指定为由 'Colormap' 和以下值之一组成的以逗号分隔的对：

- 一个 l×3 的颜色映射表。该颜色映射表中每一行的 RGB 三元组必须归一化至 [0, 1] 范围内。l 是标签矩阵 L、二值掩码 BW 中的标签数量。

- 一个与 `colormap` 函数的有效输入之一相对应的字符串或字符向量。默认情况下，`labeloverlay` 会对指定的颜色映射进行随机排序，以便相邻标签更加清晰可辨。

**示例：** `[0.2, 0.1, 0.5; 0.1, 0.5, 0.8]`  
**示例：** `"hot"`

**IncludedLabels — 要显示的标签** 
整数 | 整数向量 | 字符串 | 字符串向量

要在融合图像中显示的标签，指定为以下之一：
- 一个整数或整数向量，范围在 [0, max (L (\:))] 之间。默认情况下，labeloverlay 会显示所有非零标签。
- 一个字符串或字符串向量，对应分类矩阵 C 中的标签。默认情况下，labeloverlay 会显示所有已定义的分类标签。
- 
向量中未包含的任何标签都将被视为背景。例如，在向量 [1 3 4] 中，如果值 2 作为标签存在，它将被视为背景。

**示例：** [1 3 4]

**示例：** ["flower", "stem"]

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `string`

**Transparency — 透明度**  
0.5（默认值）| 取值范围在 [0, 1] 之间的数值

显示标签的透明度，指定为取值范围在 [0, 1] 之间的数值。
- 取值为 0 时，彩色标签完全不透明（即标签颜色完全覆盖底层内容）。
- 取值为 1 时，彩色标签完全透明（即标签颜色完全不可见，仅显示底层内容）。

**数据类型：** `single` | `double`

### 输出参量
**<a id="Q1"></a> B — 融合图像**  
数字矩阵

融合图像，以与 `A` 相同大小的数字矩阵返回。

**数据类型：** `uint8`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../imoverlay/imoverlay.html">imoverlay</a> | <a 
href="../label2rgb/label2rgb.html">label2rgb</a> | <a 
href="../imshowpair/imshowpair.html">imshowpair</a> 


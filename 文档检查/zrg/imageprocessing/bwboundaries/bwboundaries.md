## bwboundaries
跟踪二值图像中的对象边界

## 简介
[`B = bwboundaries(BW)`](#function1)  
[`B = bwboundaries(BW,conn)`](#function5)  
[`B = bwboundaries(___, options)`](#function2)  
[`B = bwboundaries(___, Name, Value)`](#function3)  
[`[B, L] = bwboundaries(___)`](#function4)

## 用法
<a id="function1"></a>
[B](#Q1)  = bwboundaries([BW](#Q3)) 跟踪二值图像 `BW` 中对象的外边界以及这些对象内部孔洞的边界。`bwboundaries` 还跟踪父对象完全包围的子对象的外边界和孔洞边界。该函数返回由边界像素位置组成的元胞数组 `B`。

<a id="function5"></a>
[B](#Q1) = bwboundaries([BW](#Q3),[conn](#Q6)) 指定跟踪目标边界时要使用的 conn 连通性。

<a id="function2"></a>
[B](#Q1) = bwboundaries(___, [options](#Q4)) 跟踪对象的外边界，并通过将 `options` 设置为 “holes” 或 “noholes” 来指定是否包括孔洞的边界。

<a id="function3"></a>
[B](#Q1) = bwboundaries(___, [Name,Value](#Q5)) 使用名称-值参量指定跟踪样式和返回的顶点坐标的顺序。

<a id="function4"></a>
[[B](#Q1), [L](#Q2)] = bwboundaries(___) 还返回标签矩阵 `L`，该矩阵用于标记对象和孔洞。

## 参数说明
### 输入参数
**<a id="Q3"></a> BW — 二值图像**  
二维逻辑矩阵 | 二维数值矩阵

二值图像，指定为二维逻辑或数值矩阵。对于数值输入，任何非零像素都被视为 1(true)。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q6"></a> conn —— 像素连通性**
默认为8 | 4

像素连通性，指定为下表中的值之一。
| 值 | 意义 | | 
| :----------- | :----------- | :----------- |
| 二维连通 |  
| 4 | 如果像素的边缘相互接触，则这些像素具有连通性。像素的邻域是水平或垂直方向上的相邻像素。 |  |
| 8 | 如果像素的边缘或角相互接触，则这些像素具有连通性。像素的邻域是水平、垂直或对角线方向上的相邻像素。 | 

**数据类型**:`double`

**<a id="Q4"></a> options — 确定是否同时搜索父对象边界和子对象边界**  
"holes" (默认) | "noholes"

确定是否同时搜索父对象边界和子对象边界，指定为以下任一项：

| **选项** | **意义** |
|:-|:-|
| "holes" | 同时搜索对象和孔洞边界，这是默认设置。 |
| "noholes" | 仅搜索对象（父对象和子对象）边界，这可以提供更好的性能。 |

**<a id="Q5"></a> 名称-值参数**  

将可选的参量对组指定为 Name1,Value1,...,NameN,ValueN，其中 Name 是参量名称，Value 是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。

**示例：** `B = bwboundaries(BW,"   TraceStyle","pixeledge")` 沿边界像素的外部边缘跟踪二值图像 `BW` 中对象的边界。

**TraceStyle — 跟踪样式**  
"pixelcenter" (默认) | "pixeledge"

沿边界的跟踪样式，指定为 "pixelcenter" 或 "pixeledge"。

| **跟踪样式** | **意义** |
|:-|:-|
| "pixelcenter" | 跟踪边界为连接边界像素中心的多边形。 |
| "pixeledge" | 跟踪边界为沿边界像素外边缘的多边形。 |

**CoordinateOrder — 返回的顶点坐标的顺序**  
"yx" (默认) | "xy"

返回的顶点坐标的顺序，指定为 "yx" 或 "xy"。

| **跟踪样式** | **意义** |
|:-|:-|
| "yx" | 以 (y, x) 坐标形式返回边界顶点，返回顺序与 (row, column) 坐标的顺序相同 |
| "xy" | 以 (x, y) 坐标形式返回边界顶点 |

### 输出参量
**<a id="Q1"></a> B — 边界顶点的坐标**  
p×1元胞数组

边界顶点的坐标，以 p×1 元胞数组形式返回，其中 p 是对象和孔洞的数量，`B` 中的前 [n](#Q6) 个元胞是对象边界，其余元胞是孔洞边界。  
元胞数组中的每个元胞都包含一个 q×2 矩阵，矩阵中的每一行都包含边界上一个顶点的坐标，q 是对应区域的边界顶点数量。

**<a id="Q2"></a> L — 标签矩阵**  
非负整数的二维矩阵

`L` 是连续区域的标签矩阵，以由非负整数组成的二维矩阵形式返回。第 k 个区域包含 `L` 中所有具有 k 值的元素，由 `L` 表示的对象和孔洞的数量等于 max(L(:\))，`L` 的零值元素构成背景。

**数据类型：** `int32`

## 参考
 [1] Gonzalez R C, Woods R E, Eddins S L.Digital image processing using MATLAB. New Jersey: Pearson Prentice Hall, 2004.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../bwlabel/bwlabel.html">bwlabel</a> | <a 
href="../bwlabeln/bwlabeln.html">bwlabeln</a> | <a 
href="../bwtraceboundary/bwtraceboundary.html">bwtraceboundary</a> | <a 
href="../bwperim/bwperim.html">bwperim</a> 


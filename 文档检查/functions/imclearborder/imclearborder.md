## imclearborder 
去除图像边界

## 简介
[`J = imclearborder(I) `](#function1)  
[`J = imclearborder(I, conn)`](#function2)  
[`J = imclearborder(___, Name, Value)`](#function3)

## 用法
<a id="function1"></a>
[J](#Q4) = imclearborder([I](#Q1)) 隐藏图像 `I` 中比其周围更亮并且连接到图像边界的结构。使用此函数清理图像边界或选择图像边界。对于灰度图像，`imclearborder` 除了隐藏边界结构外，还往往会降低整体强度级别。输出图像J是灰度或二值图像，具体取决于输入。  
<a id="function2"></a>
[J](#Q4) = imclearborder([I](#Q1), [conn](#Q2)) 指定连通性 `conn`。  
<a id="function3"></a>
[J](#Q4) = imclearborder([I](#Q1), [Name, Value](#Q3)) 通过一个或多个名称 — 值参量指定如何选择边界结构的选项，其中 `Borders` 用于指定要删除的图像边界。例如，imclearborder(I,"Borders",["left" "right"])仅删除触及图像左边界或右边界的结构。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
数值数组 | 逻辑数组

灰度或二值图像，指定为数值或逻辑数组。

**示例**: I = imread('pout.tif');

**数据类型**： `single` | `double` | `uint8` | `uint16` |  `logical`

**<a id="Q2"></a> conn — 像素连通性** 
4 | 8

像素连通性，指定为下表中的值之一。对于二维图像，默认连通性是 8。

<table><tr><td>值</td> <td colspan="2">意义</td></tr><tr><td colspan="3">二维连通</td></tr><tr><td>4</td><td>如果像素的边缘相互接触，则这些像素具有连通性。像素的邻域是水平或垂直方向上的相邻像素。</br></td></tr><tr><td>8</td><td>如果像素的边缘或角相互接触，则这些像素具有连通性。像素的邻域是水平、垂直或对角线方向上的相邻像素。</br> </br></td></tr></table>

**数据类型**：  `double` | `logical`

**<a id="Q3"></a> 名称 — 值参数**  
通过一个或多个名称 — 值参量指定如何选择边界结构的选项。

**Borders — 要删除结构的图像边界**  
字符串向量 | 由 0 和 1 组成的 N×2 矩阵

要删除结构的图像边界，指定为字符串向量或由 0 和 1 组成的 N×2 矩阵：
- 字符串向量 - 以 "left"、"right"、"top" 和 "bottom" 的任意组合指定要针对二维图像的哪些边界删除结构。当您将 `I`指定为二维图像时，`Borders` 的默认值为 ["left" "right" "top" "bottom"]。
- 由 0 和 1 组成的 N×2 矩阵 - 指定要针对 N 维图像的哪些边界删除结构，其中每行的第一个元素表示对应维度中的第一个边界，第二个元素表示该维度中的第二个边界。例如，如果 Borders(k, 1) 是 1，则删除与第 k 维中第一个边界接触的结构。如果 Borders(k, 2) 是 1，则删除与第 k 维中第二个边界接触的结构。例如，指定 Borders = [0 0; 1 1; 0 0] 等效于指定 Borders = ["left" "right"]。N 维图像的 `Borders` 的默认值为 ones(ndims(I), 2)，它指定删除触及图像所有边界的结构。

**数据类型**：  `double` | `logical`

### 输出参数
**<a id="Q4"></a> J — 已处理的图像**  
数值数组 | 逻辑数组

已处理的灰度或二值图像，根据您指定的输入图像，以数值或逻辑数组形式返回。

## 算法
`imclearborder` 使用形态学重新构造，其中：  
- 掩膜图像是输入图像。  
- 标记图像边界上的元素等于掩膜图像，其他位置的元素都为 0。

## 参考文献
[1] Soille, Pierre. Morphological Image Analysis: Principles and Applications Berlin. New York: Springer, 1999, 164-165.   
[2] Molnar, Ian. Uniform quartz - Silver nanoparticle injection experiment, Digital Rocks Portal, April 2016.  Accessed March 10, 2023. https://www.digitalrocksportal.org/projects/44, made available for documentation use under the ODC-BY 1.0 Attribution License. 

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../conndef/conndef.html">conndef</a> | <a href="../imkeepborder/imkeepborder.html">imkeepborder</a> 
## imhmin 
H - 最小值变换（抑制区域极小值）

## 简介 
[`J = imhmin(I, H)`](#function1)  
[`J = imhmin(I, H, conn)`](#function2)

## 用法
<a id="function1"></a>
[J](#Q4) = imhmin([I](#Q1), [H](#Q2)) 通过 H - 最小值变换抑制灰度图像 `I` 中的区域极小值：该变换会将所有区域极小值的 “深度” 降低最多 `H`，最终完全抑制深度小于 `H` 的区域极小值。

- 区域极小值定义为：由相同灰度值 `t` 构成的连通像素集合，且该集合被灰度值大于 `t` 的像素包围。

<a id="function2"></a>
[J](#Q4) = imhmin([I](#Q1), [H](#Q2), [conn](#Q3)) 额外指定连通性参数 `conn`，用于定义识别区域极小值时的像素连通规则。

## 参数说明
### 输入参数
**<a id="Q1"></a> I —  输入图像**  
数值数组

输入图像：指定为任意维度的数值数组。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `int8` | `int16` | `logical`

**<a id="Q2"></a> H — H 最小值变换**  
非负标量

H - 最小值变换阈值：指定为非负标量，用于控制抑制区域极小值的 “深度阈值”。

**数据类型：**`single` | `double` | `uint8` | `uint16` | `int8` | `int16` | `logical`

**<a id="Q3"></a> conn — 像素连通性**  
4 | 8

像素连通性：指定为下表中的值之一。对于二维图像，默认连通性是 8。

| 数值 | 维度 | 意义                                                         |
| :--- | ---- | ------------------------------------------------------------ |
| 4    | 二维 | 像素仅边缘接触则连通；邻域为水平 / 垂直方向的相邻像素（共 4 个）。 |
| 8    | 二维 | 像素边缘 / 角接触则连通；邻域为水平 / 垂直 / 对角线方向的相邻像素（共8 个）。 |
| 6    | 三维 | 像素仅面接触则连通；邻域为正交方向的相邻像素（共 6 个）      |
| 18   | 三维 | 像素正交 / 面对角接触则连通；邻域为 6 正交 + 12 个面对角像素（共 18 个）。 |
| 26   | 三维 | 像素正交 / 面对角 / 体对角接触则连通；邻域为 6 正交 + 12 面对角 + 8 体对角（共 26 个）。 |

### 输出参数
**<a id="Q4"></a> J — 变换后的图像**  
数值数组

变换后的图像：返回为与 `I` 尺寸和数据类型完全相同的数值数组。

## 参考文献
 Soille P. Morphological image analysis: principles and applications. Berlin: Springer, 1999.

## 版本历史
在北太天元图像处理工具箱 V1.1 推出

## 相关主题
<a href="../conndef/conndef.html">conndef</a> | <a 
href="../imextendedmin/imextendedmin.html">imextendedmin</a> | <a 
href="../imhmax/imhmax.html">imhmax</a> | <a 
href="../imreconstruct/imreconstruct.html">imreconstruct</a> | <a 
href="../imregionalmin/imregionalmin.html">imregionalmin</a> 




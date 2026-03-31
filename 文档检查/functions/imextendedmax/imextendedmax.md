## imextendedmax
扩展极大值变换

## 简介
[`BW = imextendedmax(I, H)`](#function1)  
[`BW = imextendedmax(I, H, conn)`](#function2)

## 用法
<a id="function1"></a>
[BW](#Q4) = imregionalmax([I](#Q1), [H](#Q2)) 计算图像 `I` 的扩展最大值变换，该变换本质是 H - 最大值变换的区域极大值。区域极大值指像素值恒定的连通分量，且其外部边界像素的取值均低于该分量的像素值。
<a id="function2"></a>
[BW](#Q4) = imregionalmax([I](#Q1), [H](#Q2), [conn](#Q3)) 计算扩展最大值变换，其中 `conn` 参数用于指定像素的连通性。

## 参数说明
### 输入参数
**<a id="Q1"></a> I —  输入图像**  
数值数组

输入图像：指定为任意维度的数值数组。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `int8` | `int16` | `logical`

**<a id="Q2"></a> H — H 最大值变换**  
非负标量

H 最大值变换，指定为非负标量。

**示例：** 80

**数据类型：** `single` | `double` | `uint8` | `uint16` | `int8` | `int16` | `logical`

**<a id="Q3"></a> conn — 像素连通性**  
4 | 8 

像素连通性，指定为下表中的值之一。对于二维图像，默认连通性是 8。

| 数值 | 维度 | 意义                                                         |
| :--- | ---- | ------------------------------------------------------------ |
| 4    | 二维 | 像素仅边缘接触则连通；邻域为水平 / 垂直方向的相邻像素（共 4 个）。 |
| 8    | 二维 | 像素边缘 / 角接触则连通；邻域为水平 / 垂直 / 对角线方向的相邻像素（共8 个）。 |
| 6    | 三维 | 像素仅面接触则连通；邻域为正交方向的相邻像素（共 6 个）      |
| 18   | 三维 | 像素正交 / 面对角接触则连通；邻域为 6 正交 + 12 个面对角像素（共 18 个）。 |
| 26   | 三维 | 像素正交 / 面对角 / 体对角接触则连通；邻域为 6 正交 + 12 面对角 + 8 体对角（共 26 个）。 |

### 输出参数
**<a id="Q4"></a> BW — 变换后的图像**  
逻辑数组

变换后的图像：返回为与 `I` 尺寸相同的逻辑数组。

## 参考文献
Soille P. Morphological image analysis: principles and applications. Berlin: Springer, 1999.

## 版本历史
在北太天元图像处理工具箱 V1.1 推出

## 相关主题
<a href="../conndef/conndef.html">conndef</a> | <a 
href="../imextendedmin/imextendedmin.html">imextendedmin</a> | <a 
href="../imhmax/imhmax.html">imhmax</a> | <a 
href="../imreconstruct/imreconstruct.html">imreconstruct</a> | <a 
href="../imregionalmax/imregionalmax.html">imregionalmax</a> 




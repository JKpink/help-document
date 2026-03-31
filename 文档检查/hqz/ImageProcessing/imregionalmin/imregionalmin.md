## imregionalmin 
区域极小值提取

## 简介
[`BW = imregionalmin(I)`](#function1)  
[`BW = imregionalmin(I, conn)`](#function2)

## 用法
<a id="function1"></a>
[BW](#Q3) = imregionalmin([I](#Q1)) 返回二值图像 `BW`，其中值为 `1` 的像素标记出灰度图像 `I` 中的区域极小值。区域极小值定义：由像素值恒定的连通像素构成的区域，且该区域的所有外部边界像素值均高于区域内的像素值（即 “局部最低值的连通区域”）。
<a id="function2"></a>
[BW](#Q3) = imregionalmin([I](#Q1), [conn](#Q2)) 指定连通性 `conn`。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 灰度图像**  
数值数组

输入的灰度图像：指定为任意维度的数值数组（支持 2D 图像、3D 体数据等），逻辑数组会被视为 “1（真）和 0（假）” 的数值数组处理。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `int8` | `int16` | `logical`

**<a id="Q2"></a> conn — 像素连通性**  
4 | 8

像素连通性，指定为下表中的值之一。对于二维图像，默认连通性是 8。

| 数值 | 维度 | 意义                                                         |
| :--- | ---- | ------------------------------------------------------------ |
| 4    | 二维 | 像素仅边缘接触则连通；邻域为水平 / 垂直方向的相邻像素（共 4 个）。 |
| 8    | 二维 | 像素边缘 / 角接触则连通；邻域为水平 / 垂直 / 对角线方向的相邻像素（共 8 个）。 |
| 6    | 三维 | 像素仅面接触则连通；邻域为正交方向的相邻像素（共 6 个）      |
| 18   | 三维 | 像素正交 / 面对角接触则连通；邻域为 6 正交 + 12 个面对角像素（共 18 个）。 |
| 26   | 三维 | 像素正交 / 面对角 / 体对角接触则连通；邻域为 6 正交 + 12 面对角 + 8 体对角（共 26 个）。 |

### 输出参数
**<a id="Q3"></a> BW — 区域最小值的位置**  
逻辑数组

区域极小值的位置标记：返回与 `I` 尺寸相同的逻辑数组，其中：

- 值为 `1`：对应位置是区域极小值；
- 值为 `0`：非区域极小值。

**数据类型：** `logical`

## 版本历史
在北太天元图像处理工具箱 V1.1 推出

## 相关主题
<a href="../conndef/conndef.html">conndef</a> | <a 
href="../imextendedmin/imextendedin.html">imextendedmin</a> | <a 
href="../imhmin/imhmin.html">imhmin</a> | <a 
href="../imimposemin/imimposemin.html">imimposemin</a> | <a 
href="../imreconstruct/imreconstruct.html">imreconstruct</a> | <a 
href="../imregionalmax/imregionalmax.html">imregionalmax</a> 




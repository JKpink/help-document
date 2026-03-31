## imreconstruct 
形态学重构

## 简介
[`J = imreconstruct(marker, mask)`](#function1)  
[`J = imreconstruct(marker, mask, conn)`](#function2)

## 用法
<a id="function1"></a>
[J](#Q4) = imreconstruct([marker](#Q1), [mask](#Q2))  在掩码图像 `mask` 约束下，对标记图像 `marker` 执行形态学重构并返回结果 `J`。核心规则：

- 标记图像 `marker` 的元素值必须小于等于掩码图像 `mask` 对应位置的元素值；
- 若 `marker` 中存在元素值大于 `mask` 对应值的情况，函数会先将其截断至 `mask` 的对应值，再开始重构流程。

<a id="function2"></a>
[J](#Q4) = imreconstruct([marker](#Q1), [mask](#Q2), [conn](#Q3)) 额外指定像素连通性参数 `conn`。

## 参数说明
### 输入参数
**<a id="Q1"></a> marker — 标记图像**  
数值数组 | 逻辑数组

标记图像，指定为任意维度的数值 / 逻辑数组，定义重构的 “种子” 区域。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `int8` | `int16` | `logical`

**<a id="Q2"></a> mask — 掩码图像**  
数值数组 | 逻辑数组

掩码图像，指定为与 `marker` 尺寸、数据类型完全相同的数值 / 逻辑数组，约束重构的范围和上限。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `int8` | `int16` | `logical`

**<a id="Q3"></a> conn — 像素连通性**  
4 | 8

像素连通性，指定为下表中的值之一。对于二维图像，默认连通性是 8。

| 数值 | 维度 | 意义                                                         |
| :--- | ---- | ------------------------------------------------------------ |
| 4    | 二维 | 像素仅边缘接触则连通；邻域为水平 / 垂直方向的相邻像素（共 4 个）。 |
| 8    | 二维 | 像素边缘 / 角接触则连通；邻域为水平 / 垂直 / 对角线方向的相邻像素（共 8 个）。 |
| 6    | 三维 | 像素仅面接触则连通；邻域为正交方向的相邻像素（共 6 个）      |
| 18   | 三维 | 像素正交 / 面对角接触则连通；邻域为 6 正交 + 12 个面对角像素（共 18 个）。 |
| 26   | 三维 | 像素正交 / 面对角 / 体对角接触则连通；邻域为 6 正交 + 12 面对角 + 8 体对角（共 26 个）。 |

**数据类型：** `double` | `logical`

### 输出参数
**<a id="Q5"></a> J — 重建图  
数值数组 | 逻辑数组

重构后的图像，返回为与输入图像尺寸相同的数值 / 逻辑数组（类型与输入一致）。

## 算法
`imreconstruct` 采用文献[[1]](#R1)中描述的 “快速混合灰度重构算法” 实现形态学重构。

## <a id="R1"></a> 参考文献
 Vincent L. Morphological grayscale reconstruction in image analysis: applications and efficient algorithms. IEEE transactions on image processing, 1993, 2(2): 176-201.

## 版本历史
在北太天元图像处理工具箱 V1.1 推出

## 相关主题
<a href="../imclearborder/imclearborder.html">imclearborder</a> | <a 
href="../imextendedmax/imextendedmax.html">imextendedmax</a> | <a 
href="../imextendedmin/imextendedmin.html">imextendedmin</a> | <a 
href="../imfill/imfill.html">imfill</a> | <a 
href="../imhmax/imhmax.html">imhmax</a> | <a 
href="../imhmin/imhmin.html">imhmin</a> | <a 
href="../imimposemin/imimposemin.html">imimposemin</a> 

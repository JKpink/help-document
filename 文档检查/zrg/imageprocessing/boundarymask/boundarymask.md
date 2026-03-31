## boundarymask
计算分割的区域边界

## 简介
[`mask = boundarymask(L)`](#function1)  
[`mask = boundarymask(BW)`](#function2)  
[`mask = boundarymask(___, conn)`](#function3)

## 用法
<a id="function1"></a>
[mask](#Q1) = boundarymask([L](#Q2)) 计算一个掩码，该掩码表示输入标签矩阵 `L` 的区域边界。输出 `mask` 是一个逻辑图像，在边界位置为真，非边界位置为假。
<a id="function2"></a>
[mask](#Q1) = boundarymask([BW](#Q3)) 计算输入二值图像 `BW` 的区域边界。
<a id="function3"></a>
[mask](#Q1) = boundarymask(___, [conn](#Q4)) 使用由 `conn` 指定的连通性计算区域边界。

## 参数说明
### 输入参数
**<a id="Q2"></a> L — 标签矩阵**  
二维非负数矩阵 | 二维逻辑矩阵

标签矩阵，指定为 二维非负数矩阵或 二维逻辑矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical` 

**<a id="Q3"></a> BW — 二值图像**  
数字矩阵 | 逻辑矩阵

二值图像，指定为与 `L` 相同大小的数字或逻辑矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` |  `uint8` | `uint16` | `uint32` | `uint64` | `logical` 


**<a id="Q4"></a> conn — 像素连通性**  
8 (默认) | 4

像素连通性，指定为 4 或 8。

| 值 | 意义 |
| :----------- | :----------- |
| 二维连通 |  
| 4 | 如果像素的边缘相互接触，则这些像素具有连通性。像素的邻域是水平或垂直方向上的相邻像素。 |  |
| 8 | 如果像素的边缘或角相互接触，则这些像素具有连通性。像素的邻域是水平、垂直或对角线方向上的相邻像素。 | 

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` 

### 输出参量
**<a id="Q1"></a> mask — 区域边界的栅格化网格**  
二维逻辑矩阵

区域边界的栅格化网格，指定为与输入图像大小相同的二维逻辑矩阵。当输入图像中值为 `P` 的像素的相邻像素具有与 `P` 不同的值时，掩模中的相应像素为真。

**数据类型：** `logical`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../superpixels/superpixels.html">superpixels</a> | <a 
href="../imoverlay/imoverlay.html">imoverlay</a> | <a 
href="../label2idx/label2idx.html">label2idx</a> 


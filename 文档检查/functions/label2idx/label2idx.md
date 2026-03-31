## label2idx
将标记矩阵转换为元胞数组

## 简介
[`pixelIndexList = label2idx(L)`](#function1)

## 用法
<a id="function1"></a>
[pixelIndexList](#Q1) = label2idx([L](#Q2)) 将标签矩阵 `L` 描述的区域转换为线性索引 pixelIndexList。

## 参数说明
### 输入参数
**<a id="Q2"></a> L — 标签矩阵**  
数值数组

标签矩阵，指定为任意维度的数值数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参量
**<a id="Q1"></a> pixelIndexList — 区域中像素的线性索引**  
1×n 单元数组

区域中像素的线性索引，以 1×n 单元数组的形式返回。输出的每个元素pixelIndexList{n} 都是一个向量，包含 `L` 中所有等于 n 的线性索引。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../labelmatrix/labelmatrix.html">labelmatrix</a> | <a 
href="../label2rgb/label2rgb.html">label2rgb</a> | <a 
href="../superpixels/superpixels.html">superpixels</a> 
## montage
将多幅图像显示为矩形蒙太奇

## 简介
[`montage(imagelist)`](#function1)  
[`montage(I)`](#function2)  
[`montage(___, Name, Value)`](#function3)  
[`img = montage(___)`](#function4)  

## 用法 
<a id="function1"></a> montage([imagelist](#Q1)) 显示由 `imagelist` 指定的图像拼接图。`imagelist` 表示需要拼接的图像列表。这些图像可以是不同类型和尺寸的。`montage` 函数默认会将图像排列成近似正方形的形式。   
<a id="function2"></a> montage([I](#Q2)) 显示多帧图像 `I` 的所有帧。  
<a id="function3"></a> montage(\_\_\_, [Name, Value](#Q3)) 使用名称-值参数来控制附加选项，从而自定义图像拼接图的显示方式。  
<a id="function4"></a> [img](#P1) = montage(\_\_\_) 返回包含所有显示帧的单个图像对象的句柄。  
   

## 参数说明
### 输入参数
**<a id="Q1"></a> imagelist — 需要拼接的图像集合**  
单元数组 | 字符串向量

需要拼接的图像集合，指定为单元数组或字符串向量。使用单元数组可以是以下任意元素的组合：

- 大小为 m×n 的数值矩阵，表示灰度图像。
- 大小为 m×n×3 的数值数组，表示彩色图像。
- 字符向量或字符串，指定图像文件的名称。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` | `logical` | `char` | `string` | `cell` 

**<a id="Q2"></a> I — 多帧图像**  
数值数组

多帧图像，指定为以下尺寸之一的数值数组：

- m×n×k，表示一系列 k 个二值图像或灰度图像。
- m×n×1×k，表示一系列 k 个二值图像或灰度图像。
- m×n×3×k，表示一系列 k 个真彩色图像。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` | `logical` 

### <a id="Q3"></a> 名称-值参数
将可选的参量对组指定为 Name1, Value1, ... ,NameN, ValueN，其中 Name 是参量名称，Value 是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。 

**Size — 图像的行数和列数**  
2 元向量

指定为形式为 [nrows ncols] 的 2 元向量。  
暂不支持将某个维度指定 `NaN` 或 `Inf`。当 `Size` 与指定的图像（帧）数量不匹配时，`montage` 函数会根据 `Size` 创建平铺图像。

**数据类型：** `single` | `double` 

### 输出参数

**<a id="P1"></a> img — 拼接图像**  
图像对象

拼接图像，以图像对象形式返回。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../imshow/imshow.html">imshow</a> 
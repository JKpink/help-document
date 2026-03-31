## circles2mask
由圆创建二值掩模图像

## 简介
[`mask = circles2mask(centers, radii, maskSize)`](#function1)

## 用法
<a id="function1"></a>
[mask](#Q1) = circles2mask([centers](#Q2), [radii](#Q3), [maskSize](#Q4)) 从由中心坐标、中心和半径长度指定的圆创建二进制掩码图像。`maskSize` 参数指定输出二进制掩码 `mask` 的尺寸。

## 参数说明
### 输入参数
**<a id="Q2"></a> centers — 圆心**  
P×2 矩阵

圆心，指定为 `P×2` 矩阵。每一行指定一个圆心的 `xy` 坐标。可以使用 <a href="../imfindcircles/imfindcircles.html">imfindcircles</a> 函数的 [centers](#Q2) 输出来指定此参数。

**数据类型：** `double`

**<a id="Q3"></a> radii — 圆的半径**  
向量

圆的半径，指定为向量的圆半径。可以使用 <a href="../imfindcircles/imfindcircles.html">imfindcircles</a> 函数的半径 [radii](#Q3) 输出来指定此参数。

**数据类型：** `double`

**<a id="Q4"></a> maskSize — 掩模图像尺寸**  
元素为非负整数的二维行向量

掩模图像大小，指定为形式为 [高度 宽度] 的二维行向量，其元素为非负整数。此参数指定了以像素为单位的输出二值掩模的尺寸。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出参量
**<a id="Q1"></a> mask — 二值掩码图像**  
逻辑矩阵

二值掩模图像，以逻辑矩阵的形式返回，其大小由 [maskSize](#Q4) 参数指定。

**数据类型：** `logical`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../imfindcircles/imfindcircles.html">imfindcircles</a> | <a 
href="../viscircles/viscircles.html">viscircles</a> | <a 
href="../createMask/createMask.html">createMask</a> 


## PiecewiseLinearTransformation2D
二维分片线性几何变换

## 简介
[`tform = PiecewiseLinearTransformation2D(movingPoints, fixedPoints)`](#function1)

## 用法 
<a id="function1"></a> tform = PiecewiseLinearTransformation2D([movingPoints](#Q1), [fixedPoints](#Q2)) 创建一个 `PiecewiseLinearTransformation2D` 对象，通过分段线性变换将移动图像中的控制点 `movingPoints` 映射到固定图像中的对应控制点 `fixedPoints`。可以使用 <a href="../cpselect/cpselect.html">cpselect</a>  </a> 函数来选取这些控制点。

## 参数说明
### 输入参数
**<a id="Q1"></a> movingPoints — 移动图像中的控制点**  
m × 2 矩阵  

移动图像中的控制点，指定为 m × 2 矩阵，其中 m 大于或等于 4。矩阵的每一行代表一个控制点的 (x, y) 坐标。

**数据类型：** `double` | `single` 
 
**<a id="Q2"></a> fixedPoints — 固定图像控制点**  
m × 2 矩阵  

固定图像中的控制点，指定为 m × 2 矩阵，其中 m 大于或等于 4。矩阵的每一行代表一个控制点的 (x, y) 坐标。

**数据类型：** `double` | `single`

## 属性
**Dimensionality — 几何变换维度**  
 2  

输入点和输出点的几何变换维度，这里始终为 2。  
## 算法  
在分段线性变换中，线性（仿射）变换分别应用于图像的每个三角形区域[[1]](#Ref1)。  
  1.找到固定控制点的 Delaunay三角剖分。  
  2.利用每个三角形的三个顶点，推断出从固定坐标到移动坐标的仿射映射。该映射在每个三角形上是仿射的，并且在控制点之间是连续的，但并非连续可导。    
必须通过指定至少四对不共线的控制点来定义至少两个具有不同映射的三角形。更多的控制点对可以产生更多的三角形区域。
`PiecewiseLinearTransformation2D` 对象会移除作为退化的重叠三角形顶点的控制点。当 `movingPoints` 和 `fixedPoints` 未以相同顺序列出控制点时，该对象可能无法消除所有重叠的三角形。要解决此错误，请确保移动图像和固定图像中的控制点顺序一致。
 
## 参考文献  
<a id="Ref1"></a> [1] A GOSHTASBY. Piecewise linear mapping functions for image registration. Pattern Recognition, 1986, 19(6): 459-466.


## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
 <a
href="../fitgeotform2d/fitgeotform2d.html">fitgeotform2d</a> | <a 
href="../cpselect/cpselect.html">cpselect</a> | <a 
href="../imwarp/imwarp.html">imwarp</a>

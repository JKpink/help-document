## PolynomialTransformation2D
2 维多项式几何变换

## 简介
[ `tform = PolynomialTransformation2D(movingPoints, fixedPoints, degree)`](#function1)  
## 用法
<a id="function1"></a>
[tform](#P1) = PolynomialTransformation2D([movingPoints](#Q1), [fixedPoints](#Q2), [degree](#Q3)) 。自动估计多项式系数，将运动图像中的控制点 `movingPoints` 映射到固定图像中的控制点 `fixedPoints`，并确定最优的多项式阶数 `degree`，创建一个 `PolynomialTransformation2D` 对象。  
 

## 参数说明
### 输入参数
**<a id="Q1"></a> movingPoints — 浮动图像中的控制点集合**  
m×2 矩阵

浮动图像中的控制点集合，指定为 m×2 矩阵。矩阵的每一行定义一个控制点的 (x, y) 坐标，其中第一列为 `x` 坐标（水平方向），第二列为 `y` 坐标（垂直方向）。   

**数据类型：** `single` | `double` 

**<a id="Q2"></a> fixedPoints — 固定图像中的控制点集合**  
m×2 矩阵

固定图像中的控制点集合，指定为 m×2 矩阵。矩阵的每一行定义一个控制点的 (x, y) 坐标，其中第一列为 `x` 坐标（水平方向），第二列为 `y` 坐标（垂直方向）。   

**数据类型：** `single` | `double` 

**<a id="Q3"></a> degree — 多项式变换的阶数**  
2 | 3 | 4

多项式变换的阶数，指定为数字 2、3 或 4。 


### 输出参数
**<a id="P1"></a> tform — 2 维多项式几何变换**  
`PolynomialTransformation2D` 对象

2 维局部加权平均几何变换对象，返回 `PolynomialTransformation2D` 对象。`PolynomialTransformation2D` 对象用于封装二维多项式几何变换的数学模型及相关参数，并支持执行逆变换操作。

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../imwarp/imwarp.html">imwarp</a> | <a
href="../fitgeotform2d/fitgeotform2d.html">fitgeotform2d</a> 
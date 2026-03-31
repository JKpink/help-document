## LocalWeightedMeanTransformation2D
2 维局部加权平均几何变换

## 简介
[ `tform = LocalWeightedMeanTransformation2D(movingPoints, fixedPoints, n)`](#function1)  
## 用法
<a id="function1"></a>
[tform](#P1) = LocalWeightedMeanTransformation2D([movingPoints](#Q1), [fixedPoints](#Q2), [n](#Q3)) 创建一个 `LocalWeightedMeanTransformation2D` 对象，该对象通过局部加权平均变换，将浮动图像中的控制点 `movingPoints` 映射到固定图像中的对应控制点 `fixedPoints`。变换算法基于每个控制点的局部邻域：利用其最近的 `n` 个邻近点拟合二阶多项式变换模型，实现逐点的自适应空间映射。  
 

## 参数说明
### 输入参数
**<a id="Q1"></a> movingPoints — 浮动图像中的控制点集合**  
m×2 矩阵

浮动图像中的控制点集合，指定为 m×2 矩阵。矩阵的每一行定义一个控制点的 (x, y) 坐标，其中第一列为 `x` 坐标（水平方向），第二列为 `y` 坐标（垂直方向）。控制点数量 m 必须大于或等于算法参数 n（用于局部拟合的最近邻点数）。   

**数据类型：** `single` | `double` 

**<a id="Q2"></a> fixedPoints — 固定图像中的控制点集合**  
m×2 矩阵

固定图像中的控制点集合，指定为 m×2 矩阵。矩阵的每一行定义一个控制点的 (x, y) 坐标，其中第一列为 `x` 坐标（水平方向），第二列为 `y` 坐标（垂直方向）。控制点数量 m 必须大于或等于算法参数 n（用于局部拟合的最近邻点数）。   

**数据类型：** `single` | `double` 

**<a id="Q3"></a> n — 局部加权平均计算所使用的邻近点数量**  
正整数

局部加权平均计算所使用的邻近点数量，指定为正整数。参数 `n` 最小可取值为 6，但设置过小的 `n` 可能导致拟合出的多项式出现病态问题。 

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `uint64` | `int8` | `int16` | `int32`

### 输出参数
**<a id="P1"></a> tform — 2 维局部加权平均几何变换对象**  
LocalWeightedMeanTransformation2D

2 维局部加权平均几何变换对象，返回 `LocalWeightedMeanTransformation2D` 对象。`LocalWeightedMeanTransformation2D` 对象存储有关二维局部加权平均几何变换的信息，并支持逆变换。

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../imwarp/imwarp.html">imwarp</a> | <a
href="../fitgeotform2d/fitgeotform2d.html">fitgeotform2d</a> 
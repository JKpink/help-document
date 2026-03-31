## fitgeotform2d
根据控制点对拟合二维几何变换

## 简介
[`tform = fitgeotform2d(movingPoints, fixedPoints, tformType)`](#function1)

## 用法
<a id="function1"></a> [tform](#P1) = fitgeotform2d([movingPoints](#Q1), [fixedPoints](#Q2), [tformType](#Q3)) 根据控制点对组 `movingPoints` 和 `fixedPoints` 拟合 `tformType` 类型的线性几何变换。

## 参数说明
### 输入参数
**<a id="Q1"></a> movingPoints — 移动图像中的控制点**  
m × 2 矩阵

移动图像中的控制点，指定为 m × 2 矩阵。每行指定一个控制点的 (x, y) 坐标。  

变换类型会影响控制点对组的最小数量。例如，一个没有翻转的相似变换需要至少 2 个控制点对组。

示例：movingPoints = (11 11; 41 71); 

**数据类型：** `double` | `single`

**<a id="Q2"></a> fixedPoints — 固定图像中的控制点**  
m × 2 矩阵

固定图像中的控制点，指定为 m × 2 矩阵。每行指定一个控制点的 (x, y) 坐标。

示例：fixedPoints = (14 44; 70 81);

**数据类型：**`double` | `single`

**<a id="Q3"></a> tformType — 线性变换的类型**  
`"similarity"` | `"reflectivesimilarity"` | `"affine"` | `"projective"`

线性变换的类型，指定为 `"similarity"`、`"reflectivesimilarity"`、`"affine"` 或 `"projective"`。

**数据类型：**`char` | `string`

### 输出参数
**<a id="P1"></a> tform — 几何变换**  
几何变换对象

几何变换，指定为下表中列出的几何变换对象：

| **变换类型** | **几何变换对象** |
| :----------- | :----------- |
| `"similarity"` | <a href="../simtform2d/simtform2d.html">simtform2d</a> |
| `"reflectivesimilarity"` | <a href="../affinetform2d/affinetform2d.html">affinetform2d</a> |
| `"affine"` | <a href="../affinetform2d/affinetform2d.html">affinetform2d</a> |
| `"projective"` | <a href="../projtform2d/projtform2d.html">projtform2d</a> |

## 详细信息
| **变换类型** | **描述** | **控制点对组的最小数量** |
| :----------- | :----------- | :----------- |
| `"similarity"` | 当移动图像中的形状保持不变，但图像因某种程度的平移、旋转和各向同性缩放而失真时，请使用此变换。直线保持笔直，平行线仍保持平行。 | 2 |
| `"reflectivesimilarity"` | 与 `"similarity"` 相同，只是增加了翻转（可选）。 | 3 |
| `"affine"` | 当移动图像中的形状呈现剪切或各向异性缩放时，请使用此变换。直线保持笔直，平行线仍保持平行，但矩形变为平行四边形。 | 3 |
| `"projective"` | 当场景出现倾斜时，请使用此变换。直线保持笔直，但平行线向消失点收敛。 | 4 |


## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imwarp/imwarp.html">imwarp</a> | <a 
href="../cpselect/cpselect.html">cpselect</a> | <a 
href="../fitgeotform3d/fitgeotform3d.html">fitgeotform3d</a>
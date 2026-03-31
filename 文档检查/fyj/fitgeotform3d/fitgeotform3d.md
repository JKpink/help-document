## fitgeotform3d
根据控制点对拟合三维几何变换

## 简介
[`tform = fitgeotform3d(movingPoints, fixedPoints, tformType)`](#function1)

## 用法 
<a id="function1"></a> [tform](#P1) = fitgeotform3d([movingPoints](#Q1), [fixedPoints](#Q2), [tformType](#Q3))  根据控制点对组 `movingPoints` 和 `fixedPoints` 拟合 `tformType` 类型的三维线性几何变换。返回的变换对象 `tform` 会将移动图像中的控制点位置正向映射到参考图像的对应位置。

## 参数说明
### 输入参数
**<a id="Q1"></a> movingPoints — 移动图像中的控制点**  
m × 3 矩阵

移动图像中的控制点位置，指定为 m × 3 矩阵。每行指定一个控制点的 (x, y, z) 坐标。

示例：movingPoints = (11 11 5; 41 71 50);

**数据类型：**`double` | `single`

**<a id="Q2"></a> fixedPoints — 固定图像中的控制点**  
m × 3 矩阵

固定图像中的控制点位置，指定为 m × 3 矩阵。每行指定一个控制点的 (x, y, z) 坐标。 

示例：fixedPoints = [11 11 5; 41 71 50];

**数据类型：**`double` | `single`

**<a id="Q3"></a> tformType — 线性变换的类型**  
`"translation"` | `"rigid"` | `"affine"`

线性变换的类型，指定为以下表中定义的线性变换之一：

| **值**        | **描述**                                               | **所需最小控制点对数** |
| :------------ | :----------------------------------------------------- | :--------------------- |
| `"translation"` | 平移变换                                               | 1                      |
| `"rigid"`       | 刚性变换，可包含平移和旋转。                           | 3                      |
| `"affine"`      | 仿射变换，可包含平移、旋转、各向异性缩放、反射和剪切。 | 4                      |

### 输出参量
**<a id="P1"></a> tform — 几何变换**  
几何变换对象

几何转换，指定为下表中列出的几何变换对象:

| **变换类型**  | **几何变换对象** |
| :------------ | :--------------- |
| `"translation"` | <a href="../transltform3d/transltform3d.html">transltform3d</a>    |
| `"rigid"`       | <a href="../rigidtform3d/rigidtform3d.html">rigidtform3d</a>     |
| `"affine"`      | <a href="../affinetform3d/affinetform3d.html">affinetform3d</a>    |

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../imwarp/imwarp.html">imwarp</a> | <a 
href="../fitgeotform2d/fitgeotform2d.html">fitgeotform2d</a>
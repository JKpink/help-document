## reducepoly 
使用 Ramer-Douglas-Peucker 算法降低 ROI 中点的密度

## 简介
[`P_reduced = reducepoly(P)`](#function1)  
[`P_reduced = reducepoly(P, tolerance)`](#function2)

## 用法
<a id="function1"></a>
[P_reduced](#Q3) = reducepoly([P](#Q1)) 降低感兴趣区域中点的密度。该函数使用 Ramer–Douglas–Peucker 线简化算法，通过移除直线上的冗余点，仅保留拐点（即线条弯曲处的点）来实现简化。  
<a id="function2"></a>
[P_reduced](#Q3) = reducepoly([P](#Q1), [tolerance](#Q2)) 降低感兴趣区域中点的密度，其中 `tolerance` 用于控制简化的敏感度，其值在 [0, 1] 内指定。

## 参数说明
### 输入参数
**<a id="Q1"></a> P — 待减少的点集**  
n×2 数值矩阵

待减少的点，指定为 [x1 y1; ...; xn yn] 形式的 n×2 数值矩阵。数组中的每一行都定义 ROI 形状中的顶点，例如折线、多边形等。

**数据类型**： `single` | `double` | `uint8` | `uint16` | `uint32` | `uint64` | `int8` | `int16` | `int32` |`int64`

**<a id="Q2"></a> tolerance — 降低灵敏度**  
0.001 (默认) | 范围 [0, 1] 中的数字

降低敏感度，指定为 [0, 1] 范围内的数字。增加敏感度会增加移除的点数。敏感度值为 0 时，会减少最少数量的点。敏感度值为 1 会导致点的减少量最大，只留下线的端点。

**数据类型**： `single` | `double` | `uint8` | `uint16` | `uint32` | `uint64` | `int8` | `int16` | `int32` |`int64`

### 输出参数
**<a id="Q3"></a> P_reduced — 缩减数据集**  
m×2 数值矩阵

缩减的数据集，以 m×2 数值矩阵的形式返回。减少的点数通常小于 `P` 中的原始点数。

**数据类型**： `double`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../drawpolygon/drawpolygon.html">drawpolygon</a> | <a 
href="../drawpolyline/drawpolyline.html">drawpolyline</a> 
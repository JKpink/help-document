## reduce 
降低 ROI 中点的密度

## 简介
[`reduce(p)`](#function1)  
[`reduce(p, tolerance)`](#function2)

## 用法
<a id="function1"></a>
reduce([p](#Q1)) 降低感兴趣区域中点的密度。该函数使用 Ramer–Douglas–Peucker 线简化算法 [[1]](#R1)，通过移除直线上的冗余点，仅保留拐点（即线条弯曲处的点）来实现简化。  
<a id="function2"></a>
reduce([p](#Q1), [tolerance](#Q2)) 降低感兴趣区域中点的密度，其中 `tolerance` 用于控制简化的敏感度，其值在 [0, 1] 内指定。

## 参数说明
### 输入参数

**<a id="Q1"></a> p — 多边形 ROI 的顶点**  
n×2 矩阵

多边形 ROI 的顶点位置，指定为 n×2 矩阵，表示 n 个顶点的坐标。

**<a id="Q2"></a> tolerance — 降低灵敏度**  
0.001 (默认) | 范围 [0, 1] 中的数字

降低敏感度，指定为 [0, 1] 范围内的数字。增加敏感度会增加移除的点数。敏感度值为 0 时，会减少最少数量的点。敏感度值为 1 会导致点的减少量最大，只留下线的端点。

## <a id="R1"></a> 参考文献
[1] Douglas David H, Thomas K Peucker. Algorithms for the reduction of the number of points required to represent a digitized line or its caricature. Cartographica: the international journal for geographic information and geovisualization, 1973, 10(2): 112-122.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../drawpolygon/drawpolygon.html">drawpolygon</a> | <a 
href="../drawpolyline/drawpolyline.html">drawpolyline</a> 
## roipoly 
由多边形 ROI 创建二值掩膜图像

## 简介
[`BW = roipoly(I, xi, yi) `](#function1)

## 用法
<a id="function1"></a>
[BW ](#Q4) = roipoly([I](#Q1), [xi](#Q2), [yi](#Q3)) 通过指定多边形顶点的 (x, y) 坐标 (xi, yi) 来创建二值掩膜 `BW`。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 灰度或 RGB 图像**  
m×n 数值矩阵 | m×n×3 数值数组

灰度或 RGB 图像，指定为 m×n 数值矩阵或 m×n×3 数值数组。

**<a id="Q2"></a> xi — 多边形顶点的 x 坐标**  
数值向量

多边形顶点的 x 坐标，指定为与 `yi` 长度相同的数值向量。

**<a id="Q3"></a> yi — 多边形顶点的 y 坐标**  
数值向量

多边形顶点的 y 坐标，指定为与 `xi` 长度相同的数值向量。

### 输出参数
**<a id="Q4"></a> BW — 二值图像**  
m×n 逻辑矩阵

二值图像，以 m 行 n 列的逻辑矩阵形式返回。

**数据类型**： `logical`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../drawpolygon/drawpolygon.html">drawpolygon</a> | <a 
href="../poly2mask/poly2mask.html">poly2mask</a> | <a 
href="../roicolor/roicolor.html">roicolor</a> 
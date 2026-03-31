## viscircles
绘制圆形

## 简介
[siz = viscircles(centers, radii)](#function1)  
[[m, n] = viscircles(ax, centers, radii)](#function2)

## 用法
<a id="function1"></a>
viscircles(<a href="#Q1">centers</a>, <a href="#Q2">radii</a>) 在当前坐标轴上绘制具有指定圆心和半径的圆形。您可以使用 `imfindcircles` 函数查找图像中的圆形圆心和半径。

<a id="function2"></a>
viscircles(<a href="#Q3">ax</a>, <a href="#Q1">centers</a>, <a href="#Q2">radii</a>) 在由 `ax` 指定的坐标轴上绘制圆形。

## 参数说明
### 输入参数
**<a id="Q1"></a> centers — 圆心坐标**  
两列数值矩阵

圆心坐标，指定为两列数值矩阵。圆心的 `x` 坐标位于第一列，`y` 坐标位于第二列。

**数据类型：**  `double`  

**<a id="Q2"></a> radii — 圆半径**  
正数 | 列向量

圆半径，指定为正数或与 `centers` 长度相同的正数列向量。当 `radii` 为单个正数时，`viscircles` 绘制的所有圆形均使用该相同半径；当 `radii` 为列向量时，`viscircles` 为每个圆心 `centers(j,:)` 绘制对应半径 `radii(j)` 的圆形。

**数据类型：**  `double`  

**<a id="Q3"></a> ax — 用于绘制圆形的坐标轴**  
句柄

用于绘制圆形的坐标轴，指定为 `gca` 或 `axes` 函数返回的 `Axes` 对象。

**数据类型：** Axes 对象句柄

## 版本历史

在北太天元图像处理工具箱 V3.0 推出

## 相关主题

<a href="../imfindcircles/imfindcircles.html">imfindcircles</a> | <a href="../circles2mask/circles2mask.html">circles2mask</a> | <a href="../imdistline/imdistline.html">imdistline</a> | <a href="../drawcircle/drawcircle.html">drawcircle</a>
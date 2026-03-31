## Polyline
折线 ROI

## 简介
[`roi = Polyline(p)`](#function1)

## 用法
<a id="function1"></a>
roi = Polyline([p](#Q1)) 创建一个 `Polyline` 对象，并可以指定折线中的点的位置 `Position` 。

## 参数说明
### 输入参数
**<a id="Q1"></a> p — ROI 的位置**  
n×2 数值矩阵

`ROI` 的位置，指定为 n×2 数值矩阵，其中 `n` 是定义 ROI 的顶点或点的数量。每行表示顶点或点的 [x y] 坐标。要使用更少的点，请使用 `reduce` 函数。
### 输出参数
**<a id="Q3"></a>roi — 感兴趣区域**   
ROI 对象

折线感兴趣区域。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../drawpolyline/drawpolyline.html">drawpolyline</a> | <a 
href="../Crosshair/Crosshair.html">Crosshair</a> | <a 
href="../Line/Line.html">Line</a> | <a 
href="../Polygon/Polygon.html">Polygon</a> 
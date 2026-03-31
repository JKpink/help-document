## Line 
直线 ROI

## 简介
[`roi = Line(position)`](#function1)

## 用法
<a id="function1"></a>
[roi](#Q2) = Line([position](#Q1)) 会创建一个 Line 对象，并可以指定线段的端点位置 `position`。

## 参数说明
### 输入参数
**<a id="Q1"></a>position — ROI 的位置**  
[]（默认）| 2×2 数值向量  

ROI 的位置，指定为 2×2 数值矩阵。每行表示线条端点的 [x y] 坐标。

###输出参数
**<a id="Q2"></a>roi — 感兴趣区域**  
ROI 对象

直线感兴趣区域。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../drawline/drawline.html">drawline</a> | <a
href="../Crosshair/Crosshair.html">Crosshair</a> | <a
href="../Point/Point.html">Point</a> | <a
href="../Polyline/Polyline.html">Polyline</a>
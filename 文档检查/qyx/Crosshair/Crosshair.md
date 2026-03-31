## Crosshair 
十字线 ROI

## 简介
[`roi = Crosshair(p)`](#function1)

## 用法
<a id="function1"></a>
[roi](#Q2) = Crosshair([p](#Q1)) 会创建一个 `Crosshair` 对象，并可以指定十字线的位置 Position 。

## 参数说明
### 输入参数
**<a id="Q1"></a>p — ROI 的位置**  
1×2 数值向量  

ROI 的位置，指定为 [x y] 形式的 1×2 数字向量。值 x 和 y 指定水平线与十字准线 ROI 中垂直线交叉的位置的 x 坐标和 y 坐标。当您绘制或移动 ROI 时，此值会自动更改。

### 输出参数

**<a id="Q2"></a>roi — 感兴趣区域**  
ROI 对象

感兴趣十字线交点。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../drawcrosshair/drawcrosshair.html">drawcrosshair</a> | <a
href="../Line/Line.html">Line</a> | <a 
href="../Point/Point.html">Point</a> | <a 
href="../Polyline/Polyline.html">Polyline</a>
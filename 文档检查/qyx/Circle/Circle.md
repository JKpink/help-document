## Circle 
圆形 ROI

## 简介
[`roi = Circle(center, r)`](#function1)

## 用法
<a id="function1"></a>
[roi](#Q3) = Circle([center](#Q1), [r](#Q2)) 会创建一个 Circle 对象，并可以指定圆的中心点 `Center`,圆的半径 `Radius`。

## 参数说明
###输入参数
**<a id="Q1"></a>center — ROI 中心**  
[]（默认）| 1×2 数值向量  

ROI的中心指定为 [x y] 形式的 1×2 数字向量。值 x 和 y 是 `ROI` 中心点的坐标。

**<a id="Q2"></a>r — 圆的半径**  
非负数  

圆的半径，指定为非负数。

### 输出参数
**<a id="Q3"></a>roi — 感兴趣区域**   
ROI 对象

圆形感兴趣区域。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../drawcircle/drawcircle.html">drawcircle</a> | <a
href="../Ellipse/Ellipse.html">Ellipse</a> 
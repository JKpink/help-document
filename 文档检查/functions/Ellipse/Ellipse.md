## Ellipse 
椭圆形 ROI

## 简介
[`roi = Ellipse(center, semi_axes)`](#function1)  
[`roi = Ellipse(center, semi_axes, rot)`](#function2)

## 用法
<a id="function1"></a>
roi = Ellipse([center](#Q1), [semi_axes](#Q2)) 创建一个 `Ellipse` 对象，并可以指定椭圆的中心点 `Center`，椭圆的半轴长度  `Semiaxes`。  
<a id="function2"></a>
[roi](#Q4) = Ellipse([center](#Q1), [semi_axes](#Q2), [rot](#Q3)) 围绕 ROI 中心的角度 `RotationAngle`。

## 参数说明
### 输入参数
**<a id="Q1"></a>center — ROI 中心**  
[]（默认）| 1×2 数值向量  

ROI 的中心，指定为 [x y] 形式的 1 x 2 数字向量。值 x 和 y 是 `ROI` 中心点的坐标。 

**<a id="Q2"></a>semi_axes — 椭圆的半轴长度**  
1×2 数值向量  

椭圆半轴的长度，指定为 [semiaxis1 semiaxis2] 形式的 1×2 数值向量。`Ellipse` 对象将最接近 x 方向的半轴长度分配给 `semiaxis1`。但请注意，椭圆的形状和方向可以通过交互而改变。当您绘制或重塑 ROI 时此属性的值会自动更改。  

**<a id="Q3"></a>rot — 围绕 ROI中心的角度**  
0（默认）| 非负数值标量  

围绕 ROI 中心的角度 `RotationAngle`，指定为非负数值标量。该角度以顺时针方向的度数为单位进行测量。`RotationAngle` 的值不会影响 `Position` 的值。`Position` 属性表示旋转前 ROI 的初始位置。

### 输出参数
**<a id="Q4"></a>roi — 感兴趣区域** 
ROI 对象

椭圆形感兴趣区域。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../drawellipse/drawellipse.html">drawellipse</a> | <a
href="../Circle/Circle.html">Circle</a>
## draw 
绘制 ROI 

## 简介
[`J = draw(I, ROI)`](#function1)  
[`J = draw(I, ROI, Name, Value) `](#function2)

## 用法
<a id="function1"></a>
[J](#Q4) = draw([I](#Q1), [ROI](#Q2))  将先前生成的ROI的形状叠加在 `I` 上。  
<a id="function2"></a>
[J](#Q4) = draw([I](#Q1), [ROI](#Q2), [Name, Value](#Q3)) 使用一个或多个名称 — 值参数自定义 ROI 的外观和行为。例如 draw(I,ROI, "Color", "r")。

## 参数说明
### 输入参数
**<a id="Q1"></a> I- 输入图像**  
灰度图像 | RGB 图像

指定为灰度或 RGB 图像。

**数据类型**： `uint8` 

**<a id="Q2"></a> ROI- 感兴趣**  
区域 ROI 对象

感兴趣区域，指定为以下类型之一的 ROI 对象：

|Circle|	Point|
| :----------- | :----------- |
|Crosshair	|Polygon|
|Cuboid	|Polyline|
|Ellipse|	Rectangle|
|Freehand	 |&nbsp;|

**<a id="Q3"></a> 名称 — 值参数** 
将可选的参量对组指定为 Name1, Value1, ..., NameN, ValueN，其中 Name 是参量名称，Value 是对应的值。名称 — 值参量必须出现在其他参量之后，但参量对组的顺序无关紧要。

**Color — 线条颜色** 
颜色名称 | 短名称 | 十六进制颜色代码 

线条颜色，指定为颜色名称或短名称或十六进制颜色代码。
可以按名称指定一些常见的颜色。下表列出了命名颜色选项。

| **颜色名称** | **短名称** | **十六进制颜色代码**|
|:-|:-|:-|
|"red"|"r"|"#FF0000"|
|"green"|"g"|"#00FF00"|
|"blue"|"b"|"#0000FF"|
|"cyan"|"c"|"#00FFFF"|
|"magenta"|"m"|"#FF00FF"|
|"yellow"|"y"|"#FFFF00"|
|"black"|"k"|"#000000"|
|"white"|"w"|"#FFFFFF"|    
**示例**： "Color","r"  
**示例**： "Color","green"

**LineWidth — ROI 边框**  
正数

ROI 边框的宽度，指定为以磅为单位的正数。默认值是每个屏幕像素点数的三倍，使得 border 为 3 像素宽。

**MarkerSize — 标记大小**  
正数

标记大小，指定为以磅为单位的正数。默认值为 8 乘以每个屏幕像素的点数，使得标记为 8 个像素大小。

### 输出参数
**<a id="Q4"></a> J — 输出图像**  
灰度图像 | RGB 图像

与输入图像 `I` 的大小和数据类型相同。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../drawcircle/drawcircle.html">drawcircle</a> | <a 
href="../drawellipse/drawellipse.html">drawellipse</a> | <a 
href="../drawline/drawline.html">drawline</a> | <a 
href="../drawpoint/drawpoint.html">drawpoint</a> | <a 
href="../drawpolygon/drawpolygon.html">drawpolygon</a> | <a 
href="../drawpolyline/drawpolyline.html">drawpolyline</a> | <a 
href="../drawrectangle/drawrectangle.html">drawrectangle</a>
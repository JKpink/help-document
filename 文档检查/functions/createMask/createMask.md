## createMask 
由 ROI 创建二值掩膜图像

## 简介
[`bw = createMask(ROI, m, n) `](#function1)  
[`bw = createMask(ROI, I) `](#function2)

## 用法
<a id="function1"></a>
[bw](#Q5) = createMask([ROI](#Q1), [m](#Q2), [n](#Q3)) 返回大小为` [m, n]` 的二值掩膜图像。  
<a id="function2"></a>
[bw](#Q5) = createMask([ROI](#Q1), [I](#Q4)) 返回二值掩膜图像，其大小与图像 `I` 相同。

## 参数说明
### 输入参数
**<a id="Q1"></a> ROI — 感兴趣区域**  
ROI 对象

感兴趣区域，指定为以下类型之一的 ROI 对象：

|Circle|Polygon|
|:-|:-| 
|Cuboid|Rectangle|
|Ellipse|Polyline| 

**<a id="Q2"></a> m — 掩膜图像的行维度**  
正整数

掩膜图像的行维度，指定为正整数。

**<a id="Q3"></a> n — 掩膜图像的列维度**  
正整数

掩膜图像的列维度，指定为正整数。

**<a id="Q4"></a> I — 输入图像数组**  
数值数组

输入图像数组，指定为数值数组。

### 输出参数
**<a id="Q5"></a> bw — 二值掩膜图像**  
逻辑数组

二值掩膜图像，以逻辑数组形式返回。

**数据类型**： ` logical`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../drawcircle/drawcircle.html">drawcircle</a> | <a 
href="../drawellipse/drawellipse.html">drawellipse</a> | <a 
href="../drawline/drawline.html">drawline</a> | <a 
href="../drawpolygon/drawpolygon.html">drawpolygon</a> | <a 
href="../drawpolyline/drawpolyline.html">drawpolyline</a> | <a 
href="../drawrectangle/drawrectangle.html">drawrectangle</a> | <a 
href="../inROI/inROI.html">inROI</a> | <a 
href="../circles2mask/circles2mask.html">circles2mask</a> 
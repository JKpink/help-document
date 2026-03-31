## imerase
删除感兴趣矩形区域内的图像像素

## 简介
[ `Ierased = imerase(I, rect)`](#function1)  
[ `Ierased = imerase(I, rect, 'FillValues', fillValues)`](#function2)   
## 用法
<a id="function1"></a>
[Ierased](#P1) = imerase([I](#Q1), [rect](#Q2)) 根据 `rect` 定义的矩形区域，删除图像 `I` 对应区域的像素，并返回带有被删除感兴趣矩形区域 `Ierased` 的图像。  
<a id="function2"></a> [Ierased](#P1) = imerase([I](#Q1), [rect](#Q2), 'FillValues', [fillValues](#Q3)) 指定要应用于删除像素的填充值。  

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 带有待删除感兴趣矩形区域的图像**  
数值矩阵 | 数值数组

带有待删除感兴趣矩形区域的图像，指定为表示灰度图像的数值矩阵或具有表示彩色图像的三个通道的数值数组。  

**<a id="Q2"></a> rect — 删除感兴趣矩形的大小和位置**  
Rectangle 对象

删除感兴趣矩形的大小和位置，指定为 Rectangle 对象。  

**<a id="Q3"></a> fillValues — 填充值**  
0（默认）| 数值标量 | 3 元数值向量 

应用于删除像素的填充值，指定为以下值之一。  

| 填充值 | 	结果 |
| :----------- | :----------- |
| 数值标量 | 用指定的灰度值填充灰度或 RGB 图像被删除的像素。 | 
| 3 元数值向量 | 用指定的颜色填充 RGB 图像被删除的像素。 | 


### 输出参数
**<a id="P1"></a> Ierased — 删除区域后的图像**  
数值矩阵 | 数值数组

删除区域后的图像，返回与输入图像大小相同的数值矩阵或数值数组。

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../imcrop/imcrop.html">imcrop</a> | <a
href="../Rectangle/Rectangle.html">Rectangle</a> 
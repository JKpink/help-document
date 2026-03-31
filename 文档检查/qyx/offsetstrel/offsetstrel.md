## offsetstrel 
非平坦形态学结构元

## 简介
[ `SE = offsetstrel(offset)`](#function1)

## 用法
<a id="function1"></a>
SE = offsetstrel([offset](#Q1)) 根据输入矩阵 `offset` 中指定的加法偏移量，创建一个非平坦形态学结构元。

## 参数说明
### 输入参数
**<a id="Q1"></a> offset — 需添加至邻域内各像素位置的偏移量**  
数值矩阵

在执行形态学运算时，需要添加到邻域中每个像素位置的偏移值，指定为数值矩阵。值为 -Inf 的偏移量不参与计算。

**数据类型**： `double`

## 对象函数
|函数名|功能|
|:-|:-|
|imdilate|膨胀图像|
|imerode|腐蚀图像|
|imclose|对图像执行形态学闭运算|
|imopen	|对图像执行形态学开运算|
|imbothat|底帽滤波|
|imtophat|顶帽滤波|

## 版本历史 
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../strel/strel.html">strel</a> 




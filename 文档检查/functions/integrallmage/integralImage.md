## integralImage
2维积分图

## 描述
在积分图像中，每个像素表示相应输入像素的累积总和，所有像素都在输入像素的上方和左侧。
积分图像使您能够快速计算图像子区域的求和。无论子区域的大小如何，子区域求和都可以在恒定时间内计算为积分图像中仅四个像素的线性组合。积分图像的使用是由Viola-Jones算法普及的[[1]](#R1)。

## 简介
[ `J = integralImage(I)`](#function1)  
[ `J = integralImage(I, orientation)`](#function2)

## 用法
<a id="function1"></a>
[J](#Q3) =  integralImage([I](#Q1)) 从图像 `I` 计算积分图像。该函数对输出积分图像 `J` 的顶部和左侧进行零填充。  
<a id="function2"></a>
[J](#Q3) =  integralImage([I](#Q1), [orientation](#Q2)) 用来计算由参数 `orientation` 指定图像方向的积分图像，可选 `"upright"`和 `"rotated"` 。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 图像**  
数字数组

图像，指定为任何维度的数值数组。如果输入图像具有两个以上的维度  (ndims (I) > 2)，例如对于 RGB 图像，则 `integralImage` 将计算沿较高维度的所有二维平面的积分图像。

**数据类型：** `uint8`

**<a id="Q2"></a> orientation — 图像方向**  
“直立” (默认) | “旋转”

图像方向，指定为“直立”或“旋转”。如果将方向设置为“旋转”，则 `integralImage` 返回积分图像，用于计算旋转 45 度的矩形的总和。

**数据类型：** `char` | `string`

### 输出参数
**<a id="Q3"></a> J — 积分图像**  
数字矩阵

积分图像，作为数字矩阵返回。该函数根据图像的方向对积分图像进行零填充。这种大小调整有助于沿图像边界计算像素总和。积分图像 `J` 本质上是值 cumsum(cumsum(I, 2)) 的填充版本。

|图像方向|积分图像的大小|
|:-|:-|
|直立积分图像|顶部和左侧有零填充。size(J) = size(I)+1|
|旋转的整体图像|顶部、左侧和右侧有零填充。size(J) = size(I)+[1 2]|

**数据类型：** `double`



## <a id="R1"></a> 参考文献
[1] Viola P, Jones M. Rapid Object Detection using a Boosted Cascade of Simple Features. Proceedings of the 2001 IEEE Computer Society Conference on Computer Vision and Pattern Recognition. IEEE, 2001: 511–518.
[2] Lienhart R, J. Maydt. An Extended Set of Haar-like Features for Rapid Object Detection. Proceedings of the 2002 IEEE International Conference on Image Processing. IEEE, 2002: 900–903.

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../integralBoxFilter/integralBoxFilter.html">integralBoxFilter</a>





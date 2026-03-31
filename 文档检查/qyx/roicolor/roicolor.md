## roicolor 
根据颜色选择 ROI

## 简介
[`BW = roicolor(I, low, high)`](#function1)  
[`BW = roicolor(I, v)`](#function2)

## 用法
<a id="function1"></a>
[BW](#Q5) = roicolor([I](#Q1), [low](#Q2), [high](#Q3)) 返回一个二值图像 `BW`，其中像素值在范围 [low, high] 内的区域被选中为感兴趣区域。  
<a id="function2"></a>
[BW](#Q5) =roicolor([I](#Q1), [v](#Q4)) 返回一个二值图像 `BW`，其中像素值与向量 `v` 中的值匹配的区域被选中为感兴趣区域。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 灰度或彩色图像**  
m×n 数值矩阵

灰度或彩色图像，指定为 m×n 数值矩阵。


**<a id="Q2"></a> low — 最小值**  
数值标量

要包含在 ROI 中的最小值，指定为数值标量。

**<a id="Q3"></a> high — 最大值**  
数值标量

要包含在 ROI 中的最大值，指定为数值标量。

**<a id="Q4"></a> v — 值集**  
数值向量

要包含在 ROI 中的一组值，指定为数值向量。

### 输出参数
**<a id="Q5"></a> BW— 二值图像**  
m×n 逻辑矩阵

二值图像，以 m×n 逻辑矩阵形式返回。

**数据类型**： `logical`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../roipoly/roipoly.html">roipoly</a> 
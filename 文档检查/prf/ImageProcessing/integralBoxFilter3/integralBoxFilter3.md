## integralBoxFilter3 
积分图3维框滤波

## 简介
[ `B = integralBoxFilter3(A)`](#function1)  
[ `B = integralBoxFilter3(A, filterSize)`](#function2)  
[ `B = integralBoxFilter3(___, "NormalizationFactor", normFactor)`](#function3)

## 用法
<a id="function1"></a>
[B](#Q4) = integralBoxFilter3([A](#Q1)) 使用 3×3×3 框滤波器过滤整个图像 `A` 。  
<a id="function2"></a>
[B](#Q4) = integralBoxFilter3([A](#Q1), [filterSize](#Q2)) 使用三维框形滤波器过滤整体图像 `A`，其大小由 `filterSize` 指定。  
<a id="function3"></a>
[B](#Q4) = integralBoxFilter3(___, ["NormalizationFactor",  normFactor](#Q3)) 还指定应用于框形滤波器的标准化因子。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 要过滤的整体图像**  
3-D 数字数组

要过滤的整数图像，指定为 3-D 数值数组。
`integralBoxFilter3` 期望输入积分图像 `A` 是使用 `integralImage3` 计算的直立积分图像。`integralBoxFilter3` 不支持旋转的整形图像。假定积分图像的第一行、第一列和平面是填充的，如 `integralImage3` 返回的那样。

**数据类型：**  `double`

**<a id="Q2"></a> filterSize — 方框滤波器的大小**  
3（默认值）| 正整数，奇数 | 正整数的3元素向量，且为奇数

方框滤波器的大小，可指定为正整数或正整数的3元素向量，如若 `filterSize` 为标量，则 `integralBoxFilter3` 使用立方体方框滤波器。

**<a id="Q3"></a> normFactor — 应用于盒式滤波器的归一化因子**  
数值标量

归一化因子应用于盒式滤波器，指定为数值标量。
默认情况下，当 filterSize 是标量时，归一化因子的值为 1/filterSize.^3，当 `filterSize` 是向量时，归一化因子的值为 1/prod(filterSize)。默认情况下，这具有均值滤波的效果——输出图像中的像素是图像的局部均值。
为了获取局部区域的总和，将 `normFactor` 设置为 1。为了避免在这种情况下的溢出，考虑通过将输入图像转换为双精度数据类型来使用双精度图像。

### 输出参数
**<a id="Q4"></a> B — 过滤后的图像**  
三维数值数组

过滤后的图像，返回为三维数值数组。 `integralBoxFilter3` 返回仅在无填充情况下计算的过滤部分。

**数据类型：**  `double`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../imboxfilt3/imboxfilt3.html">imboxfilt3</a> | <a 
href="../integralImage3/integralImage3.html">integralImage3</a> 
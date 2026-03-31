## integralBoxFilter 
积分图2维框滤波

## 简介
[ `B = integralBoxFilter(A)`](#function1)  
[ `B = integralBoxFilter(A, filterSize)`](#function2)  
[ `B = integralBoxFilter(___, "NormalizationFactor", normFactor)`](#function3)

## 用法
<a id="function1"></a>
[B](#Q4) = integralBoxFilter([A](#Q1)) 使用 3×3 框滤波器过滤整个图像 `A`。返回筛选后的图像 `B`。目前仅支持 `double` 数据类型的图像。  
<a id="function2"></a>
[B](#Q4) = integralBoxFilter([A](#Q1), [filterSize](#Q2)) 使用二维框形滤波器过滤整体图像 `A`，其大小由 `filterSize` 指定。参数的 `hsize` 应为由正奇数组成的2维行向量，且值需相等。  
<a id="function3"></a>
[B](#Q4) = integralBoxFilter(___, ["NormalizationFactor", normFactor](#Q3)) 还指定应用于框形滤波器的标准化因子。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 要过滤的整体图像**  
数字数组

要过滤的整数图像，指定为任何维度的数值数组。
整形图像必须是直立的 — `integralBoxFilter` 不支持旋转的整形图像。假定整数图像的第一行和第一列是零填充的，由 `integralImage` 返回。

**数据类型：**  `double`

**<a id="Q2"></a> filterSize — 方框滤波器的大小**  
3（默认）| 正奇整数 | 正奇整数的 2 元素向量

框过滤器的大小，指定为正奇整数或正奇整数的 2 元素向量。如果 `filterSize` 是标量，则 `integralBoxFilter` 使用方框过滤器。

**<a id="Q3"></a> normFactor — 应用于框滤波器的归一化因子**  
数字标量

应用于框滤波器的归一化因子，指定为数字标量。

默认情况下，当 `filterSize` 为标量时，归一化因子的值为 1/filterSize.^2，当 `filterSize` 为向量时，值为 1/prod（filterSize）。默认值具有均值滤波器的效果 — 输出图像中的像素是图像的局部均值。
若要获取局部区域总和，请将 `normFactor` 设置为 1。为避免在这种情况下溢出，请考虑通过将输入图像转换为数据类型 `double` 来使用双精度图像。

### 输出参数
**<a id="Q4"></a> B — 过滤后的图像**  
数字数组

过滤后的图像，作为数字数组返回。`integralBoxFilter` 仅返回计算的不带填充的过滤部分。

**数据类型：**  `double`

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imboxfilt/imboxfilt.html">imboxfilt</a> | <a 
href="../integralImage/integralImage.html">integralImage</a> 
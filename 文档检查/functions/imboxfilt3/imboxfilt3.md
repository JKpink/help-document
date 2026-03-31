## imboxfilt3
3维图像的3维框滤波

## 简介
[ `B = imboxfilt3(A)`](#function1)  
[ `B = imboxfilt3(A, filterSize)`](#function2)  
[ `B = imboxfilt3(___, Name, Value)`](#function3)

## 用法
<a id="function1"></a>
[B](#Q4) = imboxfilt([A](#Q1)) 使用3维、3×3×3 的框滤波器对图像 `A` 进行滤波。框滤波器也称为均值滤波器。  
<a id="function2"></a>
[B](#Q4)  = imboxfilt([A](#Q1), [filterSize](#Q2)) 使用大小由 `filterSize` 指定的 3-D 框过滤器过滤图像 `A`。  
<a id="function3"></a>
[B](#Q4) = imboxfilt(__, [Name, Value](#Q3)) 使用名称 — 值对参数来控制滤波的各个方面。代码支持NormalizationFactor选项。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 要过滤的图像**  
3维数字数组

要过滤的图像，指定为 3-D 数字数组。
如果 `A` 包含 `Infs` 或 `NaN`，则 `imboxfilt3` 的行为未定义。当使用基于图像的积分过滤时，可能会发生这种情况。若要限制 `Inf` 和 `NaN` 在输出中的传播，请考虑改用 <a href="../imfilter/imfilter.html">imfilter</a>。

**数据类型:** `uint8`

**<a id="Q2"></a> filterSize — 框过滤器的大小**  
3 (默认) | 正奇整数 | 正奇整数的 3 元素向量

框滤波器的大小，指定为正奇整数或正奇整数的 3 元素向量。如果 `filterSize` 是标量，则框过滤器是多维数据。

**数据类型:**   `uint8`

**<a id="Q3"></a> 名称 — 值参数**  
将可选的参量对组指定为 Name1, Value1, ..., NameN, ValueN，其中 Name 是参量名称，Value 是对应的值。名称 — 值参量必须出现在其他参量之后，但参量对组的顺序无关紧要。

**NormalizationFactor — 应用于框过滤器的归一化因子**  
数字标量

应用于框滤波器的归一化因子，指定为数字标量。
`NormalizationFactor` 的默认值取决于 `filterSize`。  
当`filterSize` 是标量时，默认值为 1/filterSize.^2。  
当 `filterSize` 是 2 元素向量时，默认值为 1/prod(filterSize)。  
默认的 `NormalizationFactor` 具有均值滤波器的效果 — 输出图像中的像素是图像在由 `filterSize` 确定的邻域上的局部均值。要获取局部区域总和，请将 `NormalizationFactor` 设置为 1。

**例子：** 'NormalizationFactor',1

**数据类型:**   `uint8`

### 输出参数
**<a id="Q4"></a> B — 过滤后的图像**  
3维数字数组

过滤后的图像，作为与输入图像 [A](#Q1) 大小相同的数组返回。

**数据类型:**  `uint8`

## 算法
`imboxfilt` 使用基于卷积的过滤或积分图像过滤执行过滤，使用内部启发式方法来确定使用哪种过滤方法。

## 版本历史

在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../imboxfilt/imboxfilt.html">imboxfilt</a> | <a 
href="../imfilter/imfilter.html">imfilter</a> | <a 
href="../integralBoxFilter3/integralBoxFilter3.html">integralBoxFilter3</a> 

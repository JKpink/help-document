## imquantize
使用指定的量化级别和输出值量化图像

## 简介
[ `quant_A = imquantize(A, levels)`](#function1)  
[ `quant_A = imquantize(A, levels, values)`](#function2)  
<!-- [`[quant_A, index] = imquantize(___)`](#function3) -->
## 用法
<a id="function1"></a>
[quant_A](#P1) = imquantize([A](#Q1), [levels](#Q2)) 使用N元向量 `levels` 中指定的量化值对图像 `A` 进行量化。量化后的图像 `quant_A` 与 `A` 尺寸相同，其像素值为范围在 1 至 N+1 的 N+1 个离散整数。各整数值的确定标准如下：

- 如果 A(k) ≤ levels(1)，则 quant_A(k) = 1。
- 如果 levels(m-1) < A(k) ≤ levels(m)，则 quant_A(k) = m。
- 如果 A(k) > levels(N)，则 quant_A(k) = N+1。

<a id="function2"></a>
[quant_A](#P1) = imquantize([A](#Q1), [levels](#Q2), [values](#Q3)) 指定分配给像素的量化值：

- 如果 A(k) ≤ levels(1)，则 quant_A(k) = values(1)。
- 如果 levels(m-1) < A(k) ≤ levels(m)，则 quant_A(k) = values(m)。
- 如果 A(k) > levels(N)，则 quant_A(k) = values(N+1)。

<!-- <a id="function3"></a>
[[quant_A](#P1), [index](#P2)] = imquantize(___) 返回一个数组 index，使得：quant_A = values(index)。 -->

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 输入图像**  
数值数组

输入图像，指定为任意维度的数值数组。

**<a id="Q2"></a> levels — 量化级别**  
数值向量

量化级别，指定为长度为 N 的数值向量。离散量化级别的值必须按单调递增顺序排列。

**<a id="Q3"></a> values — 量化值**  
数值向量

量化值，指定为长度为 N+1 的数值向量。

### 输出参数
**<a id="P1"></a> quant_A — 量化图像**  
数值数组

量化图像，返回为与输入图像 [A](#Q1) 大小相同的数值数组。如果指定了输入参数 [values](#Q3)，则 `quant_A` 的数据类型与 `values` 相同。否则，`quant_A` 的数据类型为 `double`。

<!-- **<a id="P2"></a> index — 映射数组**  
数值数组

映射数组，返回为与输入图像 [A](#Q1) 大小相同的数值数组。该数组包含整数索引，用于访问  [values](#Q3) 中的值以生成输出图像：[quant_A](#P1) = values(index)。如果未指定输入参数 `values`，则 `index` 与 `quant_A` 相同。

**数据类型：**`double` -->

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../multithresh/multithresh.html">multithresh</a> | <a 
href="../label2rgb/label2rgb.html">label2rgb</a> | <a 
href="../rgb2ind/rgb2ind.html">rgb2ind</a> 
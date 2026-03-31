## mat2gray
将矩阵转换为灰度图像

## 简介
[`I = mat2gray(A, [amin amax])`](#function1)  
[`I = mat2gray(A)`](#function2)  

## 用法
<a id="function1"></a>
[I](#P1) = mat2gray([A](#Q1), [[amin amax]](#Q2)) 将矩阵 `A` 转换为灰度图像 `I`，该图像包含 0（黑色）到 1（白色）范围内的值。`amin` 和 `amax` 是 `A` 中对应于 `I` 中 0 和 1 的值。小于 `amin` 的值裁剪到 0，大于 `amax` 的值裁剪到 1。  
<a id="function2"></a>
[I](#P1) = mat2gray([A](#Q1)) 将 `amin` 和 `amax` 的值设置为 `A` 中的最小值和最大值。  

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 输入图像**  
数值矩阵

输入图像，指定为数值矩阵。

**<a id="Q2"></a> [amin amax] — 灰度映射阈值**  
二元素数值向量  

灰度映射阈值，指定为包含两个数值的一维向量，用于定义矩阵 A 到灰度图像 I 的数值映射范围：  

- 输入图像 `A` 中小于或等于 amin 的值映射到灰度图像 `I` 中的值 0。
- `A` 中大于或等于 amax 的值映射到 `I` 中的值 1。

### 输出参数
**<a id="P1"></a> I — 输出灰度图像**  
数值矩阵  

灰度图像，以 [0, 1] 范围内的值组成的数值矩阵形式返回。  

**数据类型：** `double`

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../rescale/rescale.html">rescale</a> | <a
href="../gray2ind/gray2ind.html">gray2ind</a> | <a 
href="../ind2gray/ind2gray.html">ind2gray</a> | <a 
href="../im2gray/im2gray.html">im2gray </a>

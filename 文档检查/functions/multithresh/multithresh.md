## multithresh
基于大津法（Otsu’s method）的多级别图像阈值计算

## 简介
[`thresh = multithresh(A)`](#function1)  
[`thresh = multithresh(A, N)`](#function2)

## 用法
<a id="function1"></a>
[thresh](#Q1) = multithresh([A](#Q2)) 采用大津法计算图像 `A` 的单阈值，可结合 `imquantize` 将图像分割为 2 个灰度级。

<a id="function2"></a>
[thresh](#Q1) = multithresh([A](#Q2), [N](#Q3))  计算 `N` 个阈值（返回 1×N 向量），结合 `imquantize` 可将图像分割为 `N+1` 个灰度级。

## 参数说明
### 输入参数
**<a id="Q2"></a> A —— 待阈值的图像**  
数值数组

待处理图像：任意维度的数值数组（支持灰度、RGB、多维体数据）。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` 

**<a id="Q3"></a> N — 阈值数量**  
1(默认) | [1,20] 之间的整数。

需计算的阈值个数：

- N=1：单阈值（分割为 2 级）；
- N>2：采用搜索优化大津准则，仅保证局部最优，建议 N<10；
- 若 N≥图像唯一灰度级数，无有效解，返回警告 + 任意阈值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` 

### 输出参量
**<a id="Q1"></a> thresh — 阈值集合**  
1xN 的数值向量

阈值结果：与输入图像同数据类型，范围与输入图像一致（非归一化）。

- 若输入为 RGB 图像，基于全通道聚合直方图计算；
- 若 N≥图像唯一灰度级数，返回图像所有唯一值 + 任意补充值。

## 算法  
1. **直方图计算**：基于图像全局聚合直方图（RGB 图像合并 3 通道计算），范围为`[min(A(:)) max(A(:))]`；
2. **大津准则**：最大化类间方差，N>2 时采用搜索优化（局部最优）。

## 参考
Otsu N. A threshold selection method from gray-level histograms. IEEE Transactions on Systems, Man, and Cybernetics, 1979, 9(1): 62-66.

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../graythresh/graythresh.html">graythresh</a> | <a 
href="../imquantize/imquantize.html">imquantize</a> | <a 
href="../imbinarize/imbinarize.html">imbinarize</a> | <a 
href="../rgb2ind/rgb2ind.html">rgb2ind</a> 

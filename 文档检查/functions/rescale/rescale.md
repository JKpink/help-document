## dip::rescale
缩放数组元素的取值范围

## 简介
[`R = dip::rescale(A)`](#function1)  
[`R = dip::rescale(A, [l, u])`](#function2)  

## 用法
<a id="function1"></a>
R = dip::rescale([A](#Q1)) 将数组 `A` 的所有元素线性缩放到默认区间 [0, 1]，缩放依据是 `A` 中所有元素的全局最小值和最大值，输出数组 `R` 与 `A` 尺寸相同。

<a id="function2"></a>
R = dip::rescale([A](#Q1), [[l](#Q2), [u](#Q3)]) 指定目标缩放区间为 `[l, u]`（`l` 为下界，`u` 为上界，需满足 `l < u`），将 `A` 缩放到该区间。


## 参数说明
### 输入参数
**<a id="Q1"></a> A — 输入数组**  
向量 | 矩阵 | 多维数组

待缩放的输入数组：

- 数据类型：支持数值型（`single`/`double`/ 整数型），若为 `single` 则输出也为 `single`，否则为 `double`；
- 特殊情况：若 `A` 为常数数组，输出为目标区间下界（默认 0）；若目标区间含 `Inf`，输出 `NaN`。

**数据类型**：single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64

**<a id="Q2"></a> l — 下界**  
0 (默认) | 标量 | 向量 | 矩阵 | 多维数组

缩放后数组的下界，需满足 `l < u`，尺寸需与 `A` 兼容：

- 标量：所有元素使用同一下界；
- 行 / 列向量：为每列 / 每行指定不同下界（如 `l = [0 -1]` 为两列分别指定下界 0 和 - 1）。

**数据类型**：single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64

**<a id="Q3"></a> u — 上界**  
1 (默认) | 标量 | 向量 | 矩阵 | 多维数组

缩放后数组的上界，需满足 `u > l`，尺寸规则同 `l`：

- 标量：所有元素使用同一上界；
- 行 / 列向量：为每列 / 每行指定不同上界。

**数据类型**：single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64

## 名称值-参数

##### `InputMin` — 输入范围下界

标量 | 多维数组输入范围的下界，替代默认的 `min(A(:))`，超出该值的元素会被裁剪到 `InputMin` 后再缩放：

- 标量：全局所有元素使用同一输入下界；

**数据类型**：single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64

##### `InputMax` — 输入范围上界

标量 | 多维数组输入范围的上界，替代默认的 `max(A(:))`，超出该值的元素会被裁剪到 `InputMax` 后再缩放：

- 标量：全局所有元素使用同一输入上界；

**数据类型**：single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64

## 核心公式

$$
R = l + \frac{A - \text{InputMin}}{\text{InputMax} - \text{InputMin}} \times (u - l)
$$

- 未指定 `InputMin`/`InputMax` 时，默认取 `InputMin = min(A(:))`、`InputMax = max(A(:))`；
- 若 `A` 中元素超出 `[InputMin, InputMax]`，会先被裁剪到该范围再缩放。

## 版本历史

在北太天元图像处理工具箱 V1.0 推出

## 相关主题
 <a href="../bounds/bounds.html">bounds</a> | <a 
href="../max/max.html">max</a> | <a 
href="../min/min.html">min</a> | <a 
href="../normalize/normalize.html">normalize</a> | <a 
href="../clip/clip.html">clip</a> 
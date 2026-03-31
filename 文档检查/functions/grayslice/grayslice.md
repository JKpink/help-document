## grayslice
使用多级阈值分割将灰度图像转换为索引图像

## 简介
[`X = grayslice(I, N)`](#function1)  
[`X = grayslice(I, thresholds)`](#function2)

## 用法
<a id="function1"></a>
[X](#P1) = grayslice([I](#Q1), [N](#Q2)) 使用多级阈值分割将灰度图像转换为索引图像。函数会根据阈值个数 N 自动计算阈值。

<a id="function2"></a>
[X](#P1) = grayslice([I](#Q1), [thresholds](#Q3)) 使用用户指定的一组阈值对输入图像进行多级阈值分割，并返回相应的索引图像。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入灰度图像**  
m×n 数值数组

输入灰度图像，指定为 m×n 的数值矩阵。对于数据类型为 `double` 或 `single` 的图像，grayslice 要求其像素值位于 [0, 1] 范围内。若 I 的取值超出 [0, 1]，可使用 <a href="../rescale/rescale.html">rescale</a> 函数将其线性缩放到期望范围。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `int16`

**<a id="Q2"></a> N — 阈值数量**  
正标量

阈值数量，指定为正标量。该值表示用于多级阈值分割的阈值总数。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `int16`

**<a id="Q3"></a> thresholds — 阈值集合**  
数值向量

阈值集合，指定为数值向量。用于多级阈值分割的阈值数量等于阈值集合的长度。

| 图像数据类型 | 阈值范围 |
| :----------- | :----------- |
| uint8 | [0, 255] |
| int16 或 uint16 | [0, 65535] |
| single 或 double | [0, 1] |

**数据类型：** `double` | `uint8` 

### 输出参数
**<a id="P1"></a> X — 索引图像**  
m×n 矩阵

输出索引图像，返回为与输入灰度图像尺寸相同的 m×n 矩阵。X 的数据类型取决于多级阈值分割所使用的阈值数量：
- 当阈值数量小于 256 时，X 的数据类型为 `uint8`。此时，X 的取值范围为 [0, N]或 [0, length(thresholds)]。
- 当阈值数量大于或等于 256 时，X 的数据类型为 `double`。此时，X 的取值范围为 [1, N+1]或 [1, length(thresholds)+1]。

**数据类型：** `uint8` | `double`

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../gray2ind/gray2ind.html">gray2ind</a>

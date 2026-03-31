## graycoprops  
根据灰度共生矩阵计算特征

## 简介  
[ `stats = graycoprops(glcm, properties)`](#function1)

## 用法  
<a id="function1"></a>
[stats](#Q1) = graycoprops([glcm](#Q2), [properties](#Q3)) 从灰度共生矩阵 (glcm) 中计算属性中指定的统计信息。

灰度共生矩阵 (GLCM) 通过 graycoprops 进行归一化，使其元素之和等于 1。归一化后的 GLCM 中每个元素 (r, c) 是图像中具有定义的空间关系且灰度值为 r 和 c 的像素对的联合概率。graycoprops 使用归一化的 GLCM 来计算属性。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>glcm — GLCM**  
非负整数矩阵 | 非负整数矩阵

灰度共生矩阵 (GLCM)，指定为以下之一:
 - 对于单个 GLCM，是一个 m×n 非负整数矩阵；
 - 对于 p 个灰度共生矩阵 (GLCM)，是一个 m×n×p 的非负整数数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q3"></a>properties — 统计属性**  
"all"（默认） | 逗号分隔的列表字符串标量或字符向量 | 字符串标量或字符向量的单元数组 | 字符串数组 | 空格分隔的字符向量

从 GLCM 派生的图像的统计属性，指定为逗号分隔的字符串标量或字符向量列表、字符串标量或字符向量的单元数组、字符串数组、空格分隔的字符向量或 “all”。您可以指定此表中列出的任何属性名称。

| **属性** | **描述** | **公式** |
|:-|:-|:-|
| "Contrast" | 返回整个图像中像素与其邻域之间强度对比的度量。<br> Range = [0 (size(GLCM,1)-1)^2]<br>对比度在恒定图像中为 0。<br>对比度属性也被称为方差和惯性。 |$\sum_{i,j} \|i-j\|^2P(i,j)$|
| "Correlation" |返回一个衡量整个图像中像素与其邻居相关程度的指标。<br>Range = [-1 1]<br>对于完全正相关或负相关的图像，其相关系数为1或-1。<br>而对于恒定图像（即所有像素值相同的图像），其相关系数则为 NaN（非数值）。|$\sum_{i,j} \frac{(i - \mu_i)(j - \mu_j) p(i,j)}{\sigma_i \sigma_j}$|
| "Energy" | 返回 GLCM 中元素平方的和。<br>Range = [0 1]<br>能量 (Energy) 在恒定图像中为 1。<br>该能量属性也被称为均匀度、能量均匀性以及角二阶矩。  | $\sum_{i,j} P(i,j)$|
| "Homogeneity" | 返回一个值，该值衡量灰度共生矩阵 (GLCM) 中元素分布与 GLCM 对角线的接近程度。<br>Range = [0 1]<br>对于对角线方向的灰度共生矩阵 (GLCM)，其同质性值为1。|$\sum_{i,j} \frac{p(i,j)}{1 + \|i-j\|}$|


**数据类型：** `char`|`string`|`cell`

### 输出参数  
**<a id="Q1"></a>stats — 从 GLCM 衍生的统计量**  
结构

从灰度共生矩阵 (GLCM) 得出的统计信息，以结构体形式返回，其中字段由  [`properties`](#Q3) 指定,每个字段包含一个 1×p 数组，p 是 [`glcm`](#Q2) 中的灰度共生矩阵数量。例如，如果 `glcm` 是一个 8×8×3 数组且属性为 “Energy”，那么 `stats` 是一个包含字段 `Energy` 的结构体，该字段包含一个 1×3 数组。

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../graycomatrix/graycomatrix.html">graycomatrix</a>

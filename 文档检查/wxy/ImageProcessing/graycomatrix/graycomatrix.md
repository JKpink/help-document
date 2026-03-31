## graycomatrix  
从图像创建灰度共生矩阵

## 简介  
[ `glcm = graycomatrix(I)`](#function1)  
[ `glcm = graycomatrix(I, Name, Value)`](#function2)  
[ `[glcm, SI] = graycomatrix(___)`](#function3)

## 用法  
<a id="function1"></a>
[glcm](#Q1) = graycomatrix([I](#Q2)) 从图像 [`I`](#Q2) 创建灰度共生矩阵 (GLCM)。灰度共生矩阵又名灰度空间相关性矩阵。
graycomatrix 通过计算灰度级（灰度强度）值为 i 的像素与灰度级值为 j 的像素水平相邻的频率来创建 GLCM 。 glcm 中的每个元素 (i, j) 指定值为 i 的像素与值为 j 的像素水平相邻的次数。
<a id="function2"></a>  
[glcm](#Q1) = graycomatrix([I](#Q2), [Name, Value](#Q3)) 根据可选名称-值参量的值，返回一个或多个灰度共生矩阵。
<a id="function3"></a>  
[[glcm](#Q1), [SI](#Q4)] = graycomatrix(___) 返回缩放后的图像 [`SI`](#Q4) ，用于计算灰度共生矩阵。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>I — 灰度图像**  
二维数值矩阵 | 二维逻辑矩阵

输入图像，指定为二维数值矩阵或二维逻辑矩阵。

### 名称-值参数  
*将可选的参量对组指定为 Name1, Value1,...,NameN ,ValueN，其中 Name 是参量名称， Value 是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。  
**示例：** glcm = graycomatrix(I, "Offset", [2 0]) 指定行偏移量为 2，列偏移量为 0。*

**<a id="Q7"></a>GrayLimits — 用于将输入图像缩放为灰度级的范围**  
二元素向量 | []

将输入图像缩放到灰度级所使用的范围，指定为 [low high] 形式的二元素向量。如果 N 是用于缩放的灰度级的数量，则范围 [low high] 划分为 N 个等宽 bin，每个 bin 中的值映射到一个灰度级，小于或等于 low 的灰度值将缩放为 1，大于或等于 high 的灰度值将缩放至 `NumLevels`。
如果 `GrayLimits` 设置为 []，则 `graycomatrix` 使用 `I` 中的最小和最大灰度值作为限值 [min(I(:)) max(I(:))]，例如，对于数据类型为 `double` 的范围为 [0, 1]，而数据类型为 `int16` 的范围为 [-32768, 32767]。

**<a id="Q5"></a>NumLevels — 灰度级的数量**  
正整数

灰度级的数量，指定为正整数。例如，如果 `NumLevels` 为 8，则 `graycomatrix` 将 `I` 中的值缩放为 1 到 8 之间的整数。灰度级的数量确定 `GLCM` 的大小。数值图像的默认灰度级的数量为 8，逻辑图像的默认灰度级的数量为 2。

**<a id="Q6"></a>Offset — 感兴趣的像素与其邻点之间的距离**  
[0 1]（默认） | 由整数组成的 p×2 矩阵

感兴趣的像素与其邻点之间的距离，指定为由整数组成的 p×2 矩阵。矩阵中的每行均为一个二元素向量，即 [row_offset, col_offset]，它指定一对像素的关系（即偏移量）。row_offset 是关注的像素与其邻点之间的行数，col_offset 是感兴趣的像素与其邻点之间的列数。
由于偏移量通常以角度表示，下表列出了在给定像素距离 D 时与常见角度对应的偏移量值：

| **角度** | **偏移量** |
|:-|:-|
| 0 | [0 D] |
| 45 |	[-D D]|
| 90 | [-D 0] |
| 135 | [-D -D] |

**Symmetric — 考虑值的顺序**  
false（默认） | true

考虑值的顺序，指定为布尔值 true 或 false。例如，当 `Symmetric` 设置为 true 时，`graycomatrix` 在计算值 1 与值 2 相邻的次数时，会将 1,2 和 2,1 对组都进行计数。当 `Symmetric` 设置为 false 时，`graycomatrix` 根据 `Offset` 的值仅对 1,2 或 2,1 对组进行计数。

**数据类型：** `logical`

### 输出参数  
**<a id="Q1"></a>glcm — 灰度共生矩阵** 
数值数组
 
灰度共生矩阵，以 [NumLevels](#Q5)×NumLevels×P 数组形式返回，其中 P 是 [`Offset`](#Q6) 中偏移量的数目。

**数据类型：** `double`

**<a id="Q4"></a>SI — 用于GLCM计算的缩放图像**  
数值矩阵

用于 `GLCM` 计算的缩放图像，以与输入图像大小相同的数值矩阵形式返回。`SI` 中的值介于 1 和 [NumLevels](#Q5) 之间。

**数据类型：** `double`

## 算法  
`graycomatrix` 根据缩放后的图像计算 `GLCM`。默认情况下，如果 `I` 是二值图像，则 `graycomatrix` 将图像缩放到两个灰度级。如果 `I` 是灰度图像，则 `graycomatrix` 将图像缩放到八个灰度级。您可以通过使用 [`NumLevels`](#Q5) 名称-值参量来指定 `graycomatrix` 用于缩放图像的灰度级的数量。您可以使用 [`GrayLimits`](#Q7) 名称-值参量来调整 graycomatrix 缩放值的方式。

如果像素对组中有任一像素包含 NaN，则 `graycomatrix` 忽略该像素对组，并用值 NumLevels 替换正的 Infs，用值 1 替换负的 Infs。如果对应的相邻像素位于图像边界之外，则 `graycomatrix` 忽略边界像素。

当 `Symmetric` 设置为 true 时创建的 `GLCM` 是关于其对角线对称的，等效于 Haralick (1973) 描述的 `GLCM` [[1]](#Q5)。在 `Symmetric` 设置为 true 时由以下语法生成的 `GLCM`
```
graycomatrix(I, Offset=[0 1], Symmetric=true)
```
等效于在 `Symmetric` 设置为 false 时由以下语句生成的两个 `GLCM` 的总和。
```
graycomatrix(I, Offset=[0 1], Symmetric=false) 
graycomatrix(I, Offset=[0 -1], Symmetric=false)
```
该算法实现与纹理特征定义同时参考计算机视觉经典教材 [[2]](#Q6)。
## 参考文献  
<a id="Q5"></a>[1] Haralick R M, Shanmugan K, Dinstein I. Textural features for image classification[J] . IEEE Transactions on Systems, Man, and Cybernetics, 1973, SMC-3: 610-621.
<a id="Q6"></a>[2] Haralick R M, Shapiro L G. Computer and Robot Vision, Volume I[M] . Addison-Wesley, 1992: 459.

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../graycoprops/graycoprops.html">graycoprops</a>
## im2col
将图像块重新排列成列

## 简介
[`B = im2col(A, [m, n])`](#function1)  
[`B = im2col(A, [m, n], blockType)`](#function1)

## 用法
**<a id="function1"></a>**
[B](#Q3) = im2col([A](#Q1), [[m, n]](#Q2))将尺寸为 `m×n` 的滑动图像邻域重新排列为列（无零填充），并将拼接后的列返回至矩阵 `B` 中。

[B](#Q3) = im2col([A](#Q1), [[m, n]](#Q2), [blockType](#Q4))还会通过 `blockType` 参数指定块为离散块（distinct）还是滑动邻域（sliding）。

对于离散块处理，`im2col` 函数会在必要时对图像 `A` 进行填充。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 图像**  
二维灰度图像 | 二维二值图像 | 2D 索引图像

图像，指定为 2-D 灰度图像、2-D 二进制图像或 2-D 索引图像。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` 

**<a id="Q2"></a> [m, n] — 块大小**  
2 元素向量

块大小，指定为 2 元素向量。m 是行数，n 是块中的列数。

**数据类型：** `double`

**<a id="Q4"></a> blockType — 块类型**  
`sliding`（默认） | `distinct`

块大小，指定为 2 元素向量。m 是行数，n 是块中的列数。

**数据类型：** `double`

### 输出参数
**<a id="Q3"></a> B — 图像块**  

数值矩阵 | 逻辑矩阵

图像块：返回为具有 `m*n` 行的数值矩阵或逻辑矩阵。列数取决于图像块是离散块还是滑动邻域。`B` 的每一列包含 `A` 的一个块或邻域，并被重塑为列向量。

- 对于离散块处理：`B` 的列数等于 `A` 中 `m×n` 块的数量。例如，若 `A` 的尺寸为 `[mm nn]`，则 `B` 有 `(mm/m)*(nn/n)` 列。
- 对于滑动邻域处理：`B` 的列数等于 `A` 中 `m×n` 邻域的数量。例如，若 `A` 的尺寸为 `[mm nn]`，则 `B` 有 `((mm-m+1)*(nn-n+1))` 列。

矩阵 `B` 中列的顺序由按列遍历图像 `A` 的方式决定。例如，若 `A` 由离散块 `Aij` 排列为 `A = [A11 A12; A21 A22]`，则 `B = [A11(:) A21(:) A12(:) A22(:)]`。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../blockproc/blockproc.html">blockproc</a> | <a 
href="../col2im/col2im.html">col2im</a> | <a 
href="../colfilt/colfilt.html">colfilt</a> | <a 
href="../nlfilter/nlfilter.html">nlfilter</a> | <a 
href="../reshape/reshape.html">reshape</a>




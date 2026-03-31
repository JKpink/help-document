# colfilt

按列执行邻域运算

## 简介
[`B = colfilt(A,[m n], block_type, fun)`](#function1)

## 用法
<a id="function1"></a>

[BW]() = bwunpack([BWP](), [m]())：将打包后的二值图像 `BWP` 解包为具有 `m` 行的二值图像 `BW`。

[B]() = colfilt([A](#Q2), [[m n]](#Q3), [block_type](#Q4), [fun](#Q5)) 对图像 `A` 进行处理，先将 `A` 中每个 `m×n` 的块重排为临时矩阵的一列，再对该矩阵应用函数 `fun`。必要时，`colfilt` 会对 `A` 进行零填充。

## 参数说明
### 输入参数
**<a id="Q2"></a> A — 输入图像**

数组

输入图像，指定为函数 `fun` 支持的任意数据类型的数组。

**<a id="Q3"></a> [m n] — 块尺寸**

由正整数组成的二元向量

块尺寸，指定为由正整数组成的二元向量。其中 `m` 表示块的行数，`n` 表示块的列数。

**<a id="Q4"></a> block_type — 块类型**

'sliding'   |   'distinct'

块类型，指定为 `'sliding'`（滑动邻域）或 `'distinct'`（独立块）。

**数据类型**：`char` | `string`

**<a id="Q5"></a> fun — 函数句柄**

函数句柄

函数句柄，指定为一个函数句柄。该函数的输入和输出参数取决于 `block_type` 的取值。

### 输出参数
**<a id="Q5"></a> B — 滤波后的图像**  

数值矩阵

滤波后的图像，以数值矩阵形式返回。

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
 <a href="../blockproc/blockproc.html">blockproc</a> | <a 
href="../col2im/col2im.html">col2im</a> | <a 
href="../im2col/im2col.html">im2col</a> | <a 
href="../nlfilter/nlfilter.html">nlfilter</a>


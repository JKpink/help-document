## col2im
将矩阵列重新排列为块形式

## 简介
[`A = col2im(B,[m n],[M N])`](#function1)  
[`A = col2im(B,[m n],[M N], 'sliding')`](#function1)  
[`A = col2im(B,[m n],[M N], 'distinct')`](#function2)

## 用法
<a id="function1"></a>

[A](#Q4) = col2im([B](#Q1), [[m n]](#Q2), [[M N]](#Q3)) 或

[A](#Q4) = col2im([B](#Q1), [[m n]](#Q2), [[M N]](#Q3), 'sliding')：将行向量 `B` 重新排列为 `m` 行 `n` 列的邻域，生成尺寸为 `(M-m+1)` 行 `(N-n+1)` 列的矩阵 `A` 。

行向量 `B` 通常是对 `im2col(..., 'sliding')` 的输出结果，通过列压缩函数（如 `sum` 函数）处理后得到的结果。

<a id="function2"></a>

[A](#Q4) = col2im([B](#Q1), [[m n]](#Q2), [[M N]](#Q3), 'distinct')：将矩阵 `B` 的每一列重新排列为一个独立的 `m` 行 `n` 列块，生成尺寸为 `M` 行 `N` 列的矩阵 `A` 。

例如，若 `B` 由长度为 `m*n` 的列向量 `Bi(:)` 构成，且排列形式为 `B = [B1(:) B2(:) B3(:) B4(:)]`，则 `A = [B1 B3; B2 B4]`（其中每个块 `Bi` 的尺寸均为 `m` 行 `n` 列）。

## 参数说明
### 输入参数
**<a id="Q1"></a> B — 图像块**  
矩阵 | 行向量

图像块，指定为以下值之一：
- 对于独立块处理：`B` 为包含 `m*n` 行的数值型或逻辑型矩阵，每一列对应一个块。 
- 对于滑动邻域处理：`B` 为尺寸为 `1×[(M-m+1)×(N-n+1)]` 的数值型或逻辑型行向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` |`logical`|`uint32` | `uint64`

**<a id="Q2"></a> [m, n] — 块尺寸**  
由正整数组成的二元向量

块尺寸，指定为由正整数组成的二元向量。其中： `m` 为每个块的行数，`n` 为每个块的列数。`m×n` 必须等于 `B` 的行数。

**数据类型：**  `double`  

**<a id="Q3"></a> [M, N] — 图像大小**  
由正整数组成的二元向量

图像尺寸：指定为由正整数组成的二元向量。其中：`M` 为图像的行数，`N` 为图像的列数。

**数据类型：**  `double`  

### 输出参数
**<a id="Q4"></a> A — 重构后的图像**  
数值矩阵

重构后的图像：对于独立块处理，返回为尺寸为 `M×N` 的数值型矩阵；对于滑动块处理，返回为尺寸为 `(M-m+1)×(N-n+1)` 的数值型矩阵。`A` 与 `B` 的数据类型相同。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a 
href="../colfilt/colfilt.html">colfilt</a> | <a 
href="../im2col/im2col.html">im2col</a> | <a 
href="../nlfilter/nlfilter.html">nlfilter</a> | <a 
href="../reshape/reshape.html">reshape</a>


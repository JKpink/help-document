## qtdecomp
四叉树分解

## 简介
[`S = qtdecomp(I)`](#function1)  
[`S = qtdecomp(I, threshold)`](#function2)  
[`S = qtdecomp(I, threshold, mindim)`](#function3)  
[`S = qtdecomp(I, threshold, [mindim maxdim])`](#function4)  

## 用法
<a id="function1"></a>
[S](#P1) = qtdecomp([I](#Q1)) 对灰度图像 `I` 执行四叉树分解，并在稀疏矩阵 `S` 中返回四叉树结构。默认情况下，仅当块内所有元素相等时才停止分裂。

<a id="function2"></a>
[S](#P1) = qtdecomp([I](#Q1), [threshold](#Q2)) 当块内元素最大值与最小值之差大于 `threshold` 时，对该块进行分裂。

<a id="function3"></a>
[S](#P1) = qtdecomp([I](#Q1), [threshold](#Q2), [mindim](#Q3)) 阻止产生小于 `mindim` 的块，即使这些块不满足阈值条件也不再进一步分裂。

<a id="function4"></a>
[S](#P1) = qtdecomp([I](#Q1), [threshold](#Q2), [[mindim](#Q3) [maxdim](#Q4)]) 阻止产生小于 `mindim` 或大于 `maxdim` 的块。大于 `maxdim` 的块即使满足阈值条件也会被分裂。

## 参数说明
### 输入参数

**<a id="Q1"></a> I — 灰度图像**  
`m`×`n` 数值矩阵

灰度图像，指定为 `m`×`n` 数值矩阵。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` | `logical`

**<a id="Q2"></a> threshold — 块同质性阈值**  
[0, 1] 范围内的数值

块同质性阈值，指定为 [0, 1] 范围内的数值。若 `I` 的数据类型为 `uint8`，则 `qtdecomp` 将 `threshold` 乘以 255 得到实际使用的阈值；若 `I` 的数据类型为 `uint16`，则乘以 65535。

**<a id="Q3"></a> mindim — 最小块尺寸**  
正整数

最小块尺寸，指定为正整数。`mindim` 必须为图像尺寸的因子。

**<a id="Q4"></a> maxdim — 最大块尺寸**  
正整数

最大块尺寸，指定为正整数。`maxdim/mindim` 必须为 2 的幂。

### 输出参数

**<a id="P1"></a> S — 四叉树结构**  
稀疏矩阵

四叉树结构，以稀疏矩阵形式返回。若 `S(k,m)` 非零，则 `(k,m)` 为分解中一个块的左上角坐标，块的大小由 `S(k,m)` 给出。

**数据类型：** `double`

## 提示
- `qtdecomp` 主要适用于尺寸为 2 的幂的方形图像，如 128×128 或 512×512。这类图像可以一直划分至 1×1 块。若图像尺寸不是 2 的幂，则划分到某一步后无法继续分裂。例如，96×96 图像可划分为 48×48、24×24、12×12、6×6，最后为 3×3 块，无法进一步划分。处理此类图像时，需将 `mindim` 设为 3（或 3 乘以 2 的幂）；若使用包含函数句柄的语法，函数需在块无法继续分裂时返回 0。

## 算法
`qtdecomp` 将方形图像划分为四个大小相等的方形块，然后测试每个块是否满足某种同质性准则。若块满足准则，则不再分裂；若不满足，则将其进一步细分为四个子块，并对子块重复测试。该过程迭代进行，直至每个块均满足准则。结果中包含多种不同大小的块。

## 版本历史
在北太天元图像处理工具箱 V3.0 推出  

## 相关主题
<a href="../qtgetblk/qtgetblk.html">qtgetblk</a> | <a href="../qtsetblk/qtsetblk.html">qtsetblk</a>
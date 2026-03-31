## bestblk
确定块处理的最优块尺寸

## 简介
[`siz = bestblk([M N],k)`](#function1)  
[`[m,n] = bestblk([M N],k)`](#function2)

## 用法
<a id="function1"></a>

[siz](#Q4) = bestblk([[M N]](#Q2), [k](#Q3)) 返回针对 M 行 N 列图像进行块处理的最优块尺寸。该最优块尺寸可最大限度减少外围不完整块所需的填充操作。参数 `k` 用于指定块的最大行维度和列维度。

<a id="function2"></a>

[[m, n]](#Q5) = bestblk([[M N]](#Q2), [k](#Q3)) 分别在 `m` 和 `n` 中返回该块的行维度和列维度。

## 参数说明
### 输入参数
**<a id="Q2"></a> [m, n] — 块大小**  
正整数的 2 元素向量

块大小，指定为正整数的 2 元素向量。m 是行数，n 是每个块中的列数。`m×n` 必须等于 `B` 的行数。

**数据类型：**  `double`  

**<a id="Q3"></a> k — 块的最大行数或列数**  
正整数

块的最大行数或列数，指定为一个正整数（默认为100）。

**数据类型：**  `double`  

### 输出参数
**<a id="Q4"></a> six — 最优块尺寸**  
二维数值行向量

最优块尺寸，以二维数值行向量的形式返回。`siz` 等价于 `[m n]`。

**<a id="Q5"></a> [m,n] — 块的最优行数或列数**  
数值标量

块的最优行数或列数，以数值标量的形式返回。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../blockproc/blockproc.html">blockproc</a> | <a 
href="../colfilt/colfilt.html">colfilt</a> | <a 
href="../im2col/im2col.html">im2col</a> | <a 
href="../nlfilter/nlfilter.html">nlfilter</a>


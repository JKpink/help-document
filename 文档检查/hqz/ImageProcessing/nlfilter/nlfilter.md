## nlfilter
通用滑动邻域运算

## 简介
[`B = nlfilter(A, [m n], fun)`](#function1)

## 用法
<a id="function1"></a>

[B](#Q1) = nlfilter([A](#Q2), [[m n]](#Q3), [fun](#Q4)) 对灰度图像 `A` 的每个 `m×n` 滑动块应用函数 `fun` 。

### 注意
`nlfilter` 处理大图像时可能耗时较长。在某些情况下，`colfilt` 函数可以快得多地执行相同操作。

## 参数说明
### 输入参数
**<a id="Q2"></a> A — 待滤波图像**  
数值数组  

待滤波的图像，指定为 `fun` 支持的任意类别的数值数组。当 `A` 为灰度图像时，可为任意数值类型或逻辑类型；当 `A` 为索引图像时，可为 `logical`、`uint8`、`uint16`、`single` 或 `double` 类型。  

**数据类型：**  `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`  

**<a id="Q3"></a> [m n] — 块大小**  
正整数的 2 元素向量  

块大小，指定为正整数的 2 元素向量。m 是块中的行数，n 是块中的列数。  

**数据类型：** `single` | `double` | `logical`  

**<a id="Q4"></a> fun — 函数句柄**  
句柄  

指定为句柄的函数句柄。该函数必须接受一个 `m×n` 矩阵作为输入，并返回一个标量结果。  

$$
c = fun(x)
$$
`c` 是 `m×n` 块 `x` 中中心像素的输出值。`nlfilter` 会对 `A` 中的每个像素调用 `fun`。必要时，`nlfilter` 会在边缘对 `m×n` 块进行零填充。  

**数据类型：** `function_handle`  

### 输出参数
**<a id="Q1"></a> B — 滤波后的图像**  
数值数组  

滤波后的图像，以数值数组形式返回。`B` 的类型取决于 `fun` 输出的类型。  

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
 <a href="../blockproc/blockproc.html">blockproc</a> | <a href="../colfilt/colfilt.html">colfilt</a>
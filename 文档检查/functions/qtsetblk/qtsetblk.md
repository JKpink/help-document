## qtsetblk
设置四叉树分解中块的值

## 简介
[`J = qtsetblk(I, S, dim, vals)`](#functionQ1)

## 用法
[J](#Q5) = qtsetblk([I](#Q1), [S](#Q2), [dim](#Q3), [vals](#Q4))  根据四叉树结构 `S`，将图像 `I` 中所有尺寸为 `dim×dim` 的图像块替换成 `vals` 中对应的块。

## 参数说明
### 输入参数
**<a id="Q1"></a> I —— 灰度图像**
数值矩阵

灰度图像，被指定为数值矩阵。

**数据类型：**`single` | `double` | `int16` | `uint8` | `uint16` | `logical` 

**<a id="Q2"></a> S —— 四叉树结构**
稀疏矩阵

四叉树结构，被指定为一个稀疏矩阵。若` S(m,n)` 非零，则坐标 `(m,n)` 为分解中某个块的左上角，该块的大小由 `S(m,n)` 的数值给出。可通过<a href="../qtdecomp/qtdecomp.html">qtdecomp</a>函数获得此四叉树结构。

**数据类型：**`double`

**<a id="Q3"></a> dim —— 块大小**
正整数

块大小，被指定为正整数。

**<a id="Q4"></a> vals —— 块值**
(dim,dim,k)数组

块值,被指定为 `(dim,dim,k)` 数组，其中 `k` 为四叉树分解中 `dim×dim` 尺寸块的数量。

 `vals` 中块的排列顺序必须与图像 `I` 中块的列优先顺序保持一致。例如，如果 `vals` 为 `(6×6×2)` 数组，则 `vals(:,:,1)` 包含用于替换图像 `I` 中首个 `6×6` 子块的数值，`vals(:,:,2)` 包含用于替换图像 `I` 中第二个 `6×6` 子块的数值。

### 输出参数

**<a id="Q5"></a> J —— 替换后的灰度图像**
数值矩阵

替换指定尺寸子块后的灰度图像，返回为与 `I` 同尺寸、同数据类型的数值矩阵。

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../qtdecomp/qtdecomp.html">qtdecomp</a> | <a href="../qtgetblk/qtgetblk.html">qtgetblk</a>


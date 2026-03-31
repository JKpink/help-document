# size
获取图像大小（重载）

## 简介
[ `sz = size(A)`](#function1)  
[ `szdim = size(A, dim)`](#function2)  
[ `szdim = size(A, dim1, dim2, ... , dimN)`](#function3)  
[ `[sz1, ... , szN] = size(___)`](#function4)
## 用法
<a id="function1"></a>
[sz](#P1) = size([A](#Q1)) 返回输入数组各维尺寸构成的行向量。对于 M×N 矩阵，返回 [M, N]；对于表或时间表，返回的二元向量分别表示观测值（行）数量与变量（列）数量。  
<a id="function2"></a>
[szdim](#P2) = size([A](#Q1), [dim](#Q2)) 当 `dim` 为正整数标量时，函数返回数组 `A` 在第 `dim` 维上的长度。`dim` 亦可指定为正整数向量，此时函数将返回一个行向量，其元素依次为 `A` 在 `dim` 中各指定维度上的长度。例如，size(A, [2 3]) 返回的向量包含 `A` 第二维与第三维的长度。  
<a id="function3"></a>
[szdim](#P2) = size([A](#Q1), [dim1, dim2, ... , dimN](#Q3)) 以行向量形式返回维度 dim1, dim2, ... , dimN 的长度。  
<a id="function4"></a>
[[sz1, ... , szN](#P3)] = size(___) 分别返回输入数组的查询维度的长度。 

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 输入数组**  
标量 | 向量 | 矩阵 | 多维数组

输入数组，指定为标量、向量、矩阵或多维数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical` 

**复数支持: 是**

**<a id="Q2"></a> dim — 查询的维度**  
正整数标量 | 由正整数标量组成的向量 | 空数组

查询的维度，指定为正整数标量、由正整数标量组成的向量或大小为 0×0、0×1 或 1×0 的空数组。若 `dim` 的元素大于 ndims(A)，函数在对应的输出元素中返回 1。若 `dim` 为空数组，函数返回维度为 1×0 的空行向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q3"></a> dim1, dim2, ... , dimN — 查询的维度列表**   
正整数标量

查询的维度列表，指定为正整数标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出参数
**<a id="P1"></a> sz — 数组大小**  
由非负整数组成的行向量

数组大小，以非负整数组成的行向量形式返回。

- `sz` 的每个元素表示 `A` 的对应维度的长度。如果 `sz` 的任一元素等于 0，则 `A` 是空数组。
- 如果 `A` 是标量，则 `sz` 为行向量 [1 1]。
- 如果 `A` 是表或时间表，则 `sz` 是 [行数  变量数]（变量内部的列不计入维度统计）。
- 如果 `A` 是字符向量， 对于`char` 类型, `size` 返回行向量 [1 M]，其中 M 是字符数。对于字符串标量，`size` 返回 [1 1]，因为它是字符串数组的单个元素。例如，比较字符向量和字符串的 `size` 的输出：  
``` 
szchar = size('mytext')  
```
szchar =  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6  
``` 
szstr = size("mytext")  
```
szstr =  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1    
<!-- 要计算字符串中的字符数量，请使用 <a href="../strlength/strlength.html">strlength</a> 函数。 -->

**数据类型：** `double`

**<a id="P2"></a> szdim — 维度长度**  
非负整数标量 | 由非负整数标量组成的向量 | 1×0 空数组

维度长度，当 `dim` 是正整数标量时返回非负整数标量，当 `dim` 是正整数向量时返回由非负整数标量组成的行向量，当 `dim` 是空数组时返回 1×0 空数组。如果指定维度参量的元素大于 ndims(A)，则 `size` 在 `szdim` 的对应元素中返回 1。

**数据类型：** `double`  

**<a id="P3"></a> sz1, ... , szN — 维度长度**  
非负整数标量

分别列出的维度长度，以逗号分隔的非负整数标量形式返回。

- 当不指定 `dim` 且输出参数数量 `n` 小于 ndims(A) 时，前 `n-1` 个参数依次接收对应维度的长度，第 `n` 个参数接收剩余所有维度长度的乘积。例如，三维数组 `A` 是 [2 4 6]，则 [sz1, sz2] = size(A) 返回 sz1 = 2 和 sz2 = 48。
- 当指定 `dim` 时，输出参量的数量必须等于查询维度的数量。
- 若输出参量多于 ndims(A) 个，则多余的尾部参量将以 1 的形式返回。

**数据类型：** `double`

<!-- ## 提示
- 要确定数组是否为空、标量或矩阵，请使用函数 <a href="../isempty/isempty.html">isempty</a>、<a href="../isscalar/isscalar.html">isscalar</a> 和 <a href="../ismatrix/ismatrix.html">ismatrix</a>。您还可以使用 <a href="../isrow/isrow.html">isrow</a> 和 <a href="../iscolumn/iscolumn.html">iscolumn</a> 函数确定向量的方向。 -->

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../length/length.html">length</a> 
<!-- | <a 
href="../strlength/strlength.html">strlength</a> | <a 
href="../ndims/ndims.html">ndims</a> | <a 
href="../numel/numel.html">numel</a> | <a 
href="../height/height.html">height</a> | <a 
href="../width/width.html">width</a>  -->
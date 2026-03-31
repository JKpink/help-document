## maketform  
创建N维几何变换结构  
  
## 简介  
[` T = maketform("affine", A)`](#function1)  
[` T = maketform("projective", P)`](#function2)  
[` T = maketform("custom", ndims_in, ndims_out, forward_fcn, inverse_fcn, tdata)`](#function3)  
[` T = maketform("box", tsize, outCornerStart, outCornerEnd)`](#function4)  
[` T = maketform("box", inCorners, outCorners)`](#function5)  
[` T = maketform("composite", T1, T2, ..., TL)`](#function6)  
[` T = maketform("composite", [T1, T2, ..., TL])`](#function7)  
  
## 用法  
**从矩阵创建N维仿射和射影变换**  
<a id="function1"></a> [T](#P1) = maketform("affine", [A](#Q1)) 创建一个空间变换结构，用于表示由矩阵 `A` 指定的 `N` 维仿射变换。变换结构体 `T` 同时包含正向变换和逆向变换。  
这种空间变换结构可以与 <a href="../tformarray/tformarray.html">tformarray</a>  </a> 、 <a href="../tformfwd/tformfwd.html">tformfwd</a>  </a> 和 <a href="../tforminv/tforminv/.html">tforminv</a>  </a> 函数一起使用。    
<a id="function2"></a> [T](#P1) = maketform("projective", [P](#Q2)) 创建一个空间变换结构体，用于表示由矩阵 `P` 指定的 `N` 维投影变换。变换结构体 `T` 同时包含正向变换和逆向变换。  
  
**通过正向或逆向函数创建变换**     
<a id="function3"></a> [T](#P1) = maketform("custom", [ndims_in](#Q3), [ndims_out](#Q4), [forward_fcn](#Q5), [inverse_fcn](#Q6), [tdata](#Q7)) 基于用户提供的函数句柄和参数创建一个自定义变换结构体。其中，`ndims_in` 和 `ndims_out` 分别是输入和输出维度的数量；`forward_fcn` 和 `inverse_fcn` 是正向函数与逆向函数的句柄。参数 `tdata` 可以是任意数组，通常用于存储自定义变换的状态参数，它可被正向函数和逆向函数访问，并通过结构体的 `tdata` 字段传递。  
  
**为空间参考创建变换**  
<a id="function4"></a> [T](#P1) = maketform("box", [tsize](#Q8), [outCornerStart](#Q9),[outCornerEnd](#Q10)) 创建一个 `N` 维仿射结构，它将由角点 `ones(1, N)` 和大小 `tsize` 定义的输入框，映射到由对角角点 `outCornerStart` 和 `outCornerEnd` 定义的输出框。`"box"` 变换通常用于将图像或数组的行列下标注册到某个世界坐标系中。  
<a id="function5"></a> [T](#P1) = maketform("box", [inCorners](#Q11), [outCorners](#Q12)) 创建一个 `N` 维仿射变换 `T`，该变换将由 `inCorners(1, :)` 和 `inCorners(2, :)` 两个角点定义的输入框，映射到由 `outCorners(1, :)` 和 `outCorners(2, :)` 的输出框。  
  
**创建复合变换**  
<a id="function6"></a> [T](#P1) = maketform("composite",[T1, T2, ..., TL](#Q13)) 创建一个由多个变换 T1, T2, ..., TL 组合而成的复合变换 `T`。复合变换 `T` 的正向和逆向函数是其各分量变换 T1, T2, ..., TL 的正向和逆向函数的函数组合。  
  
<a id="function7"></a> [T](#P1) = maketform("composite", [[T1, T2, ..., TL](#Q13)])  创建一个由多个向量 T1, T2, ..., TL 组合而成的复合变换 `T`。复合变换 `T` 的正向和逆向函数是其各分量变换 T1, T2, ..., TL 的正向和逆向函数的函数组合。  
  
## 参数说明
### 输入参数  
**<a id="Q1"></a> A — 仿射变换**  
(N+1) × (N+1) 矩阵 | (N+1) × N 矩阵   
  
仿射变换，指定为 (N+1) × (N+1) 矩阵或 (N+1) × N 矩阵，其中 `N` 是仿射变换的维度，该矩阵必须是非奇异的实数矩阵。  
  
若矩阵 `A` 为 (N+1) × (N+1) 形式，则其最后一列必须为 [0; 0; ... ; 1]，否则矩阵会被自动增广，使其最后一列变为 (0; 0; ... ; 1)。矩阵 `A` 定义了一个正向变换：对于 1 × N 向量 `U`，函数 `tformfwd(U, T)` 会返回 1 × N 向量 `X`，满足公式：X = U * A(1:N, 1:N) + A(N+1, 1:N)  
  
**数据类型：** `double`   
 
**<a id="Q2"></a> P — 投影变换**  
(N+1) × (N+1) 矩阵  
  
投影变换，指定为 (N+1) × (N+1) 矩阵，其中 `N` 是投影变换的维度。该矩阵必须是非奇异的实数矩阵，且矩阵右下角元素 P(N+1, N+1) 不能为0。  
  
矩阵 `P` 定义了一个正向变换：对于 1 × N 的输入向量 `U` ，函数 `tformfwd(U, T)` 执行的变换过程如下：首先计算齐次坐标向量 W = [U 1] × P，然后通过归一化 X=W(1:N)/W(N+1) 得到 1 × N 的输出向量 `X` 。  
  
**数据类型：** `double`  
  
**<a id="Q3"></a> ndims_in — 输入维度数**  
正整数  
  
输入维度数，指定为正整数。  
  
**数据类型：** `double`  
  
**<a id="Q4"></a> ndims_out — 输出维度数**  
正整数  
  
输出维度数，指定为正整数。  
  
**数据类型：** `double`  
  
**<a id="Q5"></a> forward_fcn — 正向函数**  
函数句柄 | []  
  
正向函数，指定为函数句柄，支持语法 X = forward_fcn(U, T)。其中 `U` 是 numpts × [ndims_in](#Q3) 矩阵，其每一行代表变换输入空间中的一个点，`X` 是 numpts × [ndims_out](#Q4) 矩阵，其每一行代表变换输出空间中的一个点。
`forward_fcn` 可以为空。  
  
**数据类型：** `function_handle`  
  
**<a id="Q6"></a> inverse_fcn — 逆向函数**  
函数句柄  
  
逆向函数，指定为函数句柄，支持语法 U = inverse_fcn(X, T)。其中 `X` 是 numpts × [ndims_out](#Q4) 矩阵，其每一行代表变换输出空间中的一个点，`U` 是 numpts × [ndims_in](#Q3) 矩阵，其每一行代表变换输入空间中的一个点。  
`inverse_fcn 可以为空`。但是，若要将结构体 `T` 与 <a href="../tformarray/tformarray.html">tformarray</a>  </a> 函数配合使用，必须定义 `inverse_fcn`。  
  
**数据类型：** `function_handle` 
  
**<a id="Q7"></a> tdata — 自定义变换参数**  
数组  
  
自定义变换参数，指定为数组。  
  
**数据类型：** `double`  
  
**<a id="Q8"></a> tsize — 输入框大小**  
由 N 个正整数构成的向量  
  
输入框大小，指定为一个包含 `N` 个正整数构成的向量。  
  
**数据类型：** `double`  
  
**<a id="Q9"></a> outCornerStart — 输出空间中的起始角点坐标**  
N 元素向量                  
  
输出空间中的起始角点坐标，指定为一个 `N` 元素向量。除非 [tsize](#Q8)(k) 为1(此时第 k 维的仿射缩放因子默认取 1.0），否则 outCornerStart(k) 与 [outCornerEnd](#Q10)(k) 必须不同。  
  
**数据类型：** `double`   
  
**<a id="Q10"></a> outCornerEnd — 输出空间中的对角角点坐标**  
N 元素向量  
  
输出空间中的对角角点坐标，指定为一个 `N` 元素向量。除非 [tsize(k)](#Q8) 为 1（此时第 k 维的仿射缩放因子默认取 1.0)，否则 [outCornerStart](#Q9)(k) 与 outCornerEnd(k) 必须不同。  
  
**数据类型：** `double`  
  
**<a id="Q11"></a> inCorners — 输入空间中的角点坐标**  
N × 2 数值矩阵  
  
输入空间中的角点坐标，指定为一个 N×2 的数值矩阵。矩阵的第一列代表一个角点的坐标，第二列代表其对角角点的坐标。除非 [outCorners](#Q12)(1, k) 与 outCorners(2, k) 相同，否则 inCorners(1, k) 与 inCorners(2, k) 必须不同。  
  
**数据类型：** `double`  
  
**<a id="Q12"></a> outCorners — 输出空间中的角点坐标**  
N × 2 数值矩阵  
  
输出空间中的角点坐标，指定为一个 N×2 的数值矩阵。矩阵的第一列代表一个角点的坐标，第二列代表其对角角点的坐标。除非 [inCorners](#Q11)(1, k) 与 inCorners(2, k) 相同，否则 outCorners(1, k) 与 outCorners(2, k) 必须不同。  
  
**数据类型：** `double`  
  
**<a id="Q13"></a> T1, T2, ..., TL — 分量变换**  
`TFORM` 结构体  
  
分量变换，指定为 `TFORM` 结构体。  
输入的顺序与函数组合的标准记法一致：T=T1∘T2∘⋯∘TL。复合运算满足结合律，但不满足交换律。因此如果要对输入 `U` 应用变换 `T` 时，必须先应用 `TL` ，最后应用 `T1` 。例如，若 `T = T1∘T2∘T3`，则 `tformfwd(U, T)` 等价于 `tformfwd(tformfwd(tformfwd(U, T3), T2), T1)`。各分量变换 `T1, T2, ... , TL`在输入和输出维度数量上必须兼容。  
仅当所有分量变换都定义了正向变换函数时，复合变换 `T` 才有正向变换函数；同理，仅当所有分量变换都定义了逆向变换函数时，`T` 才有逆向变换函数。  
  
**数据类型：** `function_handle`  
  
### 输出参数   
**<a id="P1"></a> T — 多维空间变换**  
`TFORM` 结构体  
  
多维空间变换，指定为 `TFORM` 结构体。  
  
## 版本历史
在北太天元图像处理工具箱 V1.0 推出 

## 相关主题  

<a href="../tformfwd/tformfwd.html">tformfwd</a> | <a 
href="../tforminv/tforminv.html">tforminv</a> | <a  
href="../fliptform/fliptform.html">fliptform</a> | <a 
href="../tformarray/tformarray.html">tformarray</a>      
## tformfwd
应用 N 维正向几何变换

## 简介  
[`[X1, X2, ..., X_ndims_out] = tformfwd(T, U1, U2, ..., U_ndims_in)`](#function1)  
[`X = tformfwd(T, U)`](#function2)  
[`[X1, X2, ..., X_ndims_out] = tformfwd(T, U)`](#function3)  
[`X = tformfwd(T, U1, U2, ..., U_ndims_in)`](#function4)  

## 用法 
<a id="function1"></a> [[X1, X2, ..., X_ndims_out](#P1)] = tformfwd([T](#Q1), [U1, U2, ...,  U_ndims_in](#Q2)) 对坐标数组 U1, U2, ..., U_ndims_in 应用输入维度 ndims_in 到 ndims_out 维度的变换 `T`。 变换将点 [U1(k), U2(k), ..., U_ndims_in(k)] 映射到 [X1(k),X2(k),...,X_ndims_out(k)]。  
<a id="function2"></a> [X](#P2) = tformfwd([T](#Q1), [U](#Q3)) 对坐标数组 `U` 应用变换 `T`：  
  
- 若 `U` 是 `m × ndims_in` 二维矩阵：`X` 为 `m × ndims_out` 二维矩阵，`tformfwd` 对 `U` 的每一行独立应用变换，将点 `U(k,:)` 映射到 `X(k,:)`。  
- 若 `U` 是 `N+1` 维数组 ： `size(U, N+1)` 必须等于 `ndims_in`，`X` 为 `N+1` 维数组，前 `N` 维大小与 `U` 一致，第 `N+1` 维为 `ndims_out`。`tformfwd` 将点从 U(k1, k2, ..., kN, :) 映射到 X(k1, k2, ..., kN, :))。  
  
<a id="function3"></a> [[X1, X2, ..., X_ndims_out](#P1)] = tformfwd([T](#Q1), [U](#Q3)) 将一个 `(N+1)` 维数组映射为 `ndims_out` 个大小相同的 `N` 维数组。  
<a id="function4"></a> [X](#P2) = tformfwd([T](#Q1), [U1, U2, ..., U_ndims_in](#Q2)) 将 `ndims_in` 个 `N` 维数组映射为一个 (N+1) 维数组。  

## 参数说明
### 输入参数
**<a id="Q1"></a> T — 空间变换**   
`TFORM` 结构体  

空间变换，指定为 `TFORM` 结构体。需使用 <a href="../maketform/maketform.html">maketform</a>  </a> 函数创建 `T`。

**数据类型：** `struct`

**<a id="Q3"></a> U — 输入坐标点**  
数值数组  

输入坐标点，指定为数值数组。`U` 的大小和维度取决于所使用的具体调用语法，可能存在额外的限制。

**数据类型：** `double`  
  
**<a id="Q2"></a> U1, U2, ..., U_ndims_in — 输入坐标点**  
多个数值数组  
  
输入坐标点，指定为多个数值数组。`U1, U2, ..., U_ndims_in` 的大小和维度取决于所使用的具体调用语法，可能存在额外的限制。  
  
**数据类型：** `double`   

### 输出参数
**<a id="P2"></a> X — 输出点坐标数组**  
数值数组  

输出点坐标数组，指定为数值数组。`X` 的大小和维度取决于所使用的具体调用语法，可能存在额外的限制。  
  
**<a id="P1"></a> X1, X2, ..., X_ndims_out — 输出点坐标**  
多个数值数组  
  
输出点坐标，指定为多个数值数组。`X1, X2, ..., X_ndims_out` 的大小和维度取决于所使用的具体调用语法，可能存在额外的限制。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../maketform/maketform.html">maketform</a> | <a
href="../fliptform/fliptform.html">fliptform</a> | <a 
href="../tforminv/tforminv.html">tforminv</a> | <a 
href="../transformPointsForward/transformPointsForward.html">transformPointsForward</a> 
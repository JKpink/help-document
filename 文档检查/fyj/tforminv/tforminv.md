## tforminv
应用 N 维逆几何变换

## 简介
[`[U1, U2, ..., U_ndims_in] = tforminv(T, X1, X2, ..., X_ndims_out)`](#function1)  
[`U = tforminv(T, X)`](#function2)  
[`[U1, U2, ..., U_ndims_in] = tforminv(T, X)`](#function3)  
[`U = tforminv(T, X1, X2, ..., X_ndims_out)`](#function4) 

## 用法  
<a id="function1"></a> [[U1, U2, ..., U_ndims_in](#P1)] = tforminv([T](#Q1), [X1, X2, ..., X_ndims_out](#Q2)) 对坐标数组 X1, X2, ..., X_ndims_out 应用输出维度 `ndims_out` 到 `ndims_in` 维度的逆变换 `T`。 变换将点 [X1(k), X2(k), ..., X_ndims_out(k)] 映射到 [U1(k), U2(k), ..., U_ndims_in(k)]。     
<a id="function2"></a> [U](#P2) = tforminv([T](#Q1), [X](#Q3)) 对坐标数组 `X` 执行由 `T` 定义的从 `ndims_out` 到 `ndims_in` 的逆变换。  
  
- 若 `X` 是 `m × ndims_out` 二维矩阵：`U` 为 `m × ndims_in` 二维矩阵，`tformfwd` 对 `U` 的每一行独立应用变换，将点 `X(k,:)` 映射到 `U(k,:)`。  
- 若 `X` 是 `N+1` 维数组 ： `size(X,N+1)` 必须等于 `ndims_out` , `U` 为 `N+1` 维数组，前 `N` 维尺寸与 `X` 一致，第 `N+1` 维为 `ndims_in`。`tformfwd` 将点从 X(k1, k2, ..., kN, :) 映射到到 U(k1, k2, ..., kN, :))。  
    
<a id="function3"></a> [[U1, U2, ..., U_ndims_in](#P1)] = tforminv([T](#Q1), [X](#Q3)) 将一个 `(N+1)` 维数组映射为 `ndims_in` 个大小相同的 `N` 维数组。    
<a id="function4"></a> [U](#P2) = tforminv([T](#Q1), [X1,X2,...,X_ndims_out](#Q2)) 将 `ndims_out` 个 `N` 维数组映射为一个 `(N+1)` 维数组。    
    

## 参数说明
### 输入参数
**<a id="Q1"></a> T — 空间变换**   
`TFORM` 空间变换结构体  

空间变换，指定为 `TFORM` 空间变换结构体。需使用 <a href="../maketform/maketform.html">maketform</a>  </a> 函数创建 `T`。  
  
**数据类型：** `struct` 

**<a id="Q3"></a> X — 输入坐标点**  
数值数组  

输入坐标点，指定为数值数组。`X` 的大小和维度取决于所使用的具体调用语法，可能存在额外的限制。  

**数据类型：** `double`  
  
**<a id="Q2"></a> X1, X2, ..., X_ndims_out — 输入坐标点**  
多个数值数组  
  
输入坐标点，指定为多个数值数组。`X1, X2, ..., X_ndims_out` 的大小和维度取决于所使用的具体调用语法，可能存在额外的限制。  
  
**数据类型：** `double`  

### 输出参数
**<a id="P2"></a> U — 输出点坐标数组**  
数值数组  

输出点坐标数组，指定为数值数组。`U` 的大小和维度取决于所使用的具体调用语法，可能存在额外的限制。  
  
**<a id="P1"></a> U1, U2, ..., U_ndims_in — 输出点坐标**  
多个数值数组  
  
输出点坐标，指定为多个数值数组。`U1, U2, ..., U_ndims_in` 的大小和维度取决于所使用的具体调用语法，可能存在额外的限制。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../maketform/maketform.html">maketform</a> | <a
href="../fliptform/fliptform.html">fliptform</a> | <a 
href="../tformfwd/tformfwd.html">tformfwd</a> | <a 
href="../transformPointsInverse/transformPointsInverse.html">transformPointsInverse </a>
## maxhessiannorm  
Hessian 矩阵 Frobenius 范数最大值  
  
## 简介  
[`C = maxhessiannorm(I)`](#function1)  
[`C = maxhessiannorm(I, thickness)`](#function2)  
  
## 用法  
<a id="function1"></a> [C](#P1) = maxhessiannorm([I](#P2)) 返回灰度图像 `I` 的 `Hessian` 矩阵 `Frobenius` 范数的最大值。  
<a id="function2"></a> [C](#P1) = maxhessiannorm([I](#P2), [thickness](#P3)) 同时指定管状结构的厚度。  
  
## 参数说明
### 输入参数  
**<a id="P2"></a> I — 包含细长或管状结构的图像**  
二维灰度图像  
  
包含细长或管状结构的图像，指定为二维灰度图像。  
  
**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`  
  
**<a id="P3"></a> thickness — 管状结构的厚度**  
4（默认）| 正整数  
  
管状结构的厚度，单位为像素，指定正整数。  
  
**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `uint64`  
  
### 输出参数  
  
**<a id="P1"></a> C —  Hessian 矩阵范数最大值**  
数值标量  
  
灰度图像 `I` 的 `Hessian` 矩阵的 `Frobenius` 范数最大值，指定为数值标量。 
  
**数据类型：** `double`  
  
## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../edge/edge.html">edge</a> | <a 
href="../imgradient/imgradient.html">imgradient</a> | <a 
href="../fibermetric/fibermetric.html">fibermetric</a>   
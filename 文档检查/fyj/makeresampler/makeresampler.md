## makeresampler  
创建重采样结构  
  
## 简介  
[`R = makeresampler(interpolant, padMethod)`](#function1)  
[`R = makeresampler(Name, value)`](#function2)  
  
## 用法   
<a id="function1"></a> [R](#P1) = makeresampler([interpolant](#Q1), [padMethod](#Q2)) 会创建一个可分离重采样器结构，用于 <a href="../tformarray/tformarray.html">tformarray</a>  </a> 函数使用。`interpolant` 参数用于指定可分离重采样器所采用的插值核函数；`padMethod` 参数则控制重采样器如何为映射到输入数组边缘附近或外部的输出元素进行插值或赋值。  
<a id="function2"></a> [R](#P2) = makeresampler([Name, value](#Q3)) 会通过名称 - 值对组参数，创建一个用户自定义的重采样器。  
## 参数说明
### 输入参数  
**<a id="Q1"></a> interpolant — 插值核**  
`"cubic"` | `"linear"` | `"nearest"`  
  
插值核，指定为 `"nearest"`、`"linear"`、`"cubic"`。这些核分别对应执行最近邻插值、双线性插值、双三次插值。  
  
**数据类型：** `char` | `string`   
  
**<a id="Q2"></a> padMethod — 填充方法**  
`"bound"` | `"circular"` | `"replicate"` | `"symmetric"` | `"fill"`  
  
该填充方法用于为映射到输入数组外部的输出元素赋值，指定为下述取值之一。  
      
| **填充方法**   | **说明**                                                                | 
| ---------- | -------------------------------------------------------------------- |
| `"bound"` | 将填充值数组中的值分配给映射到输入数组外部的点；对于映射到数组内部的点，重复数组的边界元素（与 `“replicate”` 方法效果相同）。当插值核为 `“nearest”` 时，此填充方法的结果与 `“fill”` 方法一致。`“bound”` 类似 `“fill”`，但会避免混合填充值与输入图像值。 |
| `"circular"` | 在维度范围内通过循环重复元素来填充数组，与 <a href="../padarray/padarray.html">padarray</a>  </a> 函数的效果相同。|
| `"fill"` | 生成边缘视觉平滑的输出数组（使用最近邻插值时除外）。对于映射到输入数组边缘附近（内部或外部）的输出点，会结合输入图像值与填充值。当插值核为 `“nearest”` 时，此填充方法的结果与 `“bound”` 方法一致。 |
| `"replicate"` | 通过重复数组的边界元素来填充数组，与 <a href="../padarray/padarray.html">padarray</a>  </a> 函数的效果相同。|
| `"symmetric"` | 通过数组自身的镜像反射来填充数组，与 <a href="../padarray/padarray.html">padarray</a>  </a> 函数的效果相同。|

对于 `“fill”`、`“replicate”`、 `“circular”`、 或 `“symmetric”` 这些填充方法，`tformarray` 执行的重采样包含两个逻辑步骤：  
1.对数组 `A` 进行无限填充，以覆盖整个输入变换空间。  
2.在几何映射指定的输出点处，计算填充后的数组 `A` 与重采样核的卷积。  
每个非变换维度会单独处理。为了提升性能与内存效率，填充是虚拟的（通过重新映射数组下标实现)。如果实现了自定义重采样器，可以复现这些行为。  
  
**数据类型：** `char` | `string`  
### <a id="Q3"></a> 名称-值参数  
将可选的参量对组指定为 Name1, Value1, ... , NameN, ValueN，其中 `Name` 是参量名称，`Value` 是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。  
  
示例：`"Type"`,`"separable"` 会创建一个可分离重采样器。  
**Type — 重采样器类型**  
`"separable"` | `"custom"`  
重采样器类型，指定为以下值之一：  
  
| **类型** | **说明** |
| --- | --- |
| `"separable"` | 创建可分离重采样器。若指定此值，仅可额外指定 [Interpolant](#Q4) 和 [PadMethod](#Q5) 参数，效果与 makeresampler(interpolant, padMethod) 语法等价。 |
| `"custom"` | 创建自定义重采样器。若指定此值，必须指定 [NDims](#Q6) 和 [ResampleFcn](#Q7) 参数，[CustomData](#Q8) 参数为可选。 |

**数据类型：** `char` | `string`   
  
**<a id="Q5"></a> PadMethod — 填充方法**  
字符向量 | 字符串标量  
参考 [padMethood](#Q2) 参数的相关文档。  
  
**数据类型：** `char` | `string`   
 
**<a id="Q4"></a> Interpolant — 插值核函数**  
字符向量 | 字符串标量 | 元胞数组  
  
参考 [interpolant](#Q1) 参数的相关文档。  
  
**数据类型：** `char` | `string`   
  
**<a id="Q6"></a> NDims — 自定义重采样器可处理的维度数**  
正整数  
 
自定义重采样器可处理的维度数，指定为正整数。若使用 `Inf` 则表示该重采样器可以处理任意维度。当 `"Type"` 为 `"custom"` 时，必须指定 `NDims`。  
 
**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `unit8` | `unit16` | `unit32` | `unit64`  
  
**<a id="Q7"></a> ResampleFcn — 执行重采样的函数**  
函数句柄   
 
执行重采样的函数，需指定为函数句柄。调用该函数的接口格式如下:  
B = resample_fcn(A, M, TDIMS_A, TDIMS_B, FSIZE_A, FSIZE_B, F, R)  
此函数输入参数的详细说明可以参考 <a href="../tformarray/tformarray.html">tformarray</a>  </a>。其中，参数 `M` 是一个数组，用于将输出数组 `B` 的变换下标空间映射到输入数组 `A` 的变换下标空间。若 `A` 有 `N` 个变换维度( N = length(TDIMS_A))，`B` 有 `P` 个变换维度( P = length(TDIMS_B))，则当 N>1 时，`M` 的维度数 ndims(M) = P+1;当 N == 1，ndims(M) = P 且 size(M,P+1) = N。  
`M` 的前 `P` 个维度对应输出变换空间，维度顺序由 `TDIMS_B` 中输出变换维度的排列顺序决定 (通常 `TDIMS_A` 和 `TDIMS_B` 无需升序排列，部分重采样器可能会有此限制)。因此，`size(M)` 的前 `P` 个元素决定 `B` 的变换维度大小。每个点映射到的输入变换坐标，沿 `M` 的最后一维排列，顺序与 `TDIMS_A` 一致。 `M` 必须为 `double` 类型。  
`FSIZE_A` 和 `FSIZE_B` 分别是 `A` 和 `B` 的完整尺寸，必要时填充1，以保证与 `FSIZE_A`、`FSIZE_B` 及 `size(A)` 一致。  
  
**数据类型：** `function_handle`  
  
**<a id="Q8"></a> CustomData — 用户自定义数据**  
数值数组 | 字符串标量 | 字符向量  
  
用户自定义数据，指定为字符串标量、字符向量或数值数组。  
  
**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `unit8` | `unit16` | `unit32` | `unit64` | `char` | `string` |         
### 输出参数  
**<a id="P1"></a> R — 重采样器**  
结构体  

重采样器，指定为结构体。  
## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../tformarray/trormarray.html">tformarray</a>    

  
 

  


## rgb2lin
线性化伽马校正的 RGB 值

## 简介
[ `B = rgb2lin(A)`](#function1)  
[ `B = rgb2lin(A, Name, Value)`](#function2)

## 用法
<a id="function1"></a>
[B](#P1) = rgb2lin([A](#Q1)) 撤销图像 `A` 中 sRGB 值的伽马校正，使得 `B` 包含线性 RGB 值。  
<a id="function2"></a>
[B](#P1) = rgb2lin([A](#Q1), [Name, Value](#Q2)) 使用名称-值参数来控制附加选项，从而撤销伽马校正。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 伽马校正的 RGB 颜色值**  
数值数组  

伽马校正的 RGB 颜色值，指定为数值数组，采用下列格式之一。

- c×3 颜色图。每行指定一个 RGB 颜色值。
- m×n×3 图像。
- m×n×3×p 图像堆栈。

**数据类型：** `single` | `double` | `uint8` | `uint16`

### <a id="Q2"></a> 名称-值参数
指定可选的参数对，格式为 Name1, Value1, ... , NameN, ValueN，其中 Name 是参数名称，Value 是对应的值。名称-值参数必须出现在其他参数之后，但各参数对的顺序可以任意。  
示例：B = rgb2lin(I, "ColorSpace", "adobe-rgb-1998") 根据 Adobe RGB (1998) 标准将伽马校正后的图像线性化。

**ColorSpace — 输出图像的色彩空间**  
"srgb"（默认）| "adobe-rgb-1998" | "prophoto-rgb"  

输出图像的色彩空间，指定为 "srgb"、"adobe-rgb-1998" 或 "prophoto-rgb"。  

**数据类型：** `string` | `char`

**OutputType — 输出 RGB 值的数据类型**  
"double" | "single" | "uint8" |  "uint16"

输出 RGB 值的数据类型，指定为 "double"、"single"、"uint8" 或 "uint16"。默认情况下，输出数据类型与输入图像 [A](#Q1) 的数据类型相同。  

**数据类型：**  `string` | `char`

### 输出参数
**<a id="P1"></a> B — 线性化 RGB 颜色值**  
数值数组

线性化 RGB 颜色值，以与输入 [A](#Q1) 相同大小的数值数组返回。

<!-- ## 算法
### 使用 sRGB 标准进行线性化  
sRGB 三色值使用以下参数曲线进行线性化：
$$
\begin{aligned}
& f(u) = -f(-u),\qquad u < 0\\
& f(u) = c ⋅ u,\qquad 0 ≤ u < d\\
& f(u) = (a ⋅ u + b)^ɣ,\qquad   u ≥ d&
\end{aligned}
$$
其中 `u` 表示具有以下参数的颜色值：
$$
\begin{aligned}
& a = 1/1.055\\
& b = 0.055/1.055\\
& c = 1/12.92\\
& d = 0.04045\\
& ɣ = 2.4
\end{aligned}
$$

### 使用 Adobe RGB (1988) 标准进行线性化
Adobe RGB (1998) 三色值使用简单的幂函数 [[2]](#reference2) 进行线性化：
$$
\begin{aligned}
& v = u^ɣ\\
和\\
& ɣ = 2.19921875
\end{aligned}
$$

### 使用 ProPhoto (ROMM RGB) 标准进行线性化
ProPhoto (ROMM RGB) 三色值使用以下参数曲线进行线性化 [[3]](#reference3)：
$$
\begin{aligned}
& f(u) = 0,\qquad &u < 0\\
& f(u) = u/16,\qquad &0 ≤ u < 16*E_t\\
& f(u) = u^{1.8} + b,\qquad  &16*E_t < u < 1\\
& f(u) = 1,\qquad  &u ≥ 1\\
和\\
& E_t=1/512
\end{aligned}
$$ -->

## 参考文献
[1] Ebner, Marc. Color Constancy. Chichester, West Sussex: John Wiley & Sons, 2007.  
<a id="reference2"></a>
<!-- [2] Adobe Systems Incorporated. Inverting the color component transfer function[J]. Adobe RGB (1998) Color Image Encoding, 2005, 4:(12).  
<a id="reference3"></a> 
[3] ISO 22028-2:2013 Photography and graphic technology — Extended colour encodings for digital image storage, manipulation and interchange — Part 2: Reference output medium metric RGB colour image encoding (ROMM RGB)[S]. International Organization for Standardization, 2013-04. <a href="https://www.iso.org/standard/56591.html">https://www.iso.org/standard/56591.html</a>.  -->

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../lin2rgb/lin2rgb.html">lin2rgb</a> 
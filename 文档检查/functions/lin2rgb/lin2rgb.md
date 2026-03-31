## lin2rgb
对线性 RGB 值应用伽马校正

## 简介
[ `B = lin2rgb(A)`](#function1)  
[ `B = lin2rgb(A, Name, Value)`](#function2)

## 用法
<a id="function1"></a>
[B](#P1) = lin2rgb[(A)](#Q1) 对图像 `A` 中的线性 RGB 值应用伽马校正，使得 `B` 处于 sRGB 色彩空间，用于显示。  
<a id="function2"></a>
[B](#P1) = lin2rgb([A](#Q1), [Name, Value](#Q2)) 使用名称-值参数来控制附加选项，从而应用伽马校正。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 线性 RGB 颜色值**  
数值数组

线性 RGB 颜色值，指定为数值数组，采用下列格式之一。

- c×3 颜色图。每行指定一个 RGB 颜色值。
- m×n×3 图像。
- m×n×3×p 图像堆栈。

**数据类型：** `single` | `double` | `uint8` | `uint16`

### <a id="Q2"></a> 名称-值参数
指定可选的参数对，格式为 Name1, Value1, ... , NameN, ValueN，其中 Name 是参数名称，Value 是对应的值。名称-值参数必须出现在其他参数之后，但各参数对的顺序可以任意。  
示例：B = lin2rgb(I, "ColorSpace", "adobe-rgb-1998") 根据 Adobe RGB (1998) 标准对图像 `I` 应用伽马校正。

**ColorSpace — 输出图像的色彩空间**  
"srgb"（默认）| "adobe-rgb-1998" | "prophoto-rgb"

输出图像的色彩空间，指定为 "srgb"、"adobe-rgb-1998" 或 "prophoto-rgb"。  

**数据类型：** `string` | `char`

**OutputType — 输出 RGB 值的数据类型**  
"double" | "single" | "uint8" | "uint16"

输出 RGB 值的数据类型，指定为 "double"、"single"、"uint8" 或 "uint16"。默认情况下，输出数据类型与输入图像 `A` 的数据类型相同。  

**数据类型：**  `string` | `char`

### 输出参数
**<a id="P1"></a> B — 伽马校正的 RGB 图像**  
数值数组

伽马校正的 RGB 图像，以与输入 `A` 相同大小的数值数组返回。

<!-- ## 算法
### 使用 sRGB 标准进行伽玛校正  
将线性 RGB 三刺激值转换为 sRGB 的伽马校正三刺激值由以下参数曲线定义：  
$$
\begin{aligned}
& f(u) = -f(-u),\qquad u < 0\\
& f(u) = c ⋅ u,\qquad 0 ≤ u < d\\
& f(u) = a ⋅ u^ɣ + b,\qquad   u ≥ d&
\end{aligned}
$$
其中 `u` 表示具有以下参数的颜色值：
$$
\begin{aligned}
& a = 1.055\\
& b = –0.055\\
& c = 12.92\\
& d = 0.0031308\\
& ɣ = 1/2.4
\end{aligned}
$$

### 使用 Adobe RGB （1988） 标准进行伽玛校正
将线性 RGB 三刺激值转换为 Adobe RGB 的伽玛校正 （1998） 三刺激值使用简单的幂函数 [[2]](#reference2)：
$$
\begin{aligned}
& v = u^ɣ,\qquad &u ≥ 0 \\
& v = -(-u)^ɣ,\qquad  &u < 0 \\
和\\
& ɣ = 1/2.19921875
\end{aligned}
$$

### 使用 ProPhoto （ROMM RGB） 标准进行伽玛校正
将线性 RGB 三刺激值转换为 ProPhoto 的伽马校正 三刺激值由以下参数曲线定义 [[3]](#reference3)：
$$
\begin{aligned}
& f(u) = 0,\qquad &u < 0\\
& f(u) = u/16,\qquad &0 ≤ u < 16*E_t\\
& f(u) = u^{1/1.8} + b,\qquad  &16*E_t < u < 1\\
& f(u) = 1,\qquad  &u ≥ 1\\
和\\
& E_t=1/512
\end{aligned}
$$ -->

## 参考文献
[1] Ebner, Marc. Color Constancy. Chichester, West Sussex: John Wiley & Sons, 2007.    
<!-- [2] Adobe Systems Incorporated. Inverting the color component transfer function. Adobe RGB (1998) Color Image Encoding, 2005, 4:(12).  
<a id="reference2"></a> 
[3] ISO 22028-2:2013 Photography and graphic technology — Extended colour encodings for digital image storage, manipulation and interchange — Part 2: Reference output medium metric RGB colour image encoding (ROMM RGB). International Organization for Standardization, 2013-04. https://www.iso.org/standard/56591.html 
<a id="reference3"></a>-->

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../rgb2lin/rgb2lin.html">rgb2lin</a> 
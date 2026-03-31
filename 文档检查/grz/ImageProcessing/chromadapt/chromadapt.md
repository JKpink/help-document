## chromadapt
通过色彩自适应调整 RGB 图像的色彩平衡

## 简介
[`B = chromadapt(A, illuminant)`](#function1)  
[`B = chromadapt(A, illuminant, Name, Value)`](#function1)

## 用法
<a id="function1"></a>
[B](#P1) = chromadapt([A](#Q1), [illuminant](#Q2)) 根据场景光源调整 RGB 图像 `A` 的色彩平衡。光源必须与输入图像处于相同的色彩空间。  
<a id="function1"></a>
[B](#P1) = chromadapt([A](#Q1), [illuminant](#Q2), [Name, Value](#Q3)) 使用名称-值参数来控制附加选项，从而调整图像 `A` 的色彩平衡。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — RGB 图像**  
m×n×3 数值数组

RGB 图像，指定为 m×n×3 数值数组。

**数据类型：** `single` | `double` | `uint8` | `uint16`

**<a id="Q2"></a> illuminant — 场景光源**  
3 元数值向量

场景光源，指定为 3 元数值向量。光源必须与输入图像 [A](#Q1) 处于相同的色彩空间。

**数据类型：** `single` | `double` | `uint8` | `uint16`

### <a id="Q3"></a> 名称-值参数
指定可选的参数对，格式为 Name1, Value1, ... , NameN, ValueN，其中 Name 是参数名称，Value 是对应的值。名称-值参数必须出现在其他参数之后，但各参数对的顺序可以任意。  
示例：I2 = chromadapt(I, [6,4,6], "ColorSpace", "linear-rgb") 在线性 RGB 色彩空间中调整图像的色彩平衡。  

**ColorSpace — 色彩空间**  
"srgb"（默认）| "adobe-rgb-1998" | "prophoto-rgb" | "linear-rgb"

输入图像和光源的色彩空间，指定为 "srgb"、"adobe-rgb-1998"、"prophoto-rgb" 或 "linear-rgb"。  

**数据类型：** `string` | `char`

**Method — 色适应方法**  
"bradford"（默认）| "vonkries" | "simple"  

色适应方法用于缩放 [A](#Q1) 中的 RGB 值，指定为以下这些值。  

- "bradford"：使用 Bradford 体响应模型进行缩放。
- "vonkries"：使用 von Kries 体响应模型进行缩放。
- "simple"：使用光源进行缩放。
  
**数据类型：**  `string` | `char`

### 输出参数
**<a id="P1"></a> B — 色彩平衡的 RGB 图像**  
m×n×3 数值数组

色彩平衡的 RGB 图像，以 m×n×3 的数值数组形式返回，其类型与输入图像 [A](#Q1) 相同。

## 参考文献
[1] Lindbloom, Bruce. Chromatic Adaptation. http://www.brucelindbloom.com/index.html?Eqn_ChromAdapt.html.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../whitepoint/whitepoint.html">whitepoint</a> | <a
href="../colorangle/colorangle.html">colorangle</a> | <a 
href="../illumgray/illumgray.html">illumgray</a> | <a 
href="../illumpca/illumpca.html">illumpca</a> | <a 
href="../illumwhite/illumwhite.html">illumwhite </a>

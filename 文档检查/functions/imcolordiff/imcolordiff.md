## imcolordiff
基于 CIE94 或 CIE2000 标准的色差

## 简介
[ `dE = imcolordiff(I1, I2)`](#function1)  
[ `dE = imcolordiff(I1, I2, Name, Value)`](#function2) 

## 用法
<a id="function1"></a>
[dE](#P1) = imcolordiff([I1](#Q1), [I2](#Q2)) 使用 CIE94 标准计算彩色图像之间或两组颜色之间的颜色差异。该函数默认颜色位于 sRGB 色彩空间。  
<a id="function2"></a>
[dE](#P1) = imcolordiff([I1](#Q1), [I2](#Q2), [Name, Value](#Q3)) 使用名称-值参数来控制附加选项，例如输入色彩空间和 CIE 标准。

## 参数说明
### 输入参数
**<a id="Q1"></a> I1 — 第一组颜色数据**  
1×3 数值向量 | c×3 数值矩阵 | 数值数组

第一组颜色数据，指定为这些格式之一。

- 一个 1×3 的数值向量，表示参考颜色。
- 一个 c×3 的数值矩阵，表示一组包含 c 种颜色的颜色集。
- 一个 m×n×3 的数值数组，表示彩色图像。
- 一个多维数值数组，例如 m×n×3×p 数组，表示一批彩色图像。第三维必须对应于颜色通道，并且必须有 3 个通道。

如果 [I2](#Q2) 不是参考颜色，则 `I1` 必须是参考颜色，或者是一个与 `I2` 大小相同的数值数组。
`I1` 和 `I2` 必须处于相同的色彩空间。`imcolordiff` 函数默认 `I1` 和 `I2` 位于 sRGB 色彩空间。如果 `I1` 和 `I2` 实际上处于 L\*a\*b\* 色彩空间，则需要将 `isLab` 参数指定为 1。L\*a\*b\* 色彩值只能是单精度（single）或双精度（double）数据类型。

**数据类型：** `single` | `double` | `uint8` | `uint16`

**<a id="Q2"></a> I2 — 第二组颜色数据**  
1×3 数值向量 | c×3 数值矩阵 | 数值数组

第二组颜色数据，指定为这些格式之一。

- 一个 1×3 的数值向量，表示参考颜色。
- 一个 c×3 的数值矩阵，表示一组包含 c 种颜色的颜色集。
- 一个 m×n×3 的数值数组，表示彩色图像。
- 一个多维数值数组，例如 m×n×3×p 数组，表示一批彩色图像。第三维必须对应于颜色通道，并且必须有 3 个通道。

如果 [I1](#Q1) 不是参考颜色，则 `I2` 必须是参考颜色，或者是一个与 `I1` 大小相同的数值数组。
`I1` 和 `I2` 必须处于相同的色彩空间。`imcolordiff` 函数默认 `I1` 和 `I2` 位于 sRGB 色彩空间。如果 `I1` 和 `I2` 实际上处于 L\*a\*b\* 色彩空间，则需要将 `isLab` 参数指定为 1。L\*a\*b\* 色彩值只能是单精度（single）或双精度（double）数据类型。

**数据类型：** `single` | `double` | `uint8` | `uint16`

### <a id="Q3"></a> 名称-值参数
指定可选的参数对，格式为 Name1, Value1, ... , NameN, ValueN，其中 Name 是参数名称，Value 是对应的值。名称-值参数必须出现在其他参数之后，但各参数对的顺序可以任意。  
示例：dE = imcolordiff(I1, I2, "Standard", "CIEDE2000") 使用 CIEDE2000 标准计算两个 RGB 图像之间的颜色差异。

**Standard — CIE 标准**   
"CIE94"（默认）| "CIEDE2000"

CIE 标准用于计算颜色差异值，指定为以下值之一。

| 值| 描述 |
| :----------- | :----------- |
| "CIE94" | 该标准改进了在 deltaE 函数中实现的 CIE76 标准的视觉非均匀性问题。 |
| "CIEDE2000" | 该标准通过五项额外的修正进一步提高了视觉均匀性：色调旋转项、对中性颜色的补偿，以及对明度、色度和色调的补偿。 |

**数据类型：** `string` | `char`

**isInputLab — 在 L\*a\*b\* 颜色空间中的颜色值**  
0（默认）| 1

在 L\*a\*b\* 颜色空间中的颜色值，指定为数值 0 或 1。 

**kL — 亮度系数**  
1（默认）| 数值标量

亮度系数，指定为数值标量。

**kC — 色度补偿系数**  
1（默认）| 数值标量

色度补偿系数，指定为数值标量。

**kH — 色相补偿系数**  
1（默认）| 数值标量

色相补偿系数，指定为数值标量。

**K1 — K1 加权系数**  
0.045（默认）| 数值标量

K1 加权系数，指定为数值标量。K1 权重系数仅适用于 CIE94 标准。用于图形艺术的值通常为 0.045，用于纺织品的值通常为 0.048。

**K2 — K2 加权系数**  
0.015（默认）| 数值标量

K2 加权系数，指定为数值标量。K2 权重因子仅适用于 CIE94 标准。用于图形艺术的值通常为 0.015，用于纺织品的值通常为 0.014。

### 输出参数
**<a id="P1"></a> dE — 颜色差异**  
数值矩阵 | c×1 列向量 | 数值标量 | 数值数组

颜色差异（delta E），以下形式之一返回：

- 一个 m×n 的数值矩阵。该矩阵表示两幅彩色图像之间，或者一幅彩色图像与参考颜色之间的逐像素颜色差异。
- 一个 c×1 的数值列向量。该向量表示两组 c 种颜色之间，或者一组 c 种颜色与参考颜色之间的颜色差异。
- 一个数值标量，表示两个参考颜色之间的颜色差异。
- 一个多维数值数组。该数组表示两批彩色图像之间，或者一批彩色图像与参考颜色之间的逐像素颜色差异。第三维的长度为 1，表示颜色差异。

如果 [I1](#Q1) 或 [I2](#Q2) 的数据类型为双精度（double），则 dE 的数据类型为双精度（double）。否则，dE 的数据类型为单精度（single）。  

**数据类型：** `string` | `double`

## 技巧
- 要按照 CIE76 标准计算颜色差异，请使用 <a href="../deltaE/deltaE.html">deltaE</a> 函数。该函数比 `imcolordiff` 函数速度更快，但精度较低。
- 通常情况下，应该保留 kL、kC、kH、K1 和 K2 参数的默认值。这些值可能会根据特定行业（例如图形艺术和纺织品行业）经过实验验证的照明条件而改变。

## 参考文献
[1] Sharma, Gaurav, Wencheng Wu, and Edul N. Dalal. The CIEDE2000 Color-Difference Formula: Implementation Notes, Supplementary Test Data, and Mathematical Observations. Color Research and Application, 2005, 30(1): 21–30.  
[2] ISO/CIE 11664-6:2014. Colorimetry — Part 6: CIEDE2000 Colour-difference formula. International Organization for Standardization, 2014. URL: <a href="https://cie.co.at/publications/industrial-colour-difference-evaluation">https://www.iso.org/standard/63731.html</a>.  
[3] CIE 116-1995. Industrial Colour-Difference Evaluation (E). International Commission on Illumination (CIE), 1995. URL: <a href="https://cie.co.at/publications/industrial-colour-difference-evaluation">https://cie.co.at/publications/industrial-colour-difference-evaluation</a>.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../deltaE/deltaE.html">deltaE</a> | <a 
href="../colorangle/colorangle.html">colorangle</a> 
<!-- | <a 
href="../measureColor/measureColor.html">measureColor</a>  -->
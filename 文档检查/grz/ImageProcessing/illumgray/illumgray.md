## illumgray
使用灰度世界算法估计照度

## 简介
[`illuminant = illumgray(A)`](#function1)  
[`illuminant = illumgray(A, percentile)`](#function2)  
[`illuminant = illumgray(___, Name, Value)`](#function3)  

## 用法
<a id="function1"></a>
[illuminant](#P1) = illumgray([A](#Q1)) 通过假设场景的平均颜色为灰色来估计 RGB 图像 `A` 中的场景照度。  
<a id="function2"></a>
[illuminant](#P1) = illumgray([A](#Q1), [percentile](#Q2)) 通过排除指定的底部和顶部像素的百分位数来估计照度。   
<a id="function2"></a>
[illuminant](#P1) = illumgray( ___, [Name, Value](#Q3)) 使用名称-值参数来控制附加选项，从而估计照度。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — RGB 图像**  
m×n×3 数值数组

RGB 图像，指定为 m×n×3 数值数组。

**数据类型：** `single` | `double` | `uint8` | `uint16`

**<a id="Q2"></a> percentile — 要排除像素的百分位数**  
1（默认值）| 数值标量 | 二元数值向量

要排除像素的百分位数，指定为数值标量或二元数值向量。排除像素有助于防止过度曝光或曝光不足的像素扭曲估计结果。

- 如果 `percentile` 是标量，则该值同时用于底部百分位数和顶部百分位数。在这种情况下，`percentile` 必须在范围 [0, 50] 内，以确保底部和顶部百分位数之和不超过 100。
- 如果 `percentile` 是二元向量，则第一个元素是底部百分位数，第二个元素是顶部百分位数。两个百分比都必须在范围 [0, 100) 内，并且它们的和不能超过 100。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### <a id="Q3"></a> 名称-值参数
指定可选的参数对，格式为 Name1, Value1, ... , NameN, ValueN，其中 Name 是参数名称，Value 是对应的值。名称-值参数必须出现在其他参数之后，但各参数对的顺序可以任意。  
示例：Iilluminant = illumgray(I, "Mask", m) 使用图像 `I` 中的像素子集来估计场景照度，这些像素子集是根据二值掩码 `m` 选择的。  

**Mask — 图像掩码**  
m×n 逻辑或数值数组

图像掩码，指定为 m×n 逻辑或数值数组。掩码指示在估计照度时使用输入图像 [A](#Q1) 的哪些像素。排除 [A](#Q1) 中对应掩码值为 0 的像素。默认情况下，掩码全部为 1，即在估计时包含 [A](#Q1) 中的所有像素。  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**Norm — 向量范数（p-范数）的类型**  
1（默认）| 正数标量  

向量范数（p-范数）的类型，指定为正数标量。p-范数影响输入图像 [A](#Q1) 中 RGB 平均值的计算。p-范数定义为  (∑|x|<sup>p</sup>)<sup>1/p</sup>。  
  
**数据类型：**  `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出参数
**<a id="P1"></a> illuminant — 场景照度估计值**  
3 元数值行向量

场景照度的估计值，以 3 元数值行向量形式返回。这三个元素分别对应照度的红色、绿色和蓝色值。

**数据类型：** `double`

## 技巧
- 灰度世界算法假设照度是均匀的，并且 RGB 值是线性的。如果你正在处理非线性的 sRGB 或 Adobe RGB 图像，请在使用 `illumgray` 之前，使用 <a href="../rgb2lin/rgb2lin.html">rgb2lin</a> 函数撤销伽马校正。此外，确保使用 <a href="../lin2rgb/lin2rgb.html">lin2rgb</a> 函数将色度适应后的图像重新转换为 sRGB。
- 当你指定 `Mask` 时，底部百分位数和顶部百分位数将应用于被掩码的图像。
- 你可以通过使用 <a href="../chromadapt/chromadapt.html">chromadapt</a> 函数调整图像的色彩平衡，以去除场景照度。

## 参考文献
[1] Marc Ebner. The Gray World Assumption. Color Constancy. Chichester, West Sussex: John Wiley & Sons, 2007.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../chromadapt/chromadapt.html">chromadapt</a> | <a
href="../illumpca/illumpca.html">illumpca</a> | <a
href="../illumwhite/illumwhite.html">illumwhite</a> | <a
href="../lin2rgb/lin2rgb.html">lin2rgb</a> | <a
href="../rgb2lin/rgb2lin.html">rgb2lin </a>

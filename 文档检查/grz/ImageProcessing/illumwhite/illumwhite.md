## illumwhite
使用 White Patch Retinex 算法估计照度

## 简介
[`illuminant = illumwhite(A)`](#function1)  
[`illuminant = illumwhite(A, topPercentile)`](#function2)   
[`illuminant = illumwhite(___, Mask, mask)`](#function3)    

## 用法
<a id="function1"></a>
[illuminant](#P1) = illumgray([A](#Q1)) 通过假设场景的平均颜色为灰色来估计 RGB 图像 `A` 中的场景照度。  
<a id="function2"></a>
[illuminant](#P1) = illumgray([A](#Q1), [percentile](#Q2)) 通过排除指定的底部和顶部像素的百分位数来估计照度。  
<a id="function3"></a>
[illuminant](#P1) = illumgray(___, Mask, [mask](#Q3)) 仅使用由二进制掩码定义的 ROI 内的像素来估计照度。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — RGB 图像**  
m×n×3 数值数组

RGB 图像，指定为 m×n×3 数值数组。

**数据类型：** `single` | `double` | `uint8` | `uint16`

**<a id="Q2"></a> topPercentile — 最亮颜色的百分位数**  
1（默认值）| 数值标量

用于照度估计的最亮颜色的百分位数，指定为范围在 [0, 100) 内的数值标量。若要返回最大的红色、绿色和蓝色值，可将 `topPercentile` 设置为 0。  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q3"></a> mask — 图像掩码**  
m×n 逻辑或数值数组  

图像掩码，指定为 m×n 逻辑或数值数组。掩码指示在估计照度时使用输入图像 [A](#Q1) 的哪些像素。排除 [A](#Q1) 中对应掩码值为 0 的像素。默认情况下，掩码全部为 1，即在估计时包含 [A](#Q1) 中的所有像素。  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数
**<a id="P1"></a> illuminant — 场景照度估计值**  
3 元数值行向量

场景照度的估计值，以 3 元数值行向量形式返回。这三个元素分别对应照度的红色、绿色和蓝色值。

**数据类型：** `double`

## 参考文献
[1] Marc Ebner. The Gray World Assumption. Color Constancy. Chichester, West Sussex: John Wiley & Sons, 2007.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../whitepoint/whitepoint.html">whitepoint</a> | <a
href="../chromadapt/chromadapt.html">chromadapt</a> | <a
href="../illumgray/illumgray.html">illumgray</a> | <a
href="../illumpca/illumpca.html">illumpca</a> | <a
href="../lin2rgb/lin2rgb.html">lin2rgb</a> | <a
href="../rgb2lin/rgb2lin.html">rgb2lin </a>

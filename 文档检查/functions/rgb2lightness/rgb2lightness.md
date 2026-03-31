## rgb2lightness
将 RGB 颜色值转换为 lightness 值

## 简介
[`lightness = rgb2lightness(rgb)`](#function1)  

## 用法
<a id="function1"></a>
[lightness](#P1) = rgb2lightness([rgb](#Q1)) 将 RGB 颜色值转换为 lightness 值，转换过程中不包含色度分量。其中 lightness 等同于 CIE 1976 L\*a\*b\* 颜色空间中的 L* 分量。

## 参数说明
### 输入参数
**<a id="Q1"></a> rgb — RGB 颜色值**  
m×n×3 数值数组

RGB 颜色值，指定为 m×n×3 的数值数组。输入 `rgb` 必须位于 sRGB 色彩空间，并以 D65 作为参考白点。

**数据类型：** `single` | `double` | `uint8` | `uint16`

### 输出参数
**<a id="P1"></a> lightness — 转换后 m×n 图像数组的 lightness 值**  
m×n 数值数组

转换后的 lightness 值，返回为 m×n 的数值数组。若输入数据类型为 `double`，则输出数据类型为 `double`；否则输出数据类型为 `single`。

**数据类型：** `single` | `double` 

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../rgb2xyz/rgb2xyz.html">rgb2xyz</a> | <a
href="../lab2rgb/lab2rgb.html">lab2rgb</a> | <a 
href="../xyz2lab/xyz2lab.html">xyz2lab </a> | <a 
href="../rgb2lab/rgb2lab.html">rgb2lab</a> | <a 
href="../lab2xyz/lab2xyz.html">lab2xyz</a> | <a 
href="../xyz2rgb/xyz2rgb.html">xyz2rgb</a>



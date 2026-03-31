## dither
转换图像，通过抖动提高表观颜色分辨率

## 简介
[`X = dither(RGB, map)`](#function1)  

## 用法
<a id="function1"></a>
[X](#P1) = dither([RGB](#Q1), [map](#Q2)) 通过在颜色图 map 上执行抖动量化，将 RGB 图像近似为索引图像 X。

## 参数说明
### 输入参数
**<a id="Q1"></a> RGB — RGB 图像**  
m×n×3 非负数值数组

RGB 图像，指定为 m×n×3 非负数值数组。如果 RGB 的数据类型为 double，其取值必须在 [0, 1] 范围内。

**数据类型：** `single` | `double` | `uint8` | `uint16`

**<a id="Q2"></a> map — 输入颜色图**  
c×3 数值数组

输入颜色图，指定为由范围 [0, 1] 内的值组成的 c×3 数值数组。map 的每行都是一个三元素 RGB，分别表示该颜色的红、绿、蓝分量。该颜色图最多有 65536 种颜色。

**数据类型：** `double` 

### 输出参数
**<a id="P1"></a> X — 索引图像**  
m×n 非负整数数组

索引图像，返回由非负整数组成的 m×n 数值数组。如果 map 的长度小于或等于 256，则输出图像的数据类型为 uint8。否则，输出图像的数据类型为 uint16。输出图像 X 中的数值 0 对应于颜色图中的第一个颜色。

**数据类型：** `uint8` | `uint16`

## 算法
dither 通过应用 Floyd-Steinberg 的误差扩散抖动算法提高图像表观颜色分辨率。

## 参考
[1] R. W. Floyd and L. Steinberg, An Adaptive Algorithm for Spatial Grey Scale, International Symposium Digest of Technical Papers, Society for Information Displays, 1975, pp. 36-37.
[2] Lim, Jae S., Two-Dimensional Signal and Image Processing, Englewood Cliffs, NJ, Prentice Hall, 1990, pp. 469–476.

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../rgb2ind/rgb2ind.html">rgb2ind</a> | <a
href="../imapprox/imapprox.html">imapprox</a> 



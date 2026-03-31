## rgb2ind
将 RGB 图像转换为索引图像

## 简介
[`[X,cmap] = rgb2ind(RGB, tol)`](#function1)  

## 用法
<a id="function1"></a>
[[X](#P1),[cmap](#P2)] = rgb2ind([RGB](#Q1), [tol](#Q2)) 使用均匀量化并结合抖动，将 RGB 图像转换为索引图像，其中 tol 为量化容差参数。

## 参数说明
### 输入参数
**<a id="Q1"></a> RGB — RGB 图像**  
m×n×3 数值数组

RGB 图像，指定为 m×n×3 的数值数组。

rgb2ind 函数要求数据类型为 double 和 single 的 RGB 图像取值在范围 [0, 1] 内。如果一个图像的值超出 [0, 1]，则可以使用 <a href="../rescale/rescale.html">rescale</a> 函数将其线性缩放到期望范围。

**数据类型：** `single` | `double` | `uint8` | `uint16`

**<a id="Q2"></a> tol — 容差**  
[0, 1] 范围内的标量

均匀量化所用的容差参数，指定为 [0, 1] 范围内的标量。返回的颜色图 <a href="../cmap/cmap.html">cmap</a> 包含的颜色不超过 $(\mathrm{floor}(1/tol)+1)^3$ 种。

### 输出参数
**<a id="P1"></a> X — 索引图像**  
由非负整数组成的 m×n 矩阵

索引图像，返回由非负整数组成的 m×n 矩阵。如果 cmap 的长度小于或等于 256，则输出 X 的数据类型为 `uint8`。否则输出 X 的数据类型为 `uint16`。输出数组 X 中的数值 0 对应于颜色图中的第一个颜色。

**数据类型：** `uint8` | `uint16`

**<a id="P2"></a> cmap — 颜色图**  
c×3 矩阵

颜色图，返回为由 [0, 1] 范围内的值组成的 c×3 矩阵。cmap 的每行都是一个三元素 RGB 向量，分别表示该颜色的红、绿、蓝分量，颜色图最多有 65536 种颜色。

**数据类型：** `double`

## 参考
[1] Spencer W. Thomas, Efficient Inverse Color Map Computation, Graphics Gems II, (ed. James Arvo), Academic Press: Boston. 1991.

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../cmunique/cmunique.html">cmunique</a> | <a
href="../dither/dither.html">dither</a> | <a 
href="../imapprox/imapprox.html">imapprox</a> | <a 
href="../ind2rgb/ind2rgb.html">ind2rgb</a>

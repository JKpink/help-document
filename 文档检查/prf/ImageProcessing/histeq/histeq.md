## histeq 
使用直方图均衡增强对比度

## 简介
[ `J = histeq(I) `](#function1)  
[ `J = histeq(I, n)`](#function2)  
[ `J = histeq(I, hgram)`](#function3)  

## 用法
<a id="function1"></a>
[J](#Q4) = histeq([I](#Q1)) 变换灰度图像 `I`，以使输出灰度图像 J 的直方图具有 64 个 bin 且大致平坦。  
<a id="function2"></a>
[J](#Q4) = histeq([I](#Q1), [n](#Q3)) 变换灰度图像 I，以使输出灰度图像 `J` 具有 n 个 bin 的直方图大致平坦。当 n 远小于 `I` 中的离散灰度级数时，`J` 的直方图更平坦。并且函数 `histeq` 仅支持灰度图像，对彩色图像进行直方图均衡时需要分别对 3 个通道进行直方图均衡化。  
<a id="function3"></a>
[J](#Q4) = histeq([I](#Q1), [hgram](#Q2))  变换灰度图像 `I`，以使输出灰度图像 `J` 的直方图近似匹配目标直方图 `hgram`。输出图像的直方图中 bin 的数量等于 length(hgram)。  

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 灰度图像**  
数值数组  

灰度图像，指定为任意维度的数值数组。

**数据类型:** `uint8`

**<a id="Q2"></a> hgram — 目标直方图**  
数值向量  

目标直方图，指定为数值向量。目标直方图必须在适当的范围内具有等间距 bin 跨度强度值。强度值范围取决于输入图像的数据类型。

- double - [0, 1]。  
- uint8 - [0, 255]。

默认情况下，目标直方图中 bin 的数量等于 length(hgram)。

**数据类型:** `single` | `double`

**<a id="Q3"></a> n — 离散灰度级的数量**  
64 (默认) | 正整数  

离散灰度级的数量，指定为正整数。

**数据类型:** `single` | `double`   

### 输出参数
**<a id="Q4"></a> J — 变换后的灰度图像**  
数值数组  

变换后的灰度图像，以大小和类与输入图像 `I` 相同的数值数组形式返回。

**数据类型:**  `double`

## 算法
当您提供目标直方图 hgram 时，`histeq` 选择灰度变换 T 以最小化

∣c<sub>1</sub>(T(k))−c<sub>0</sub>(k)∣,

c<sub>0</sub> 是输入图像 `I` 的累积直方图，c<sub>1</sub> 是 hgram 中所有强度 k 上的累积总和。这种最小化受以下条件的限制：

- T 必须单调
- c<sub>1</sub>(T(a)) 对 c<sub>0</sub>(a) 的过冲不能超过 a 处直方图计数之间差距的一半。

`histeq` 使用变换 b = T(a) 将 X（或颜色图）中的灰度级映射到其新值。

如果您不指定 `hgram`，则 `histeq` 创建平坦的 `hgram`，

hgram = ones(1,n)\*prod(size(A))/n;  

然后应用前面的算法。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../adapthisteq/adapthisteq.html">adapthisteq</a> | <a
href="../brighten/brighten.html">brighten</a> | <a 
href="../imadjust/imadjust.html">imadjust</a> | <a 
href="../imhist/imhist.html">imhist</a> 



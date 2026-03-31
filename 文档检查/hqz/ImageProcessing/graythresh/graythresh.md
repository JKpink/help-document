## graythresh
使用 Otsu 方法计算全局图像阈值

## 简介
[`T = graythresh(I)`](#section1)  
[`[T, EM] = graythresh(I)`](#section2)

## 用法
<a id="section1"></a>
[T](#section3) = graythresh([I](#section4))基于大津法（Otsu's method）[[1]](#section6) 从灰度图像 `I` 计算全局阈值 `T`。大津法会选择一个阈值，使阈值化后的黑白像素的类内方差最小化。该全局阈值 `T` 可与 <a href="../imbinarize/imbinarize.html">imbinarize</a> 配合使用，将灰度图像转换为二值图像。

<a id="section2"></a>
[[T](#section3), [EM](#section5)] = graythresh([I](#section4)) 还会返回有效性指标 `EM`。

## 参数说明
### 输入参数
**<a id="section4"></a> I —— 灰度图像**  
数值数组

灰度图像：指定为任意维度的数值数组。对于数据类型为 `double` 和 `single` 的图像，`graythresh` 函数要求其数值范围为 `[0, 1]`。若 `I` 的数值超出 `[0, 1]` 范围，可使用 `rescale` 函数将数值重新缩放至预期范围。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` 

### 输出参数
**<a id="section3"></a> T —— 全局阈值</a>**  
非负数

全局阈值：返回为范围 `[0, 1]` 内的非负数。 

**数据类型：** `double`

**<a id="section5"></a> EM —— 有效性度量**  
非负数

阈值的有效性指标：返回为范围 `[0, 1]` 内的非负数。下限仅在图像仅有单一灰度级时可达，上限仅在二值图像（双值图像）时可达。

**数据类型：** `double`

## 提示
默认情况下，函数  <a href="../imbinarize/imbinarize.html">imbinarize</a> 会使用通过大津法（Otsu’s method）得到的阈值创建二值图像。该默认阈值与 `graythresh` 返回的阈值完全一致。但 `imbinarize` 仅返回二值图像，若你想获取阈值（level）或有效性指标（effectiveness metric），需在调用 `imbinarize` 前先使用 `graythresh`。

## 参考
<a id="section6"></a>  

[1] Otsu N. A threshold selection method from gray-level histograms. IEEE Transactions on Systems, Man, and Cybernetics, 1979, 9(1): 62-66.

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imbinarize/imbinarize.html">imbinarize</a> | <a 
href="../imquantize/imquantize.html">imquantize</a> | <a 
href="../multithresh/multithresh.html">multithresh</a> | <a 
href="../rgb2ind/rgb2ind.html">rgb2ind</a> 

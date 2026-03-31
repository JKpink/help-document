## imbinarize
通过阈值化将灰度图像二值化

## 简介
[ `BW = imbinarize(I)`](#function1)  
[ `BW = imquantize(I, method)`](#function2)  
[ `BW = imquantize(I, T)`](#function3)  
[ `BW = imquantize(I, "adaptive", Name, Value)`](#function4)
## 用法
<a id="function1"></a>
[BW](#P1) = imbinarize([I](#Q1)) 将所有高于全局阈值的值替换为 1 并将所有其他值设置为 0，从二维或三维灰度图像 `I` 创建二值图像。`imbinarize` 默认使用 Otsu 方法，该方法选择特定阈值来最小化阈值化的黑白像素的类内方差 [[1]](#ref1)。`imbinarize` 使用包含 256 个 bin 的图像直方图来计算 Otsu 阈值。若使用不同直方图，请参阅 <a href="../otsuthresh/otsuthresh.html">otsuthresh</a>。  
<a id="function2"></a>
[BW](#P1) = imbinarize([I](#Q1), [method](#Q2)) 使用 `method` 指定的阈值化方法（"global" 或 "adaptive"）从图像 `I` 创建二值图像。  
<a id="function3"></a>
[BW](#P1) = imbinarize([I](#Q1), [T](#Q3)) 使用阈值 `T` 从图像 `I` 创建二值图像。`T` 可以是指定为标量亮度值的全局图像阈值，也可以是指定为亮度值矩阵的局部自适应阈值。  
<a id="function4"></a>
[BW](#P1) = imbinarize([I](#Q1), "adaptive", [Name, Value](#Q4)) 使用名称-值参量从图像 `I` 创建二值图像，以控制自适应阈值的各个方面。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
二维灰度图像 | 三维灰度图像体

输入图像，指定为二维灰度图像或三维灰度图像体。imbinarize 需要数据类型为 `double` 和 `single` 的图像的值在 [0, 1] 的范围内。如果 `I` 的值超出范围 [0, 1]，则可以使用 <a href="../rescale/rescale.html">rescale</a> 函数将值重新缩放到需要的范围。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

**<a id="Q2"></a> method — 用于二值化图像的方法**  
"global"（默认）| "adaptive"

用于二值化图像的方法，指定为下列值之一。

| **值**     | **意义**                                                                                                                                                                                                                                                                                           |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "global"   | 用 Otsu 方法计算全局图像阈值。有关 Otsu 方法的详细信息，请参阅 <a href="../graythresh/graythresh.html">graythresh</a>。                                                                                                                                                                              |
| "adaptive" | 使用每个像素周围的局部一阶图像统计量来计算局部自适应图像阈值。有关详细信息，请参阅 <a href="../adaptthresh/adaptthresh.html">adaptthresh</a>。如果图像包含 `Inf` 或 `NaN`，则 `imbinarize` 对于 "adaptive" 方法的行为是未定义的。`Inf` 或 `NaN` 的传播可能不会局限于 `Inf` 和 `NaN` 像素周围的邻域。 |

**数据类型：** `char` | `string`

**<a id="Q3"></a> T — 阈值**  
数值标量 | 数值数组

亮度阈值，指定为由范围 [0, 1] 内的值组成的数值标量或数值数组。

- 如果 `T` 是数值标量，则 imbinarize 将 `T` 解释为全局图像阈值。使用 <a href="../graythresh/graythresh.html">graythresh</a> 或 <a href="../otsuthresh/otsuthresh.html">otsuthresh</a> 计算全局图像阈值。
- 如果 `T` 是数值数组，则 imbinarize 将 `T` 解释为局部自适应阈值。使用 <a href="../adaptthresh/adaptthresh.html">adaptthresh</a> 计算局部自适应阈值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### <a id="Q4"></a> 名称-值参数
指定可选的参数对，格式为 Name1, Value1, ... , NameN, ValueN，其中 Name 是参数名称，Value 是对应的值。名称-值参数必须出现在其他参数之后，但各参数对的顺序可以任意。  
示例: BW = imbinarize(I, "adaptive", "Sensitivity", 0.4); 将灵敏度因子指定为 0.4。

**Sensitivity — 自适应阈值的敏感度因子**  
0.50（默认）| [0, 1]范围内的数值

自适应阈值化的敏感度因子，指定为 [0, 1] 范围内的数值。高敏感度值会使更多像素阈值化为前景，但存在混入部分背景像素的风险。  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**ForegroundPolarity — 确定哪些像素被视为前景像素**  
"bright"（默认） | "dark"  

确定将哪些像素视为自适应阈值化的前景像素，指定为下列值之一。

| 值       | 意义           |
| :------- | :------------- |
| "bright" | 前景比背景亮。 |
| "dark"   | 前景比背景暗。 |

**数据类型：** `char` | `string` 

### 输出参数
**<a id="P1"></a> BW — 输出二值图像**  
逻辑矩阵 | 逻辑数组

输出二值图像，以与 [I](#Q1) 大小相同的逻辑矩阵或逻辑数组形式返回。

**数据类型：** `logical`

<!-- ## 算法
"adaptive" 方法使用局部自适应阈值对图像进行二值化。`imbinarize` 使用像素邻域的局部均值强度计算每个像素的阈值。这种方法也称为布拉德利方法 [[2]](#ref2)。"adaptive" 方法使用约为图像大小 1/8 的邻域大小（由 2*floor(size(I)/16)+1 求得）。要使用其他一阶局部统计量或不同的邻域大小，请参阅 <a href="../adaptthresh/adaptthresh.html">adaptthresh</a>。 -->

## 参考文献
<a id="ref1"></a>[1] Otsu, N. A Threshold Selection Method from Gray-Level Histograms. IEEE Transactions on Systems, Man, and Cybernetics, 1979, 9(1): 62–66.  
<!-- <a id="ref2"></a>[2] Bradley, D., G. Roth. Adapting Thresholding Using the Integral Image[J]. Journal of Graphics Tools, 2007, 12(2): 13–21. -->

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../graythresh/graythresh.html">graythresh</a> | <a 
href="../otsuthresh/otsuthresh.html">otsuthresh</a> | <a 
href="../adaptthresh/adaptthresh.html">adaptthresh</a> 
<!-- | <a 
href="../Image Segmenter/Image Segmenter.html">Image Segmenter</a>  -->
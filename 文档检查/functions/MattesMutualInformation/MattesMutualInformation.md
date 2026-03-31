## MattesMutualInformation
互信息度量配置

## 用法 
MattesMutualInformation 创建用于配置互信息度量的对象，可以将其传递给 `imregister` 函数以解决图像配准问题。

## 属性
**NumberOfSpatialSamples — 空间样本的数量**  
500（默认值）| 正整数  

用于计算互信息度量的空间样本数量，指定为一个正整数，默认为 500。
`NumberOfSpatialSamples` 定义了 `imregister` 函数用于计算该度量的随机像素数量。增大此值时，配准结果的可重复性会提高,但会牺牲性能。仅当 `UseAllPixels` 为 0（false）时，`imregister` 函数才会使用 `NumberOfSpatialSamples`。

**数据类型：** `double` | `single` | `uint8` | `uint16` | `uint32` | `uint64` | `int8` | `int16` | `int32` | `int64`  

**NumberOfHistogramBins — 直方图区间数量**  
50（默认值）| 正整数  

用于计算互信息度量的直方图区间数量，指定为一个正整数标量，默认为 50。  
`NumberOfHistogramBins` 定义了 `imregister` 函数在计算联合分布直方图时所使用的区间数量。最小值为 5，默认为 50。

**数据类型：** `double` | `single` | `uint8` | `uint16` | `uint32` | `uint64` | `int8` | `int16` | `int32` | `int64`

**UseAllPixels — 在重叠区域中使用所有像素**  
1 或 true（默认）| 0 或 false  

在计算互信息度量时，指定是否在图像的重叠区域中使用所有像素，以逻辑标量形式指定。默认为 1 或 true。
如果将此属性设置为 0（false），可以显著提高性能。当 `UseAllPixels` 为 0 时， `NumberOfSpatialSamples` 属性控制 `imregister` 函数用于计算度量的随机像素位置的数量。当`UseAllPixels` 为 0 时，配准结果可能无法重复。这是因为 `imregister` 函数会从图像中随机选择一部分像素来计算度量。



## 参考文献

[1] Rahunathan S, Stredney D, Schmalbrock P, et al. Image registration using rigid registration and maximization of mutual information. The 13th Annual Medicine Meets Virtual Reality Conference. Long Beach, CA: MMVR, 2005.  
[2] Mattes D, Haynor D R, Vesselle H, et al. Non-rigid multimodality image registration. Medical Imaging 2001: Image Processing. Bellingham, WA: SPIE, 2001: 1609-1620.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
### 函数
<a href="../imregister/imregister.html">imregister</a> | <a
href="../imregconfig/imregconfig.html">imregconfig</a> 
### 对象
 <a 
href="../MeanSquares/MeanSquares.html">MeanSquares</a> | <a 
href="../OnePlusOneEvolutionary/OnePlusOneEvolutionary.html">OnePlusOneEvolutionary</a> | <a 
href="../ RegularStepGradientDescent/ RegularStepGradientDescent.html"> RegularStepGradientDescent</a> 

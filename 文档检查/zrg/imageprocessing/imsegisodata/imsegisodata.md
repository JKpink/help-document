## imsegisodata
基于 ISODATA 聚类的图像分割

## 简介
[`[L,centers] = imsegisodata(I)`](#function2)  
[`[L,centers] = imsegisodata(I, Name,Value)`](#function1)

## 用法
<a id="function2"></a>
[[L](#Q1),[centers](#Q2)]=imsegisodata([I](#Q3)) 通过 ISODATA 聚类算法自动将图像中特征相似的像素（如颜色、灰度相近的区域）归为同一类，最终返回与输入图像I空间维度一致的单通道整数型矩阵和每个类别的聚类中心。

<a id="function1"></a>
[[L](#Q1), [centers](#Q2)] = imsegisodata([I](#Q3), [Name , Value](#Q4)) 使用一个或多个可选名称-值参数对 `ISODATA` 算法进行精细调优。例如，InitialNumClusters = 5 表示以五个聚类簇启动聚类过程。

## 参数说明
### 输入参数
**<a id="Q3"></a> I — 待分割图像**  
二维灰度图像 | 二维 RGB 图像 | 二维高光谱图像 | 超立方体对象 | 多立方体对象

待分割图像，指定为二维灰度图像、二维 RGB 图像、二维高光谱图像、超立方体对象或多立方体对象。若 `I` 为多立方体对象，则其所有光谱波段必须具有相同的数据分辨率。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q4"></a>**
### 名称-值参数

将可选参数对指定为 Name1,Value1,...,NameN,ValueN 的形式，其中 `Name` 为参数名称，`Value` 为对应值。名称-值参数必须位于其他参数之后，但参数对的顺序可任意排列。

**示例：** imsegisodata(I, 'InitialNumClusters', 5) 表示以五个聚类簇启动聚类过程。

**<a id="Q5"></a> NormalizeInput — 输入数据归一化**  
true（默认）| false

输入数据归一化，指定为数值或逻辑值 1（true）或 0（false）。若将 NormalizeInput 指定为 true，该函数将逐通道对图像进行零均值和单位方差的归一化处理。当图像各通道具有不同强度范围时，建议对输入图像进行归一化。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q6"></a> InitialNumClusters — 初始聚类数量**  
5（默认） | 正整数

初始聚类数量，指定为正整数。`ISODATA` 算法以指定的聚类数量开始，随着迭代进行不断分裂或合并聚类，最终达到最优聚类数量。接近最优值的初始聚类数量可提高算法精度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`


**<a id="Q7"></a> MaxIterations — 最大迭代次数**  
10（默认） | 正整数

最大迭代次数，指定为正整数。增加最大迭代次数会提高 `ISODATA` 算法的精度，但同时会增加执行时间。需要注意的是，根据输入图像的特性，超过一定迭代次数后精度可能不会显著提升。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q8"></a> MinSamples — 类最小样本数**  
正整数

类最小样本数，指定为正整数。若输入图像尺寸为 M×N×C（其中 M 为行数，N 为列数，C 为通道数或波段数），则 `MinSamples` 的默认值为 M*N/(10*InitialNumClusters)。若某聚类包含的样本数少于 `MinSamples`，函数将移除该聚类。若输入图像中的较小聚类具有重要意义，请减小 `MinSamples` 的值；若要忽略较小聚类，则增大该参数值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q9"></a> MaxStandardDeviation — 类最大标准差**  
非负标量

类最大标准差，指定为非负标量。若将 `NormalizeInput` 指定为 true，则 `MaxStandardDeviation` 的默认值为 1；若将 `NormalizeInput` 指定为 false，则默认值为输入图像的标准差。若某聚类内样本的标准差大于 `MaxStandardDeviation`，函数将把该聚类分裂为两个。需要降低聚类可变性时减小该值；需要允许较大可变性时增大该值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q10"></a> MinClusterSeparation — 最小聚类间距**  
1（默认） | 非负标量

最小聚类间距，指定为非负标量。若两个聚类中心之间的距离小于或等于 `MinClusterSeparation`，函数将合并这两个聚类。需要降低聚类可变性时减小该值；需要允许较大可变性时增大该值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="11"></a> MaxPairsToMerge — 单次迭代中可合并的候选聚类对最大数量**  
2（默认） | 正整数

单次迭代中可合并的候选聚类对最大数量，指定为正整数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出参量
**<a id="Q1"></a> L — 标签图像**  
正整数二维矩阵

标签图像，以正整数二维矩阵形式返回。若输入图像尺寸为 M×N×C（其中 M 为行数，N 为列数，C 为通道数或波段数），则 `L` 的尺寸为 M×N。

**数据类型：** `double`

**<a id="Q2"></a> centers — 聚类中心**  
数值矩阵

聚类中心，以数值矩阵形式返回，其数据类型与输入图像相同。该矩阵尺寸为 K×C，其中 `K` 表示函数最终确定的最优聚类数量，`C` 表示输入图像的通道数或波段数。

## 参考
Tou J T, Gonzalez R C. Pattern recognition principles. Applied mathematics and computation, no. 7. Reading, MA: Addison-Wesley Pub. Co, 1974.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../imsegkmeans/imsegkmeans.html">imsegkmeans</a> 
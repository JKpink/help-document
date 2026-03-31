## imsegkmeans
基于K均值聚类的图像分割

## 简介
[`L = imsegkmeans(I, k)`](#function1)  
[`[L, centers] = imsegkmeans(I, k)`](#function2)  
[`L = imsegkmeans(I, k, Name, Value)`](#function3)

## 用法
<a id="function1"></a>
[L](#Q1) = imsegkmeans([I](#Q2), [k](#Q3)) 通过执行 k 均值聚类将图像 `I` 分割成 k 个簇，并在 L 中返回分割后带标签的输出。

<a id="function2"></a>
[[L](#Q1), [centers](#Q4)] = imsegkmeans([I](#Q2), [k](#Q3)) 还返回簇质心位置 centers。

<a id="function3"></a>[L](#Q1) = imsegkmeans([I](#Q2), [k](#Q3), [Name, Value](#Q5)) 使用名称-值参量来控制 k 均值聚类算法的各个方面。

## 参数说明
### 输入参数
**<a id="Q2"></a> I — 要分割的图像**  
二维灰度图像 | 二维彩色图像 | 二维多光谱图像

要分割的图像，指定为二维灰度图像，二维彩色图像或二维多光谱图像。

**数据类型：** `uint8` | `single` | `int16` | `int8` | `uint16`

**<a id="Q3"></a> k — 簇的数量**  
正整数

要创建的簇的数量，指定为正整数。

**<a id="Q5"></a> 名称-值参数**  
将可选的参量对组指定为 Name1, Value1,..., NameN, ValueN，其中 Name 是参量名称，Value 是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。

**示例：** imsegkmeans(I, k, "NumAttempts", 5) 重复聚类过程五次。

**NormalizeInput — 归一化输入数据**  
true 或 1(默认) | fasle 或 0

将输入数据归一化为零均值和单位方差，指定为数值或逻辑值 1(true) 或 0(false)。如果您指定 true，则 imsegkmeans 单独归一化输入的每个通道。

**NumAttempts — 重复聚类过程的次数**  
3 (默认) | 正整数

使用新初始簇质心位置重复聚类过程的次数，指定为正整数。

**MaxIterations — 最大迭代次数**  
100 (默认) | 正整数

迭代的最大次数，指定为正整数。

**Threshold — 准确度阈值**  
1e-4 (默认) | 正数

准确度阈值，指定为正值。当每个簇中心在连续迭代中的移动小于阈值时，算法停止。

### 输出参量
**<a id="Q1"></a> L — 标签矩阵**  
正整数矩阵

标签矩阵，指定为正整数矩阵。标签为 1 的像素属于第一个簇，标签为 2 的像素属于第二个簇，对全部 k 个簇依此类推。`L` 的前两个维度与图像 `I` 相同。L 的数据类型取决于簇的数量。

| **L的数据类型** | **簇的数量** |
|:-|:-|
| uint8 | k <= 255 |
| uint16 | 256 <= k <= 65535 |
| uint32 | 65536 <= k <= 2^32-1 |
| double | 2^32 <= k |

**<a id="Q4"></a> centers — 簇质心位置**  
数值矩阵

簇质心位置，以数值矩阵形式返回，大小为 k×c，其中 k 是簇的数量，c 是通道数量。centers 与图像 `I` 属于同一种数据类型。

## 参考
Arthur D, Vassilvitskii S. K-means++: the advantages of careful seeding//Proceedings of the eighteenth annual ACM-SIAM symposium on discrete algorithms. SODA '07. USA: Society for Industrial and Applied Mathematics, 2007: 1027-1035.

## 版本历史
在北太天元图像处理工具箱 V1.1 推出

## 相关主题
 <a href="../imsegkmeans3/imsegkmeans3.html">imsegkmeans3</a> | <a 
href="../imsegisodata/imsegisodata.html">imsegisodata</a> | <a 
href="../gabor/gabor.html">gabor</a> | <a 
href="../imgaborfilt/imgaborfilt.html">imgaborfilt</a> | <a 
href="../labeloverlay/labeloverlay.html">labeloverlay</a> | <a 
href="../label2rgb/label2rgb.html">label2rgb</a> | <a 
href="../superpixels/superpixels.html">superpixels</a> | <a 
href="../lazysnapping/lazysnapping.html">lazysnapping</a> | <a 
href="../watershed/watershed.html">watershed</a> | <a 
href="../labelmatrix/labelmatrix.html">labelmatrix</a>
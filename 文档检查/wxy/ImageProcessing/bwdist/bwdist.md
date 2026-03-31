## bwdist  
二值图像的距离变换

## 简介  
[ `D = bwdist(BW)`](#function1)  
[ `[D, idx] = bwdist(BW)`](#function2)  
[ `[D, idx] = bwdist(BW, method)`](#function3)

## 用法  
<a id="function1"></a>
[D](#Q1) = bwdist([BW](#Q2)) 计算二值图像 [`BW`](#Q2) 的欧几里得距离变换。对于 [`BW`](#Q2) 中的每个像素，距离变换会指定一个数值，该数值表示该像素与 [`BW`](#Q2) 中最近的非零像素之间的距离。  
<a id="function2"></a>
[[D](#Q1), [idx](#Q4)]  = bwdist([BW](#Q2)) 还以索引数组 [`idx`](#Q4) 形式计算最近像素图，[`idx`](#Q4) 的每个元素都包含 [`BW`](#Q2) 的最近非零像素的线性索引。最近像素图也称为最近邻变换（Nearest Neighbor Transform, NNT） 或特征变换（Feature Transform, FT）。
<a id="function3"></a>  
[[D](#Q1), [idx](#Q4)]  = bwdist([BW](#Q2), [method](#Q3)) 使用 [`method`](#Q3) 指定的替代距离度量来计算距离变换。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 二值图像**  
数值数组 | 逻辑数组

二值图像，指定为任意维度的数值或逻辑数组。对于数值输入，任何非零像素都被视为 1(true)。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q3"></a>method — 距离度量**  
'euclidean'（默认）| 'chessboard' | 'cityblock' | 'quasi-euclidean'

距离度量，指定为下列值之一:

| **方法** | **描述** |
|:-|:-|
| 'chessboard' | 在二维空间中，(x, y) 和 (a, b) 之间的棋盘距离是 $\max(\|x-a\|,\|y-b\|)$ |
| 'cityblock' | 在二维空间中，(x, y)和 (a, b) 之间的城市街区距离（曼哈顿距离）是 $\|x-a\|-\|y-b\|$ |
| 'euclidean' | 在二维空间中，(x, y)和 (a, b) 之间的欧几里得距离是 $\sqrt{(x-a)^2+(y-a)^2}$ |
| 'quasi-euclidean' | 在二维空间中，(x, y) 和 (a, b) 之间的准欧几里得距离为，如果$\|x-a\|>\|y-b\|$,则距离为$\|x-a\|+(\sqrt2-1)\|y-b\|$，否则为$(\sqrt2-1)\|x-a\|+\|y-b\|$ |

**数据类型：** `char` | `string`

### 输出参数  
**<a id="Q1"></a>D — 距离数组**  
数值数组

距离，以与 [`BW`](#Q2) 大小相同的数值数组形式返回。BW 中的非零像素（目标像素）对应的 D 中元素值为 0，零像素对应值为到最近非零像素的距离，由距离度量 [`method`](#Q3) 定义。

**数据类型：** `double`

**<a id="Q4"></a>idx — 索引数组**  
数值数组

索引数组，以与 `BW` 大小相同的数值数组形式返回。`idx` 的每个元素都包含 `BW` 的最近非零像素的线性索引。idx 的类取决于输入图像中的元素数，并按如下方式确定:

| **类** | **范围** |
|:-|:-|
| uint32 | $numel(BW)<=2^{32}-1$ |
| uint64 | $numel(BW)>=2^{32}$ |

**数据类型：** `uint32` | `uint64`

## 提示  
 - `bwdist` 使用快速算法来计算精确欧几里得距离变换，尤其是在二维情况下。其他方法主要是出于教学原因而提供。然而，对于多维输入图像，尤其是那些具有许多非零元素的图像，替代距离变换有时要快得多。

## 算法  
 - 对于欧几里得距离变换，`bwdist` 使用快速算法。[[1]](#Q5)
 - 对于城市街区、棋盘和准欧几里得距离变换，`bwdist` 使用两遍序贯扫描算法（Rosenfeld-Pfaltz 算法）。[[2]](#Q6)
 - 不同距离测度是通过在扫描中使用不同权重集来实现的，如 [[3]](#Q7) 中所述。

## 参考文献  
<a id="Q5"></a>[1] Maurer, Calvin, Rensheng Qi, et al. A Linear Time Algorithm for Computing Exact Euclidean Distance Transforms of Binary Images in Arbitrary Dimensions[J]. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2003, 25(2): 265-270.  
<a id="Q6"></a>[2] Rosenfeld, Azriel, John Pfaltz. Sequential operations in digital picture processing[J]. Journal of the Association for Computing Machinery, 1966, 13(4): 471-494.  
<a id="Q7"></a>[3] Paglieroni, David. Distance Transforms: Properties and Machine Vision Applications[J]. Computer Vision, Graphics, and Image Processing: Graphical Models and Image Processing, 1992, 54(1): 57-58.  

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题   
<a href="../bwulterode/bwulterode.html">bwulterode</a> | <a 
href="../watershed/watershed.html">watershed</a>

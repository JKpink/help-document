## bwarea 
计算二值图像中对象的面积

## 简介
[ `total = bwarea(BW)`](#function1)

## 用法
<a id="function1"></a>
[total](#Q1) = bwarea([BW](#Q2)) 估计二值图像 `BW` 中对象的面积。`total` 是标量，其值大致对应于图像中 `on` 像素的总数，但可能不完全相同，因为不同像素图案的加权不同。

## 参数说明
### 输入参数
**<a id="Q2"></a>BW — 二值图像**  
二维数值矩阵 | 二维逻辑矩阵

二值图像，指定为二维数值或逻辑矩阵。对于数值输入，任何非零像素都被视为 1(true)。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参量
**<a id="Q1"></a>total — on 像素的估计数量**  
数值标量

二值图像 [`BW`](#Q2) 中 `on` 像素的估计数量，以数值标量形式返回。

**数据类型：** `double`

## 参考文献
[1] Pratt W K. Digital Image Processing. New York: John Wiley & Sons, Inc., 1991: 634.

## 版本历史
在北太天元图像处理工具箱 V1.1 推出 

## 相关主题
<a href="../bweuler/bweuler.html">bweuler</a> | <a
href="../bwperim/bwperim.html">bwperim</a> 

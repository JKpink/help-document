## imgaussfilt3
3 维图像的 3 维高斯滤波

## 简介
[ `B = imgaussfilt3(A, sigma)`](#function1)

## 用法
<a id="function1"></a>
[B](#Q3) = imgaussfilt3([A](#Q1), [sigma](#Q2)) 使用由 `sigma` 指定标准差的三维高斯平滑核对三维图像 A 进行滤波。

## 参数说明
### 输入参数
**<a id="Q1"></a>A — 要滤波的图像**  
三维数值数组

要滤波的图像，指定为三维数值数组。

**数据类型：** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

**<a id="Q2"></a>sigma — 高斯分布的标准差**  
0.5（默认）| 正数

高斯分布的标准差，指定为正数或由正数组成的三元素向量。如果 `sigma` 是标量，则 `imgaussfilt3` 使用一个三次高斯核。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出参数
**<a id="Q3"></a>B — 滤波后的图像**  
数值数组

滤波后的图像，返回为与输入图像具有相同的数据类型和大小的数值数组。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出 

##相关主题
<a href="../imgaussfilt/imgaussfilt.html">imgaussfilt</a> | <a 
href="../imfilter/imfilter.html">imfilter</a>
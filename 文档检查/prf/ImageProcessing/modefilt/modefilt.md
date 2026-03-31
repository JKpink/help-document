## modefilt
模式滤波

## 简介
[ `B = modefilt(A)`](#function1)  
[ `B = modefilt(A, filtSize)`](#function2)  
[ `B = modefilt(___, padopt)`](#function3)

## 用法
<a id="function1"></a>
[B](#Q4) = modefilt([A](#Q1)) 对二维图像执行模式滤波。`B` 中的每个输出像素包含 `A` 中对应像素周围邻域内的模式（最常出现的值）。`modefilt` 通过镜像边界元素来填充 `A`。
模式滤波可用于处理分类数据，因为其他类型的滤波（如中值滤波）无法使用。  
<a id="function2"></a>
[B](#Q4) = modefilt([A](#Q1), [filtSize](#Q2)) 还指定了滤波器邻域的大小。  
<a id="function3"></a>
[B](#Q4) = modefilt(___, [padopt](#Q3)) 还指定了 `modefilt` 如何填充数组边界。

## 参数说明
### 输入参数
**<a id="Q1"></a>A — 二维图像**  
二维逻辑数组 | 二维数值数组

二维图像，指定为逻辑数组或数值数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`

**<a id="Q2"></a>filtSize — 滤波器大小**  
正奇数向量

滤波器大小，以正奇整数向量表示。对于二维图像，应指定形式为[高度 宽度]，二维图像的默认值为 [3 3]。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q3"></a>padopt — 填充方法**  
"symmetric"（默认）| "replicate" | "zeros"

填充方法，指定为以下值之一：

| **值** | **描述** |
|:--|:--|
| "symmetric" |用自身的镜像翻转填充数组。|
| "replicate" |通过重复边界元素来填充数组。|
| "zeros" | 用值 0 填充数组边界。|

**数据类型：** `char` | `string`

### 输出参数
**<a id="Q4"></a>B — 滤波后的图像**  
数值矩阵

经过滤波处理的图像，以与输入图像 [A](#Q1) 相同大小的数值数组形式返回。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出 

##相关主题
<a href="../ordfilt2/ordfilt2.html">ordfilt2</a> | <a 
href="../medfilt2/medfilt2.html">medfilt2</a> | <a 
href="../medfilt3/medfilt3.html">medfilt3</a> 
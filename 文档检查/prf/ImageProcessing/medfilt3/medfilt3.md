## medfilt3
3 维中值滤波

## 简介
[ `B = medfilt3(A)`](#function1)  
[ `B = medfilt3(A, [m n p])`](#function2)

## 用法
<a id="function1"></a>
[B](#Q3) = medfilt3([A](#Q1)) 使用 3×3×3 滤波器对三维图像 `A` 进行滤波。默认情况下，`medfilt3` 通过在边界处以镜像方式复制值来填充图像。  
<a id="function2"></a>
[B](#Q3) = medfilt3([A](#Q1), [[m n p]](#Q2)) 对三维图像 `A` 执行三维中值滤波。`B` 中的每个输出体素包含 `A` 中对应体素周围 m×n×p 邻域的中值。

## 参数说明
### 输入参数
**<a id="Q1"></a>A — 输入图像**  
三维数值数组 | 三维逻辑数组

输入图像，指定为三维数值或逻辑数组。

**数据类型：** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` 

**<a id="Q2"></a>[m n p] — 邻域大小**  
[3 3 3]（默认）| 三元向量

邻域大小，指定为由正奇整数组成的三元向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出参数
**<a id="Q3"></a>B — 输出图像**  
三维数值数组

输出图像，以与输入图像 [`A`](#Q1) 大小和数据类型相同的数值三维数组形式返回。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出 

##相关主题
<a href="../medfilt2/medfilt2.html">medfilt2</a>

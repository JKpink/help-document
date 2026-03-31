## immse  
均方误差

## 简介  
[ `err = immse(X, Y)`](#function1) 

## 用法  
<a id="function1"></a>
[err](#Q1) = immse([X](#Q2), [Y](#Q3)) 计算数组 [`X`](#Q2) 和 [`Y`](#Q3) 之间的均方误差 (MSE)。MSE 值越低，表明 [`X`](#Q2) 和 [`Y`](#Q3) 之间的相似性越高。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>X — 输入数组**  
数值数组

输入数组，指定为任意维度的数值数组， [X](#Q2) 与 [Y](#Q3) 必须在维度与各维度长度上完全一致。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
 
**<a id="Q3"></a>Y — 输入数组**  
数值数组

输输入数组，指定为任意维度的数值数组， [X](#Q2) 与 [Y](#Q3) 必须在维度与各维度长度上完全一致。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` 

#### 输出参数  
**<a id="Q1"></a>err — 均方误差**  

均方误差，以非负数形式返回。`err` 的数据类型为 `double`。

**数据类型：** `double`

## 版本历史  
在北太天元图像处理工具箱 V1.1 推出

## 相关主题  
<a href="../psnr/psnr.html">psnr</a> | <a 
href="../ssim/ssim.html">ssim</a>
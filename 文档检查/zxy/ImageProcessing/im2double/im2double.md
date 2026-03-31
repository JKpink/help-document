## im2double
将图像转换为双精度值

## 简介
[`I2 = im2double(I)`](#function1)

## 用法
<a id="function1"></a>
[I2](#P1) = im2gray([I](#Q1)) 将图像 `I` 的数据类型转换为双精度。`I` 可以是灰度图像、真彩色图像或二值图像。im2double 将整数数据类型的输出重新缩放到范围 [0, 1]。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
标量 | 向量 | 矩阵 | 多维数组

输入图像，指定为数值标量、向量、矩阵或多维数组。  

- 如果 `I` 是灰度或真彩色图像，它可以是 `uint8`、`uint16`、`double`、`logical`、`single` 或 `int16`。
- 如果 `I` 为二值图像，它必须是 `logical`。  

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` | `logical`

### 输出参数
**<a id="P1"></a> I2 — 转换后的图像**  
数值数组

转换后的图像，返回为与输入图像 [I](#Q1) 大小相同的数值数组。  

**数据类型：** `double`

## 提示
- 如果输入图像 `I` 的数据类型是 `double`、`single` 或 `logical`，则输出像素值与输入像素值相同。  
- 如果 `I` 是灰度或真彩色图像且数据类型为 `uint8`、`uint16` 或 `int16`，则 im2double 将输出像素值重新缩放到范围 [0, 1]。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../double/double.html">double</a> | <a
href="../im2single/im2single.html">im2single</a> | <a
href="../im2int16/im2int16.html">im2int16</a> | <a
href="../im2uint8/im2uint8.html">im2uint8</a> | <a
href="../im2uint16/im2uint16.html">im2uint16 </a>

## im2single
将图像转换为单精度

## 简介
[`J = im2single(I)`](#function1)

## 用法
<a id="function1"></a>
[J](#P1) = im2single([I](#Q1)) 将灰度、RGB 或二值图像 `I` 的数据类型转换为 `single`，并根据需要对数据进行重新缩放或偏移。如果输入图像数据类型为 `single` 类，则输出图像相同。如果输入图像数据类型为 `logical`，则 `im2single` 将逻辑值 true 转换为 single(1)，逻辑值 false 转换为 single(0)。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
数值数组 | 逻辑数组

输入图像，指定为任意大小和维度的数值数组或逻辑数组。

- 如果 `I` 是灰度或 RGB 图像，则它的数据类型可以是 `uint8`、`uint16`、`double`、`logical`、`single` 或 `int16`。  
- 如果 `I` 为二值图像，它的数据类型必须是 `logical`。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` | `logical`

### 输出参数
**<a id="P1"></a> J — 数据类型为 single 的图像**  
数值数组

数据类型为 `single` 的图像，返回为与输入图像 [I](#Q1) 大小相同的数值数组。

**数据类型：** `single`

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../im2double/im2double.html">im2double</a> | <a
href="../im2int16/im2int16.html">im2int16</a> | <a
href="../im2uint8/im2uint8.html">im2uint8</a> | <a
href="../im2uint16/im2uint16.html">im2uint16</a> | <a
href="../single/single.html">single </a>

## im2int8
将图像转换为 8 位有符号整数

## 简介
[`J = im2int8(I)`](#function1)

## 用法
<a id="function1"></a>
[J](#P1) = im2int8([I](#Q1)) 将灰度、彩色或二值图像 I 的数据类型转换为 `int8`，并根据需要对数据进行必要的线性缩放，以便在 `int8` 的可表示范围内表达图像数据。
- 如果输入图像的数据类型为 `int8`，则输出图像与输入图像相同。
- 如果输入图像的数据类型为 `logical`，则 `im2int8` 将值为 true 的元素转换为 127，将值为 false 的元素转换为 0。
- 如果输入图像为彩色图像，则对每个颜色通道独立进行相同的转换。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
数值数组 | 逻辑数组

输入图像，指定为任意大小和维度的数值数组或逻辑数组。

支持的图像类型与要求：

- 如果 I 是灰度或彩色图像，则它的数据类型可以是 `uint8`、`uint16`、`int16`、`double`、`single` 或 `logical`。`im2int8` 需要数据类型为 `double` 和 `single` 的图像的值在 [0, 1] 的范围内。如果 I 的值超出范围 [0, 1]，则可以使用 <a href="../rescale/rescale.html">rescale</a> 函数将值重新缩放到需要的范围。
- 如果 I 是索引图像，则其数据类型可以是 `uint8`、`uint16`、`double` 或 `logical`。如果索引图像属于 `double` 数据类型，则最大值必须等于或小于 256。如果索引图像属于 `uint16` 数据类型，则最大值必须等于或小于 255。
- 如果 I 是二值图像，则它的数据类型必须为 `logical`。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` | `logical`

### 输出参数
**<a id="P1"></a> J — 数据类型为 int8 的图像**  
数值数组

输出图像，数据类型为 `int8`，大小与输入图像 [I](#Q1) 相同。

**数据类型：** `int8`

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../im2double/im2double.html">im2double</a> | <a
href="../im2int16/im2int16.html">im2int16</a> | <a
href="../im2single/im2single.html">im2single</a> | <a
href="../im2uint8/im2uint8.html">im2uint16</a> | <a
href="../int8/int8.html">int8 </a>

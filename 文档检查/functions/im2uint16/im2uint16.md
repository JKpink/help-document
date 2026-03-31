## im2uint16
将图像转换为 16 位无符号整数

## 简介
[`J = im2uint16(I)`](#function1)

## 用法
<a id="function1"></a>
[J](#P1) = im2uint16([I](#Q1)) 将灰度、RGB 或二值图像 `I` 的数据类型转换为 `uint16`，并根据需要对数据进行重新缩放或偏移。如果输入图像的数据类型为 `uint16`，则输出图像相同。如果输入图像的数据类型为 `logical`，则 `im2uint16` 将值为 true 的元素更改为 65535。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
数值数组 | 逻辑数组

输入图像，指定为任意大小和维度的数值数组或逻辑数组。

- 如果 `I` 是灰度或 RGB 图像，则它的数据类型可以是 `uint8`、`uint16`、`int16`、`double`、`single` 或 `logical`。`im2uint16` 需要数据类型为 `double` 和 `single` 的图像的值在 [0, 1] 的范围内。如果 `I` 的值超出范围 [0, 1]，则可以使用 <a href="../rescale/rescale.html">rescale</a> 函数将值重新缩放到需要的范围。
- 如果 `I` 是二值图像，则它的数据类型必须为 `logical`。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` | `logical`

### 输出参数
**<a id="P1"></a> J — 数据类型为 uint16 的图像**  
数值数组

数据类型为 `uint16` 的图像，以与输入图像 [I](#Q1) 大小相同的数值数组形式返回。

**数据类型：** `uint16`

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../im2uint8/im2uint8.html">im2uint8</a> | <a
href="../double/double.html">double</a> | <a
href="../im2double/im2double.html">im2double</a> | <a
href="../uint8/uint8.html">uint8</a> | <a
href="../uint16/uint16.html">uint16</a> | <a
href="../imapprox/imapprox.html">imapprox </a>

## lab2uint8
将 CIE 1976 L\*a\*b\* 颜色值转换为 8 位无符号整数

## 简介
[`lab8 = lab2uint8(lab)`](#function1)

## 用法
<a id="function1"></a>
[lab8](#P1) = lab2uint8([lab](#Q1)) 将 Lab 颜色值转换为 `uint8` 类型。

## 参数说明
### 输入参数
**<a id="Q1"></a> lab — L\*a\*b\* 颜色值**  
m×3 数值数组 | m×n×3 数值数组

L\*a\*b\* 颜色值，指定为 m×3 数值数组颜色值（每行一种颜色）或 m×n×3 数值数组。

**数据类型：** `double` | `uint16`

### 输出参数
**<a id="P1"></a> lab8 — 转换后的颜色值**  
数值数组

转换后的颜色值，返回为与输入相同大小的数值数组。

**数据类型：** `uint8`

## 算法
该函数将 L\*a\*b\* 颜色值转换为 `uint8` 类型。图像处理工具箱软件遵循的约定是，双精度的 L\*a\*b\* 数组包含 1976 年 CIE L\*a\*b\* 值。而数据类型为 `uint8` 或 `uint16` 的 L\*a\*b\* 数组则遵循 ICC 配置文件规范 (ICC.1:2001-4, www.color.org) 中关于将 L\*a\*b\* 值表示为无符号 8 位或 16 位整数的约定。ICC 编码约定可以通过以下表格进行说明。

| Value( L ) | uint8 Value | uint16 Value |
| :----------------------- | :----------------------- | :----------------------- |
| 0.0 | 0 | 0 |
| 100.0 | 255 | 65280 |
| 100.0 + (25500/65280) | None | 65535 |

| Value( a or b ) | uint8 Value | uint16 Value |
| :----------------------- | :----------------------- | :----------------------- |
| -128.0 | 0 | 0 |
| 0.0 | 128 | 32768 |
| 127.0 | 255 | 65280 |
| 127.0 + (255/256) | None | 65535 |

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../applycform/applycform.html">applycform</a> | <a
href="../lab2double/lab2double.html">lab2double</a> | <a
href="../lab2uint16/lab2uint16.html">lab2uint16</a> | <a
href="../makecform/makecform.html">makecform</a> | <a
href="../whitepoint/whitepoint.html">whitepoint</a> | <a
href="../xyz2double/xyz2double.html">xyz2double</a> | <a
href="../xyz2uint16/xyz2uint16.html">xyz2uint16 </a>

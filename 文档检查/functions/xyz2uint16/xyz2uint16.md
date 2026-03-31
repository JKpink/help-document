## xyz2uint16
将 XYZ 颜色值转换为 16 位无符号整数

## 简介
[`xyz16 = xyz2uint16(xyz)`](#function1)

## 用法
<a id="function1"></a>
[xyz16](#P1) = xyz2uint16([xyz](#Q1)) 将 XYZ 颜色值转换为 `uint16` 类型。

## 参数说明
### 输入参数
**<a id="Q1"></a> xyz — 要转换的颜色值**  
m×3 数值矩阵 | m×n×3 数值数组

要转换的颜色值，指定为 m×3 数值矩阵或 m×n×3 数值数组，每行代表一种颜色。

**数据类型：** `double`

### 输出参数
**<a id="P1"></a> xyz16 — 转换后的颜色值**  
数值数组

转换后的颜色值，返回为与输入相同大小的数值数组。

**数据类型：** `uint16`

## 算法
图像处理工具箱软件遵循的约定是，`double` 类型的 XYZ 数组包含 1931 年 CIE XYZ 值（2° 标准观察者）。数据类型为 `uint16` 的 XYZ 数组则遵循 ICC 配置文件规范（ICC.1:2001-4, www.color.org）中关于将 XYZ 值表示为无符号 16 位整数的约定。目前没有标准的将 XYZ 值表示为无符号 8 位整数的方法。ICC 编码约定可以通过以下表格进行说明。

| Value (X, Y, or Z) | uint16 Value |
| :----------------------- | :----------------------- |
| 0.0 | 0 |
| 1.0 | 32768 |
| 1.0 + (32767/32768) | 65535 |

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../applycform/applycform.html">applycform</a> | <a
href="../lab2double/lab2double.html">lab2double</a> | <a
href="../lab2uint8/lab2uint8.html">lab2uint8</a> | <a
href="../lab2uint16/lab2uint16.html">lab2uint16</a> | <a
href="../makecform/makecform.html">makecform</a> | <a
href="../whitepoint/whitepoint.html">whitepoint</a> | <a
href="../xyz2double/xyz2double.html">xyz2double </a>

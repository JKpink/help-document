## rgb2hsi
将 RGB 图像转换为 HSI 图像

## 简介
[`HSI = rgb2hsi(RGB)`](#function1)

## 用法
<a id="function1"></a>
[HSI](#P1) = rgb2hsi[(RGB)](#Q1) 将 RGB 图像的红色、绿色和蓝色值转换为 HSI 图像的色调、饱和度和强度值。

## 参数说明
### 输入参数
**<a id="Q1"></a> RGB — RGB 图像**  
m×n×3 数值数组

真彩色图像，指定为 m×n×3 数值数组。RGB 的第三个维度为每个像素分别定义红色、绿色和蓝色强度。`rgb2hsi` 函数要求数据类型为 `double` 和 `single` 的 RGB 图像的值在范围 [0, 1] 内。

**数据类型：** `single` | `double` | `uint8` | `uint16`

### 输出参数
**<a id="P1"></a> HSI — HSI 图像**  
m×n×3 数值数组

HSI 图像，指定为 m×n×3 数值数组。HSI 的第三个维度为每个像素分别定义色调、饱和度和强度，其范围如下：

- H: [0 1)
- S: [0 1]
- I: [0 1]

**数据类型：** `double` 

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../hsi2rgb/hsi2rgb.html">hsi2rgb</a> | <a
href="../hsi/hsi.html">hsi </a>

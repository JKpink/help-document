## hsi2rgb
将 HSI 图像转换为 RGB 图像

## 简介
[`RGB = hsi2rgb(HSI)`](#function1)  
[`rgbmap = hsi2rgb(hsimap)`](#function2)

## 用法
<a id="function1"></a>
[RGB](#P1) = hsi2rgb[(HSI)](#Q1) 将 HSI 图像的色调、饱和度和强度分量转换为 RGB 图像的红色、绿色和蓝色分量。

<a id="function2"></a>
[rgbmap](#P2) = hsi2rgb[(hsimap)](#Q2) 将 HSI 颜色图转换为 RGB 颜色图。

## 参数说明
### 输入参数
**<a id="Q1"></a> HSI — HSI 图像**  
m×n×3 数值数组

HSI 图像，指定为 m×n×3 数值数组。HSI 的第三维的三个通道分别为色调、饱和度和强度，其范围如下：

- H: [0 360)
- S: [0 1]
- I: [0 1]

**数据类型：** `single` | `double` | `uint8` | `uint16`

**<a id="Q2"></a> hsimap — HSI 颜色图**  
c×3 数值数组

HSI 颜色图，指定为 c×3 数值矩阵。hsimap 的每一行都是一个 HSI 三元组，分别表示颜色图中一种颜色的色调、饱和度和强度分量。

**数据类型：** `double` 

### 输出参数
**<a id="P1"></a> RGB — RGB 图像**  
m×n×3 数值数组

RGB 图像，指定为由范围 [0, 1] 内的值组成的 m×n×3 数值数组。RGB 的第三个维度为每个像素分别定义红色、绿色和蓝色强度。

**数据类型：** `single` | `double` 

**<a id="P2"></a> rgbmap — RGB 颜色图**  
c×3 数值矩阵

RGB 颜色图，指定为由 [0, 1] 内的值组成的 c×3 数值矩阵。rgbmap 的每一行都是一个 RGB 三元组，指定颜色图的单种颜色的红、绿和蓝分量。

**数据类型：** `double` | `single`

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../rgb2hsi/rgb2hsi.html">rgb2hsi</a> | <a
href="../hsi/hsi.html">hsi </a>

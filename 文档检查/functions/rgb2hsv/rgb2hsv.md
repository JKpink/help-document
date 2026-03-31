## rgb2hsv
将 RGB 图像转换为 HSV 图像

## 简介
[`HSV = rgb2hsv(RGB)`](#function1)  
[`hsvmap = rgb2hsv(rgbmap)`](#function2)

## 用法
<a id="function1"></a>
[HSV](#P1) = rgb2hsv[(RGB)](#Q1) 将 RGB 图像的红色、绿色和蓝色值转换为 HSV 图像的色调、饱和度和亮度值。

<a id="function2"></a>
[hsvmap](#P2) = rgb2hsv[(rgbmap)](#Q2) 将 RGB 颜色图转换为 HSV 颜色图。

## 参数说明
### 输入参数
**<a id="Q1"></a> RGB — RGB 图像**  
m×n×3 数值数组

RGB 图像，指定为 m×n×3 数值数组。`RGB` 的第三维的三个通道分别表示每个像素的红、绿和蓝强度。

**数据类型：** `single` | `double` | `uint8` | `uint16`

**<a id="Q2"></a> rgbmap — RGB 颜色图**  
c×3 数值矩阵

RGB 颜色图，指定为由范围 [0, 1] 内的值组成的 c×3 数值矩阵。rgbmap 的每行都是一个 RGB 三元组，指定颜色图的单种颜色的红、绿和蓝分量。

**数据类型：** `double` 

### 输出参数
**<a id="P1"></a> HSV — HSV 图像**  
m×n×3 数值数组

HSV 图像，指定为由范围 [0, 1] 内的值组成的 m×n×3 数值数组。HSV 的第三维的三个通道分别表示每个像素的色调、饱和度和亮度，具体说明如下表所示。

| 属性 | 描述 |
| :----------------------- | :----------------------- |
| 色调 | 值从 0 到 1，对应于颜色在颜色圈上的位置。随着色调从 0 增加到 1，颜色从红色过渡到橙色、黄色、绿色、青色、蓝色、品红色，最后又回到红色。 |
| 饱和度 | 色调的量或距离中性色的量。0 表示中性色，1 表示最大饱和度。 |
| 明度 | 特定颜色的红色、绿色和蓝色分量的最大明度。 |

**数据类型：** `double` | `single` 

**<a id="P2"></a> hsvmap — HSV 颜色图**  
c×3 数值矩阵

HSV 颜色图，指定为由范围 [0, 1] 内的值组成的 c×3 数值矩阵。hsvmap 的每行都是一个 HSV 三元组，指定颜色图的单种颜色的色调、饱和度和明度分量。

**数据类型：** `double` | `single` 

## 参考文献
[1] Smith A R. Color gamut transform pairs. SIGGRAPH 78 Conference Proceedings, 1978, 12(3): 12–19.

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../hsv2rgb/hsv2rgb.html">hsv2rgb</a> | <a
href="../hsv/hsv.html">hsv </a>

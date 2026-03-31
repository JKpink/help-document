## ntsc2rgb
将 NTSC 图像转换为 RGB 图像

## 简介
[`RGB = ntsc2rgb(YIQ)`](#function1)

## 用法
<a id="function1"></a>
[RGB](#P1) = ntsc2rgb[(YIQ)](#Q1) 将 NTSC 图像的亮度和色度值转换为 RGB 图像的红、绿、蓝值。

## 参数说明
### 输入参数
**<a id="Q1"></a> YIQ — YIQ 颜色值**  
数值数组

要转换的 YIQ  颜色值，指定为数值数组，采用下列格式之一。

- c×3 颜色图。每行指定一个 YIQ  颜色值。
- m×n×3 图像。

| 属性 | 描述 |
| :----------------------- | :----------------------- |
| Y | 亮度或图像的明度。值的范围是 [0, 1]，其中 0 表示黑色，1 表示白色。随着 Y 值的增加，颜色的亮度增加。 |
| I | 同相位，大致表示图像中蓝色或橙色调的数量。I 的范围是 [-0.5959, 0.5959]，其中负数表示蓝色调，正数表示橙色调。随着 I 的绝对值增加，颜色的饱和度增加。 |
| Q | 象限，大致表示图像中绿色或紫色调的数量。Q 的范围是 [-0.5229, 0.5229]，其中负数表示绿色调，正数表示紫色调。随着 Q 的绝对值增加，颜色的饱和度增加。 |

**数据类型：** `single` | `double` | `uint8` | `uint16` | `int16`

### 输出参数
**<a id="P1"></a>  RGB — 转换后的 RGB 颜色值**  
数值数组

转换后的 RGB 颜色值，返回与输入大小相同的数值数组。

**数据类型：** `double`

## 算法
在 NTSC 颜色空间中，亮度是用于在单色（黑白）电视上显示图像的灰度信号。其他组件携带色调和饱和度信息。值 0 对应于组件的缺失，而值 1 对应于组件的完全饱和。
`ntsc2rgb` 使用以下代码定义 NTSC  
$$
\begin{bmatrix}
R \\
G  \\
B
\end{bmatrix} = \begin{bmatrix}
1.000 & 0.956 & 0.621 \\
1.000 & -0.272 & -0.647 \\
1.000 & -1.106 & 1.703
\end{bmatrix}
\begin{bmatrix}
Y  \\
I  \\
Q
\end{bmatrix}
$$

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../ntsc2rgb/ntsc2rgb.html">ntsc2rgb</a> | <a
href="../rgb2ycbcr/rgb2ycbcr.html">rgb2ycbcr</a> | <a 
href="../rgb2lab/rgb2lab.html">rgb2lab</a> | <a 
href="../rgb2xyz/rgb2xyz.html">rgb2xyz</a> | <a 
href="../rgb2hsv/rgb2hsv.html">rgb2hsv </a>

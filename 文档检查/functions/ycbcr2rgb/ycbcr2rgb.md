## ycbcr2rgb
将 YCbCr 转换为 RGB

## 简介
[`RGB = ycbcr2rgb(YCBCR)`](#function1)

## 用法
<a id="function1"></a>
[RGB](#P1) = ycbcr2rgb[(YCBCR)](#Q1) 将 YCbCr 图像亮度和色度值转换为 RGB 图像的红、绿、蓝值。

## 参数说明
### 输入参数
**<a id="Q1"></a> YCBCR — YCbCr 颜色值**  
数值数组

要转换的 YCbCr 颜色值，指定为数值数组，采用下列格式之一。

- c×3 颜色图。每行指定一个 YCbCr 颜色值。
- m×n×3 图像。

**数据类型：** `single` | `double` | `uint8` | `uint16`

### 输出参数
**<a id="P1"></a> RGB — 转换后的 RGB 颜色值**  
数值数组

转换后的 RGB 颜色值，返回与输入大小相同的数值数组。

## 参考文献
[1] Poynton C A. A Technical Introduction to Digital Video. John Wiley & Sons, Inc., 1996.  
[2] Sector I T U R .Studio encoding parameters of digital television for standard 4 : 3 and wide-screen 16 : 9 aspect ratios. International Telecommunication Union Radiocommunications Sector (ITU-R), BT.601-5, 1995.

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../ntsc2rgb/ntsc2rgb.html">ntsc2rgb</a> | <a
href="../rgb2ntsc/rgb2ntsc.html">rgb2ntsc</a> | <a 
href="../rgb2ycbcr/rgb2ycbcr.html">rgb2ycbcr</a> | <a 
href="../ycbcr2rgbwide/ycbcr2rgbwide.html">ycbcr2rgbwide</a> | <a 
href="../rgbwide2ycbcr/rgbwide2ycbcr.html">rgbwide2ycbcr </a>

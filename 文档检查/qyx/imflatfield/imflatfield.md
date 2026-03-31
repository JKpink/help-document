## imflatfield
2维图像平场校正

## 简介
[ `J = imflatfield(I, sigma)`](#function1)  

## 用法
<a id="function1"></a>
[J](#Q5) = imflatfield([I](#Q1), [sigma](#Q2))对灰度图像或 RGB 图像 `I` 执行平场校正。该校正过程通过标准差为 sigma 的高斯平滑滤波，来拟合图像 `I` 中的背景阴影分量，校正后的图像返回至 `J`。  

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 失真图像**  
二维灰度图像 | 二维 RGB 图像

待校正的失真图像，指定为尺寸为 m×n 的二维灰度图像，或尺寸为 m×n×3 的二维 RGB 图像。

**数据类型**：`single` | `double` | `int16` | `uint8` | `uint16` 

**<a id="Q2"></a> sigma — 高斯平滑滤波器的标准差**  
正数 | 二元正数值向量

高斯平滑滤波器的标准差，指定为正数或二元正数值向量。若指定为标量，则函数使用方形的高斯核进行滤波。

**数据类型**：`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出参数
**<a id="Q5"></a> J — 校正后的图像**    
二维灰度图像 | 二维 RGB 图像

校正后的图像，返回为与输入图像 [I](#Q1) 尺寸相同、数据类型相同的二维灰度图像或 RGB 图像。

## 提示
- 当输入图像 [I](#Q1) 为 RGB 图像时，`imflatfield` 会先通过 `rgb2hsv` 函数将图像转换至 HSV 色彩空间，仅对 HSV 空间的亮度（Value）通道执行平场校正，校正完成后再通过 `hsv2rgb` 函数将图像转换回 RGB 色彩空间。 

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../rgb2hsv/rgb2hsv.html">rgb2hsv</a> | <a href="../hsv2rgb/hsv2rgb.html">hsv2rgb</a>
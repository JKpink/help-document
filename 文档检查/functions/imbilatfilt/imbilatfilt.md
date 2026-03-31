## imbilatfilt
使用高斯核对图像进行双边滤波

## 简介
[ `J = imbilatfilt(I)`](#function1)  
[ `J = imbilatfilt(I, degreeOfSmoothing)`](#function2)  
[ `J = imbilatfilt(I, degreeOfSmoothing, spatialSigma)`](#function3)

## 用法
<a id="function1"></a>
[J](#Q4) = imbilatfilt([I](#Q1)) 对灰度或 RGB 图像 `I` 应用边缘保持高斯双边滤波器。  
<a id="function2"></a>
[J](#Q4) = imbilatfilt([I](#Q1), [degreeOfSmoothing](#Q2)) 指定平滑量。当 `degreeOfSmoothing` 是一个小值时，`imbilatfilter` 会平滑方差较小的邻域（均匀区域），但不会平滑方差较大的邻域，如强边。当 `degreeOfSmoothing` 的值增加时， `imbilatwelt` 会平滑方差较大的均匀区域和邻域。  
<a id="function3"></a>
[J](#Q4) = imbilatfilt([I](#Q1), [degreeOfSmoothing](#Q2), [spatialSigma](#Q3)) 也指定了空间高斯平滑核的标准偏差 `spatialSigma`。`spatialSigma` 值越大，越远的相邻像素的贡献越大，有效地增加了邻域大小。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 要过滤的图像**  
二维灰度图像 | 二维彩色图像

要过滤的图像，指定为大小为 m×n 的二维灰度图像或大小为 m×n×3 的二维彩色图像。

**数据类型：**    `double` | `uint8` | `logical`

**<a id="Q2"></a> degreeOfSmoothing — 平滑程度**  
正数

平滑程度，指定为正数。`degreeOfSmoothing` 的默认值取决于图像 `I` 的数据类型，计算为 0.01*diff(getrangefromclass(I)).^2。例如，对于数据类型为 `uint8` 的图像，默认平滑程度为 650.25，对于像素值在 [0, 1] 范围内的数据类型为 `double` 的图像，默认值为 0.01。

**<a id="Q3"></a> spatialSigma — 空间高斯平滑核的标准偏差**  
 1 (默认) | 正数

空间高斯平滑核的标准偏差，指定为正数。

### 输出参数
**<a id="Q4"></a> J — 过滤后的图像**  
数字数组

过滤后的图像，以与输入图像 `I` 相同的大小和数据类型的数字数组返回。

## 算法
- `degreeOfSmoothing` 的值对应于双边滤波器的 `Range` 高斯核的方差[[1]](#R1)。范围高斯应用于像素值与其相邻值的欧几里得距离。
- 要平滑 RGB 图像的感知接近颜色，请在应用双边滤波器之前使用 rgb2lab 将图像转换为 CIE L\*a\*b\* 空间。要查看结果，请使用 lab2rgb 将过滤后的图像转换为 RGB。
- 增加 `spatialSigma` 会增加 `NeighborhoodSize`，从而增加过滤器执行时间。您可以指定较小的 `NeighborhoodSize` 以换取准确性以换取更快的执行时间。

## **<a id="R1"></a> 参考文献**  
[1] Tomasi C, Manduchi R. Bilateral filtering for gray and color images. Sixth international conference on computer vision (IEEE Cat. No. 98CH36271). IEEE, 1998: 839-846.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../imgaussfilt/imgaussfilt.html">imgaussfilt</a> | <a 
href="../imfilter/imfilter.html">imfilter</a> | <a 
href="../imnlmfilt/imnlmfilt.html">imnlmfilt</a> 
## randomWindow2d  
创建随机矩形裁剪窗口  
  
## 简介  
[`win = randomWindow2d(inputSize, targetSize)`](#function1)  
[`win = randomWindow2d(inputSize, scale, dimensionRatio)`](#function2)  
  
## 用法  
<a id="function1"></a> [win](#P1) = randomWindow2d([inputSize](#P2), [targetSize](#P3)) 从大小为 `inputSize` 的图像中，随机选择一块大小为 `targetSize` 的矩形区域。  
<a id="function2"></a> [win](#P1) = randomWindow2d([inputSize](#P2), [scale](#P4), [dimensionRatio](#P5)) 通过指定区域相对于输入图像的大小比例，以及区域的宽高比，来选择一个矩形区域。  
  
## 参数说明
### 输入参数   
**<a id="P2"></a> inputSize — 输入图像大小**  
2 元素正整数向量 | 3 元素正整数向量  
  
输入图像大小，指定为以下格式之一：  
  
| **输入图像类型** | **`inputsize` 格式** |
| --- | --- |
| 二维灰度图像或二值图像 | 2 元素正整数向量，格式为 `[height width]` |
| 二维RGB图像或多光谱图像 | 3 元素正整数向量，格式为 `[height width channels]` |
  
**<a id="P3"></a> targetSize — 目标图像大小**  
2 元素正整数向量 | 3 元素正整数向量  
  
目标图像大小，指定为以下格式之一：  
  
| **目标图像类型** | **`targetsize` 格式** |
| --- | --- |
| 二维灰度图像或二值图像 | 2 元素正整数向量，格式为 `[height width]` |
| 二维RGB图像或多光谱图像 | 3 元素正整数向量，格式为 `[height width channels]` |
  
**<a id="P4"></a> scale — 区域面积占输入图像面积的比例**  
2 元素数值向量 | 函数句柄  
  
区域面积占输入图像面积的比例，指定为以下值之一：  
  
- 2 元素非递减数值向量：取值范围为 [0, 1]。两个元素分别定义了区域面积占比的最小值和最大值。 `randomWindow2d` 函数会在该范围内随机选择一个值作为区域面积的占比。若要使用固定的区域面积占比，只需将两个元素设置为相同的值。  
- 函数句柄：该函数必须无输入参数，并返回一个取值在 [0, 1] 范围内的数值，用于指定有效的区域面积占比。  
  
**<a id="P5"></a> dimensionRatio — 矩形区域的宽高比范围**  
2 × 2 正数矩阵 | 函数句柄  
  
矩形区域的宽高比范围，可指定为以下值之一：  
  
- 2 × 2 正数矩阵：第一行定义宽高比的最小值，第二行定义宽高比的最大值。`randomWindow2d` 函数会在该范围内随机选择一个值作为矩形区域的宽高比。若要使用固定的宽高比，只需将第一行和第二行设置为相同的值。  
- 函数句柄：该函数必须无输入参数，并返回一个正数，用于指定有效的宽高比。(例如，值 1.2 对应 5:4 的宽高比)。  
  
### 输出参数  
**<a id="P1"></a> win — 矩形窗口**  
`Rectangle` 对象  
  
矩形窗口，指定为 <a href="../Rectangle/Rectangle.html">Rectangle</a>  </a> 对象。  
  
## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../centercropwindow2d/centercropwindow2d.html">centercropwindow2d</a> | <a   
href="../randomCropWindow3d/randomCropWindow3d.html">randomCropWindow3d</a> | <a
href="../imcrop/imcrop.html">imcrop</a>     
  
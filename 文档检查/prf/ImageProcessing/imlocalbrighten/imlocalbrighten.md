## imlocalbrighten 
低光图像增强

## 简介
[ `B = imlocalbrighten(A) `](#function1)  
[ `B = imlocalbrighten(A, amount)`](#function2)  
[ `B = imlocalbrighten(___, "AlphaBlend", alphaBlend) `](#function3)

## 用法
<a id="function1"></a>
[B](#Q4) = imlocalbrighten([A](#Q1)) 使 RGB 或灰度图像 `A` 中的低光区域变亮。  
<a id="function2"></a>
[B](#Q4) = imlocalbrighten([A](#Q1), [amount](#Q2)) 将 `A` 中的低光区域增亮指定量。  
<a id="function3"></a>
[B](#Q4) = imlocalbrighten(___, "AlphaBlend", [alphaBlend](#Q3))  还指定是否通过执行 `Alpha` 混合来保留输入图像的明亮区域。
## 参数说明
### 输入参数
**<a id="Q1"></a> A — 要增亮的图像**  
RGB 图像 | 灰度图像  

要增亮的图像，指定为 RGB 图像或灰度图像。

**数据类型:** `uint8`

**<a id="Q2"></a> amount — 使图像变亮的量**  
1（默认）| 范围 [0, 1] 中的数字  

用于提亮图像的量，指定为范围 [0, 1] 内的数字。当值为 1（默认值）时，`imlocalbrighten` 会尽可能提亮 `A` 的低光区域。当值为 0 时，`imlocalbrighten` 将返回未修改的输入图像。

**示例：** 0.2  
**数据类型:** `uint8`

**<a id="Q3"></a> alphaBlend — Alpha 混合原始图像和增强图像**  
false 或 0 （默认）| true 或 1  

`Alpha` 混合原始图像和增强图像，指定为数字或逻辑 0 （false） 或 1 （true）。`Alpha` 混合将原始图像与增强图像合并，以保留原始图像的较亮区域。如果为 `true`，则 `imlocalbrighten` 使用暗度矩阵的估计值 `D` 来保留与每个像素中的光量成比例的输入图像的内容。

### 输出参数
**<a id="Q4"></a> B — 增亮的图像**  
数字数组  

增亮后的图像，与输入图像 `A` 的大小和数据类型相同。

## 参考文献
[1] Dong X, Pang Y A, Wen J G. Fast efficient algorithm for enhancement of low lighting video. IEEE International Conference on Multimedia and Expo. IEEE,2011: 1-6.  
[2] He K, Sun J, Fellow, et al. Single Image Haze Removal Using Dark Channel Prior. IEEE Transactions on Pattern Analysis & Machine Intelligence, 2011,33(12):2341-2353.  
[3] Park D, Park H, Han D K, et al. Single image dehazing with image entropy and information fidelity. IEEE,  2014.

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../adapthisteq/adapthisteq.html">adapthisteq</a> | <a
href="../histeq/histeq.html">histeq</a> | <a 
href="../mat2gray/mat2gray.html">mat2gray</a> | <a 
href="../imreducehaze/imreducehaze.html">imreducehaze</a>  
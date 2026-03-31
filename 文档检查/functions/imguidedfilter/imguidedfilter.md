## imguidedfilter
图像引导滤波
## 简介
[ `B = imguidedfilter(A)`](#function1)  
[ `B = imguidedfilter(A, G)`](#function2)    
[ `B = imguidedfilter(___, Name, Value)`](#function3)  
## 用法
<a id="function1"></a>
[B](#Q3) = imguidedfilter([A](#Q1)) 以图像 `A` 自身作为引导图，对其进行自引导滤波。该语法可用于对图像 `A` 进行边缘保留平滑处理。  
<a id="function2"></a>
[B](#Q3) = imguidedfilter([A](#Q1), [G](#Q2))以图像 `G` 为引导图，对二值、灰度或 RGB 图像 `A` 进行滤波。  
<a id="function3"></a> 
[B](#Q3) = imguidedfilter(___, [Name, Value](#Q4))通过名称 - 值参数控制引导滤波的相关属性，对图像 `A` 进行滤波。  
## 参数说明
### 输入参数
**<a id="Q1"></a> A — 待滤波的图像**  
二值图像 | 灰度图像 | RGB 图像  

需指定为二值、灰度或 RGB 格式的待滤波图像  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`  | `logical`  

**<a id="Q2"></a> G — 引导图像**  
二值图像 | 灰度图像 | RGB 图像  

需指定为与图像`A`高度和宽度一致的二值、灰度或 RGB 图像  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`  | `logical` 

### **<a id="Q4"></a> 名称 - 值参数**  

将可选的参量对组指定为 Name1, Value1, ..., NameN, ValueN，其中 Name 是参量名称，Value 是对应的值。名称 — 值参量必须出现在其他参量之后，但参量对组的顺序无关紧要。  

**NeighborhoodSize-矩形邻域的大小**  
[5 5]（默认值） | 正整数 | 2 元素正整数向量  

引导滤波中每个像素周围矩形邻域的大小，需指定为单个正整数或 2 元素正整数向量。  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint64`  

**DegreeOfSmoothing-平滑程度**  
正数值  

输出图像的平滑量，需指定为正数值。若值较小，仅会平滑方差小的区域（均匀区域），方差大的区域（如边缘附近）不会被平滑；若值较大，除均匀区域外，方差大的区域（如更明显的边缘）也会被平滑。建议先使用默认值，再根据效果调整该值以达到预期的平滑程度。  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`  | `uint64`
## 输出参量
**<a id="P1"></a> B — 滤波后的图像**  
数值数组  

滤波后的图像，以与输入图像 `A` 尺寸和数据类型均相同的数值数组形式返回。
## 参考文献
[1] Kaiming He, Jian Sun, Xiaoou Tang. Guided Image Filtering. IEEE® Transactions on Pattern Analysis and Machine Intelligence, Volume 35, Issue 6, pp. 1397-1409, June 2013.
## 版本历史
在北太天元图像处理工具箱 V3.0 推出
## 相关主题
<a href="../edge/edge.html">edge</a> | <a
href="../ imdiffuseest/ imdiffuseest.html">imdiffuseest</a>| <a
href="../imfilter/imfilter.html">imfilter</a>| <a
href="../imgaussfilt/imgaussfilt.html">imgaussfilt</a>| <a
href="../locallapfilt/locallapfilt.html">locallapfilt</a>| <a
href="../imnlmfilt/imnlmfilt.html">imnlmfilt</a>| <a
href="../imsharpen/imsharpen.html">imsharpen</a>
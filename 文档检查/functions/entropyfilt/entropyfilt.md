## entropyfilt
局部熵滤波

## 简介
[ `J = entropyfilt(I)`](#function1)  
[ `J = entropyfilt(I, nhood)`](#function2)  

## 用法
<a id="function1"></a>
[J](#Q3) = entropyfilt([I](#Q1)) 返回数组 `J`，其中每个输出像素包含输入图像 `I` 中对应像素周围 9×9 邻域的熵值。  
对于 `I` 边界上的像素， `entropyfilt` 使用对称填充。在对称填充中，填充像素的值是 `I` 中边界像素的镜像反射值。  
<a id="function2"></a>
[J](#Q3) = entropyfilt([I](#Q1), [nhood](#Q2)) 使用邻域 `nhood` 对输入图像 `I` 进行熵滤波。

## 参数说明
### 输入参数
**<a id="Q1"></a>I — 待滤波的图像**  
逻辑数组 | 数值数组

要滤波的图像，指定为任意维度的数值数组。如果输入图像的维度超过两个 (ndims(I) > 2)，例如对于 RGB 图像，则 `entropyfilt` 将沿更高维度对所有二维平面进行滤波。对于 `double` 数据类型，`I` 的强度值必须位于范围 [0, 1] 内。

**数据类型：** `double` | `uint8` | `uint16` | `uint32` | `logical`

**<a id="Q2"></a>nhood — 邻域**  
true(9)（默认）| 数值数组 | 逻辑数组

邻域，指定为包含 0 和 1 的数值或逻辑数组。`nhood` 的大小在每个维度上必须是奇数。
默认情况下，`entropyfilt` 使用邻域true(9)。邻域的中心元素是 floor((size(nhood) + 1)/2)。
要指定其他形状 (如圆盘) 的邻域，请使用 <a href="../strel/strel.html">`strel`</a> 函数创建所需形状的结构元素对象，然后，从结构元素对象的邻域属性中提取邻域。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数
**<a id="Q3"></a>J — 滤波后的图像**  
数值数组

经过滤波处理的图像，以与输入图像 `I` 大小相同的数值数组形式返回，`J` 的数据类型为 `double`。

**数据类型：** `double`



## 参考文献
[1] Gonzalez R C, Woods R E, Eddins S L. Digital Image Processing Using MATLAB. New Jersey: Prentice Hall, 2003. 

## 版本历史
在北太天元图像处理工具箱 V1.0 推出 

##相关主题
<a href="../entropy/entropy.html">entropy</a> | <a 
href="../stdfilt/stdfilt.html">stdfilt</a> | <a 
href="../imhist/imhist.html">imhist</a> | <a 
href="../rangefilt/rangefilt.html">rangefilt</a>    
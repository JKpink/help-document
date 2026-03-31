## stdfilt
标准差滤波

## 简介
[ `J = stdfilt(I)`](#function1)  
[ `J = stdfilt(I, nhood)`](#function2)

## 用法
<a id="function1"></a>
[J](#Q3) = stdfilt([I](#Q1)) 对图像 `I` 执行标准差滤波，并返回滤波后的图像 `J`。每个输出像素的值是对应输入像素周围 3×3 邻域的标准差，对于位于 `I` 边缘的像素，`stdfilt` 使用对称填充。在对称填充中，填充像素的值是对 `I` 中边界像素的镜像反射。  
<a id="function2"></a>
[J](#Q3) = stdfilt([I](#Q1), [nhood](#Q2)) 指定用于计算标准差的邻域，即 `nhood` 。

## 参数说明
### 输入参数
**<a id="Q1"></a>I — 待滤波的图像**  
逻辑数组 | 数值数组

要滤波的图像，指定为任意维度的数值数组或逻辑数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q2"></a>nhood — 邻域**  
true(3)（默认）| 数值数组 | 逻辑数组


邻域，指定为包含 0 和 1 的数值或逻辑数组。`nhood` 的大小在每个维度上必须是奇数。  
默认情况下，`stdfilt` 使用邻域 true(3)，`stdfilt` 通过 floor((size(nhood) + 1)/2) 确定邻域的中心元素。  
要指定各种形状的邻域（例如圆盘），请使用 <a href="../strel/strel.html">`strel`</a> 函数创建所需形状的结构元素对象，然后从结构元素的邻域属性中提取邻域。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数
**<a id="Q3"></a>J — 滤波后的图像**  
数值数组

滤波后的图像，以与输入图像 [`I`](#Q1) 大小相同的数值数组形式返回。`J` 的数据类型为 `double`。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出 

## 相关主题
<a href="../entropyfilt/entropyfilt.html">entropyfilt</a> | <a 
href="../rangefilt/rangefilt.html">rangefilt</a> | <a 
href="../std2/std2.html">std2</a>  

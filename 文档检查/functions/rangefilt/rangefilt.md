## rangefilt
局部范围滤波

## 简介
[ `J = rangefilt(I)`](#function1)  
[ `J = rangefilt(I, nhood)`](#function2)

## 用法
<a id="function1"></a>
[J](#Q3) = rangefilt([I](#Q1)) 返回数组 `J`，其中每个输出像素包含输入图像 `I` 中对应像素周围 3×3 邻域的范围值（最大值减最小值）。  
<a id="function2"></a>
[J](#Q3) = rangefilt([I](#Q1), [nhood](#Q2)) 使用指定的邻域 `nhood` 返回图像 `I` 的局部范围。

## 参数说明
### 输入参数
**<a id="Q1"></a>I — 待滤波的图像**  
逻辑数组 | 数值数组

要滤波的图像，指定为任意维度的数值数组或逻辑数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` 

**<a id="Q2"></a>nhood — 邻域**  
true(3)（默认）| 数值数组 | 逻辑数组

邻域，指定为包含 0 和 1 的逻辑数组或数值数组。`nhood` 的大小在每个维度上必须是奇数。`rangefilt` 通过 floor((size(nhood) + 1)/2) 确定邻域的中心元素。
要指定其他形状（如圆盘）的邻域，请使用 <a href="../strel/strel.html">`strel`</a> 函数创建所需形状的结构元素对象。然后，从结构元素对象的 neighborhood 属性中提取邻域。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数
**<a id="Q3"></a>J — 滤波后的图像**  
数值数组

经过滤波处理的图像，以与输入图像 [`I`](#Q1) 大小相同的数值数组形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` 

## 版本历史
在北太天元图像处理工具箱 V1.0 推出 

##相关主题
<a href="../entropyfilt/entropyfilt.html">entropyfilt</a> | <a 
href="../stdfilt/stdfilt.html">stdfilt</a> | <a 
href="../strel/strel.html">strel</a>  
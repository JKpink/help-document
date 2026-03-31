## locallapfilt
快速局部拉普拉斯滤波

## 简介
[ `B = locallapfilt(I, sigma, alpha)`](#function1)  
[ `B = locallapfilt(I, sigma, alpha, beta)`](#function2)  
[ `B = locallapfilt(___, Name, Value)`](#function3)

## 用法
<a id="function1"></a>
[B](#Q6) = locallapfilt([I](#Q1), [sigma](#Q2), [alpha](#Q3)) 函数使用边缘感知的快速局部拉普拉斯滤波器，对灰度图像或 RGB 图像 `I` 进行滤波处理。参数 `sigma` 用于表征图像I中边缘的幅值；参数 `alpha` 用于控制图像细节的平滑程度。   
<a id="function2"></a>
[B](#Q6) = locallapfilt([I](#Q1), [sigma](#Q2), [alpha](#Q3), [beta](#Q4)) 函数通过参数 `beta` 控制图像 `A` 的动态范围，进而完成滤波操作。  
<a id="function3"></a>
[B](#Q6) = locallapfilt(___,[Name, Value](#Q5))   函数通过名称 - 值对组参数，对滤波器的高级特性进行控制。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 待滤波图像**  
二维灰度图像 | 二维 RGB 图像

待滤波的图像，指定为二维灰度图像或二维 RGB 图像。

**数据类型**：`single` | `int8` | `int16` |  `uint8` | `uint16` 

**<a id="Q2"></a> sigma — 边缘幅值**  
非负数

边缘的幅值，指定为非负数。对于整型图像，以及取值范围为[0, 1]的单精度图像，sigma的取值范围应为[0, 1]；对于取值范围为[a, b]的单精度图像，sigma的取值范围也应设为[a, b]。

**数据类型**：`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` 

**<a id="Q3"></a> alpha — 细节平滑度**  
正数 

图像细节的平滑程度，指定为正数。alpha的典型取值范围为[0.01, 10]。

| **取值情况** | **功能描述** |  
|:-|:-|  
|alpha < 1|增强输入图像的细节，在不影响边缘、不引入光晕伪影的前提下，有效提升图像的局部对比度|  
|alpha > 1|平滑输入图像的细节，同时保留清晰的边缘|  
|alpha = 1|保持输入图像的细节不变|  

**数据类型**：`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q4"></a> beta — 动态范围**  
1（默认值） | 非负数

图像的动态范围，指定为非负数。beta的典型取值范围为[0, 5]，该参数用于调整图像 A 的动态范围。  
| **取值情况** | **功能描述** |  
|:-|:-|  
|beta < 1|降低图像中边缘的幅值，在不影响细节的前提下，有效压缩图像的动态范围|  
|beta > 1|扩展图像的动态范围|  
|beta = 1|保持图像的动态范围不变（默认设置）|

**数据类型**：`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`  

**<a id="Q5"></a> 名称 — 值参数**  
指定可选的、成对出现的参数，格式为Name1, Value1,...,NameN, ValueN，其中Name为参数名，Value为对应的参数值。名称 - 值对组参数必须放在其他参数之后，且参数对的顺序不影响运行结果。  
**示例**：B = locallapfilt(I,sigma,alpha,"ColorMode","luminance")

**ColorMode — RGB 图像滤波方式**  
"luminance"（默认值）|"separate"

RGB 图像的滤波方式，指定为以下取值之一。该参数对灰度图像无效。

| **取值** | **功能描述** |  
|:-|:-|  
|"luminance"|滤波前，先将输入的 RGB 图像转换为灰度图；滤波完成后，再重新赋予图像色彩。此方式可在不改变颜色的前提下调整图像对比度|  
|"separate"|函数对 RGB 图像的每个颜色通道分别独立执行滤波操作|
  
**数据类型**：`char` | `string`

### 输出参数
**<a id="Q6"></a> B — 滤波后图像**    
数值数组

滤波后的图像，以数值数组形式返回，其尺寸和数据类型与输入图像 A 完全一致。

**数据类型**： `single` | `double`

## 参考文献
[1] Paris, Sylvain, Samuel W. Hasinoff, and Jan Kautz. Local Laplacian filters: edge-aware image processing with a Laplacian pyramid, ACM Trans. Graph. 30.4 (2011): 68.  
[2] Aubry, Mathieu, et al. Fast local laplacian filters: Theory and applications. ACM Transactions on Graphics (TOG) 33.5 (2014): 167.

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../localcontrast/localcontrast.html">localcontrast</a> 
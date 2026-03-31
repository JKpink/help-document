## imgaborfilt
将gabor滤波器或滤波器组应用于二维图像
## 简介
[ `[mag, phase] = imgaborfilt(A, wavelength, orientation)`](#function1)  
[ `[mag, phase] = imgaborfilt(A, wavelength, orientation)`](#function2)   
[ `[mag, phase] = imgaborfilt(A, gaborbank)`](#function3)
## 用法
<a id="function1"></a>
[[mag, phase](#Q4)] = imgaborfilt([A](#Q1), [wavelength](#Q2), [orientation](#Q3)) 计算输入灰度图像 A 的gabor滤波器的幅值和相位响应。wavelength 描述正弦载波的波长，以像素/周期为单位。orientation 是滤波器的方向，以度为单位。  
<a id="function2"></a>
[[mag, phase](#Q4)] = imgaborfilt([A](#Q1),[wavelength](#Q2), [orientation](#Q3), [Name=Value](#Q5))  使用名称-值参量应用单个gabor滤波器来控制滤波的各个方面。  
<a id="function3"></a>
[[mag, phase](#Q4)] = imgaborfilt([A](#Q1), [gaborbank](#Q6))将gabor滤波器组 gaborbank 应用于输入图像 A。
## 参数说明
### 输入参数
**<a id="Q1"></a> A — 二位灰度图像**  
数值矩阵  

二维灰度图像，指定为数值矩阵。  

**<a id="Q2"></a> wavelength — 正弦载波的波长**  
数字  

正弦载波的波长，指定为大于或等于 2 的数字，以像素/周期为单位。wavelength 的典型值范围是从 2 到输入图像的斜边长度。 

**<a id="Q3"></a> orientation — 滤波器的方向**  
数字  

以度为单位的滤波器方向，指定为范围 [0, 360] 内的数值标量。方向定义为正弦平面波的法线方向。  

**<a id="Q4"></a> gaborbank — gabor滤波器组**  
gabor对象 | gabor对象的数组  

gabor滤波器组，指定为 gabor 对象或 gabor 对象数组。

### **<a id="Q4"></a> 名称 - 值参数**  

将可选的参量对组指定为 Name, Value1, ..., NameN, ValueN，其中 Name 是参量名称，Value 是对应的值。名称 — 值参量必须出现在其他参量之后，但参量对组的顺序无关紧要。 

**<a id="Q1"></a> SpatialFrequencyBandwidth — 空间频率带宽**  
1（默认）| 正数值 | 正数值向量  

**<a id="Q1"></a> SpatialAspectRatio — 空间纵横比**   
0.5（默认）| 正数值 | 正数值向量

## 输出参量
**<a id="P1"></a> mag — 幅值响应**  
数值矩阵 | 数值数组  

**数据类型：** `double`  

**<a id="P1"></a> phase — 相位响应**  
数值矩阵 | 数值数组  

**数据类型：** `double`
## 参考文献
[1]  Jain, Anil K., and Farshid Farrokhnia. "Unsupervised Texture Segmentation Using Gabor Filters." Pattern Recognition 24, no. 12 (January 1991): 1167–86. https://doi.org/10.1016/0031-3203(91)90143-S.
## 版本历史
在北太天元图像处理工具箱 V3.0 推出
## 相关主题
<a href="../gabor/gabor.html">gabor</a>|<a href="../edge/edge.html">edge|</a><a href="../imfilter/imfilter.html">imfilter</a>|</a><a href="../imgradient/imgradient.html">imgradient</a>|</a><a href="../fspecial/fspecial.html">fspecial</a>
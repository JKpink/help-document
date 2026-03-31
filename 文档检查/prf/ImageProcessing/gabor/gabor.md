## gabor  
创建 Gabor 滤波器或 Gabor 滤波器组
## 简介
[ `g = gabor(wavelength, orientation)`](#function1)  
[ `g = gabor(wavelength, orientation, Name, Value)`](#function2)   
## 用法
<a id="function1"></a>
[g](#Q3) = gabor([wavelength](#Q1), [orientation](#Q2)) 创建 Gabor 滤波器，并将其Wavelength（波长）和Orientation（方向）属性设置为输入的波长与方向。  
<a id="function2"></a>
[g](#Q3) = gabor([wavelength](#Q1), [orientation](#Q2), [Name, Value](#Q4)) 在设置波长、方向的基础上，通过名称 - 值参数配置SpatialFrequencyBandwidth（空间频率带宽）、SpatialAspectRatio（空间纵横比）中的一个或多个属性。
## 参数说明
### 输入参数
**<a id="Q1"></a> Wavelength — 正弦载波的波长**   
数值标量 | 数值向量  

**<a id="Q1"></a> Orientation — 滤波器的方向**  
数值标量 | 数值向量  

###**<a id="Q4"></a> 名称 - 值参数**  

将可选的参量对组指定为 Name1, Value1, ..., NameN, ValueN，其中 Name 是参量名称，Value 是对应的值。名称 — 值参量必须出现在其他参量之后，但参量对组的顺序无关紧要。  

**<a id="Q1"></a> SpatialFrequencyBandwidth — 空间频率带宽**  
1（默认）| 正数值 | 正数值向量  

**<a id="Q1"></a> SpatialAspectRatio — 空间纵横比**   
0.5（默认）| 正数值 | 正数值向量

## 参考文献
[1]  Jain, Anil K., and Farshid Farrokhnia. "Unsupervised Texture Segmentation Using Gabor Filters." Pattern Recognition 24, no. 12 (January 1991): 1167–86. 
## 版本历史
在北太天元图像处理工具箱 V3.0 推出
## 相关主题
<a href="../imgaborfilt/imgaborfilt.html">imgaborfilt</a>
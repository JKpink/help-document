## deconvblind  
使用盲反卷积对图像进行去模糊处理

## 简介  
[ `[J,psfr] = deconvblind(I, psfi)`](#function1)  
[ `[J,psfr] = deconvblind(I, psfi, iter)`](#function2)  
[ `[J,psfr] = deconvblind(I, psfi, iter, dampar)`](#function3)  
[ `[J,psfr] = deconvblind(I, psfi, iter, dampar, weight)`](#function4)  
[ `[J,psfr] = deconvblind(I, psfi, iter, dampar, weight, readout)`](#function5)  
 
## 用法  
<a id="function1"></a>
[[J](#Q1), [psfr](#Q2)] = deconvblind([I](#Q3), [psfi](#Q4))  
使用最大似然算法和点扩散函数 (PSF) [psfi](#Q4) 的初始估计值对图像 [I](#Q3) 进行反卷积。deconvblind 函数返回去模糊后的图像 [J](#Q1) 和还原后的 PSF [psfr](#Q2)。  
<a id="function2"></a>  
[[J](#Q1), [psfr](#Q2)] = deconvblind([I](#Q3), [psfi](#Q4), [iter](#Q5))  
指定迭代次数 [iter](#Q5)。  
<a id="function3"></a>  
[[J](#Q1), [psfr](#Q2)] = deconvblind([I](#Q3), [psfi](#Q4), [iter](#Q5), [dampar](#Q6))  
通过抑制偏差较小（与噪声相比）的像素的迭代来控制噪声放大，偏离量由阻尼阈值 [dampar](#Q6) 指定。默认情况下，不发生阻尼。  
<a id="function4"></a>  
[[J](#Q1), [psfr](#Q2)] = deconvblind([I](#Q3), [psfi](#Q4), [iter](#Q5), [dampar](#Q6), [weight](#Q7))  
指定在复原图像时应考虑输入图像 [I](#Q3) 中的哪些像素。[weight](#Q7) 数组中元素的值指定在处理图像时输入图像中某位置处像素的参与度。例如，要将某个像素排除在考虑范围之外，请在 [weight](#Q7) 数组中为其分配 0 值。您可以根据平场校正量调整分配给每个像素的权重值。  
<a id="function5"></a>  
[[J](#Q1), [psfr](#Q2)] = deconvblind([I](#Q3), [psfi](#Q4), [iter](#Q5), [dampar](#Q6), [weight](#Q7), [readout](#Q8))  
指定加性噪声（如背景和前景噪声）和读出的相机噪声 [readout](#Q8) 的方差。  

## 参数说明  
### 输入参数  

**<a id="Q3"></a>I — 模糊图像**  
数值数组

模糊图像，指定为任意维度的数值数组。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` 

**<a id="Q4"></a>psfi — PSF的初始估计值**  
数值数组

PSF 的初始估计值，指定为数值数组。PSF 还原受初始估计值 psfi 的大小的影响很大，受其中包含的值的影响较小。因此，请指定由 1 组成的数组作为您的 psfi。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` 

**<a id="Q5"></a>iter — 迭代次数**  
10（默认） | 正整数

迭代次数，指定为正整数。

**数据类型：** `double`

**<a id="Q6"></a>dampar — 阻尼的阈值**  
0（默认） | 数值标量

阻尼的阈值，指定为数值标量。迭代之间的偏差小于阈值的像素会出现阻尼。dampar 的数据类型与 I 相同。

**<a id="Q7"></a>weight — 每个像素的权重**
数值数组

每个像素的权重值，指定为由 [0, 1] 范围内的值组成的数值数组。weight 与输入图像 I 大小相同。默认情况下，weight 中的所有元素的值均为 1，因此在还原过程中所有像素的权重相同。

**数据类型：** `double`

**<a id="Q8"></a>readout — 噪声**
0（默认） | 数值标量 | 数值数组

噪声，指定为数值标量或数值数组。readout 的值对应于加性噪声（例如来自前景和背景的噪声）和读出的相机噪声的方差。readout 的数据类型与 I 相同。

### 输出参数  
**<a id="Q1"></a>J — 去模糊后图像**  
数值数组

去模糊后的图像，以数值数组形式返回。

**数据类型：** `double`

**<a id="Q2"></a>psfr — 还原后的PSF**  
由正数组成的数值数组

还原后的 PSF，以正数数组形式返回。psfr 的大小与 PSF 的初始估计值 psfi 的大小相同，并且它经过了归一化，因此元素的总和为 1。

**数据类型：** `double`

## 版本历史  
在北太天元图像处理工具箱 V3.0 推出

## 相关主题  
<a href="../deconvlucy/deconvlucy.html">deconvlucy</a> | <a 
href="../deconvreg/deconvreg.html">deconvreg</a> | <a 
href="../deconvwnr/deconvwnr.html">deconvwnr</a> | <a 
href="../edgetaper/edgetaper.html">edgetaper</a> | <a 
href="../imnoise/imnoise.html">imnoise</a> | <a 
href="../otf2psf/otf2psf.html">otf2psf</a> | <a 
href="../padarray/padarray.html">padarray</a> | <a 
href="../psf2otf/psf2otf.html">psf2otf</a>
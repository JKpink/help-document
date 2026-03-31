## deconvwnr
使用 Wiener 滤波去除图像模糊

## 简介
[`J = deconvwnr(I, psf, nsr)`](#function1)  
[`J = deconvwnr(I, psf, ncorr, icorr)`](#function2)  
[`J = deconvwnr(I, psf)`](#function3)

## 用法
<a id="function1"></a>
[J](#Q6) = deconvwnr([I](#Q1), [psf](#Q2), [nsr](#Q3)) 使用 `Wiener` 滤波算法对图像 `I` 进行反卷积，从而返回去模糊后的图像 `J`。psf 是对 `I` 进行卷积的点扩散函数 `PSF`。nsr 是加性噪声的噪信功率比。在估计图像与真实图像之间的最小均方误差意义上，该算法是最优的。

<a id="function2"></a>
[J](#Q6)  = deconvwnr([I](#Q1), [psf](#Q2), [ncorr](#Q4), [icorr](#Q5)) 对图像 `I` 进行反卷积，其中 `ncorr` 是噪声的自相关函数，`icorr` 是原始图像的自相关函数。

<a id="function3"></a>
[J](#Q6) = deconvwnr([I](#Q1), [psf](#Q2)) 使用 `Wiener` 滤波算法对图像 `I` 进行反卷积，无估计噪声。在不含噪情况下，`Wiener` 滤波等效于理想的逆滤波。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 模糊图像**  
数值数组

模糊图像，指定为任意维度的数值数组。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` | `logical`

**<a id="Q2"></a> psf — 点扩散函数**  
数值数组

点扩散函数，指定为数值数组。

**数据类型：**  `double` 

**<a id="Q3"></a>nsr — 噪信比**  
0 | 非负标量

噪信比，指定为非负标量或与图像 `I` 大小相同的数值数组。如果 `nsr` 是数组，则它表示频谱域。为 `nsr` 指定 0 等效于创建一个理想的逆滤波器。

**数据类型：**  `double` 

**<a id="Q4"></a> ncorr — 噪声的自相关函数**  
数值数组

噪声的自相关函数，指定为任意大小或维度（不超过原始图像）的数值数组。
- 如果 `ncorr` 的维度与图像 `I` 的维度匹配，则值对应于每个维度内的自相关。
- 如果 `ncorr` 是向量，`psf` 也是向量，则 `ncorr` 中的值表示第一个维度的自相关函数。
- 如果 `ncorr` 是向量，`psf` 是数组，则一维自相关函数通过对称性外插至 psf 的所有非单一维度。
- 如果 `ncorr` 是标量，则值表示噪声的功率。

**数据类型：**  `double` 

**<a id="Q5"></a> icorr — 图像的自相关函数**  
数值数组

图像的自相关函数，指定为任意大小或维度（不超过原始图像）的数值数组。
- 如果 `icorr` 的维度与图像 `I` 的维度匹配，则值对应于每个维度内的自相关。
- 如果 `icorr` 是向量，`psf` 也是向量，则 `icorr` 中的值表示第一个维度的自相关函数。
- 如果 `icorr` 是向量，`psf` 是数组，则一维自相关函数通过对称性外插至 `psf` 的所有非单一维度。
- 如果 `icorr` 是标量，则值表示图像的功率。

**数据类型：**  `double` 

### 输出参数
**<a id="Q6"></a> J — 去模糊后的图像**  
数值数组

去模糊后的图像，以数值数组形式返回。`J` 与 `I` 的数据类型相同。

## 参考
Gonzalez R C, Woods R E. Digital image processing. Addison-Wesley Publishing Company, Inc., 1992.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../deconvblind/deconvblind.html">deconvblind</a> | <a href="../deconvlucy/deconvlucy.html">deconvlucy</a> | <a 
href="../deconvreg/deconvreg.html">deconvreg</a> | <a 
href="../edgetaper/edgetaper.html">edgetaper</a> | <a 
href="../otf2psf/otf2psf.html">otf2psf</a> | <a 
href="../padarray/padarray.html">padarray</a> | <a 
href="../psf2otf/psf2otf.html">psf2otf</a> 

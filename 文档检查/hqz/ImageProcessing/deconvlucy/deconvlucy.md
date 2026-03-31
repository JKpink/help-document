## deconvlucy
使用 Lucy-Richardson（露西 - 理查森）算法对图像进行去模糊处理

## 简介
[`J = deconvlucy(I, psf)`](#function1)  

## 用法
<a id="function1"></a>
[J](#Q4) = deconvlucy([I](#Q1), [psf](#Q2))  用于复原图像 `I`，该图像因与点扩散函数（PSF）卷积而退化，也可能叠加了加性噪声。该算法基于泊松统计，最大化复原后图像 `J` 是原始图像 `I` 实例的似然概率。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 模糊图像**  
数值数组

模糊图像：指定为任意维度的数值数组。更多信息，请参见[提示](#提示)。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` | `logical`

**<a id="Q2"></a> psf — 点扩散函数**  
数值数组

点扩散函数：指定为数值数组。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16`

### 输出参数
**<a id="Q4"></a> J — 去模糊后的图像**  
数值数组 | 1x4 单元数组

去模糊后的图像：返回为数值数组或 1×4 元胞数组。`J`（若 `J` 为元胞数组则为 `J{1}`）与 `I` 的数据类型相同。有关将 `J` 以元胞数组形式返回以支持中断迭代的详细信息，请参阅[提示](#提示)。

## 提示
- 您可以使用 `deconvlucy` 执行接续上一次反卷积中断位置的反卷积操作。要使用此功能，需将输入图像 `I` 以元胞数组 `{I}` 的形式传入。此时 `deconvlucy` 函数会以元胞数组形式返回输出图像 `J`，您可将该元胞数组作为输入传入下一次 `deconvlucy` 调用。输出元胞数组 `J` 包含四个元素：

​	`J{1}` 包含原始图像 `I`。

​	`J{2}` 包含最后一次迭代的结果。

​	`J{3}` 包含倒数第二次迭代的结果。

​	`J{4}` 是由迭代算法生成的数组。

- 输出图像 `J` 可能会出现算法中使用的离散傅里叶变换所引入的振铃效应。要减轻振铃效应，可在调用 `deconvlucy` 前执行 `I = edgetaper(I,psf)`。

- `deconvlucy` 会将点扩散函数（PSF）转换为 `double` 类型，且不进行归一化处理。

- `deconvlucy` 返回的输出图像数值范围可能超出输入图像的数值范围。

## 参考
[1] Hanisch R J, White R L, Gilliland R L.Deconvolutions of Hubble Space Telescope images and spectra//Jansson P A. Deconvolution of images and spectra. 2nd ed. CA: Academic Press, 1997.

[2] Biggs D S C, Andrews M.Acceleration of iterative image restoration algorithms. Applied Optics, 1997, 36(8).

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../deconvblind/deconvblind.html">deconvblind</a> | <a href="../deconvreg/deconvreg.html">deconvreg</a> | <a 
href="../deconvwnr/deconvwnr.html">deconvwnr</a> | <a 
href="../edgetaper/edgetaper.html">edgetaper</a> | <a 
href="../otf2psf/otf2psf.html">otf2psf</a> | <a 
href="../padarray/padarray.html">padarray</a> | <a 
href="../psf2otf/psf2otf.html">psf2otf</a> 

## deconvblind
使用盲反卷积对图像进行去模糊

## 简介
[`[J,psfr] = deconvblind(I, psfi)`](#function1)  
[`[J,psfr] = deconvblind(I, psfi, iter)`](#function2)  
[`[J,psfr] = deconvblind(I, psfi, iter, dampar)`](#function3)  
[`[J,psfr] = deconvblind(I, psfi, iter, dampar, weight)`](#function4)  
[`[J,psfr] = deconvblind(I, psfi, iter, dampar, weight, readout)`](#function5)  

## 用法
<a id="function1"></a>
[[J](#P1), [psfr](#P1)] = deconvblind([I](#Q1), [psfi](#Q2))  使用最大似然算法和点扩散函数 (PSF) 的初始估计 `psfi` 对图像 `I` 进行去卷积。该函数返回去模糊后的图像 `J` 和恢复的 PSF `psfr`。

<a id="function2"></a>
[[J](#P1), [psfr](#P1)] = deconvblind([I](#Q1), [psfi](#Q2), [iter](#Q3)) 指定迭代次数 `iter`。

<a id="function3"></a>
[[J](#P1), [psfr](#P1)] = deconvblind([I](#Q1), [psfi](#Q2), [iter](#Q3), [dampar](#Q4)) 通过阻尼阈值 `dampar` 控制噪声放大。默认情况下不进行阻尼。

<a id="function4"></a>
[[J](#P1), [psfr](#P1)] = deconvblind([I](#Q1), [psfi](#Q2), [iter](#Q3), [dampar](#Q4), [weight](#Q5)) 指定在复原过程中考虑输入图像 `I` 中的哪些像素。`weight` 数组中的元素值决定了对应位置像素的考虑权重。

<a id="function5"></a>
[[J](#P1), [psfr](#P1)] = deconvblind([I](#Q1), [psfi](#Q2), [iter](#Q3), [dampar](#Q4), [weight](#Q5), [readout](#Q6)) 指定加性噪声（如背景和前景噪声）以及读出相机噪声的方差 `readout`。

## 参数说明
### 输入参数

**<a id="Q1"></a> I — 模糊图像**  
数值数组 | 元胞数组

模糊图像，指定为任意维度的数值数组。也可以将图像指定为元胞数组以实现中断迭代。有关详细信息，请参阅提示部分。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16`

**<a id="Q2"></a> psfi — PSF 的初始估计**  
数值数组

点扩散函数的初始估计，指定为数值数组。PSF 复原受初始猜测 `psfi` 的大小影响很大，而受其包含的值影响较小。因此，建议将 `psfi` 指定为全 1 数组。

也可以将 `psfi` 指定为元胞数组以实现中断迭代。有关详细信息，请参阅提示部分。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16`

**<a id="Q3"></a> iter — 迭代次数**  
10 （默认） | 正整数

迭代次数，指定为正整数。

**数据类型：** `double`

**<a id="Q4"></a> dampar — 阻尼阈值**  
0 （默认） | 数值标量

阻尼阈值，指定为数值标量。当像素在迭代之间的偏差小于该阈值时，将进行阻尼。`dampar` 与 `I` 具有相同的数据类型。

**<a id="Q5"></a> weight — 每个像素的权重**  
数值数组

每个像素的权重值，指定为取值在 [0, 1] 范围内的数值数组。`weight` 的大小与输入图像 `I` 相同。默认情况下，`weight` 的所有元素值为 1，因此在复原中所有像素被同等考虑。

**数据类型：** `double`

**<a id="Q6"></a> readout — 噪声**  
0 （默认） | 数值标量 | 数值数组

噪声，指定为数值标量或数值数组。`readout` 的值对应于加性噪声（如前景区和背景区的噪声）以及读出相机噪声的方差。`readout` 与 `I` 具有相同的数据类型。

### 输出参数

**<a id="P1"></a> J — 去模糊后的图像**  
数值数组 | 1×4 元胞数组

去模糊后的图像，以数值数组或 1×4 元胞数组形式返回。`J`（或当 `J` 为元胞数组时的 `J{1}`）与 `I` 具有相同的数据类型。有关将 `J` 作为元胞数组返回以实现中断迭代的详细信息，请参阅[提示](#A1)部分。

**<a id="P2"></a> psfr — 恢复的 PSF**  
正数数组 | 1×4 元胞数组

恢复的点扩散函数，以正数数组或 1×4 元胞数组形式返回。`psfr` 的大小与 `PSF` 的初始估计 `psfi` 相同，并且被归一化使其元素之和为 1。有关将 `psfr` 作为元胞数组返回以实现中断迭代的详细信息，请参阅[提示](#A1)部分。

**数据类型：** `double`

## 提示<a id="A1"></a> 

- 可以使用 `deconvblind` 从先前停止的反卷积处继续执行。要实现此功能，将输入图像 `I` 和 PSF 的初始估计 `psfi` 作为元胞数组传递：`{I}` 和 `{psfi}`。此时，`deconvblind` 函数将输出图像 `J` 和恢复的 PSF `psfr` 也作为元胞数组返回，这些元胞数组可以作为输入数组传递给下一次 `deconvblind` 调用。输出元胞数组 `J` 包含四个元素：
    - `J{1}` 包含原始图像 `I`。
    - `J{2}` 包含最后一次迭代的结果。
    - `J{3}` 包含倒数第二次迭代的结果。
    - `J{4}` 是由迭代算法生成的数组。

- 输出图像 `J` 可能会出现由算法中使用的离散傅里叶变换引入的振铃效应。为减少振铃，可以在调用 `deconvblind` 之前使用 `I = edgetaper(I,psfi)`。

## 算法

`deconvblind` 使用最大似然算法进行盲反卷积。该算法通过迭代优化图像和 PSF 的估计，使得复原的图像与观测到的模糊图像之间的误差最小化。具体实现基于加速迭代图像复原算法，并适用于多种图像退化模型。

## 版本历史

在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../deconvlucy/deconvlucy.html">deconvlucy</a> | <a href="../deconvreg/deconvreg.html">deconvreg</a> | <a href="../deconvwnr/deconvwnr.html">deconvwnr</a> | <a href="../edgetaper/edgetaper.html">edgetaper</a> | <a href="../imnoise/imnoise.html">imnoise</a> | <a href="../otf2psf/otf2psf.html">otf2psf</a> | <a href="../padarray/padarray.html">padarray</a> | <a href="../psf2otf/psf2otf.html">psf2otf</a>
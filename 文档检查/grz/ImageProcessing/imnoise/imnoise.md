## imnoise
向图像添加噪声

## 简介
[ `J = imnoise(I, "gaussian")`](#function1)  
[ `J = imnoise(I, "gaussian", m)`](#function2)  
[ `J = imnoise(I, "gaussian", m, var_gauss)`](#function3)  
[ `J = imnoise(I, "localvar", var_local)`](#function4)  
[ `J = imnoise(I, "localvar", intensity_map, var_local)`](#function5)  
[ `J = imnoise(I, "poisson")`](#function6)  
[ `J = imnoise(I, "salt & pepper")`](#function7)  
[ `J = imnoise(I, "salt & pepper", d)`](#function8)  
[ `J = imnoise(I, "speckle")`](#function9)  
[ `J = imnoise(I, "speckle", var_speckle)`](#function10)  
## 用法
<a id="function1"></a>
[J](#P1) = imnoise([I](#Q0), "gaussian") 对灰度图像 `I` 叠加均值为零、方差为 0.01 的高斯白噪声。  
<a id="function2"></a>
[J](#P1) = imnoise([I](#Q0), "gaussian", [m](#Q1)) 在图像 `I` 上叠加均值为 `m`、方差为 0.01 的高斯白噪声。  
<a id="function3"></a>
[J](#P1) = imnoise([I](#Q0), "gaussian", [m](#Q1), [var_gauss](#Q2)) 对图像 `I` 叠加均值为 `m`、方差为 `var_gauss` 的高斯白噪声。  
<a id="function4"></a>
[J](#P1) = imnoise([I](#Q0), "localvar", [var_local](#Q3)) 对图像 `I` 叠加局部方差为 `var_local` 的零均值高斯白噪声。  
<a id="function5"></a>
[J](#P1) = imnoise([I](#Q0), "localvar", [intensity_map](#Q4), [var_local](#Q3)) 叠加零均值高斯白噪声，其局部方差 `var_local` 通过强度映射表与图像 `I` 的像素强度相关联，该映射由向量 `intensity_map` 定义。  
<a id="function6"></a>
[J](#P1) = imnoise([I](#Q0), "poisson") 从数据中生成泊松噪声，而不是向数据中添加人为噪声。  
<a id="function7"></a>
[J](#P1) = imnoise([I](#Q0), "salt & pepper") 以默认密度 0.05 向图像 `I` 中叠加椒盐噪声，预计约 5% 的像素将受影响。  
<a id="function8"></a>
[J](#P1) = imnoise([I](#Q0), "salt & pepper", [d](#Q5)) 按指定噪声密度 `d` 叠加椒盐噪声，预计受影响像素数约为 d*numel(I)。  
<a id="function9"></a>
[J](#P1) = imnoise([I](#Q0), "speckle") 使用方程 J = I+n\*I 添加乘性噪声，其中 `n` 是均值为 0、方差为 0.05 的均匀分布随机噪声。  
<a id="function10"></a>
[J](#P1) = imnoise([I](#Q0), "speckle", ["var_speckle"](#Q6)) 添加方差为 `var_speckle` 的乘性噪声。

## 参数说明
### 输入参数
**<a id="Q0"></a> I — 灰度图像**  
数值数组

灰度图像，指定为任意维度的数值数组。 
对于 `double` 或 `single` 类型的输入图像，`imnoise` 函数要求其像素值处于归一化区间 [0, 1]。若输入数据超出该范围，函数会在噪声添加阶段自动执行边界裁剪。为确保处理过程的数值稳定性与预期效果，建议在处理流程中预先使用 <a href="../rescale/rescale.html">rescale</a> 函数完成数值范围的正规化。 

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16`

**<a id="Q1"></a> m — 高斯噪声的均值**  
0（默认）| 数值标量

高斯噪声的均值，指定为数值标量。

**<a id="Q2"></a> var_gauss — 高斯噪声的方差**  
0.01（默认）| 数值标量

高斯噪声的方差，指定为数值标量。

**<a id="Q3"></a> var_local — 高斯噪声的局部方差**  
数值数组 | 数值向量

高斯噪声的局部方差，指定为数值数组或数值向量。如果指定 [intensity_map](#Q4) 参量，则 `var_local` 必须为长度相同的向量。否则，`var_local` 必须为与输入图像 `I` 大小相同的数组。

**<a id="Q4"></a> intensity_map — 图像强度到噪声方差的映射**  
数值向量

图像强度到噪声方差的映射，指定为数值向量。`imnoise` 函数将图像强度值归一化到范围 [0, 1]。  

**<a id="Q5"></a> d — 噪声密度**  
0.05（默认）| 数值标量

椒盐噪声的噪声密度，指定为数值标量。噪声应用于大约 d*numel(I) 个像素。

**<a id="Q6"></a> var_speckle — 乘性噪声的方差**  
0.05（默认）| 数值标量

乘性噪声的方差，指定为数值标量。

### 输出参数
**<a id="P1"></a> J — 含噪图像**  
数值矩阵

含噪图像，以与输入图像 [I](#Q0) 具有相同数据类型的数值矩阵形式返回。对于数据类型为 `double` 或 `single` 的图像，`imnoise` 函数在添加噪声后将输出像素值裁剪到范围 [0, 1]。

<!-- ## 算法
- 对于指定了均值与方差参数的 "gaussian"、"localvar" 及 "speckle" 噪声类型，其参数定义均基于 `double` 类型且值域归一化至 [0, 1] 的图像模型。当输入图像类型不符时，函数执行以下流程：先将图像转换为 `double` 类型并添加噪声，随后将结果裁剪至 [0, 1] 范围，最终将图像还原至原始数据类型。
- 泊松分布取决于输入图像 [I](#Q0) 的数据类型：  
如果 `I` 为双精度，则会将像素值放大 1e12 倍作为泊松分布的均值参数，生成结果后再等比缩小。例如，如果输入像素的值为 5.5e-12，则对应的输出像素将根据均值为 5.5 的泊松分布生成，然后缩小为 1e12 分之一。  
如果 `I` 为单精度，则使用的缩放因子是 1e6。  
如果 `I` 为 `uint8` 或 `uint16`，则直接使用输入像素值，无需缩放。
- 要将密度为 [d](#Q5) 的 "salt & pepper" 噪声添加到图像中，`imnoise` 首先从开区间 (0, 1) 上的一个标准均匀分布中为每个像素分配一个随机概率值。  
对于概率值在范围 (0, d/2) 内的像素，像素值设置为图像数据类型的最小值（通常为 0）。  
对于概率值在 [d/2, d) 范围内的像素，像素值设置为图像数据类型的最大值。  
对于概率值在 [d, 1) 范围内的像素，像素值保持不变。 -->

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

<!-- ## 相关主题
<a href="../rand/rand.html">rand</a> | <a 
href="../randn/randn.html">randn</a>  -->
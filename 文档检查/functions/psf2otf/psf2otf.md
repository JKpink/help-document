## psf2otf
将点扩散函数（PSF）转换为光学传递函数（OTF）

## 简介
[`OTF = psf2otf(PSF)`](#function1)

## 用法
<a id="function1"></a>
[OTF](#Q2) = psf2otf([PSF](#Q1))  对点扩散函数（PSF） 执行快速傅里叶变换（FFT），生成光学传递函数（OTF），并通过循环移位消除 PSF 中心偏移对 OTF 的影响。

## 参数说明
### 输入参数
**<a id="Q1"></a> PSF — 点扩散函数**  
数值数组

点扩散函数：任意维度的数值数组（支持复数，如含相位信息的 PSF），代表成像系统对单点光源的响应。

**数据类型：**`single` | `double` | `int8/16/32/64` | `uint8/16/32/64`；

**复数支持：**是（若 PSF 含相位偏移，转换后的 OTF 也会保留相位信息）。

### 输出参数
**<a id="Q2"></a> OTF — 光传递函数**  
数值数组

核心特性：

- 幅值（`abs(OTF)`）：表示成像系统对不同空间频率的响应强度，幅值越大，该频率分量保留越好；
- 相位（`angle(OTF)`）：表示成像系统对不同频率分量的相位偏移；
- 物理意义：OTF 是 PSF 的频域表示，空域中 PSF 与图像的卷积等价于频域中 OTF 与图像 FFT 的乘积。

**数据类型：**  `double`   
**复数支持：** 是

## 提示
- PSF 的中心位置不影响最终 OTF：函数通过循环移位将 PSF 中心对齐到 `(1,1)`，确保无论输入 PSF 中心是否偏移，转换后的 OTF 均反映真实的频域响应；
- 补零扩展的作用：避免 FFT 的 “边界效应”，同时匹配图像尺寸，保证频域运算时维度一致。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../circshift/circshift.html">circshift</a> | <a 
href="../fftn/fftn.html">fftn</a> | <a 
href="../ifftn/ifftn.html">ifftn</a> | <a 
href="../otf2psf/otf2psf.html">otf2psf</a> | <a 
href="../padarray/padarray.html">padarray</a>




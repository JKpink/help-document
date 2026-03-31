## otf2psf
将光学传递函数（OTF）转换为点扩散函数（PSF）

## 简介
[`PSF = otf2psf(OTF)`](#function1)

## 用法
<a id="function1"></a>
[PSF](#Q2) = otf2psf([OTF](#Q1)) 对光学传递函数（OTF）执行逆快速傅里叶变换（IFFT），生成以原点为中心的点扩散函数（PSF）。

## 参数说明
### 输入参数
**<a id="Q1"></a> OTF — 光传递函数**  
数值数组

光学传递函数：任意维度的数值数组（支持复数，对应频域的振幅 + 相位信息）。

- **数据类型：**`single` | `double` | `int8/16/32/64` | `uint8/16/32/64`；

- **复数支持：**是（OTF 通常为复数，幅值表示频率响应强度，相位表示频率偏移）。

### 输出参数
**<a id="Q2"></a> PSF — 点扩散函数**  
数值数组

以原点为中心的点扩散函数。

- **数据类型：** `double`。

- **复数支持：**是（若 OTF 含相位信息，PSF 可能为复数）；

## 提示
- 频域运算中，OTF 与图像的 FFT 相乘等价于空域中 PSF 与图像的卷积，`otf2psf` 是验证频域 / 空域转换正确性的关键工具。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../circshift/circshift.html">circshift</a> | <a 
href="../fftn/fftn.html">fftn</a> | <a 
href="../ifftn/ifftn.html">ifftn</a> | <a 
href="../padarray/padarray.html">padarray</a> | <a 
href="../psf2otf/psf2otf.html">psf2otf</a> 




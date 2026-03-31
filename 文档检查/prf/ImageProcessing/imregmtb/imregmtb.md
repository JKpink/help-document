## imregmtb
使用中值阈值位图配准 2 维图像的方法

## 简介
[`[R1, R2,..., Rn, shift] = imregmtb(M1, M2,..., Mn, F)`](#function1)

## 用法 
<a id="function1"></a> [[R1, R2,..., Rn](#P1), [shift](#P2)] = imregmtb([M1, M2,..., Mn](#Q1), [F](#Q2)) 使用中值阈值位图技术，将任意数量的移动图像 M1, M2,.., Mn 与固定参考图像 `F` 进行配准。配准后的图像通过 R1, R2,..., Rn 返回，而配准图像的估计位移通过 shift 返回。

## 参数说明
### 输入参数
**<a id="Q1"></a> M1, M2,..., Mn — 移动图像序列**  
灰度图像 | RGB 图像  

移动图像序列，可指定为一系列灰度图像或 RGB 图像，允许固定曝光或可变曝光。所有图像必须有相同的大小和数据类型。

**数据类型：** `single` | `double` | `uint8` | `uint16`

**<a id="Q2"></a> F —  参考图像**  
灰度图像 | RGB 图像  

参考图像，指定为灰度图像或 RGB 图像。固定图像 `F` 的大小和数据类型必须与移动图像 M1、M2、...、Mn 相同。

**数据类型：** `single` | `double` | `uint8` | `uint16`

## 输出参量
**<a id="P1"></a> R1, R2,..., Rn — 配准后的图像**  
灰度图像 | RGB 图像  

配准后的图像，以一系列灰度图像或 `RGB` 图像的形式返回。配准后图像的大小和数据类型与移动图像 M1、M2、...、Mn 相同。

**<a id="P2"></a> shift — 估计的位移**  
n×2 的数值矩阵  

n 幅配准后的图像在水平和垂直方向上的估计位移，以一个 n×2 的数值矩阵形式返回。
## 参考文献
[1] Reinhard E, Heidrich W, Debevec P, et al. High dynamic range imaging. 2nd ed. San Francisco, CA: Morgan Kaufmann Publishers Inc., 2010: 155–170.
## 版本历史
在北太天元图像处理工具箱 V2.0 推出
## 相关主题
<a href="../blendexposure/blendexposure.html">blendexposure</a> | <a
href="../imtranslate/imtranslate.html">imtranslate</a> | <a 
href="../imregister/imregister.html">imregister</a> | <a 
href="../imregcorr/imregcorr.html">imregcorr</a> | <a 
href="../imregmoment/imregmoment.html">imregmoment</a>
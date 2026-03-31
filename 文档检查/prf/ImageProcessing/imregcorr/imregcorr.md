## imregcorr
使用互相关估计对齐两幅 2 维图像的几何变方法

## 简介
[`tform = imregcorr(moving, fixed)`](#function1)  
[`tform = imregcorr(___, tformType)`](#function2)

## 用法 
<a id="function1"></a> [tform](#P1) = imregcorr([moving](#Q1), [fixed](#Q2)) 采用默认刚体变换模型完成配准，使用互相关估计对齐图像 `moving` 与参考图像 `fixed` 的几何变换。  
<a id="function2"></a> [tform](#P1) = imregcorr(\_\_\_, [tformType](#Q3)) 在基础上，通过 `tformType` 参数指定几何变换类型，灵活适配不同的图像形变场景。`tformType` 指定变换类型。

## 参数说明
### 输入参数
**<a id="Q1"></a> moving — 待配准图像**  
灰度图像 | 二值图像 | RGB 图像  

移动图像，即待配准的图像，可指定为灰度图像、二值图像或 RGB 图像。`imregcorr` 函数在处理前会将 RGB 图像转换为灰度图像。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`

**<a id="Q2"></a> fixed — 参考图像**  
灰度图像 | 二值图像 | RGB 图像  

目标空间中的参考图像，可指定为灰度图像、二值图像或 RGB 图像。
`imregcorr` 函数在处理前会将 `RGB` 图像转换为灰度图像。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`

**<a id="Q3"></a> tformType — 待估计的变换类型**  
"similarity"（默认值）| "rigid（刚体变换）" | "translation（相似变换）" 

待估计的变换类型，根据图像的实际形变类型，选择合适的变换模型，在保证配准精度的同时提升运算速度。

| **值** | **描述** | **约束条件** |
|:-|:-|:-|
| "translation" | 平移变换 | 使用空间参考对象 `Rmoving` 和 `Rfixed` 时，输入图像在世界坐标系中的像素间距必须相同 |
| "rigid" | 刚性变换：平移+旋转 | 使用空间参考对象 `Rmoving` 和 `Rfixed` 时，输入图像在世界坐标系中的像素间距必须相同 |
| "similarity" | 相似性变换：平移+旋转+各向同性缩放 | 使用相位相关法（phase correlation）时，`imregcorr` 无法检测小于 1/4 或大于 4 倍的尺度差异 |

**数据类型：** `char` | `string`

### 输出参数
**<a id="P1"></a> tform — 几何变换对象**  
transltform2d 对象 | rigidtform2d 对象 | simtform2d 对象  

根据变换类型 `tformType`，返回对应的几何变换对象。

| **带估计的变换类型** | **几何变换对象** |
|:-|:-|
| "translation" | transltform2d |
| "rigid" | rigidtform2d |
| "similarity" | simtform2d |  


## 参考文献
[1] Reddy B S , Chatterji B N .An FFT-based technique for translation, rotation, and scale-invariant image registration[J].IEEE Trans Image Process, 1996, 5(8):1266-1271.  
[2] Tzimiropoulos G, Argyriou V, Zafeiriou S, Stathaki T. Robust FFT-based scale-invariant image registration with image gradients. IEEE Trans Pattern Anal Mach Intell, 2010, 32(10):1899-1906. 
## 版本历史
在北太天元图像处理工具箱 V2.0 推出
## 相关主题
<a href="../imwarp /imwarp .html">imwarp </a> | <a
href="../imshowpair/imshowpair.html">imshowpair</a> | <a 
href="../imregister/imregister.html">imregister</a> | <a 
href="../imregtform/imregtform.html">imregtform</a>

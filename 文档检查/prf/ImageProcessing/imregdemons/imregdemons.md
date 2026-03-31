##  imregdemons
基于 Demons 算法的非刚性图像配准函数

## 简介
[`[D,moving_reg] = imregdemons(moving, fixed)`](#function1)  
[`[D,moving_reg] = imregdemons(moving, fixed, N)`](#function2)  
[`[D,moving_reg] = imregdemons(__, Name, Value)`](#function3)

## 用法
<a id="function1"></a> [[D, moving_reg]](#P1) = imregdemons([moving](#Q1), [fixed](#Q2)) 用于将待配准图像`moving`与参考图像`fixed`对齐的位移场`D`。每个像素位置上的位移向量，会将参考图像（`fixed`）像素网格中的位置映射到待配准图像（`moving`）中的对应位置。

<a id="function2"></a> [[D, moving_reg]](#P1) = imregdemons([moving](#Q1), [fixed](#Q2), [N](#Q3)) 用于快速完成非刚性图像配准，通过自定义迭代次数 `N` 控制配准精度 / 耗时，直接返回像素级位移场 `D` 和配准后图像 `moving_reg` 。  

<a id="function3"></a> [[D, moving_reg]](#P1) = imregdemons([__](#Q1), [Name](#Q2), [Value](#Q3)) 通过Name-Value（名称 - 值）对参数精细调控配准细节。
## 参数说明
### 输入参数
**<a id="Q1"></a> moving — 待配准图像**  
二维灰度图 | 三维灰度图  
待配准图像，指定为二维或三维灰度图像。  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`  

**<a id="Q2"></a> fixed — 目标方向的参考图像**      
二维灰度图 | 三维灰度图   

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`  

**<a id="Q3"></a> N — 迭代次数**  
默认次数为100
### 输出参数
**<a id="P1"></a> D — 位移场**  
位移场

**数据类型：** `double`  

**<a id="P1"></a> moving_reg — 对齐图像**  、

二维灰度图 | 三维灰度图  
## 参考文献
[1] Thirion, J.-P. "Image matching as a diffusion process: an analogy with Maxwell’s demons". Medical Image Analysis. Vol. 2, Number 3, 1998, pp. 243–260.

[2] Vercauteren, T., X. Pennec, A. Perchant, N. Ayache, "Diffeomorphic Demons: Efficient Non-parametric Image Registration", NeuroImage. Vol. 45, Number 1, Supplement 1, March 2009, pp. 61–72.
## 版本历史
在北太天元图像处理工具箱 V2.0 推出
## 相关主题
<a href="../imwarp /imwarp .html">imwarp </a> | <a href="../imregcorr /imregcorr .html">imregcorr </a> | <a
href="../imshowpair/imshowpair.html">imshowpair</a> | <a 
href="../imregister/imregister.html">imregister</a> | <a 
href="../imregtform/imregtform.html">imregtform</a>
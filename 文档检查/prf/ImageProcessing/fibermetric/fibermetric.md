## fibermetric
使用 Frangi 血管增强滤波器增强图像中的细长或管状结构
## 简介
[ `J = fibermetric(I)`](#function1)  
[ `J = fibermetric(I，thickness)`](#function2)    
[ `J = fibermetric(___, Name, Value)`](#function3)  
## 用法
<a id="function1"></a>
[J](#Q3) = fibermetric([I](#Q1)) 会使用基于黑塞矩阵的多尺度 Frangi 血管增强滤波器，增强二维或三维灰度图像`I`中的细长或管状结构。返回的图像`J`包含滤波器在与图像中管状结构尺寸大致匹配的厚度下的最大响应。  
<a id="function2"></a>
[J](#Q3) = fibermetric([I](#Q1),[thickness](#Q2)) 用于指定要增强的管状结构的厚度。   
<a id="function3"></a> 
[J](#Q3) = fibermetric(___, [Name, Value](#Q4)) 会使用名称 - 值对参数来控制滤波算法的不同方面。
## 参数说明
### 输入参数
**<a id="Q1"></a> I — 包含细长或管状结构的图像**  
二维灰度图 | 三维灰度图  

二维灰度图像或三维灰度数据的包含细长或管状结构的图像。  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` 
 
**<a id="Q2"></a> thickness — 管状结构的厚度**  
[4 6 8 10 12 14]（默认值） | 正整数 | 正整数向量

以像素为单位的管状结构厚度，需指定为单个正整数或正整数向量。  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`  
###**<a id="Q4"></a> 名称 - 值参数**  

将可选的参量对组指定为 Name1, Value1, ..., NameN, ValueN，其中 Name 是参量名称，Value 是对应的值。名称 — 值参量必须出现在其他参量之后，但参量对组的顺序无关紧要。  

**StructureSensitivity-结构敏感度**  

以`StructureSensitivity`与正数值组成的参数对形式指定，是区分管状结构与背景的阈值。    

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`  

**ObjectPolarity-管状结构的明暗极性**  
'bright'（默认） | 'dark'  

以'ObjectPolarity'与以下值组成的参数对形式指定，用于定义管状结构与背景的明暗关系。  

**数据类型：** `char` | `string`
## 输出参量
**<a id="P1"></a> J — 增强后的图像**  
数值数组  

增强后的图像，其尺寸与输入图像 `I` 一致。若`I`的数据类型为 `double` ，则 `J` 的数据类型也为 `double` ；否则 `J` 的数据类型为`single`。   
**数据类型：**  `single` | `double`
## 参考文献
[1] Frangi, Alejandro F., et al. Multiscale vessel enhancement filtering. Medical Image Computing and Computer-Assisted Intervention — MICCAI'98. Springer Berlin Heidelberg, 1998. pp. 130–137.
## 版本历史
在北太天元图像处理工具箱 V3.0 推出
## 相关主题
<a href="../edge/edge.html">edge</a> | <a
href="../imgradient/imgradient.html">imgradient</a>
## imregister 
基于强度的图像配准

## 简介
[`moving_reg = imregister(moving, fixed, transformType, optimizer, metric) `](#function1)
[`[moving_reg, R_reg] = imregister(moving, Rmoving, fixed, Rfixed, transformType, optimizer, metric) `](#function2)  
[`___ = imregister(___, Name, Value) `](#function3)

## 用法  
<a id="function1"></a> [moving_reg](#P1) = imregister([moving](#Q1), [fixed](#Q3), [transformType](#Q5), [optimizer](#Q6), [metric](#Q7)) 对二维、三维图像 `moving` 进行变换，使其与参考图像 `fixed` 配准。`transformType` 定义要执行的变换类型。`metric` 定义待优化的图像间相似度定量度量。`optimizer` 定义优化该度量的算法。   
<a id="function2"></a> [[moving_reg](#P1), [R_reg](#P2)] = imregister([moving](#Q1), [Rmoving](#Q2), [fixed](#Q3), [Rfixed](#Q4), [transformType](#Q5), [optimizer](#Q6), [metric](#Q7)) 对图像 `moving` 进行变换，使其与参考图像 `fixed` 对齐。`Rmoving` 和 `Rfixed` 为空间参考对象，描述 `moving` 和 `fixed` 图像的世界坐标范围与分辨率。  
<a id="function3"></a> \_\_\_ = imregister(\_\_\_, [Name,Value](#Q8)) 使用一个或多个名称-值对参数指定附加选项。

## 参数说明
### 输入参数
**<a id="Q1"></a> moving — 待配准图像**  
数值矩阵 | 三维数值数组  

待配准图像，指定为表示二维灰度图像的数值矩阵或表示三维灰度体的三维数值数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

**<a id="Q2"></a> Rmoving — 与待配准图像相关联的空间参考信息**  
`imref2d` 对象 | `imref3d` 对象  

与待配准图像相关联的空间参考信息，指定为 <a href="../imref2d/imref2d.html">imref2d</a>  </a> 对象或 <a href="../imref3d/imref3d.html">imref3d</a>  </a> 对象。

**<a id="Q3"></a> fixed — 参考图像**  
数值矩阵 | 三维数值数组  

目标空间中的参考图像，指定为表示二维灰度图像的数值矩阵或表示三维灰度体的三维数值数组。但参考图像的维度必须与待配准图像 [moving](#Q1) 保持一致。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

**<a id="Q4"></a> Rfixed — 与参考图像相关联的空间参考信息**  
`imref2d` 对象 | `imref3d` 对象 

与与参考图像相关联的空间参考信息，指定为 <a href="../imref2d/imref2d.html">imref2d</a>  </a> 对象或 <a href="../imref3d/imref3d.html">imref3d</a>  </a> 对象形式。

**<a id="Q5"></a> transformType — 应用于待配准图像的几何变换**  
`"translation"` | `"rigid"` | `"similarity"` | `"affine"`  

应用于待配准图像的几何变换，指定为以下值之一：

| **值** | **描述** |
|:-|:-|
| `"translation"` | 二维中的 (x, y) 平移，或三维中的 (x, y, z) 平移。 |
| `"rigid"` | 由平移和旋转组成的刚体变换。 |
| `"similarity"` | 由平移、旋转和缩放组成的非反射相似变换。 |
| `"affine"` | 由平移、旋转、缩放和剪切组成的仿射变换。 |

`"similarity"` 和 `"affine"` 变换类型不支持反射。

**数据类型：** `char` | `string`

**<a id="Q6"></a> optimizer — 用于优化相似度度量的方法**  
`RegularStepGradientDescent` 优化器对象 |  `OnePlusOneEvolutionary` 对象    

用于优化相似度度量的方法，指定为 <a href="../RegularStepGradientDescent/RegularStepGradientDescent.html">RegularStepGradientDescent</a>  </a> 或 <a href="../OnePlusOneEvolutionary/OnePlusOneEvolutionary.html">OnePlusOneEvolutionary</a>  </a> 优化器对象。  

**<a id="Q7"></a> metric — 配准过程中要优化的图像相似性度量**  
`MeanSquares` 或 `MattesMutualInformation` 度量对象  

配准过程中要优化的图像相似性度量，指定为 <a href="../MeanSquares/MeanSquares.html">MeanSquares</a>  </a>  或 <a href="../MattesMutualInformation/MattesMutualInformation.html">MattesMutualInformation</a>  </a> 度量对象。

### <a id="Q8"></a> 名称-值参数  

将可选的参量对组指定为 Name1,Value1,...,NameN,ValueN，其中 `Name` 是参量名称，`Value` 是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。

**示例：** "DisplayOptimization"，1 启用详细优化模式。

**DisplayOptimization — 详细优化标志**  
`false`（默认）| `true`  

详细优化标志，指定为逻辑值 `true` 或 `false` ，用于控制 `imregister` 函数在配准过程中是否在命令窗口显示优化信息。

**数据类型：** `logical`

**InitialTransformation — 初始几何变换**  
`affinetform2d` 对象 | `affinetform3d` 对象  

初始几何变换，指定为 <a href="../affinetform2d/affinetform2d.html">affinetform2d</a>  </a> 或 <a href="../affinetform3d/affinetform3d.html">affinetform3d</a>  </a> 对象，作为配准优化的起始变换。

**PyramidLevels — 配准过程中使用的金字塔层级数**  
3（默认）| 正整数  

配准过程中使用的金字塔层级数，指定为正整数。

**数据类型：** `double`

### 输出参量

**<a id="P1"></a> moving_reg — 配准后的图像**  
数值矩阵 | 三维数值数组  

配准后的图像，指定为表示二维灰度图像的二维数值矩阵或表示三维灰度体的三维数值数组。引入的任何与原始图像位置不对应的像素点，填充像素值均为 0。

**<a id="P2"></a> R_reg — 与配准后的图像相关联的空间参考信息**  
`imref2d` 对象 | `imref3d` 对象  

与配准后的图像相关联的空间参考信息，指定为 <a href="../imref2d/imref2d.html">imref2d</a>  </a> 对象或 <a href="../imref3d/imref3d.html">imref3d</a>  </a> 对象。

## 提示
- <a href="../imregtform/imregtform.html">imregtform</a>  </a> 和 `imregister` 使用相同的底层配准算法。`imregister` 在 `imregtform` 计算出的几何变换估计的基础上，额外执行了重采样步骤，以生成与固定图像对齐的输出图像。当您需要获取描述 [moving](#Q1) 图像与 [fixed](#Q3) 图像之间关系的几何变换时，请使用 `imregtform`；当您需要生成对齐后的输出图像时，请使用 `imregister`。
- 在调用 `imregister` 之前，使用 <a href="../imreconfig/imreconfig.html">imreconfig</a>  </a> 函数创建  [optimizer](#Q6) 和 [metric](#Q7)。基于优化的图像配准要获得良好的结果，通常需要根据待配准的图像对修改优化器或度量的设置。`imregconfig` 函数提供了一个默认配置，该配置仅应作为起点。例如，如果您增加优化器中的迭代次数、减小优化器步长，或者更改随机度量中的样本数量，在牺牲性能的前提下，配准效果会在一定程度上得到提升。有关您可以修改的不同参数的更多信息，请参见 `imregconfig` 的输出。
- 如果图像的空间缩放比例差异超过 10%，请在配准之前使用 <a href="../imresize/imresize.html">imresize</a>  </a> 调整其大小。
- 使用 <a href="../imshowpair/imshowpair.html">imshowpair</a>  </a> 或 <a href="../imfuse/imfuse.html">imfuse</a>  </a> 可视化配准结果。
- 您可以在自动化工作流程中使用 `imregister` 来配准多个图像。
- 当您拥有要配准图像的空间参考信息时，请使用空间参考对象将该信息指定给 `imregister`。因为可以考虑到比例差异，所以这有助于 `imregister` 更快地获得更好的结果。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../imregconfig/imregconfig.html">imregconfig</a> | <a
href="../imregcorr/imregcorr.html">imregcorr</a> | <a 
href="../imregtform/imregtform.html">imregtform</a> | <a 
href="../imwarp/imwarp.html">imwarp</a> | <a 
href="../imshowpair/imshowpair.html">imshowpair</a> | <a 
href="../imfuse/imfuse.html">imfuse </a> | <a 
href="../imregicp/imregicp.html">imregicp</a> 

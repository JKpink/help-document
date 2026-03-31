## imregtform
估计对齐两幅二维或三维图像的几何变换

## 简介
[`tform = imregtform(moving, fixed, tformType, optimizer, metric)`](#function1)  
[`tform = imregtform(moving, Rmoving, fixed, Rfixed, tformType, optimizer, metric)`](#function2)  
[`tform = imregtform(___, Name, Value)`](#function3)

## 用法 
<a id="function1"></a> [tform](#P1) = imregtform([moving](#Q1), [fixed](#Q2), [tformType](#Q5), [optimizer](#Q6), [metric](#Q7)) 估计将待配准的图像 `moving` 与参考图像 `fixed` 对齐的几何变换。`tformType` 定义要执行的变换类型，`optimizer` 定义优化图像之间相似度度量 `metric` 的方法。  
<a id="function2"></a> [tform](#P1) = imregtform([moving](#Q1), [Rmoving](#Q3), [fixed](#Q2), [Rfixed](#Q4), [tformType](#Q5), [optimizer](#Q6), [metric](#Q7)) 估计将待配准图像 `moving` 与参考图像 `fixed` 对齐的几何变换。`Rmoving` 和 `Rfixed` 分别指定与配准图像和参考图像关联的空间参考对象。  
<a id="function3"></a> tform = imregtform(\_\_\_, [Name, Value](#Q8)) 使用名称-值参量来控制各个方面。

## 参数说明
### 输入参数
**<a id="Q1"></a> moving — 待配准图像**  
二维灰度图像 | 三维灰度体数据  

待配准图像，指定为表示二维灰度图像的数值矩阵或表示三维灰度体的三维数值数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

**<a id="Q2"></a> fixed — 参考图像**  
二维灰度图像 | 三维灰度体数据  

目标空间中的参考图像，指定为二维灰度图像或三维灰度体图像。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

**<a id="Q3"></a> Rmoving — 与待配准图像相关联的空间参考信息**  
`imref2d` 对象 | `imref3d` 对象  

与待配准图像相关联的空间参考信息，指定为 <a href="../imref2d/imref2d.html">imref2d</a>  </a> 或 <a href="../imref3d/imref3d.html">imref3d</a>  </a> 对象。

**<a id="Q4"></a> Rfixed — 与参考图像相关联的空间参考信息**  
`imref2d` 对象 | `imref3d` 对象  

与参考图像相关联的空间参考信息，指定为 <a href="../imref2d/imref2d.html">imref2d</a>  </a> 或 <a href="../imref3d/imref3d.html">imref3d</a>  </a> 对象。

**<a id="Q5"></a> tformType — 应用于待配准图像的几何变换**  
`"translation"` | `"rigid"` | `"similarity"` | `"affine"`   

应用于待配准图像的几何变换，指定为以下值之一：

| **值** | **描述** |
|:-|:-|
| `"translation"` | 二维中的 (x, y) 平移，或三维中的 (x, y, z) 平移。 |
| `"rigid"` | 由平移和旋转组成的刚体变换。 |
| `"similarity"` | 由平移、旋转和缩放组成的非反射相似变换。 |
| `"affine"` | 由平移、旋转、缩放和剪切组成的仿射变换。 |
  
`"similarity"` 和 `"affine"` 变换类型不支持反射。

**<a id="Q6"></a> optimizer — 用于优化相似度度量的方法**  
`RegularStepGradientDescent` 对象 | `OnePlusOneEvolutionary` 对象  

用于优化相似度度量的方法，指定为 <a href="../RegularStepGradientDescent/RegularStepGradientDescent.html">RegularStepGradientDescent</a>  </a> 或 <a href="../OnePlusOneEvolutionary/OnePlusOneEvolutionary.html">OnePlusOneEvolutionary</a>  </a> 优化器对象。  

**数据类型：** `char` | `string`  

**<a id="Q7"></a> metric — 配准过程中要优化的图像相似度度量**  
`MeanSquares` 对象 | `MattesMutualInformation` 对象  

配准过程中要优化的图像相似度度量，指定为一个 <a href="../MeanSquares/MeanSquares.html">MeanSquares</a>  </a>  或 <a href="../MattesMutualInformation/MattesMutualInformation.html">MattesMutualInformation</a>  </a> 度量对象。

### <a id="Q8"></a> 名称-值参数

将可选的参量对组指定为 Name1,Value1,...,NameN,ValueN，其中 `Name` 是参量名称，`Value` 是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。

**DisplayOptimization — 显示优化信息**  
`false`（默认）| `true`  

配准过程中是否在命令行窗口显示优化信息，指定为逻辑值 `true` 或 `false`。

**数据类型：** `logical`

**InitialTransformation — 初始几何变换**  
几何变换对象  
  
初始几何变换，指定为下表所列的几何变换对象之一：  

|几何变换对象|描述|
|---|---|
|二维线性几何变换|
|<a href="../transltform2d/transltform2d.html">transltform2d</a>  </a>|平移变换|
|<a href="../rigidtform2d/rigidtform2d.html">rigidtform2d</a>  </a>|刚性变换：平移和旋转|
|<a href="../simtform2d/simtform2d.html">simtform2d</a>  </a>|相似变换：平移、旋转和各向同性缩放|
|<a href="../affinetform2d/affinetform2d.html">affinetform2d</a>  </a>|仿射变换：平移、旋转、各向异性缩放、反射和剪切|
|<a href="../projtform2d/projtform2d.html">projtform2d</a>  </a>|投影变换|
|三维线性几何变换|
|<a href="../transltform3d/transltform3d.html">transltform3d</a>  </a>|平移变换|
|<a href="../rigidtform3d/rigidtform3d.html">rigidtform3d</a>  </a>|刚性变换：平移和旋转|
|<a href="../simtform3d/simtform3d.html">simtform3d</a>  </a>|相似变换：平移、旋转和各向同性缩放|
|<a href="../affinetform3d/affinetform2、3d.html">affinetform3d</a>  </a>|仿射变换：平移、旋转、各向异性缩放、反射和剪切|

**PyramidLevels — 配准金字塔层级数**  
3（默认）| 正整数  

配准金字塔层级数，指定为正整数。

### 输出参量
**<a id="P1"></a> tform — 几何变换**  
几何变换对象  

根据输入图像的维度和指定的变换类型参数 [tformType](#Q5)，返回对应的几何变换对象。

| **变换类型** | **二维几何变换对象** | **三维几何变换对象** |
|:-|:-|:-|
| "translation" | <a href="../transltform2d/transltform2d.html">transltform2d</a>  </a> | <a href="../transltform3d/transltform3d.html">transltform3d</a>  </a> |
| "rigid" | <a href="../rigidtform2d/rigidtform2d.html">rigidtform2d</a>  </a> | <a href="../rigidtform3d/rigidtform3d.html">rigidtform3d</a>  </a> |
| "similarity" | <a href="../simtform2d/simtform2d.html">simtform2d</a>  </a> | <a href="../rigidtform3d/rigidtform3d.html">rigidtform3d</a>  </a> |
| "affine" | <a href="../affinetform2d/affinetform2d.html">affinetform2d</a>  </a> | <a href="../affinetform3d/affinetform3d.html">affinetform3d</a>  </a> |


## 提示
- 当你拥有空间参考信息时，使用空间参考对象将此信息提供给 `imregtform` 是很重要的。此信息有助于 `imregtform` 更快地收敛到更佳的结果，因为可以考虑到尺度差异。
- `imregtform` 和 <a href="../imregister/imregister.html">imregister</a>  </a> 使用相同的底层配准算法。`imregister` 在 `imregtform` 计算得到几何变换的基础上，额外对 [moving](#Q1) 执行重采样步骤，以生成配准后的输出图像。当需要获取关联 `moving` 与 [fixed](#Q2) 的几何变换时，请使用 `imregtform`；当您需要获得配准输出图像时，请使用 `imregister`。
- 基于优化的图像配准要取得良好的效果，通常需要根据待配准的图像对调整优化器和/或相似性测度的设置。`imregconfig` 函数提供了一个默认配置，但这仅应视为一个起点。有关可调整的不同参数的更多信息，请参见 `imregconfig` 的输出内容。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出
## 相关主题
### 函数
<a href="../imregconfig/imregconfig.html">imregconfig</a> | <a
href="../imregister/imregister.html">imregister</a> | <a 
href="../imshowpair/imshowpair.html">imshowpair</a> | <a 
href="../imwarp/imwarp.html">imwarp</a>
### 对象
 <a 
href="../affinetform2d/affinetform2d.html">affinetform2d</a> | <a 
href="../affinetform3d/affinetform3d.html">affinetform3d</a> 

## imregconfig
配置基于强度的配准

## 简介
[`[optimizer, metric] = imregconfig(modality)`](#function1)

## 用法 
<a id="function1"></a> [[optimizer](#P1), [metric](#P2)] = imregconfig([modality](#Q1)) 创建基于灰度值的图像配准的优化器和相似性度量配置，将它们传递给 <a href="../imregister/imregister.html">imregister</a>  </a> 以执行基于强度的图像配准，其中 `modality` 用于指定图像采集模式。

## 参数说明
### 输入参数
**<a id="Q1"></a> modality — 图像采集模式**  
`"monomodal"` | `"multimodal"`   

图像采集模式，可选值为以下两种：

| **模式** | **说明** |
|:---|:---|
| `"monomodal"` | 图像具有相似的亮度和对比度，通常由同类型扫描仪或传感器采集 |
| `"multimodal"` | 图像具有不同的亮度和对比度，可能来自不同设备（如不同型号相机或 CT/MRI 等不同医学成像设备）或同一设备的不同设置（如相机不同曝光参数、MRI 不同成像序列）|

**数据类型：** `char` | `string`

### 输出参数
**<a id="P1"></a> optimizer — 优化器配置**  
`RegularStepGradientDescent` 或 `OnePlusOneEvolutionary` 优化器对象  
  
优化器配置，以 <a href="../RegularStepGradientDescent/RegularStepGradientDescent.html">RegularStepGradientDescent</a>  </a> 或 <a href="../OnePlusOneEvolutionary/OnePlusOneEvolutionary.html">OnePlusOneEvolutionary</a>  </a> 优化器对象返回。

**<a id="P2"></a> metric — 相似性度量配置**  
`MeanSquares` 或 `MattesMutualInformation` 度量对象  

相似性度量配置，描述配准过程中待优化的图像相似度度量方法，以 <a href="../MeanSquares/MeanSquares.html">MeanSquares</a>  </a> 或 <a href="../MattesMutualInformation/MattesMutualInformation.html">MattesMutualInformation</a>  </a> 度量对象形式返回。

## 提示
- `imregconfig` 返回具有默认设置的 [optimizer](#P1) 和 [metric](#P2)，以提供基本的配准配置。如果调整优化器或度量属性，则可以改善配准结果。例如，如果增加优化器中的迭代次数、减小优化器步长，或者更改随机度量中的样本数，配准效果会在一定程度上得到提升，但会以性能为代价。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
### 函数
<a href="../imshowpair/imshowpair.html">imshowpair</a> | <a
href="../imregister/imregister.html">imregister</a> 
### 对象
<a 
href="../MattesMutualInformationMattesMutualInformation.html">MattesMutualInformation</a> |<a 
href="../MeanSquares/MeanSquares.html">MeanSquares</a> | <a href="../RegularStepGradientDescent|RegularStepGradientDescent.html">RegularStepGradientDescent</a> | <a 
href="../ OnePlusOneEvolutionary/ OnePlusOneEvolutionary.html"> OnePlusOneEvolutionary</a> 

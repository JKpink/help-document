## RegularStepGradientDescent
基于固定步长的梯度下降优化算法

## 简介 
RegularStepGradientDescent 是基于固定步长的梯度下降优化算法，核心用于图像配准中的变换参数优化，通过沿着相似性度量的梯度方向，以固定步长迭代更新几何变换参数，最终找到使度量值最优（MSE 最小化 / 互信息最大化）的配准参数。

## 属性
**GradientMagnitudeTolerance — 梯度幅值容差**  
1e-4（默认） | 正标量  

梯度幅值容差，指定为正标量，默认为 1e-4。此参数控制优化过程的停止条件：当梯度幅值小于此阈值时，可能表示优化器已到达平稳状态。

**数据类型：** `double` | `single` | `uint8` | `uint16` | `uint32` | `uint64` | `int8` | `int16` | `int32` | `int64`

**MinimumStepLength — 收敛容差**  
1e-5（默认）| 正标量  

收敛容差，指定为一个正标量，默认为 1e-5。`MinimumStepLength` 控制收敛的精度。如果你将 `MinimumStepLength` 设置为一个较小的值，优化计算所需的时间会更长，但更有可能收敛到更精确的度量值。

**数据类型：** `double` | `single` | `uint8` | `uint16` | `uint32` | `uint64` | `int8` | `int16` | `int32` | `int64`

**MaximumStepLength — 初始步长**  
0.0625（默认值）| 正标量  

初始步长，指定为一个正标量，默认为 0.0625。由于优化器在收敛过程中会减小步长，所以初始步长即为最大步长。如果将 `MaximumStepLength` 设置为一个较大的值，计算时间会减少。然而，如果将 `MaximumStepLength` 设置得过大，优化器可能无法收敛。

**数据类型：** `double` | `single` | `uint8` | `uint16` | `uint32` | `uint64` | `int8` | `int16` | `int32` | `int64`

**MaximumIterations — 迭代的最大次数**  
100（默认值）| 正整数标量  

迭代的最大次数，指定为一个正整数标量，默认为 100。`MaximumIterations` 是一个正整数值，它决定了优化器在任意给定的金字塔层级上执行的最大迭代次数。在优化器达到最大迭代次数之前，配准过程可能就已经收敛。

**数据类型：** `double` | `single` | `uint8` | `uint16` | `uint32` | `uint64` | `int8` | `int16` | `int32` | `int64`

**RelaxationFactor — 步长缩减因子**  
0.5（默认）| 介于 0 和 1 之间的正标量   

步长缩减因子，指定为一个 0 到 1 之间的正标量，默认为 0.5。`RelaxationFactor`定义了优化器在收敛过程中缩减步长的速率。每当优化器判定梯度方向发生改变时，就会缩减步长。如果你的度量值存在噪声，你可以将 `RelaxationFactor` 设置为一个更大的值。这样能使收敛过程更稳定，但会增加计算时间。

**数据类型：** `double` | `single` | `uint8` | `uint16` | `uint32` | `uint64` | `int8` | `int16` | `int32` | `int64`

## 算法
常规步长梯度下降优化会调整变换参数，使优化过程沿着图像相似性度量的梯度方向趋近极值点。它在计算之间沿梯度方向采用固定长度的步长前进，直到梯度方向发生变化。此时，步长会根据 `RelaxationFactor`（松弛因子）进行缩减，默认情况下步长将减半。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
### 函数
<a href="../imregister/imregister.html">imregister</a> | <a
href="../imregconfig/imregconfig.html">imregconfig</a> 
### 对象
<a 
href="../MattesMutualInformation/MattesMutualInformation.html">MattesMutualInformation</a> | <a 
href="../MeanSquares/MeanSquares.html">MeanSquares </a> | <a 
href="../OnePlusOneEvolutionary/OnePlusOneEvolutionary.html">OnePlusOneEvolutionary</a> 
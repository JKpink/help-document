## OnePlusoneEvolutionary  
One-plus-one进化优化器配置  
  
## 属性  
**GrowthFactor —— 搜素半径的增长因子**  
1.05 (默认) | 正标量  
  
搜索半径的增长因子，指定为正标量。优化器会借助 `GrowthFactor` 来控制参数空间中搜索半径的增长速率。若将 `GrowthFactor` 设为较大值，优化速度会更快，但可能仅能找到度量的局部极值；若将 `GrowthFactor` 设为较小值，优化速度会更慢，但更有可能收敛到更优的解。
  
**数据类型：**`double` | `single` | `int8` | `int16` | `int32` | `int64` | `unit8` | `unit16` | `unit32` | `unit64`  
  
**Epsilon —— 搜素半径的最小值**  
1.5e-6（默认）| 正标量  
  
搜索半径的最小值，指定为正标量。`Epsilon` 通过调整搜索半径的最小值来控制收敛精度。若将 `Epsilon` 设为较小值，度量的优化结果会更精确，但计算耗时会更长；若将 `Epsilon` 设为较大值，计算时间会缩短，但精度会因此降低。  
  
**数据类型：**`double` | `single` | `int8` | `int16` | `int32` | `int64` | `unit8` | `unit16` | `unit32` | `unit64`   
  
**InitialRadius  —— 搜索半径的初始值**  
6.25e-3 | 正标量  
  
搜索半径的初始值，指定为正标量。若将 `InitialRadius` 设为较大值，可减少计算时间；但 `InitialRadius` 设置过大可能会导致优化过程无法收敛。  
  
**数据类型：**`double` | `single` | `int8` | `int16` | `int32` | `int64` | `unit8` | `unit16` | `unit32` | `unit64`     
  
**MaximumIterations  —— 优化器的最大迭代次数**  
100（默认）| 正标量  
    
优化器的最大迭代次数，指定为正标量。`MaximumIterations` 决定了优化器在任意给定金字塔层级下执行的最大迭代次数，而配准过程可能在优化器达到最大迭代次数之前就完成收敛。  
  
**数据类型：**`double` | `single` | `int8` | `int16` | `int32` | `int64` | `unit8` | `unit16` | `unit32` | `unit64` 
  
  
## 相关主题
<a href="../imregister/imregister.html">imregister</a> | <a
href="../imregconfig/imregconfig.html">imregconfig</a> 
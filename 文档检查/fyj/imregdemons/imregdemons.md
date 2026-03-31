## imregdemons  
估计对齐两幅二维或三维图像的位移场  
  
## 简介  
[`[D, moving_reg] = imregdemons(moving, fixed)`](#function1)  
[`[D, moving_reg] = imregdemons(moving, fixed, N)`](#function2)  
[`[D, moving_reg] = imregdemons(__, Name, Value)`](#function3)  
  
## 用法  
<a id="function1"></a>[[D](#P1), [moving_reg](#P2)] = imregdemons([moving](#P3), [fixed](#P4)) 估计一个位移场 `D`，用于将待配准图像 `moving` 与参考图像 `fixed` 对齐。每个像素位置的位移向量，会将待配准图像网格中的位置映射到参考图像中的对应位置。根据位移场 `D` 变形并通过线性插值重新采样，输出待配准图像的变形版本。  
<a id="function2"></a>[[D](#P1), [moving_reg](#P2)] = imregdemons([moving](#P3), [fixed](#P4), [N](#P5)) 指定迭代计算的次数 `N` 。该函数不使用收敛判断准则，因此会确保运行指定次数（或默认次数）的迭代。    
<a id="function3"></a>[[D](#P1), [moving_reg](#P2)] = imregdemons(__,  [Name, Value](#P6)) 通过名称 - 值对参数控制权重计算的相关环节，完成待配准图像的配准。  
  
## 参数说明
### 输入参数
**<a id="P3"></a> moving — 待配准图像**  
二维灰度图像 | 三维灰度图像  
  
待配准的图像，指定为二维或三维灰度图像。  
  
**数据类型：** `logical` | `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`  
  
**<a id="P4"></a> fixed — 目标姿态下的参考图像**   
二维灰度图像 | 三维灰度图像  
  
目标姿态下的参考图像，指定为二维或三维灰度图像。  
  
**数据类型：** `logical` | `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`  
  
**<a id="P5"></a> N — 迭代次数**  
100（默认） | 正整数标量或向量  
  
迭代次数，指定为正整数标量或向量。   
当你指定为向量时，则 `N` 代表每个金字塔层级对应的的迭代次数。例如，如果有 3 个金字塔层级，你可以指定向量 (100, 50, 25)，这表示在最低分辨率层级执行 100 次迭代，在中间金字塔层级执行 50 次，在最后一个迭代层级执行 25 次。由于低分辨率层级的处理速度更快，因此在低分辨率层级运行更多迭代、在金字塔的高分辨率层级运行更少迭代，有助于提升性能。  
  
**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` |  `uint32`  
  
### <a id="P6"></a> 名称-值参数  
将可选的参量对组指定为 Name1,Value1,...,NameN,ValueN，其中 `Name` 是参量名称，`Value` 是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。  
  
**示例** : 'AccumulatedFieldSmoothing' , 1.5 表示每次迭代应用标准差为 1.5 的高斯平滑。  
  
**AccumulatedFieldSmoothing — 每次迭代的平滑参数**  
1.0（默认）| 正标量  

`AccumulatedFieldSmoothing` 是用于控制每次迭代平滑操作的名称 - 值对参数，需以 `AccumulatedFieldSmoothing` 和一个数值形式的逗号分割对来指定；该参数用于调控类扩散正则化的强度，`imregdemons` 会在每次迭代时，以该参数指定的标准差对累计位移场进行高斯平滑正则化，参数取值越大，输出位移场越平滑；取值越小，输出形变越局部化，典型的取值范围为 [0.5,3.0] ;若指定了多个金字塔层级，各金字塔层级所使用的高斯平滑标准差将保持一致，

**数据类型：** `double`  
  
**PyramidLevels — 要使用的多分辨率图像金字塔层级数**  
3.0（默认）| 正整数  
  
要使用的多分辨率图像金字塔层级数，需以 `PyramidLevels` 和一个正整数组成的逗号分隔对形式设置。  
  
**数据类型：** `double`  
  
**DisplayWaitbar — 显示进度条**  
`true`（默认）| `false`  
  
显示进度条以指示配准进度，需以 `DisplayWaitbar` 和 `true` 或 `false` 组成的逗号分割对形式设置。当设为 `true` 时，对于耗时较长的运算，`imregdemons` 会显示进度条；若要禁止显示进度条，需将`DisplayWaitbar` 设为 `false`。  
  
**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `int64` |`uint8` | `uint16` |  `uint32` | `unit64` | `logical`      
  
  
###  输出参数  
**<a id="P1"></a> D — 位移场**  
数值数组  
  
位移场，指定为数值数组。位移值的单位为像素。  
  
- 若参考图像 [fixed](#P4) 是尺寸为 m × n 的二维灰度图像，则位移场数组的大小为 m × n × 2。其中，D( : , : , 1) 存储 `x` 轴方向的位移，D( : , : , 2 ) 存储 `y` 轴方向的位移。  
- 若参考图像 `fixed` 是尺寸为 m × n × p 的三维灰度图像，则位移场数组的大小为 m × n × p × 3。其中，D( : , : , : , 1 ) 存储 `x` 轴方向的位移，D( : , : , : , 2 ) 存储 `y` 轴方向的位移，D( : , : , : , 3 ) 存储 `z` 轴方向的位移。  
  
**数据类型：** `double`  
  
**<a id="P2"></a> moving_reg — 配准后的图像**  
二维或三维灰度图像  
  
配准后的图像，指定为二维或三维灰度图像。该图像会根据位移场 `D` 完成变形，并通过线性插值重新采样得到。  

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../imregcorr/imregcorr.html">imregcorr</a> | <a  
href="../imregister/imregister.html">imregister</a> | <a  
href="../imregtform/imregtform.html">imregtform</a> | <a   
href="../imshowpair/imshowpair.html">imshowpair</a> | <a  
href="../imwarp/imwarp.html">imwarp</a> | <a  
href="../imregdeform/imregdeform.html">imregdeform</a> | <a      
href="../imreggroupwise/imreggroupwise.html">imreggroupwise</a>  
   
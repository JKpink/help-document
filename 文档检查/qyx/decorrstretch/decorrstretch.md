## decorrstretch
对多通道图像应用去相关性拉伸

## 简介
[ `S = decorrstretch(A)`](#function1)  
[ `S = decorrstretch(A,Name,Value)`](#function2)

## 用法
<a id="function1"></a>
[S](#Q3) = decorrstretch([A](#Q1)) 对 RGB 图像或多光谱图像 A 执行去相关拉伸，并将处理结果返回至 S。输出图像 S  中每个通道的均值和方差与输入图像 A 保持一致。  
去相关性拉伸的主要用途是图像视觉增强，它是一种提升图像色彩差异辨识度的处理手段。  
<a id="function2"></a>
[S](#Q3) = decorrstretch([A](#Q1), [Name,Value](#Q2)) 通过名称 - 值对组参数，控制去相关性拉伸的各项特性，例如设置去相关性的计算方法。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 待增强图像**  
RGB 图像 | 多光谱图像

待增强的输入图像，指定为尺寸为 m×n×nBands 的 RGB 图像或多光谱图像。对于 RGB 图像，通道数 nBands 固定为 3。

**数据类型**：`single` | `double` | `int16` | `uint8` | `uint16`

**<a id="Q2"></a> 名称 — 值参数**    
指定可选的参数对 Name1=Value1,...,NameN=ValueN。名称参数需放在其他参数之后，参数对的顺序不影响结果。  
示例：S = decorrstretch(A,"Mode","covariance") 将去相关方法指定为 “协方差” 法。

**Mode — 去相关性计算方法**   
"correlation"（默认） | "covariance" 

去相关性计算方法，指定为以下两种取值之一：  

- "correlation" — 对通道间的相关矩阵进行特征分解。  
- "covariance" — 对通道间的协方差矩阵进行特征分解。

**数据类型**：`char` | `string`

### 输出参数
**<a id="Q3"></a> S — 去相关性拉伸后的图像**  
数值数组

去相关拉伸后的输出图像，返回的数值数组与输入图像 [A](#Q1) 尺寸相同、数据类型相同。

## 提示
- 直接执行去相关性拉伸（不启用对比度拉伸选项）时，输出结果可能超出 uint8 或 uint16 类型的数值范围（例如出现负值，或数值超过 255、65535）。这种情况下，函数会将输出值截断至该数据类型支持的取值范围内。  
- 对于 double 类型的图像，只有在指定 Tol 参数（即执行线性对比度拉伸）后，函数才会将输出结果截断至区间 [0,1] 内。
- 各可选参数之间基本不存在交互影响，但线性对比度拉伸通常会同时改变图像各通道的均值和标准差。因此，即使同时指定 TargetMean、TargetSigma 和 Tol，前两个参数的效果也会被 Tol 改变。

## 算法
去相关性拉伸是一种线性的逐像素运算，其运算参数由图像的实际统计量和期望（目标）统计量决定。对于输入图像 A 中某一像素在各通道的取值向量 a，其在输出图像 B 中对应像素的向量 b 按如下公式变换：

$b = T \cdot (a - m) + m_{\mathrm{target}}$ 

其中：  

- a 和 b 为 nBands×1 的列向量。  

- T 为 nBands×nBands 的变换矩阵。  

- m 和 mtarget​ 为 nBands×1 的列向量。  

- m 包含图像（或指定像素子集）各通道的均值。  

- mtarget​ 包含输出图像各通道的期望均值，默认取值为 mtarget​=m。  
  线性变换矩阵 T 的计算取决于以下：  

- 图像（或指定像素子集）的通道间采样协方差矩阵 Cov（与计算 m 所用的像素子集相同）。  

- 输出图像各通道的期望标准差，可方便地表示为对角矩阵 SIGMAtarget。默认取值为 SIGMAtarget=SIGMA，其中 SIGMA 是包含图像各通道采样标准差的对角矩阵，其元素满足：

$\text{SIGMA}(k,k) = \sqrt{\text{Cov}(k,k)}, \quad k=1,2,\dots,n\text{Bands}$

Cov、SIGMA、SIGMAtarget​ 均为 nBands×nBands 的矩阵，后续定义的相关矩阵 Corr、特征值矩阵 LAMBDA 和正交矩阵 V 也为同尺寸矩阵。  

变换矩阵 T 的计算步骤如下：
对协方差矩阵 Cov 或相关矩阵 Corr 进行特征分解，其中相关矩阵的计算公式为：

$\text{Corr} = \text{SIGMA}^{-1} \cdot \text{Cov} \cdot \text{SIGMA}^{-1}$

- 基于相关矩阵的方法：对 Corr 分解，满足：  
$\text{Corr} = \boldsymbol{V} \cdot \text{LAMBDA} \cdot \boldsymbol{V}'$  

- 基于协方差矩阵的方法：对 Cov 分解，满足：  
$\text{Cov} = \boldsymbol{V} \cdot \text{LAMBDA} \cdot \boldsymbol{V}'$      
其中 LAMBDA 为特征值对角矩阵，V 为能将 Corr 或 Cov 变换为 LAMBDA 的正交矩阵。  
计算各通道的拉伸因子，取值为对应特征值的平方根倒数。将拉伸因子表示为对角矩阵 S，其元素满足：   
$S(k,k) = \frac{1}{\sqrt{\text{LAMBDA}(k,k)}}$   
  根据不同的去相关方法，计算变换矩阵 T：

- 基于相关矩阵的方法：       
$\boldsymbol{T} = \text{SIGMA}_{\text{target}} \cdot \boldsymbol{V} \cdot \boldsymbol{S} \cdot \boldsymbol{V}' \cdot \text{SIGMA}^{-1}$

- 基于协方差矩阵的方法：  
  $\boldsymbol{T} = \text{SIGMA}_{\text{target}} \cdot \boldsymbol{V} \cdot \boldsymbol{S} \cdot \boldsymbol{V}'$ 
  
  当图像各通道的方差一致时，两种方法的计算结果完全相同。
  将 T 代入 b 的计算公式，可得：    
$$
\boldsymbol{b} = \boldsymbol{m}_{\mathrm{target}} + \mathrm{SIGMA}_{\mathrm{target}} \cdot \boldsymbol{V} \cdot \boldsymbol{S} \cdot \boldsymbol{V}' \cdot \mathrm{SIGMA}^{-1} \cdot (\boldsymbol{a} - \boldsymbol{m})
$$
  或  
                                   $\boldsymbol{b} = \boldsymbol{m}_{\text{target}} + \text{SIGMA}_{\text{target}} \cdot \boldsymbol{V} \cdot \boldsymbol{S} \cdot \boldsymbol{V}' \cdot (\boldsymbol{a} - \boldsymbol{m})$    

  从右向左拆解公式可以看出，去相关拉伸的处理流程为：  

- 对各通道像素值进行去均值处理。  

- 对各通道像素值进行标准差归一化（仅基于相关矩阵的方法包含此步骤）。  

- 将通道空间旋转至相关矩阵或协方差矩阵的特征空间。  

- 在特征空间内执行拉伸操作，使图像在特征空间内实现去相关和归一化。  

- 旋转回原始通道空间，此时各通道仍保持去相关和归一化状态。  

- 按照目标标准差 SIGMAtarget​ 对各通道进行缩放。  

- 恢复各通道的目标均值。

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../imadjust/imadjust.html">imadjust</a> 
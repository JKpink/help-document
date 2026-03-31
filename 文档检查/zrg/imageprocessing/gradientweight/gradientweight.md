## gradientweight
根据图像梯度计算图像像素的权重

## 语法
[`W = gradientweight(I)`](#function1)  
[`W = gradientweight(I, sigma)`](#function2)  
[`W = gradientweight(__,Name, Value)`](#function3)

## 说明
<a id="function1"></a>
[W](#Q1) = gradientweight([I](#Q2)) 基于该像素的梯度大小为图像 `I` 中的每个像素计算像素权重，并返回权重数组 `W`。像素的权重与像素位置处的梯度值成反比。梯度幅度较小的像素（平滑区域）的权重较大，而梯度幅度较大的像素（例如边缘）的权重较小。  
<a id="function2"></a>
[W](#Q1) = gradientweight([I](#Q2), [sigma](#Q3)) 将 `sigma` 作为高斯导数的标准差，该高斯导数用于计算图像梯度。  
<a id="function3"></a>
[W](#Q1) = gradientweight(__,[Name, Value](#Q4))  通过命名值参数控制权重计算的相关特性，返回权重数组 `W`。

## 参数说明
### 输入参数
**<a id="Q2"></a> I —— 灰度图像**  
数值矩阵

灰度图像，指定为数值矩阵。

**数据类型：** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

**<a id="Q3"></a> sigma —— 高斯**
高斯导数的标准差（默认值为1.5） | 正数

高斯导数的标准差，被认定为正数。

**数据类型：**`double`

**<a id="Q4"></a> Name, Value —— 命名值参数**
可选参数对需按 Name1, Value1,…, NameN, ValueN 的形式指定，其中 Name 为参数名称，Value 为对应的参数值。名称 - 值对参数必须出现在其他参数之后，但参数对的排列顺序不影响执行结果。
例如：W = gradientweight(I,1.5,'RolloffFactor',3,'WeightCutoff',0.25);

**RolloffFactor —— 输出权重衰减因子**
默认值为3 | 正标量

输出权重衰减因子，指定为由'RolloffFactor' 和 double 类型正标量组成的逗号分隔对参数。该参数控制权重值随梯度幅值变化的衰减速率。将梯度幅值与权重值的关系绘制成二维曲线时，区域边缘处的像素强度值可能会平缓变化，形成平缓的斜率；而在分割后的图像中，你可能希望边缘的界定更清晰。通过设置该衰减因子，可控制 “像素强度值开始变化位置处” 的权重值曲线斜率：若指定较高的衰减因子值，平滑区域边缘附近的输出权重值会急剧下降；若指定较低的值，平滑区域边缘附近的输出权重值衰减会更平缓。该参数的建议取值范围为 [0.5  4]。

**数据类型：**`double`

**WeightCutoff —— 权重阈值**
默认值为0.5 | 正数范围为[1e-3 1]

权重值阈值,指定为由 'WeightCutoff' 和取值范围为 [1e-3 1] 的正数组成的逗号分隔对参数。若通过该参数为权重值设置阈值，函数会抑制所有小于该阈值的权重值—— 将这些像素的权重值统一设为一个较小的常量值（1e-3）。

**数据类型：**`double`

### 输出参数
**<a id="Q1"></a> W — 权重数组**  
数值数组

权重数组，以与输入图像 `I` 相同大小的数值数组形式返回。除非 `I` 是 single，这种情况下权重数组是 single，否则权重数组为 double。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../graydiffweight/graydiffweight.html">graydiffweight</a> 
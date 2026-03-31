## localcontrast
边缘感知局部对比度处理

## 简介
[ `B = localcontrast(A)`](#function1)  
[ `B = localcontrast(A, edgeThreshold, amount)`](#function2)

## 用法
<a id="function1"></a>
[B](#Q4) = localcontrast([A](#Q1)) 对灰度图像或 RGB 图像 `A`进行边缘感知局部对比度增强。  
<a id="function2"></a>
[B](#Q4) = localcontrast([A](#Q1),  [edgeThreshold](#Q2), [amount](#Q#3)) 可增强或弱化图像的局部对比度 —— 具体操作为增强细节或平滑细节，同时保持强边缘不变。参数 `edgeThreshold` 定义了需要保留的强边缘的最小亮度幅值，参数 `amount` 用于设置所需的增强或平滑程度。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 待处理的灰度或 RGB 图像**  
实型非稀疏矩阵，尺寸为 m×n 或 m×n×3

待处理的输入图像，需指定为实型、非稀疏的二维矩阵（灰度图）或三维矩阵（RGB 图）

**数据类型**：`single` | `int8` | `int16` | `uint8` | `uint16` 

**<a id="Q2"></a> edgeThreshold — 需保留的强边缘幅值**  
0.3（默认值） | 取值范围在 [0,1] 内的数值标量

用于定义需要完整保留的强边缘的最小亮度幅值，参数值需在 [0,1] 区间内。

**数据类型**：`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q3"></a> amount — 对比度增强或平滑的程度**  
0.25（默认值） | 取值范围在 [-1,1] 内的数值标量

用于设置所需的局部对比度增强或平滑程度，参数值需在 [-1,1] 区间内。负值表示执行边缘感知型平滑，正值表示执行边缘感知型增强。

|**参数值**|**功能描述**|  
|:-|:-|
|0|保持输入图像不变|  
|1|大幅度增强输入图像的局部对比度|  
|-1|大幅平滑输入图像的细节|


**数据类型**：`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`


### 输出参数
**<a id="Q4"></a> B — 边缘感知局部对比度处理后的图像**    
数值数组

边缘感知局部对比度处理后输出的图像，返回的数值数组与输入图像 A 尺寸相同、数据类型相同。

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../imadjust/imadjust.html">imadjust</a> |
<a href="../imcontrast/imcontrast.html">imcontrast</a> | <a href="../imsharpen/imsharpen.html">imsharpen</a> | <a href="../locallapfilt/locallapfilt.html">locallapfilt</a>
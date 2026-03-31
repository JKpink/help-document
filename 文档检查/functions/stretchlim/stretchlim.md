## stretchlim 
查找图像对比度拉伸的限值


## 简介
[`lowhigh = stretchlim(I)`](#function1)  
[ `lowhigh = stretchlim(I, Tol)`](#function2)

## 用法
<a id="function1"></a>
[lowhigh](#Q3) = stretchlim([I](#Q1)) 计算对灰度图像或 RGB 图像 `I` 应用对比度拉伸时的可用下限和上限。限值在 `lowhigh` 中返回。默认情况下，限值指定为所有像素值中最低的 1% 和最高的 1%。  
<a id="function2"></a>
[lowhigh](#Q3) = stretchlim([I](#Q1), [Tol](#Q2)) 指定图像在低像素值端和高像素值端进行饱和处理的比例 Tol。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 要进行对比度拉伸的图像**  
二维灰度图像 | 二维 RGB 图像  

要进行对比度拉伸的图像，指定为二维灰度图像或二维 RGB 图像。

**数据类型:** `single` | `double` | `int16` | `uint8` | `uint16` | `logical` 

**<a id="Q2"></a>Tol — 要进行饱和处理的图像的比例**  
[0.01 0.99] (默认) | 数值标量 | 二元素数值向量  

要进行饱和处理的图像的比例，指定为数值标量或范围 [0, 1] 内的二元素向量 [Low_Fract High_Fract]。

| **值** | **描述**  |
| :----------- | :----------- |
| "标量" | 如果 Tol 是标量，则 Low_Fract = Tol， High_Fract = 1 - Low_Fract，以相同比例对低像素值端和高像素值端进行饱和处理。。 |
| "0"  | 如果 Tol = 0，则 lowhigh = [min(I(:)); max(I(:))]。|
| "默认值" | 如果省略 Tol 参量，则 [Low_Fract High_Fract] 默认为 [0.01 0.99]，对总像素值的 2% 进行饱和处理。|
| "太大" | 如果 Tol 太大，以至于在对低像素值和高像素值进行饱和处理后不会留下任何像素，则 stretchlim 返回 [0 1]。|


**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出参数
**<a id="Q3"></a> lowhigh — 对比度拉伸的下限和上限**  
二元素数值向量 | 2×3 数值矩阵  

对比度拉伸的下限和上限，返回为以下值之一。  
当 `I` 是灰度图像时，返回一个二元素数值向量。
当 `I` 是 RGB 图像时，返回一个 2×3 数值矩阵。这些列表示三个颜色通道中每一个的下限和上限。

**数据类型:** `double`

## 提示
使用 imadjust 函数并通过限值 [lowhigh](#Q3) 来调整图像 [I](#Q1) 的对比度。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../brighten/brighten.html">brighten</a> | <a
href="../decorrstretch/decorrstretch.html">decorrstretch</a> | <a 
href="../histeq/histeq.html">histeq</a> | <a 
href="../imadjust/imadjust.html">imadjust</a> 
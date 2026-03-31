## imoverlay
基于二值掩模使用纯色填充二维图像

## 简介
[`B = imoverlay(A, BW)`](#function1)  
[`B = imoverlay(A, BW,color)`](#function2)

## 用法
<a id="function1"></a>
[B](#Q1) = imoverlay([A](#Q2), [BW](#Q3)) 基于二值掩膜输入 `BW` 中的 true 值对灰度或 RGB 图像 `A` 中的对应元素填充纯色。  
<a id="function2"></a>
[B](#Q1) = imoverlay([A](#Q2), [BW](#Q3),[color](#Q4)) 指定`imoverlay`填充图像所用的颜色

## 参数说明
### 输入参数
**<a id="Q2"></a> A — 输入图像**  
二维灰度图像 | 二维彩色图像

输入图像，指定为二维灰度图像或二维彩色图像。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16` | `logical`

**<a id="Q3"></a> BW — 掩膜图像**  
二维二值矩阵 | 二维数值矩阵

掩膜图像，指定的二维二值矩阵或二维数值矩阵，其大小与图像 `A` 的前两个维度相同。对于数值输入，任何非零像素都被视为 1(true)。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`

**<a id="Q4"></a> color —— 叠加所用颜色**
"yellow(默认)" | RGB三元组 | 颜色名称 | 短颜色名称

叠加所用颜色，指定为 RGB 三元组、颜色名称或短颜色名称。

可以使用 RGB 三元组指定任何颜色。RGB 三元组是一个包含 3 个元素的行向量，其元素分别指定颜色中红、绿、蓝分量的强度。强度必须在 [0, 1] 范围内。

可以按名称将一些常见颜色指定为字符串标量或字符向量。下表列出了命名颜色选项和等效的 RGB 三元组。
| 颜色名称 | 短名称| RGB三元组|
|-------|-------|-------|
|"red"|	"r"|	[1 0 0]	|
|"green"|	"g"|	[0 1 0]	|
|"blue"	|"b"	|[0 0 1]	|
|"yellow"	|"y"	|[1 1 0]	|
|"black"	|"k"	|[0 0 0]	|
|"white"|	"w"	|[1 1 1]	|

### 输出图像
**<a id="Q1"></a> B — 输出图像**  
二维 RGB 图像

输出图像，以二维 RGB 图像形式返回。

**数据类型：** `uint8`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../imblend/imblend.html">imblend</a> | <a 
href="../superpixels/superpixels.html">superpixels</a> | <a 
href="../boundarymask/boundarymask.html">boundarymask</a> | <a 
href="../labeloverlay/labeloverlay.html">labeloverlay</a> 
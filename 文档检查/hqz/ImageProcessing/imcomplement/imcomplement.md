## imcomplement
计算图像的补集

## 简介
[`J = imcomplement(I)`](#function1)

## 用法
<a id="function1"></a>
[J](#Q2) = imcomplement([I](#Q1))  计算图像 `I` 的补集，并将结果返回至 `J` 中。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
RGB 图像 | 灰度图像 | 二值图像

输入图像：指定为 RGB 图像、灰度图像或二值图像。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `logical`  

### 输出参数
**<a id="Q2"></a> J — 图像反色**  
RGB 图像 | 灰度图像 | 二值图像

图像补集：返回为 RGB 图像、灰度图像或二值图像。`J` 与输入图像 `I` 尺寸和数据类型完全相同。

## 详细信息
**图像反色**  

- 对于二值图像的补集：0 变为 1，1 变为 0，黑白像素完全反转。
- 对于灰度图像或彩色图像的补集：每个像素值减去该数据类型支持的最大像素值（若为双精度（`double`）图像则减去 1.0），差值作为输出图像的像素值。输出图像中暗区域变亮、亮区域变暗；彩色图像中，红色变为青色、绿色变为品红色、蓝色变为黄色，反之亦然。

## 提示
- 若 `I` 为 `double` 类型的灰度图像或 RGB 图像，则可使用表达式 `1-I` 替代本函数。
- 若 `I` 为二值图像，则可使用表达式 `~I` 替代本函数。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
 <a href="../imabsdiff/imabsdiff.html">imabsdiff</a> | <a 
href="../imadd/imadd.html">imadd</a> | <a 
href="../imdivide/imdivide.html">imdivide</a> | <a 
href="../imlincomb/imlincomb.html">imlincomb</a> | <a 
href="../immultiply/immultiply.html">immultiply</a> | <a 
href="../imsubtract/imsubtract.html">imsubtract</a>

## imrotate
旋转图像

## 简介
[`J = imrotate(I, angle)`](#function1)  
[`J = imrotate(I, angle, method)`](#function2)  
[`J = imrotate(I, angle, method, bbox)`](#function3)

## 用法 
<a id="function1"></a> [J](#P1) = imrotate([I](#Q1), [angle](#Q2)) 将图像 `I` 围绕其中心点旋转 `angle` 度。逆时针旋转图像，应指定 `angle` 为正值；顺时针旋转图像，应指定 `angle` 为负值。默认情况下，`imrotate` 使用双线性插值。且默认输出图像 `J` 足够大，以包含整个旋转后的图像。对于数值和逻辑图像，`J` 中位于旋转后的图像外的像素的值将设置为0。  
<a id="function2"></a> [J](#P1) = imrotate([I](#Q1), [angle](#Q2), [method](#Q3)) 使用 `method` 指定的插值方法旋转图像 `I`。  
<a id="function3"></a> [J](#P1) = imrotate([I](#Q1), [angle](#Q2), [method](#Q3), [bbox](#Q4)) 使用 `bbox` 参量来定义输出图像的大小。可以将输出图像裁剪到与输入图像相同的大小，或返回整个旋转后的图像。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 要旋转的图像**  
数值数组 | 逻辑数组

要旋转的图像，指定为数值数组或逻辑数组。 

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q2"></a> angle — 旋转量**  
数值标量

旋转量，单位为度，指定为数值标量。

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q3"></a> method — 插值方法**  
`"bilinear"` (默认)  | `"nearest"` | `"bicubic"`

插值方法，指定为 `"bilinear"` (默认)、`"nearest"` 或 `"bicubic"`。

| **值** | **描述** |
| :----------- | :----------- |
| `"nearest"` | 最近邻点插值。赋给输出像素的值就是输入点所在像素的值。不考虑其他像素。|
| `"bilinear"` | 双线性插值。输出像素值是最近的 2 × 2 邻域中像素的加权平均值。 |
| `"bicubic"` | 双三次插值。输出像素值是最近的 4 × 4 邻域中像素的加权平均值。（注意：双三次插值可能生成在原始范围之外的像素值。） |

**数据类型：**`char` | `string`

**<a id="Q4"></a> bbox — 定义输出图像大小的边界框**   
`"loose"` (默认) | `"crop"`

定义输出图像大小的边界框，指定为 `"loose"`(默认) 或 `"crop"`。

| **值** | **描述** |
| :----------- | :----------- |
| `"crop"` | 使输出图像 `J` 与输入图像 `I` 大小相同，裁剪旋转后的图像以适应边界框。 |
| `"loose"` | 使输出图像 `J` 足够大，以包含整个旋转后的图像。`J` 大于 `I`。 |

**数据类型：**`char` | `string`

### 输出参数

**<a id="P1"></a> J — 旋转后的图像**  
数值数组 | 逻辑数组

旋转后的图像，指定为与输入图像 [I](#Q1) 具有相同数据类型的数值或逻辑数组。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imcrop/imcrop.html">imcrop</a> | <a 
href="../imrotate3/imrotate3.html">imrotate3</a> | <a 
href="../imresize/imresize.html">imresize</a> | <a 
href="../imtransform/imtransform.html">imtransform</a> | <a 
href="../tformarray/tformarray.html">tformarray</a>  

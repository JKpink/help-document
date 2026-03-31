## imwarp
对图像应用几何变换

## 简介
[`B = imwarp(A, tform)`](#function1)  
[`[B,RB] = imwarp(A, RA, tform)`](#function2)  
[`[___] = imwarp(___, interp)`](#function3)  
[`[___] = imwarp(___, Name, Value)`](#function4)

## 用法 
<a id="function1"></a> [B](#P1) = imwarp([A](#Q1), [tform](#Q2)) 根据几何变换 `tform` 来变换数值或逻辑图像 `A`。该函数在 `B` 中返回变换后的图像。  
<a id="function2"></a> [[B](#P1), [RB](#P2)] = imwarp([A](#Q1), [RA](#Q3), [tform](#Q2)) 变换由图像数据 `A` 指定的空间参照图像及其关联的空间参照对象 `RA` 进行变换。输出由图像数据 `B` 指定的空间参照图像及其关联的空间参照对象 `RB` 。  
<a id="function3"></a> [\_\_\_] = imwarp(\_\_\_, [interp](#Q4)) 指定使用的插值方法。  
<a id="function4"></a> [\_\_\_] = imwarp(\_\_\_, [Name, Value](#Q5)) 指定名称-值参量来控制几何变换的各个方面。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 要变换的图像**  
数值数组 | 逻辑数组   

要变换的图像，指定为任意维度的数值或逻辑数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q2"></a> tform — 几何变换**  
几何变换对象  

几何变换，指定为表中列出的几何变换对象：

|几何变换对象|描述|
|---|---|
|二维线性几何变换|
|<a href="../transltform2d/transltform2d.html">transltform2d</a>  </a>|平移变换|
|<a href="../rigidtform2d/rigidtform2d.html">rigidtform2d</a>  </a>|刚性变换：平移和旋转|
|<a href="../simtform2d/simtform2d.html">simtform2d</a>  </a>|相似变换：平移、旋转和各向同性缩放|
|<a href="../affinetform2d/affinetform2d.html">affinetform2d</a>  </a>|仿射变换：平移、旋转、各向异性缩放、反射和剪切|
|<a href="../projtform2d/projtform2d.html">projtform2d</a>  </a>|投影变换|
|三维线性几何变换|
|<a href="../transltform3d/transltform3d.html">transltform3d</a>  </a>|平移变换|
|<a href="../rigidtform3d/rigidtform3d.html">rigidtform3d</a>  </a>|刚性变换：平移和旋转|
|<a href="../simtform3d/simtform3d.html">simtform3d</a>  </a>|相似变换：平移、旋转和各向同性缩放|
|<a href="../affinetform3d/affinetform2、3d.html">affinetform3d</a>  </a>|仿射变换：平移、旋转、各向异性缩放、反射和剪切|
|非线性几何变换|
|<a href="../PiecewiseLinearTransformation2D/PiecewiseLinearTransformation2D.html">PiecewiseLinearTransformation2D</a>  </a>|分段线性变换|

- 如果 `tform` 为二维并且 [A](#Q1) 有两个以上的维度（例如对于RGB图像），则 `imwarp` 会将相同的二维变换应用于沿更高维度的所有二维平面。
- 如果 `tform` 为三维，则 `A` 必须为三维图像体。

**<a id="Q3"></a> RA — 要变换的图像的空间参照信息**  
`imref2d` 对象 | `imref3d` 对象  

要变换的图像的空间参照信息，对于二维变换指定为 <a href="../imref2d/imref2d.html">imref2d</a>  </a> 对象，对于三维变换指定为 <a href="../imref3d/imref3d.html">imref3d</a>  </a> 对象。

**<a id="Q4"></a> interp — 使用的插值的类型**  
"nearest" | "linear" | "cubic"  

使用的插值的类型，指定为下列值之一：  

| 插值方法 | 描述 |
|---|---|
| `"nearest"` |  最近邻点插值。赋给输出像素的值就是输入点所在像素的值，不考虑其他像素。|
| `"linear"`  |线性插值。线性插值是数值和逻辑图像的默认插值方法。| 
|`"cubic"` |三次插值。 |

**数据类型：** `char` | `string`
### <a id="Q5"></a> 名称-值参数  
将可选的参量对组指定为 Name1, Value1, ..., NameN, ValueN，其中 `Name` 是参量名称，`Value`是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。

**OutputView — 输出图像的大小和位置**  
`imref2d` 对象 | `imref3d` 对象  

输出图像在世界坐标系中的大小和位置，指定为 <a href="../imref2d/imref2d.html">imref2d</a>  </a> 或 <a href="../imref3d/imref3d.html">imref3d</a>  </a> 空间参照对象。对象具有定义输出图像大小和输出图像在世界坐标系中位置的属性。
可以使用 <a href="../affineOutputView/affineOutputView.html">affineOutputView</a>  </a> 函数创建输出视图。

**FillValues — 填充值**  
数值标量 | 数值数组 | 字符串标量 | 字符向量   

当输出图像落在输入图像之外时的填充值，指定为表中的值之一。如果输出像素对应的位置经逆变换后完全处于输入图像边界之外，`imwarp` 将对该输出像素使用填充值。  
数值和逻辑图像的默认填充值为 0。  

| 图像类型 | 变换维度 | 填充值的格式 |
|---|---|---|
| 二维灰度或逻辑图像 | 二维 | 数值标量 |
 | 二维彩色图像或二维多光谱图像 |二维|数值标量，包含 c 个元素的数值向量，为 c 个通道中的每个通道指定一个填充值。对于彩色图像，通道数 c 为 3。|
|包含p个二维图像的序列 |二维|   数值标量，c × p 数值矩阵。对于灰度图像，通道数 c 为 1，对于彩色图像为 3。|
| N维图像 | 二维 |数值标量，数值数组，其大小与输入图像 A 的维度 3 至 N 相匹配。例如，如果 A 是 200 × 200 × 10 × 3，则 `FillValues` 可以是 10 × 3 数组。|
| 三维灰度或逻辑图像 | 二维 | 数值标量 |

**示例:** 255 表示用白色像素填充 `uint8` 图像  
**示例:** 1 表示用白色像素填充 `double` 图像  
**示例:** [0 1 0] 表示用绿色像素填充 `double` 彩色图像  
**示例:** 对于一个包含两个 `double` 彩色图像的序列，[0 1 0; 0 1 1] 表示用绿色像素填充第一个图像，用青色像素填充第二个图像。
### 输出参数
**<a id="P1"></a> B — 变换后的图像**   
数值数组 | 逻辑数组  

变换后的图像，指定为与输入图像 [A](#Q1) 具有相同数据类型的数值或逻辑数组。

**<a id="P2"></a> RB — 变换后图像的空间参照信息**  
`imref2d` 对象 | `imref3d` 对象  

变换后图像的空间参照信息，指定为 <a href="../imref2d/imref2d.html">imref2d</a>  </a> 或 <a href="../imref3d/imref3d.html">imref3d</a>  </a> 空间参照对象。
## 提示
- 如果您要对一批大小相同的图像应用相同的几何变换，请考虑使用 <a href="../warper/warper.html">warper</a>  </a> 对象和 <a href="../warp/warp.html">warp</a>  </a> 函数。与 `imwarp` 相比，`Warper` 对象能够显著加快中小型图像批量的变换速度，但对于较大图像的加速效果会递减。


## 版本历史
在北太天元数字图像处理工具箱 V1.0 推出

## 相关主题
<a href="../Warper/Warper.html">Warper</a> | <a
href="../affineOutputView/affineOutputView.html"> affineOutputView</a> | <a 
href="../imregister/imregister.html">imregister</a> | <a 
href="../imregtform/imregtform.html">imregtform</a> | <a 
href="../imregdemons/imregdemons.html">imregdemons</a> | <a 
href="../imtranslate/imtranslate.html">imtranslate</a> | <a
href="../randomWindow2d/randomWindow2d.html">randomWindow2d</a> | <a 
href="../centerCropWindow2d/centerCropWindow2d.html">centerCropWindow2d </a>
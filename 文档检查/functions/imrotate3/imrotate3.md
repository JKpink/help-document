## imrotate3
旋转三维图像

## 简介
[`B = imrotate3(V, angle, W)`](#function1)  
[`B = imrotate3(V, angle, W, method)`](#function2)  
[`B = imrotate3(V, angle, W, method, bbox)`](#function3)  
[`B = imrotate3(___, "FillValues", fillValues)`](#function4)

## 用法 
<a id="function1"></a> [B](#P1) = imrotate3([V](#Q1), [angle](#Q2), [W](#Q3)) 将三维图像 `V` 绕通过原点的轴旋转 `angle` 度。逆时针旋转图像，应指定 `angle` 为正值；顺时针旋转图像，应指定 `angle` 为负值。`W` 是一个 1 × 3 向量，用于指定旋转轴在三维空间中的方向。默认情况下，`imrotate3` 会将旋转后图像边界之外的像素值设置为 0。  
<a id="function2"></a> [B](#P1) = imrotate3([V](#Q1), [angle](#Q2), [W](#Q3),[method](#Q4)) 额外指定插值方法 `method`。  
<a id="function3"></a> [B](#P1) = imrotate3([V](#Q1), [angle](#Q2), [W](#Q3), [method](#Q4), [bbox](#Q5)) 额外指定输出体数据的大小 `bbox`。若指定 `"crop"`，则 `imrotate3` 会将输出体数据的大小设置为与输入体数据大小相同。若指定 `"loose"`，则 `imrotate3` 会将输出体数据的大小扩展至足够大，以完全容纳旋转后的体数据。  
<a id="function4"></a> [B](#P1) = imrotate3(\_\_\_, "FillValues", [fillValues](#Q6)) 为输出中无对应输入像素的位置设置填充值。

## 参数说明
### 输入参数
**<a id="Q1"></a> V — 需要旋转的体数据**  
三维数值数组 | 三维逻辑数组

需要旋转的体数据，指定为三维数值数组或三维逻辑数组。

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q2"></a> angle — 旋转角度**  
数值标量

旋转角度，单位为度，指定为数值标量。若要顺时针旋转图像，应为 `angle` 指定负值。`imrotate3` 会自动调整数据使输出体积 [B](#P1) 足够大以包含整个旋转后的三维图像。

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` 

**<a id="Q3"></a> W — 旋转轴的方向**  
1 × 3 数值向量

旋转轴的方向，指定为 1×3 数值向量，表示笛卡尔坐标系中三维空间中的旋转轴方向。  
若需要以球坐标指定旋转轴方向，可先使用 <a href="../sph2cart/sph2cart.html">sph2cart</a>  </a> 将坐标值转换为笛卡尔坐标，再传入 `imrotate3`。

示例：[0 0 1] 表示绕 Z 轴旋转图像。

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q4"></a> method — 插值方法**  
`"bilinear"`(默认)  | `"nearest"` | `"bicubic"`

插值方法，指定为`"bilinear"`(默认)、`"nearest"` 或 `"bicubic"`。

| **值** | **描述** |
| :----------- | :----------- |
| `"nearest"` | 最近邻点插值。赋给输出像素的值就是输入点所在像素的值。不考虑其他像素。|
| `"bilinear"` | 双线性插值。输出像素值是最近的 2 × 2 × 2 邻域中像素的加权平均值。 |
| `"bicubic"` | 双三次插值。输出像素值是最近的 4 × 4 × 4 邻域中像素的加权平均值。（注意：双三次插值可能生成在原始范围之外的像素值。） |

**数据类型：**`char` | `string`

**<a id="Q5"></a> bbox — 输出体数据大小**  
`"loose"`(默认) | `"crop"`

输出体数据大小，指定为以下任意值：

| **值** | **描述** |
| :----------- | :----------- |
| `"crop"` | 通过对旋转后的体数据进行裁剪以匹配原来的大小，使输出体数据与输入体数据大小相同 |
| `"loose"` | 使输出体数据足够大，以完整容纳旋转后的体数据。通常，输出体数据大小会大于输入体数据。 |

**数据类型：**`char` | `string`

**<a id="Q6"></a> fillValues — 填充值**  
数值标量

用于填充输出图像中超出原图像范围的像素值，指定为以下形式。当输出像素经逆变换后，对应位置完全超出原图像边界时，`imrotate3` 会使用该值填充对应输出像素。

| **图像类型** | **填充值格式** |
| :----------- | :----------- |
| 数值图像或逻辑图像 | 数值标量、数值图像和逻辑图像的默认填充值为 0。 |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数
**<a id="P1"></a> B — 旋转后的体数据**  
数值数组 | 逻辑数组

旋转后的体数据，指定为与输入体数据 [V](#Q1) 相同数据类型的数值数组或逻辑数组。 

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../imrotate/imrotate.html">imrotate</a> | <a 
href="../imresize3/imresize3.html">imresize3</a> | <a 
href="../imtranslate/imtranslate.html">imtranslate</a> | <a 
href="../imwarp/imwarp.html">imwarp</a>
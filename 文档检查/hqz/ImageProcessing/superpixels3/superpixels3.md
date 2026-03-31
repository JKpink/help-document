## superpixels3  
三维图像的三维超像素过分割

## 简介  
[`[L, NumLabels] = superpixels3(A, N)`](#function1)  
[`[L, NumLabels] = superpixels3(A, N, Name, Value)`](#function2)

## 用法  
<a id="function1"></a>
[`L,NumLabels`](#output) = superpixels3([A](#inputA), [N](#inputN)) 计算三维图像 `A` 的三维超像素。`N` 指定要创建的超像素数量。函数返回三维标签矩阵 `L` 和实际返回的超像素数量 `NumLabels`。

<a id="function2"></a>
[`L,NumLabels`](#output) = superpixels3([A](#inputA), [N](#inputN), Name,Value) 使用名称-值参数控制分割的各个方面来计算图像 `A` 的超像素。

## 参数说明  
### 输入参数  
**<a id="inputA"></a> A — 待分割的体积**  
三维数值数组

待分割的体积，指定为三维数值数组。

**数据类型**：`single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

**<a id="inputN"></a> N — 期望的超像素数量**  
正整数

期望的超像素数量，指定为正整数。

**数据类型**：`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出参数  
**<a id="output"></a> L — 标签矩阵**  
正整数三维数组

标签矩阵，返回为正整数三维数组。值 1 表示第一个区域，2 表示第二个区域，依此类推，对应图像中的每个超像素区域。

**数据类型**：`double`

**NumLabels — 计算出的超像素数量**  
正数

计算出的超像素数量，返回为正数。

**数据类型**：`double`

## 算法  
`superpixels3` 使用的算法是 `superpixels` 中使用的简单线性迭代聚类（SLIC）算法的改进版本。高层次上，它创建聚类中心，然后交替进行将像素分配到最近的聚类中心和更新聚类中心位置的过程。`superpixels3` 使用距离度量来确定每个像素最近的聚类中心。该距离度量结合了强度距离和空间距离。

函数的 `Compactness` 参数源自距离度量的数学形式。算法的紧凑度参数是一个标量值，用于控制超像素的形状。两个像素 i 和 j 之间的距离（其中 m 为紧凑度值）为：

$$
d_{\text{intensity}} = \sqrt{(l_i - l_j)^2}
$$

$$
d_{\text{spatial}} = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2 + (z_i - z_j)^2}
$$

$$
D = \sqrt{\left(\frac{d_{\text{intensity}}}{m}\right)^2 + \left(\frac{d_{\text{spatial}}}{S}\right)^2}
$$



紧凑度的含义与二维 `superpixels` 函数中相同：它决定了强度距离和空间距离在总体距离度量中的相对重要性。较低的值使超像素更贴合边界，形状更不规则；较高的值使超像素形状更规则。算法内部会将输入图像的动态范围归一化到 [0,1]，从而使得紧凑度值在不同图像间具有一致的含义。

## 版本历史  
在北太天元图像处理工具箱 V3.0 推出

## 相关主题  
[superpixels](../superpixels/superpixels.html) | [boundarymask](../boundarymask/boundarymask.html) | [imoverlay](../imoverlay/imoverlay.html) | [label2idx](../label2idx/label2idx.html) | [label2rgb](../label2rgb/label2rgb.html) | [hyperslic](../hyperslic/hyperslic.html)

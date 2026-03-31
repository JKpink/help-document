## edge3
在 3-D 灰度体数据中查找边缘

## 简介
[`BW = edge3(V, "Sobel", thresh)`](#function3)  
[`BW = edge3(V, "Sobel", thresh, "nothinning")`](#function4)

## 用法
<a id="function3"></a>
[BW](#P1) = edge3([V](#Q1), "Sobel", [thresh](#Q2)) 接受强度体数据或二值体数据 `V`，返回二值体数据 `BW`，其中边缘点位置的值为 1，其余位置的值为 0。Sobel 方法使用 Sobel 近似求导来检测边缘，它返回梯度达到最大值处的边缘点。所有强度不高于阈值 `thresh` 的边缘将被忽略。

<a id="function4"></a>
[BW](#P1) = edge3([V](#Q1), "Sobel", [thresh](#Q2) , "nothinning")通过跳过边缘细化步骤来加速算法。默认情况下（或指定 `"thinning"` 时）会进行边缘细化。

## 参数说明
### 输入参数

**<a id="Q1"></a> V — 输入体数据**  
3-D 数值数组

输入体数据，指定为 3-D 数值数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q2"></a> thresh — 灵敏度阈值**  
数值标量 | 2 元素数值行向量

灵敏度阈值，根据所选方法指定为以下形式之一。

| 方法  | 阈值取值 |
| ----- | -------- |
| Sobel | 数值标量 |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q3"></a> sigma — 高斯滤波器的标准差**  
`sqrt(2)` （默认） | 数值标量 | 1×3 数值向量

高斯平滑滤波器的标准差。对于各向同性体数据，指定为数值标量；对于各方向尺度不同的各向异性体数据，指定为 `[SigmaX SigmaY SigmaZ]` 形式的 1×3 数值向量。滤波器的大小根据 `sigma` 自动确定。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数

**<a id="P1"></a> BW — 检测到的边缘**  
3-D 数值数组

检测到的边缘，以与 `V` 相同大小的 3-D 数值数组形式返回。像素值为 1 表示边缘，像素值为 0 表示平坦区域。

## 提示
- 对于 Sobel 方法，默认进行边缘细化以得到更精确的单像素宽边缘；若需加快处理速度，可以使用 `"nothinning"` 选项跳过细化步骤。

## 算法
- **Sobel 方法**：使用 Sobel 算子近似计算梯度，然后通过寻找梯度局部最大值确定边缘位置。

## 版本历史
在北太天元图像处理工具箱 V3.0 推出  

## 相关主题
<a href="../edge/edge.html">edge</a> | <a href="../imgradient3/imgradient3.html">imgradient3</a> 

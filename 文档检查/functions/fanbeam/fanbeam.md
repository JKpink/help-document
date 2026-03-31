## fanbeam
扇形束变换

## 简介
[`F = fanbeam(I, D)`](#function1)  
[`F = fanbeam(I, D, Name, Value)`](#function2)  

## 用法
<a id="function1"></a>
[F](#P1) = fanbeam([I](#Q1), [D](#Q2)) 计算图像 `I` 的扇形束投影数据（正弦图）`F`。`F` 的每一列包含一个旋转角度下的扇形束投影数据。`D` 为从扇形束顶点到旋转中心的距离（像素单位）。

<a id="function2"></a>
[F](#P1) = fanbeam([I](#Q1), [D](#Q2), Name Value) 通过名称-值参数指定旋转角度增量和传感器间距。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
2-D 数值矩阵 | 2-D 逻辑矩阵

输入图像，指定为二维数值矩阵或二维逻辑矩阵。

**<a id="Q2"></a> D — 扇形束顶点到旋转中心的距离**  
正数

扇形束顶点到旋转中心的距离，以像素为单位，指定为正数。旋转中心为图像的中心像素，定义为 `floor((size(I)+1)/2)`。`D` 必须足够大，以确保扇形束顶点在所有旋转角度下都位于图像外部。有关选择 `D` 的指导原则，请参阅提示部分。

**数据类型：** `double` | `single`

### 名称-值参数
使用名称-值参数指定可选的参数对。参数名必须为字符向量，参数值为对应值。名称-值参数必须出现在其他参数之后，但各对的顺序不限。

**<a id="Q3"></a> FanRotationIncrement — 扇形束旋转角度增量**  
`1` （默认） | 正标量

扇形束旋转角度增量，以度为单位，指定为正标量。

**数据类型：** `double`

**<a id="Q4"></a> FanSensorGeometry — 扇形束传感器排列方式**  
`"arc"` （默认） | `"line"`

扇形束传感器的排列方式，指定为 `"arc"` 或 `"line"`。
- `"arc"` — 传感器沿圆弧等角度间隔排列，圆弧中心为扇形束顶点。此时 `FanSensorSpacing` 定义角度间隔（度）。
- `"line"` — 传感器沿平行于 x' 轴的直线等距排列，离旋转中心最近的传感器距离为 `D`。此时 `FanSensorSpacing` 定义 x' 轴上扇形束之间的线性距离（像素）。

**<a id="Q5"></a> FanSensorSpacing — 扇形束传感器间距**  
`1` （默认） | 正标量

扇形束传感器的间距，指定为正标量。
- 若 `FanSensorGeometry` 为 `"arc"`，则间距单位为度。
- 若 `FanSensorGeometry` 为 `"line"`，则间距单位为像素（沿 x' 轴测量）。

**数据类型：** `double`

### 输出参数
**<a id="P1"></a> F — 扇形束投影数据**  
`numSensors` × `numAngles` 数值矩阵

扇形束投影数据，以 `numSensors` × `numAngles` 数值矩阵形式返回。`numSensors` 为扇形束传感器个数，`numAngles` 为扇形束旋转角度个数。`F` 的每一列包含一个旋转角度下的扇形束传感器采样值。

`fanbeam` 通过计算使用 `FanRotationIncrement` 角度间隔覆盖 360 度所需的旋转角度数来确定 `numAngles`。`fanbeam` 通过计算覆盖任意旋转角度下整个图像所需的射线数来确定 `numSensors`。当扇形束顶点到旋转中心的距离 `D` 较大时，覆盖图像所需的传感器数量较少。

**数据类型：** `double`

## 提示
- 选择 `D` 的指导原则：尝试使 `D` 比图像对角线长度的一半大几个像素。图像对角线长度可通过以下公式计算：
  $$
  sqrt(size(I,1)^2 + size(I,2)^2)
  $$

- `F` 中返回的数值是扇形束投影的数值近似值。该算法依赖于 Radon 变换，并插值到扇形束几何结构上。结果会根据所用参数的不同而变化。当图像较大、`D` 较大且计算点靠近图像中心（远离边缘）时，可获得更精确的结果。

## 算法

扇形束变换通过将 Radon 变换重采样到扇形束几何上来实现。算法首先计算图像的 Radon 变换，然后根据扇形束参数（顶点距离、传感器几何和间距）将平行束投影插值到对应的扇形束投影。

## 参考文献

Kak Avinash C, Malcolm Slaney. Principles of Computerized Tomographic Imaging. New York: IEEE Press, 1988. pp. 92–93.

## 版本历史

在北太天元图像处理工具箱 V3.0 推出

## 相关主题

<a href="../fan2para/fan2para.html">fan2para</a> | <a href="../ifanbeam/ifanbeam.html">ifanbeam</a> | <a href="../iradon/iradon.html">iradon</a> | <a href="../para2fan/para2fan.html">para2fan</a> | <a href="../phantom/phantom.html">phantom</a> | <a href="../radon/radon.html">radon</a>
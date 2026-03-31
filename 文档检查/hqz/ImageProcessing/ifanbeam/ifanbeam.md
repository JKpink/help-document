## ifanbeam
逆扇形束变换

## 简介
[`I = ifanbeam(F, D)`](#function1)  

## 用法
<a id="function1"></a>
[I](#P1) = ifanbeam([F](#Q1), [D](#Q2)) 从扇形束投影数据 `F` 重建图像 `I`。`F` 的每一列包含一个旋转角度下的扇形束投影数据。假定传感器之间的夹角均匀，且等于扇形束旋转角度增量。`D` 为从扇形束顶点到旋转中心的距离（像素单位）。

## 参数说明
### 输入参数
**<a id="Q1"></a> F — 扇形束投影数据**  
`numSensors` × `numAngles` 数值矩阵

扇形束投影数据，指定为 `numSensors` × `numAngles` 数值矩阵。`numSensors` 为扇形束传感器个数，`numAngles` 为扇形束旋转角度个数。`F` 的每一列包含一个旋转角度下的扇形束传感器采样值。

**数据类型：** `double` | `single`

**<a id="Q2"></a> D — 扇形束顶点到旋转中心的距离**  
正数

扇形束顶点到旋转中心的距离，以像素为单位，指定为正数。`ifanbeam` 假定旋转中心为投影的中心点，该点定义为 `ceil(size(F,1)/2)`。

**数据类型：** `double` | `single`

### 输出参数
**<a id="P1"></a> I — 重建图像**  
2-D 数值矩阵

重建图像，以二维数值矩阵形式返回。

## 提示
- 执行逆扇形束重建时，必须为 `ifanbeam` 提供与计算投影数据 `F` 时相同的参数。若使用 `fanbeam` 计算投影，则在调用 `ifanbeam` 时需确保参数一致。

## 参考文献
Kak Avinash C, Malcolm Slaney. Principles of Computerized Tomographic Imaging. New York: IEEE Press, 1988.

## 版本历史
在北太天元图像处理工具箱 V3.0 推出  

## 相关主题
<a href="../fan2para/fan2para.html">fan2para</a> | <a href="../fanbeam/fanbeam.html">fanbeam</a> | <a href="../iradon/iradon.html">iradon</a> | <a href="../para2fan/para2fan.html">para2fan</a> | <a href="../phantom/phantom.html">phantom</a> | <a href="../radon/radon.html">radon</a>
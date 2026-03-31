## para2fan
将平行束投影数据转换为扇形束投影数据

## 简介
[`F = para2fan(P, D)`](#function1)  

## 用法
<a id="function1"></a>
[`P`](#P1) = fan2para([F](#Q1), [D](#Q2)) 将平行束投影数据 `P` 转换为扇形束投影数据 `F`。`P` 的每一列包含一个旋转角度下的平行束传感器采样值。`D` 为从扇形束顶点到旋转中心的距离（像素单位）。

假定平行束传感器的间距为 1 像素，平行束旋转角度等间隔覆盖 [0, 180] 度。计算得到的扇形束旋转角度与平行束旋转角度具有相同的间隔，并覆盖 [0, 360) 度。计算得到的扇形束角度等间隔，间隔设为传感器间距所隐含的最小角度。

## 参数说明
### 输入参数

**<a id="Q1"></a> P — 平行束投影数据**  
数值矩阵

平行束投影数据，指定为数值矩阵。`P` 的每一列包含一个旋转角度下的平行束数据。列数表示平行束旋转角度的个数，行数表示平行束传感器的个数。

**数据类型：** `double` | `single`

**<a id="Q2"></a> D — 扇形束顶点到旋转中心的距离**  
正数

扇形束顶点到旋转中心的距离，以像素为单位，指定为正数。`para2fan` 假定旋转中心为投影的中心点，该点定义为 `ceil(size(F, 1)/2)`。`D` 必须大于或等于 `ParallelSensorSpacing * (size(P, 1)-1) / 2`。示意图中 `D` 表示扇形束顶点到旋转中心的距离。

**数据类型：** `double` | `single`

### 输出参数

**<a id="P1"></a> F — 扇形束投影数据**  
数值矩阵

扇形束投影数据，以数值矩阵形式返回。`F` 的每一列包含一个旋转角度下的扇形束传感器采样值。列数等于 `fanRotAngles` 的长度，行数等于 `fanSensorPos` 的长度。

**数据类型：** `double`

## 版本历史
在北太天元图像处理工具箱 V3.0 推出  

## 相关主题
<a href="../fan2para/fan2para.html">fan2para</a> | <a href="../fanbeam/fanbeam.html">fanbeam</a> | <a href="../ifanbeam/ifanbeam.html">ifanbeam</a> | <a href="../iradon/iradon.html">iradon</a> | <a href="../phantom/phantom.html">phantom</a> | <a href="../radon/radon.html">radon</a>
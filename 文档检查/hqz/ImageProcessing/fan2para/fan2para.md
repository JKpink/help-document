## fan2para
将扇形束投影数据转换为平行束投影数据

## 简介
[`P = fan2para(F, D)`](#function1)  

## 用法
<a id="function1"></a>
[P](#P1) = fan2para([F](#Q1), [D](#Q2)) 将扇形束投影数据 `F` 转换为平行束投影数据 `P`。`F` 的每一列包含一个旋转角度下的扇形束数据。`D` 为从扇形束顶点到旋转中心的距离（像素单位）。

## 参数说明
### 输入参数
**<a id="Q1"></a> F — 扇形束投影数据**  
数值矩阵

扇形束投影数据，指定为数值矩阵。`F` 的每一列包含一个旋转角度下的扇形束投影数据。列数表示扇形束旋转角度的个数，行数表示扇形束传感器的个数。

**数据类型：** `double` | `single`

**<a id="Q2"></a> D — 扇形束顶点到旋转中心的距离**  
正数

扇形束顶点到旋转中心的距离，以像素为单位，指定为正数。`fan2para` 假定旋转中心为投影的中心点，该点定义为 `ceil(size(F,1)/2)`。示意图中 `D` 表示扇形束顶点到旋转中心的距离。

**数据类型：** `double` | `single`

### 输出参数
**<a id="P1"></a> P — 平行束投影数据**  
数值矩阵

平行束投影数据，以数值矩阵形式返回。`P` 的每一列对应一个旋转角度下的平行束投影数据。列数等于 `paraRotAngles` 的长度，行数等于 `paraSensorPos` 的长度。

**数据类型：** `double`

## 版本历史
在北太天元图像处理工具箱 V3.0 推出  

## 相关主题
<a href="../fanbeam/fanbeam.html">fanbeam</a> | <a href="../ifanbeam/ifanbeam.html">ifanbeam</a> | <a href="../iradon/iradon.html">iradon</a> | <a href="../para2fan/para2fan.html">para2fan</a> | <a href="../phantom/phantom.html">phantom</a> | <a href="../radon/radon.html">radon</a>
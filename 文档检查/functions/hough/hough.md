## hough
Hough变换

## 简介
[`[H, theta, rho] = hough(BW)`](#function1)  
[`[H, theta, rho] = hough(BW, Name, Value)`](#function2)

## 用法
<a id="function1"></a>
[[H](#Q1), [theta](#Q2), [rho](#Q3)] = hough([BW](#Q4)) 计算二值图像 `BW` 的标准霍夫变换 (SHT)。`hough` 函数旨在检测线条。  
返回 `rho` (沿垂直于线条的向量从原点到线条的距离)和 `theta` (x轴与该向量之间的角度，以度为单位)，该函数还返回 `H` ，它是一个参数空间矩阵，其行和列分别对应于 `rho` 和 `theta` 值。  
<a id="function2"></a>
[[H](#Q1), [theta](#Q2), [rho](#Q3)] = hough([BW](#Q4), [Name, Value](#Q5)) 计算二值图像 `BW` 的标准霍夫变换 SHT，其中指定的参数影响计算。

## 参数说明
### 输入参数
**<a id="Q4"></a> BW — 二值图像**  
二维逻辑矩阵 | 二维数值矩阵

二值图像，指定为二维逻辑矩阵或二维数值矩阵。对于数值输入，任何非零像素都被视为 1 (true)。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `int8` | `int16` | `logical`

**<a id="Q5"></a> 名称-值参数**  

将可选的参量对组指定为 Name1, Value1,..., NameN, ValueN，其中 Name 是参量名称，Value 是对应的值。名称-值参量必须出现在其他参量后，但对各个参量对组的顺序没有要求。

**RhoResolution — 霍夫变换 bin 的间距**  
1 (默认) | 正数

霍夫变换 bin 沿 rho 轴的间距，指定为介于 0 和 norm (size(BW)) 之间（不包含两者）的正数。

**数据类型：** `double`

**Theta — SHT 的 Theta 值**  
-90:89 (默认) | 数值向量

SHT 的 Theta 值，指定为数值向量，其中包含在 [-90, 90) 范围内的元素。

**数据类型：** `double`

### 输出参量
**<a id="Q1"></a> H — 霍夫变换矩阵**  
数值矩阵

霍夫变换矩阵，以大小为 nrho×ntheta 的数值矩阵形式返回。行和列对应于 rho 和 theta 值。

**<a id="Q2"></a> theta — x 轴和 rho 向量之间的角度**  
数值矩阵

x 轴和 rho 向量之间的角度，以度为单位，以数值矩阵形式返回。

**数据类型：** `double`

**<a id="Q3"></a> rho — 从原点到线条的距离**  
数值数组

沿垂直于线条的向量从原点到线条的距离，以数值数组形式返回。

**数据类型：** `double`

## 版本历史
在北太天元图像处理工具箱 V1.1 推出

## 相关主题
<a href="../houghlines/houghlines.html">houghlines</a> | <a 
href="../houghpeaks/houghpeaks.html">houghpeaks</a> 

## 主题
<a href="../使用霍夫变换检测图像中的线条/使用霍夫变换检测图像中的线条.html">使用霍夫变换检测图像中的线条</a> 

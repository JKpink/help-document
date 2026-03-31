## transltform3d
三维平移几何变换  

## 简介
[`tform = transltform3d`](#function1)  
[`tform = transltform3d(t)`](#function2)  
[`tform = transltform3d(tx, ty, tz)`](#function3)    
[`tform = transltform3d(translMat)`](#function4)  
[`tform = transltform3d(tformIn)`](#function5) 

## 用法 
<a id="function1"></a> [tform](#P1) = transltform3d 创建一个执行恒等变换的 `transltform3d` 对象。  
<a id="function2"></a> [tform](#P1) = transltform3d([t](#Q1)) 从指定的平移向量 `t` 创建一个进行平移变换的 `transltform3d` 对象。  
<a id="function3"></a> [tform](#P1) = transltform3d([tx](#Q2), [ty](#Q3), [tz](#Q4)) 从指定 `x` 方向平移量 `tx`、`y` 方向平移量 `ty` 和 `z` 方向平移量 `tz` 创建一个进行平移变换的 `transltform3d` 对象。  
<a id="function4"></a> [tform](#P1) = transltform3d([translMat](#Q5)) 从指定的三维平移变换矩阵 `translMat` 创建一个 `transltform3d` 对象。    
<a id="function5"></a> [tform](#P1) = transltform3d([tformIn](#Q6)) 从另一个表示有效二维平移变换的几何变换对象 `tformIn` 创建一个 `transltform3d` 对象。     

## 参数  
### 输入参数  
**<a id="Q1"></a> t — 平移量**  
[0 0 0]（默认）| 3 元素数值向量  

平移量指定为 $[t_x\ t_y\ t_z]$ 格式的 3 元素数值向量，这些平移量用于设置 [A](#Q7) 属性定义的平移变换矩阵中的 $t_x$ 、 $t_y$ 和 $t_z$ 值。  
该参数用于设置 [Translation](#Q8) 属性。 

**数据类型：** `double` | `single`  
  
**<a id="Q2"></a> tx — x 方向平移量**  
0 (默认) | 数值标量  
  
`x` 方向的平移量，指定为数值标量。此参数用于设置 [Translation](#Q8) 属性的第一个元素。  
  
**<a id="Q3"></a> ty — y 方向平移量**  
0 (默认) | 数值标量  
  
`y` 方向的平移量，指定为数值标量。此参数用于设置 [Translation](#Q8) 属性的第二个元素。  
  
**<a id="Q4"></a> tz — z 方向平移量**  
0 (默认) | 数值标量  
  
`z` 方向的平移量，指定为数值标量。此参数用于设置 [Translation](#Q8) 属性的第三个个元素。  
  
**<a id="Q5"></a> translMat — 三维正向平移变换矩阵**  
4 × 4 单位矩阵 (默认) | 4 × 4 数值矩阵   
  
三维正向平移变换，指定为 4 × 4 数值矩阵。创建对象时，也可以将 `translMat` 指定为 3 × 4 数值矩阵，此时对象会自动在矩阵末尾拼接行向量 [0 0 0 1]，形成 4 × 4 矩阵。  
一个有效的三维平移变换矩阵 `A` 格式为：  
$$
A = \begin{pmatrix}
1 & 0 & 0 & t_x \\
0 & 1 & 0 & t_y \\
0 & 0 & 1 & t_z \\
0 & 0 & 0 & 1
\end{pmatrix}
$$  
$t_x$ 、 $t_y$ 和 $t_y$ 分别为 `x` 、 `y` 和 `z` 方向的平移量，用于设置 [Translation](#Q8) 属性。  
该参数用于设置 [A](#Q7) 属性。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q6"></a> tformIn — 三维平移几何变换**  
`affinetform3d` 对象 | `rigidtform3d` 对象 | `simtform3d` 对象 | `transltform3d` 对象 
  
三维平移几何变换，指定为 <a href="../affinetform3d/affinetform3d.html">affinetform3d</a>  </a> 、 <a href="../rigidtform3d/rigidtform3d.html">rigidtform3d</a>  </a> 、 <a href="../simtform3d/simtform3d.html">simtform3d</a>  </a> 、 或 `transltform3d` 对象。  
  
### 输出参数  
**<a id="P1"></a> tform — 三维平移几何变换**   
`transltform3d` 对象  

三维平移几何变换，指定为 `transltform3d` 对象形式。           

## 属性           

**<a id="Q7"></a> A — 三维正向平移变换**  
4 × 4 单位矩阵 | 4 × 4 数值矩阵  
  
三维正向平移变换，指定为 4 × 4 数值矩阵。 `A` 的默认值为单位矩阵。  
矩阵 `A` 遵循以下约定，将输入坐标空间中的点 (u, v, w) 变换为输出坐标空间中的点 (x, y, z)：  
$$
\begin{pmatrix}
x \\ y \\ z \\ 1
\end{pmatrix}
=
A \times
\begin{pmatrix}
u \\ v \\ w \\ 1
\end{pmatrix}
$$  
对于平移变换，`A` 的形式为： 
$$
A = \begin{pmatrix}
1 & 0 & 0 & t_x \\
0 & 1 & 0 & t_y \\
0 & 0 & 1 & t_z \\
0 & 0 & 0 & 1
\end{pmatrix}
$$ 
其中 $t_x$ 、 $t_y$ 和 $t_z$  分别为 `x` 、 `y` 和 `z` 方向的平移量，用于设置 [Translation](#Q8) 属性。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q8"></a> Translation — 平移量**  
[0 0 0] (默认) | 3 元素数值向量  
  
平移量指定为 $(t_x\ t_y\ t_z)$ 格式的 3 元素数值向量。  
  
  **数据类型：** `double` | `single`  
  
**Dimensionality — 几何变换的维度**  
只读：3（默认）

此属性为只读。 
输入点和输出点的几何变换维度，这里始终为3。  

**数据类型：** `double` 


## 对象函数
| <a href="../invert/invert.html">invert </a>  | 反转几何变换 |
| :----------- | :----------- |
| <a href="../outputlimits/outputlimits.html">outputlimits </a>  | 根据输入空间限制找到输出空间限制 |
| <a href="../transformPointsForward /transformPointsForward .html">transformPointsForward  </a> | 应用正向几何变换 |
|<a href="../transformPointsInverse/transformPointsInverse.html">transformPointsInverse </a>| 应用逆几何变换|

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../affinetform3d/affinetform3d.html">affinetform3d</a> | <a
href="../rigidtform3d/rigidtform3d.html">rigidtform3d</a> | <a 
href="../simtform3d/simtform3d.html">simtform3d</a> | <a 
href="../imwarp/imwarp.html">imwarp</a> 
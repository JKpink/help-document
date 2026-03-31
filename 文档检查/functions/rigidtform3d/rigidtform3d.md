## rigidtform3d
三维刚性几何变换  

## 简介  
[`tform = rigidtform3d`](#function1)  
[`tform = rigidtform3d(rotMat,t)`](#function2)  
[`tform = rigidtform3d(eulerAngles, t)` ](#function3)  
[`tform = rigidtform3d(rigidMat)`](#function4)  
[`tform = rigidtform2d(tformIn)`](#function5)  

## 用法  
<a id="function1"></a> [tform](#P1) = rigidtform3d 创建一个执行恒等变换的 `rigidtform3d` 对象。    
<a id="function2"></a> [tform](#P1) = rugidtform3d([rotMat](#Q2), [t](#Q1)) 从指定的旋转矩阵 `rotMat` 和每个维度上的平移量 `t`，创建一个进行刚性变换的 `rigidtform3d` 对象。   
<a id="function3"></a> [tform](#P1) = rugidtform3d([eulerAngles](#Q3), [t](#Q1)) 从指定的欧拉角 `eulerAngles` 和每个维度上的平移量 `t`，创建一个进行刚体变换的 `rigidtform2d` 对象。  
<a id="function4"></a> [tform](#P1) = rugidtform3d([rigidMat](#Q4)) 从指定的三维刚性变换矩阵 `rigidMat` 中创建一个 `rigidtform3d` 对象。     
<a id="function5"></a> [tform](#P1) = rugidtform3d([tformIn](#Q5)) 从另一个代表有效三维刚性几何变换的几何变换对象 `tformIn` 中，创建一个 `rigidtform3d` 对象。

## 参数说明
### 输入参数
  
**<a id="Q2"></a> rotMat — 旋转矩阵**  
3 × 3 单位矩阵（默认）| 3 × 3 数值矩阵  
  
旋转矩阵，指定为 3×3 数值矩阵。旋转矩阵的效果是先绕 `z` 轴旋转，然后绕 `y` 轴旋转，最后绕 `x` 轴旋转。  
该参数用于设置 [R](#Q8) 属性。  
  
**<a id="Q1"></a> t — 平移量**  
[0 0 0]（默认）| 3 元素数值向量  

平移量指定为 $(t_x\ t_y\ t_z)$ 格式的 3 元素数值向量，这些平移量用于设置 [A](#Q6) 属性定义的刚性变换矩阵中的 $t_x$ 、 $t_y$ 和 $t_z$ 值。  
该参数用于设置 [Translation](#Q7) 属性。 

**数据类型：** `double` | `single`  

**<a id="Q3"></a> eulerAngles — 欧拉角**  
[0 0 0]（默认）| 3 元素数值向量  

 x、y、z 顺序的欧拉角，单位为度，指定为 $(r_x\ r_y\ r_z)$ 格式的 3 元素数值向量。欧拉角根据以下公式将 [R](#Q8) 属性设置为三个旋转矩阵的乘积 :    
$$
\begin{aligned}
R_x &= \begin{pmatrix}
1 & 0 & 0 \\
0 & \cos d(r_x) & -\sin d(r_x) \\
0 & \sin d(r_x) & \cos d(r_x)
\end{pmatrix}, \\
R_y &= \begin{pmatrix}
\cos d(r_y) & 0 & \sin d(r_y) \\
0 & 1 & 0 \\
-\sin d(r_y) & 0 & \cos d(r_y)
\end{pmatrix}, \\
R_z &= \begin{pmatrix}
\cos d(r_z) & -\sin d(r_z) & 0 \\
\sin d(r_z) & \cos d(r_z) & 0 \\
0 & 0 & 1
\end{pmatrix}, \\
R &= R_z R_y R_x.
\end{aligned}
$$

**数据类型：** `double` | `single`  
  
**<a id="Q4"></a> rigidMat — 三维正向刚性变换**  
4 × 4 单位矩阵(默认) | 4 × 4 数值矩阵 | 3 × 4 数值矩阵  
  
三维正向刚性变换，指定为 4×4 数值矩阵。创建对象时，也可以将 `rigidMat` 指定为 3 × 4 数值矩阵，此时对象会自动在矩阵末尾拼接行向量 [0 0 0 1]，形成 4 × 4 矩阵。  
一个有效的三维刚性变换矩阵 `A` 形式如下：  
$$
A = \begin{pmatrix}
R(1,1) & R(1,2) & R(1,3) & t_x \\
R(2,1) & R(2,2) & R(2,3) & t_y \\
R(3,1) & R(3,2) & R(3,3) & t_z \\
0 & 0 & 0 & 1
\end{pmatrix}
$$    
R(i, j) 是旋转矩阵的元素，用于设置 [R](#Q8) 属性。$t_x$ 、 $t_y$ 、 $t_z$ 分别是 `x`、`y` 和 `z` 方向上的平移量，用于设置 [Translation](#Q7) 属性。     
该参数用于设置 [A](#Q6) 属性。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q5"></a> tformIn — 三维刚性几何变换**  
`affinetform3d` 对象 | `rigidtform3d` 对象 | `simtform3d` 对象 | `transltform3d` 对象 
  
三维刚性几何变换，指定为 <a href="../affinetform3d/affinetform3d.html">affinetform3d</a>  </a> 、`rigidtform3d` 、 <a href="../simtform3d/simtform3d.html">simtform3d</a>  </a> 或 <a href="../transltform3d/transltform3d.html">transltform3d</a>  </a>  对象。 
 

### 输出参数
**<a id="P1"></a> tform — 三维刚性几何变换**  
`rigidtform3d` 对象

三维刚性几何变换，指定为 `rigidtform3d` 对象。
## 属性  
  
**<a id="Q6"></a> A — 三维正向刚性变换**  
4 × 4 单位矩阵 | 4 × 4 数值矩阵  
  
三维正向刚性变换，指定为 4×4 数值矩阵。 `A` 的默认值为单位矩阵。  
矩阵 `A` 使用以下约定，将输入坐标空间中的点 (u, v, w) 变换为输出坐标空间中的点 (x, y, z)：  
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
对于刚性变换，`A` 的形式为：  
$$
A = \begin{pmatrix}
R(1,1) & R(1,2) & R(1,3) & t_x \\
R(2,1) & R(2,2) & R(2,3) & t_y \\
R(3,1) & R(3,2) & R(3,3) & t_z \\
0 & 0 & 0 & 1
\end{pmatrix}
$$  
其中 R(i, j) 是旋转矩阵的元素，用于设置 [R](#Q8) 属性。 $t_x$ 、 $t_y$ 和 $t_z$ 分别为 `x`、`y` 和 `z` 方向上的平移量，用于设置 [Translation](#Q7) 属性。
  
**数据类型：** `double` | `single`  
  
**<a id="Q8"></a> R — 旋转矩阵**  
3 × 3 单位矩阵(默认) | 3 × 3 数值矩阵  
  
旋转矩阵，指定为 3×3 数值矩阵，旋转矩阵的效果是先绕 `z` 轴旋转，然后绕 `y` 轴旋转，最后绕 `x` 轴旋转。
  
**<a id="Q7"></a> Translation — 平移量**  
[0 0 0] (默认) | 3 元素数值向量  
  
平移量指定为 $[t_x\ t_y\ t_z]$ 格式的 3 元素数值向量。
  
**数据类型：** `double` | `single`  
  
**Dimensionality — 几何变换的维度**  
只读：3（默认）

此属性为只读。 
输入点和输出点的几何变换维度，这里始终为3。  
**数据类型：** `double`  



## 版本历史 
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../affinetform3d/affinetform3d.html">affinetform3d</a> | <a
href="../transltform3d/transltform3d.html">transltform3d</a> | <a 
href="../simtform3d/simtform3d.html">simtform3d</a> | <a 
href="../imwarp/imwarp.html">imwarp</a> 

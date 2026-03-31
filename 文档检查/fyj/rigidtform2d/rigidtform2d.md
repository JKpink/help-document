## rigidtform2d
二维刚性几何变换  

## 简介
[`tform = rigidtform2d`](#function1)  
[`tform = rigidtform2d(t)`](#function2)  
[`tform = rigidtform2d(rotAngle, t)`](#function3)  
[`tform = rigidtform2d(rotMat, t)`](#function4)  
[`tform = rigidtform2d(rigidMat)`](#function5)  
[`tform = rigidtform2d(tformIn)`](#function6)   

## 用法 
<a id="function1"></a> [tform](#P1) = rigidtform2d 创建一个执行恒等变换的 `rigidtform2d` 对象。    
<a id="function2"></a> [tform](#P1) = rugidtform2d([t](#Q1)) 从指定的平移量 `t`，创建一个进行平移刚性变换的 `rigidtform2d` 对象，  
如果只需要纯二维平移变换，建议使用 <a href="../transltform2d/transltform2d.html">transltform2d</a>  </a> 对象。    
<a id="function3"></a> [tform](#P1) = rugidtform2d([rotAngle](#Q2), [t](#Q1)) 从指定的绕原点旋转角度 `rotAngle` 和平移量 `t`，创建一个进行刚性变换的 `rigidtform2d` 对象。  
<a id="function4"></a> [tform](#P1) = rugidtform2d([rotMat](#Q3), [t](#Q1)) 从指定的旋转矩阵 `rotMat` 和平移量 `t`，创建一个进行刚性变换的 `rigidtform2d` 对象。   
<a id="function5"></a> [tform](#P1) = rugidtform2d([rigidMat](#Q4)) 从指定的二维刚性变换矩阵 `rigidMat` 中创建一个 `rigidtform2d` 对象。  
<a id="function6"></a> [tform](#P1) = rigidtform2d([tformIn](#Q5)) 从另一个代表有效二维刚性几何变换的几何变换对象 `tformIn` 中，创建一个 `rigidtform2d` 对象。

## 参数说明
### 输入参数
**<a id="Q1"></a> t — 平移量**  
[0 0]（默认）| 2 元素数值向量  

平移量指定为 $(t_x\ t_y)$ 格式的 2 元素数值向量，这些平移量用于设置 [A](#Q6) 属性定义的刚性变换矩阵中的 $t_x$ 和 $t_y$ 值。  
该参数用于设置 [Translation](#Q7) 属性。 

**数据类型：** `double` | `single`

**<a id="Q2"></a> rotAngle — 绕原点的旋转角度**  
0（默认）| 数值标量  

绕原点的旋转角度,单位为度，指定为数值标量。该旋转角度用于设置 [A](#Q6) 属性定义的变换矩阵中的角度值 `r`，也用于设置 [R](#Q9) 属性所定义的旋转矩阵中的角度值。  
该参数用于设置 [RotationAngle](#Q8) 属性。

**数据类型：** `double` | `single`

**<a id="Q3"></a> rotMat — 旋转矩阵**  
2 × 2 单位矩阵（默认）| 2 × 2 数值矩阵  
  
旋转矩阵，指定为 2 × 2 数值矩阵。该矩阵必须满足以下形式：
$$   
 \mathrm{rotMat} =
 \begin{pmatrix}
    \cos d(r) & -\sin d(r) \\
    \sin d(r) & \cos d(r)
 \end{pmatrix}.
$$
其中 `r` 为绕原点的旋转角度，单位为度。  
该参数用于设置 [R](#Q9) 属性。  
  
**<a id="Q4"></a> rigidMat — 二维正向刚性变换**  
3 × 3 单位矩阵(默认) | 3 × 3 数值矩阵 | 2 × 3 数值矩阵  
  
二维正向刚性变换，指定为 3 × 3 数值矩阵。创建对象时，也可以将 `rigidMat` 指定为 2 × 3 数值矩阵，此时对象会自动在矩阵末尾拼接行向量 [0 0 1]，形成 3 × 3 矩阵。  
一个有效的二维刚性变换矩阵 `A` 形式如下：  
$$  
A = \begin{pmatrix}
\cos d(r) & -\sin d(r) & t_x \\
\sin d(r) & \cos d(r) & t_y \\
0 & 0 & 1
\end{pmatrix}  
$$  
`r` 为旋转角度，用于设置 [RotationAngle](#Q8) 属性，$t_x$ 和 $t_y$ 分别为 `x` 方向和 `y` 方向的平移量，用于设置 [Translation](Q7) 属性。  
该参数用于设置 [A](#Q6) 属性。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q5"></a> tformIn — 二维刚性几何变换**  
`affinetform2d` 对象 | `rigidtform2d` 对象 | `simtform2d` 对象 | `transltform2d` 对象 | `projtform2d` 对象  
  
二维刚性几何变换，指定为 <a href="../affinetform2d/affinetform2d.html">affinetform2d</a>  </a>、`rigidtform2d`、<a href="../simtform2d/simtform2d.html">simtform2d</a>  </a>、<a href="../transltform2d/transltform2d.html">transltform2d</a>  </a> 或 <a href="../projtform2d/projtform2d.html">projtform2d</a>  </a> 对象。  
  
### 输出参数
**<a id="P1"></a> tform — 二维刚性几何变换**   
`rigidtform2d` 对象  

二维刚性几何变换，指定为 `rigidtform2d` 对象。  
 
## 属性  
**<a id="Q6"></a> A — 二维正向刚性变换**  
3 × 3 单位矩阵 | 3 × 3 数值矩阵  
  
二维正向刚性变换，指定为 3 × 3 数值矩阵。 `A` 的默认值为单位矩阵。  
矩阵 `A` 遵循以下约定，将输入坐标空间中的点 (u, v) 变换为输出坐标空间中的点 (x, y)：  
$$  
\begin{pmatrix} x \\ y \\ 1 \end{pmatrix} = A \times \begin{pmatrix} u \\ v \\ 1 \end{pmatrix}  
$$  
对于刚性变换，`A` 的形式为： 
$$
A = \begin{pmatrix}
\cos d(r) & -\sin d(r) & t_x \\
\sin d(r) & \cos d(r) & t_y \\
0 & 0 & 1
\end{pmatrix}
$$  
其中，`r` 为旋转角度，用于设置 [RotationAngle](#Q8) 属性。 $t_x$ 和 $t_y$ 分别为 `x` 方向和 `y` 方向的平移量，用于设置 [Translation](#Q7) 属性。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q9"></a> R — 旋转矩阵**  
2×2 单位矩阵(默认) | 2×2 数值矩阵  
  
旋转矩阵，指定为 2×2 数值矩阵，该矩阵必须满足以下形式 :  
R = [cosd(r) -sind(r);sind(r) cosd(r)]  
其中 `r` 为旋转角度值，用于设置 [RotationAngle](#Q8) 属性。  
  
**<a id="Q8"></a> RotationAngle — 绕原点的旋转角度**  
0 (默认) | 数值标量  
  
绕原点的旋转角度，单位为度，指定为数值标量。该旋转角度用于设置 [A](#Q6) 属性所定义的变换矩阵中的 `r` 值，也用于设置 [R](#Q9) 属性所定义的旋转矩阵中的 `r` 值。  
  
**数据类型：** `double` | `single`   
  
**<a id="Q7"></a> Translation — 平移量**  
[0 0] (默认) | 2 元素数值向量  
  
平移量指定为 $(t_x\ t_y)$ 格式的 2 元素数值向量形式。这些平移量用于设置 [A](#Q6) 属性所定义的刚性变换矩阵中的 $t_x$ 和 $t_y$ 值。  
  
**数据类型：** `double` | `single`     
 
**Dimensionality — 几何变换的维度**  
只读：2（默认）

此属性为只读。 
输入点和输出点的几何变换维度，这里始终为2。  
  
**数据类型：** `double`



## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../fitgeotform2d/fitgeotform2d.html">fitgeotform2d</a> | <a
href="../affinetform2d/affinetform2d.html">affinetform2d</a> | <a 
href="../transltform2d/transltform2d.html">transltform2d</a> | <a 
href="../simtform2d/simtform2d.html">simtform2d</a> | <a 
href="../projtform2d/projtform2d.html">projtform2d</a> | <a 
href="../imwarp/imwarp.html">imwarp</a> 

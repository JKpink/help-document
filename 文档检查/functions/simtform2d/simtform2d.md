## simtform2d
二维相似几何变换
  
## 简介  
[`tform = simtform2d`](#function1)  
[`tform = simtform2d(s, rotAngle, t)`](#function2)  
[`tform = simtform2d(s, rotMat, t)`](#function3)  
[`tform = simtform2d(simMat)`](#function4)  
[`tform = simtform2d(tformIn)`](#function5)      

## 用法 
<a id="function1"></a> [tform](#P1) = simtform2d 创建一个执行恒等变换的 `simtform2d` 对象。    
<a id="function2"></a> [tform](#P1) = simtform2d([s](#Q3), [rotAngle](#Q2), [t](#Q1)) 从指定的缩放因子 `s` 、 旋转角度 `rotAngle` 和平移量 `t` ，创建一个进行相似变换的 `simtform2d` 对象。    
<a id="function3"></a> [tform](#P1) = simtform2d([s](#Q3), [rotMat](#Q4), [t](Q1)) 从指定的缩放因子 `s`、旋转矩阵 `rotMat` 和平移量 `t`，创建一个进行相似变换的 `simtform2d` 对象。    
<a id="function4"></a> [tform](#P1) = simtform2d([simMat](#Q5)) 从指定的二维相似变换矩阵 `simMat` 创建一个 `simtform2d` 对象。    
<a id="function5"></a> [tform](#P1) = simtform2d([tformIn](#Q6)) 从另一个代表有效二维相似几何变换的几何对象 `tformIn` 创建一个 `simtform2d` 对象。   

## 参数说明
### 输入参数
**<a id="Q3"></a> s — 缩放因子**  
1 (默认) | 正数  

缩放因子，指定为一个正数。该缩放因子用于设置 [A](#Q7) 属性所定义的相似变换矩阵中的参数 `s`。  
此参数用于设置 [Scale](#Q8) 属性。 

**数据类型：** `double` | `single`  
  
**<a id="Q2"></a> rotAngle — 绕原点旋转角度**  
0 (默认) | 数值标量  
  
绕原点的旋转角度，单位为度，指定为区间 [-180, 180] 内的数值标量。若指定的旋转角度超出该范围， `simtform2d` 对象会通过加减 360 的整数倍自动将其规整至 [-180,180] 区间内。  
该旋转角度用于设置 [A](#Q7) 属性所定义的变换矩阵中的参数 `r`，以及设置 [R](#Q9) 属性所定义的旋转矩阵中的参数 `r` 。  
此参数用于设置 [RotationAngle](#Q10) 属性。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q4"></a> rotMat — 旋转矩阵**  
2 × 2 单位矩阵 | 2 × 2 数值矩阵  
  
旋转矩阵，指定为 2 × 2 数值矩阵。该矩阵必须满足以下形式:  
R = [cosd(r) -sind(r) ; sind(r) cosd(r)]  
其中 `r` 为绕原点的旋转角度，单位为度。  
此参数用于设置 [R](#Q9) 属性。  
  
**<a id="Q1"></a> t — 平移量**  
[0 0] (默认值) | 2 元素数值向量  
  
平移量指定为 $[t_x\ t_y]$ 格式的 2 元素数值向量。这些平移量用于设置 [A](#Q7) 属性所定义的相似变换矩阵中的参数 $t_x$ 和 $t_y$ 。  
此参数用于设置 [Translation](#Q11) 属性。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q5"></a> simMat — 二维正向相似变换**  
3 × 3 单位矩阵(默认) | 3 × 3 数值矩阵 | 2 × 3 数值矩阵  
  
二维正向相似变换，指定为 3 × 3 数值矩阵。创建对象时，也可将 `simMat` 指定为 2 × 3 数值矩阵，此时对象会自动在矩阵末尾拼接行向量 [0 0 1] ，形成 3 × 3 矩阵。  
一个有效的二维相似变换矩阵 `A` 形式如下 :  
$$
A = \begin{pmatrix}
s \times \cos d(r) & -s \times \sin d(r) & t_x \\
s \times \sin d(r) & s \times \cos d(r) & t_y \\
0 & 0 & 1
\end{pmatrix}
$$  
其中`s` 为缩放因子，用于设置 [Scale](#Q8) 属性。 `r` 为旋转角度，用于设置 [RotationAngle](#Q10) 属性。$t_x$ 和 $t_y$ 分别为 `x`、`y `方向的平移量，用于设置 [Translation](#Q11) 属性。  
此参数用于设置 [A](#Q7) 属性。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q6"></a> tformIn — 二维相似几何变换**  
`affinetform2d` 对象 | `rigidtform2d` 对象 | `simtform2d` 对象 | `transltform2d` 对象 | `projtform2d` 对象  
  
二维相似几何变换，指定为 <a href="../affinetform2d/affinetform2d.html">affinetform2d</a>  </a> 、 <a href="../rigidtform2d/rigidtform2d.html">rigidtform2d</a>  </a> 、 `simtform2d` 、 <a href="../transltform2d/transltform2d.html">transltform2d</a>  </a> 或 <a href="../projtform2d/projtform2d.html">projtform2d</a>  </a> 对象。    
 
### 输出参数
**<a id="P1"></a> tform — 二维相似几何变换**  
`simtform2d` 对象  

二维相似几何变换，指定为 `simtform2d` 对象。
## 属性    
**<a id="Q7"></a> A — 二维正向相似变换**  
3 × 3 单位矩阵 | 3 × 3 数值矩阵  
  
二维正向相似变换，指定为 3 × 3 数值矩阵。 `A` 的默认值为单位矩阵。  
矩阵 `A` 遵循以下约定，将输入坐标空间中的点 (u, v) 变换为输出坐标空间中的点 (x, y) :  
$$  
\begin{pmatrix} x \\ y \\ 1 \end{pmatrix} = A \times \begin{pmatrix} u \\ v \\ 1 \end{pmatrix}  
$$  
对于相似变换，`A` 的形式为： 
$$
A = \begin{pmatrix}
s \times \cos d(r) & -s \times \sin d(r) & t_x \\
s \times \sin d(r) & s \times \cos d(r) & t_y \\
0 & 0 & 1
\end{pmatrix}
$$ 
其中`s` 为缩放因子，用于设置 [Scale](#Q8) 属性。 `r` 为旋转角度，用于设置 [RotationAngle](#Q10) 属性。 $t_x$ 和 $t_y$ 分别为 `x` 方向和 `y` 方向的平移量，用于设置 [Translation](#Q11) 属性。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q8"></a> Scale — 缩放因子**  
1 (默认) | 正数  
  
缩放因子，指定为一个正数。该缩放因子用于设置 [A](#Q7) 属性所定义的相似变换矩阵中的参数 `s`。  
  
**数据类型：** `double` | `single`   
  
**<a id="Q9"></a> R — 旋转矩阵**  
2 × 2 单位矩阵 (默认) | 2 × 2 数值矩阵  
  
旋转矩阵，指定为 2 × 2 数值矩阵，该矩阵必须满足以下形式 :  
R = [cosd(r) -sind(r) ; sind(r) cosd(r)]  
其中 `r` 用于设置 [RotationAngle](#Q10) 属性。  
  
**<a id="Q10"></a> RotationAngle — 绕原点的旋转角度**  
0 (默认) | 数值标量  
  
绕原点的旋转角度，单位为度,指定区间 [-180,180] 内的数值标量。若指定的旋转角度超出该范围， `simtform2d` 对象会通过加减360的整数倍自动将其规整至 [-180,180] 区间内。  
该旋转角度用于设置 [A](#Q7) 属性所定义的变换矩阵中的参数 `r`，以及用于设置 [R](#Q9) 属性所定义的旋转矩阵中的参数 `r`。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q11"></a> Translation — 平移量**  
[0 0] (默认值) | 2 元素数值向量  
  
平移量指定为 $[t_x\ t_y]$ 格式的 2 元素数值向量。这些平移量用于设置 [A](#Q7) 属性所定义的相似变换矩阵中的 $t_x$ 和 $t_y$ 值。  
  
**数据类型：** `double` | `single`        
  
**Dimensionality — 几何变换的维度**  
只读：2（默认）

此属性为只读。 
输入点和输出点的几何变换维度，这里始终为2。  
  
**数据类型：** `double`



## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../affinetform2d/affinetform2d.html">affinetform2d </a> | <a
href="../rigidtform2d/rigidtform2d.html">rigidtform2d</a> | <a 
href="../transltform2d/transltform2d.html">transltform2d</a> | <a 
href="../projtform2d/projtform2d.html">projtform2d</a> | <a 
href="../fitgeotform2d/fitgeotform2d.html">fitgeotform2d</a> | <a 
href="../imwarp/imwarp.html">imwarp</a> 

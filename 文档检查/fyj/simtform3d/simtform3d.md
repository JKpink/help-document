## simtform3d
三维相似几何变换
 
## 简介
[`tform = simtform3d`](#function1)    
[`tform = simtform3d(s, rotMat, t)`](#function2)  
[`tform = simtform3d(s, eulerAngles, t)`](#function3)  
[`tform = simtform3d(simMat)`](#function4)  
[`tform = simtform3d(tformIn)`](#function5)      


## 用法 
<a id="function1"></a> [tform](#P1) = simtform3d 创建一个执行恒等变换的 `simtform3d` 对象。      
<a id="function3"></a> [tform](#P1) = simtform3d([s](#Q3), [rotMat](#Q2), [t](#Q1)) 从指定的缩放因子 `s`、旋转矩阵 `rotMat` 和平移量 `t`，创建一个进行相似变换的 `simtform3d` 对象。    
<a id="function3"></a> [tform](#P1) = simtform3d([s](#Q3), [eulerAngles](#Q4), [t](#Q1)) 从指定的缩放因子 `s`、欧拉角度 `eulerAngles` 和平移量 `t`，创建一个进行相似变换的 `simtform3d` 对象。    
<a id="function4"></a> [tform](#P1) = simtform3d([simMat](#Q5)) 从指定的三维相似变换矩阵 `simMat` 创建一个 `simtform3d` 对象。    
<a id="function5"></a> [tform](#P1) = simtform3d([tformIn](#Q6)) 从另一个代表有效三维相似几何变换的几何对象 `tformIn` 创建一个 `simtform3d` 对象。    

## 参数说明
### 输入参数  
**<a id="Q3"></a> s — 缩放因子**  
1 (默认)| 正数  

缩放因子，指定为一个正数。该缩放因子用于设置 [A](#Q7) 属性所定义的相似变换矩阵中的参数 `s`。  
此参数用于设置 [Scale](#Q8) 属性。 

**数据类型：** `double` | `single`  
  
**<a id="Q2"></a> rotMat — 旋转矩阵**  
3 × 3 单位矩阵 | 3 × 3 数值矩阵  
  
旋转矩阵，指定为 3×3 数值矩阵。该旋转矩阵的效果是先绕 `z` 轴旋转，再绕 `y` 轴旋转，最后绕 `x` 轴旋转。   
此参数用于设置 [R](#Q9) 属性。  
  
**<a id="Q1"></a> t — 平移量**  
[0 0 0] (默认) | 3 元素数值向量  
  
平移量指定为 $(t_x\ t_y\ t_z)$ 格式的 3 元素数值向量。这些平移量用于设置 [A](#Q7) 属性所定义的相似变换矩阵中的参数 $t_x$ 、 $t_y$ 和 $t_z$ 。  
此参数用于设置 [Translation](#Q10) 属性。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q4"></a> eulerAngles — 欧拉角**  
[0 0 0]（默认值）| 3 元素数值向量  

 x、y、z 顺序的欧拉角，单位为度，指定为 $(r_x\ r_y\ r_z)$ 格式的 3 元素数值向量。欧拉角根据以下公式将 [R](#Q9) 属性设置为三个旋转矩阵的乘积 :  
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
  
**<a id="Q5"></a> simMat — 三维正向相似变换**  
4 × 4 单位矩阵 (默认) | 4 × 4 数值矩阵 | 3 × 4 数值矩阵  
  
三维相似变换，指定为 4 × 4 数值矩阵。创建对象时，也可将 `simMat` 指定为 3 × 4 数值矩阵，此时对象会自动在矩阵末尾拼接行向量 [0 0 0 1]，形成 4 × 4 矩阵。  
一个有效的三维相似变换矩阵 `A` 形式如下： 
$$
\boldsymbol{A} = 
\begin{pmatrix}
s * R(1,1) & s * R(1,2) & s * R(1,3) & t_x \\
s * R(2,1) & s * R(2,2) & s * R(2,3) & t_y \\
s * R(3,1) & s * R(3,2) & s * R(3,3) & t_z \\
0 & 0 & 0 & 1
\end{pmatrix}
$$    
其中`s` 为缩放因子，用于设置 [Scale](#Q8) 属性。 R(i,j) 为旋转矩阵的元素，用于设置 [R](#Q9) 属性。$t_x$ 、 $t_y$ 和 $t_z$ 分别为 `x`、`y`、`z` 方向的平移量，用于设置 [Translation](#Q10) 属性。  
此参数用于设置 [A](#Q7) 属性。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q6"></a> tformIn — 三维相似几何变换**  
`affinetform3d` 对象 | `rigidtform3d` 对象 | `simtform3d` 对象 | `transltform3d` 对象 
  
三维相似几何变换，指定为 <a href="../affinetform3d/affinetform3d.html">affinetform3d</a>  </a> 、 <a href="../rigidtform3d/rigidtform3d.html">rigidtform3d</a>  </a> 、 `simtform3d` 或 <a href="../transltform3d/transltform3d.html">transltform3d</a>  </a>  对象。        
 

### 输出参数
**<a id="P1"></a> tform — 三维相似几何变换**  
`simtform3d` 对象  

三维相似几何变换，指定为 `simtform3d` 对象。
## 属性  
**<a id="Q7"></a> A — 三维正向相似变换**  
4 × 4 单位矩阵 | 4 × 4 数值矩阵  
  
三维正向相似变换，指定为 4 × 4 数值矩阵。 `A` 的默认值为单位矩阵。  
矩阵 `A` 遵循以下约定，将输入坐标空间中的点 (u, v, w) 变换为输出坐标空间中的点 (x, y, z)：  
$$
\begin{pmatrix}
x \\ y \\ z \\ 1
\end{pmatrix}
=
\boldsymbol{A} \times
\begin{pmatrix}
u \\ v \\ w \\ 1
\end{pmatrix}
$$ 
对于相似变换，`A` 的形式为：  
$$
\boldsymbol{A} =
\begin{pmatrix}
s * R(1,1) & s * R(1,2) & s * R(1,3) & t_x \\
s * R(2,1) & s * R(2,2) & s * R(2,3) & t_y \\
s * R(3,1) & s * R(3,2) & s * R(3,3) & t_z \\
0 & 0 & 0 & 1
\end{pmatrix}
$$ 
其中 `s` 为缩放因子用于设置 [Scale](#Q8) 属性。R(i, j) 是旋转矩阵的元素，用于设置 [R](#Q9) 属性。  $t_x$ 、 $t_y$ 和 $t_z$ 分别为 `x `、`y`、`z` 方向的平移量，用于设置 [Translation](#Q10) 属性。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q8"></a> Scale — 缩放因子**  
1 (默认) | 正数  
  
缩放因子，指定为一个正数。该缩放因子用于设置 [A](#Q7) 属性所定义的相似变换矩阵中的参数 `s`。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q9"></a> R — 旋转矩阵**  
3 × 3 单位矩阵 (默认) | 3 × 3 数值矩阵  
  
旋转矩阵，指定为 3×3 数值矩阵，该旋转矩阵的效果是先绕 `z` 轴旋转，再绕 `y` 轴旋转，最后绕 `x` 轴旋转。     
  
**<a id="Q10"></a> Translation — 平移量**  
[0 0 0] (默认) | 3 元素数值向量  
  
平移量，指定为 $(t_x\ t_y\ t_z)$ 格式的 3 元素数值向量。
  
**数据类型：** `double` | `single`  
   
**Dimensionality — 几何变换的维度**  
只读：3（默认）

此属性为只读。 
输入点和输出点的几何变换维度，这里始终为3。  
  
**数据类型：** `double`  



## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../affinetform3d /affinetform3d .html">affinetform3d </a> | <a
href="../rigidtform3d/rigidtform3d.html">rigidtform3d</a> | <a 
href="../transltform3d/transltform3d.html">transltform3d</a> | <a 
href="../imwarp/imwarp.html">imwarp</a> 

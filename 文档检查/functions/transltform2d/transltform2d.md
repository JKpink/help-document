## transltform2d
二维平移几何变换 

## 简介
[`tform = transltform2d`](#function1)  
[`tform = transltform2d(t)`](#function2)  
[`tform = transltform2d(tx, ty)`](#function3)    
[`tform = transltform2d(translMat)`](#function4)  
[`tform = transltform2d(tformIn)`](#function5) 

## 用法  

<a id="function1"></a> [tform](#P1) = transltform2d 创建一个执行恒等变换的 `transltform2d` 对象。  
<a id="function2"></a> [tform](#P1) = transltform2d([t](#Q1)) 从指定的平移向量 `t` 创建一个进行平移变换的 `transltform2d` 对象。  
<a id="function3"></a> [tform](#P1) = transltform2d([tx](#Q2), [ty](#Q3)) 从指定 `x` 方向平移量 `tx` 和 `y` 方向平移量 `ty` 创建一个进行平移变换的 `transltform2d` 对象。  
<a id="function4"></a> [tform](#P1) = transltform2d([translMat](#Q4)) 从指定的二维平移变换矩阵 `translMat` 创建一个 `transltform2d` 对象。    
<a id="function5"></a> [tform](#P1) = transltform2d([tformIn](#Q5)) 从另一个表示有效二维平移变换的几何变换对象 `tformIn` 创建一个 `transltform2d` 对象。     

## 参数  
### 输入参数  
**<a id="Q1"></a> t — 平移量**  
[0 0]（默认）| 2 元素数值向量  

平移量，指定为 $(t_x\ t_y)$ 格式的 2 元素数值向量，这些平移量用于设置 [A](#Q6) 属性定义的平移变换矩阵中的 $t_x$ 和 $t_y$ 值。  
该参数用于设置 [Translation](#Q7) 属性。 

**数据类型：** `double` | `single`  
  
**<a id="Q2"></a> tx — x 方向平移量**  
0 (默认) | 数值标量  
  
`x` 方向的平移量，指定为数值标量。此参数用于设置 [Translation](#Q7) 属性的第一个元素。  
  
**<a id="Q3"></a> ty — y 方向平移量**  
0(默认值) | 数值标量  
  
`y` 方向的平移量，指定为数值标量。此参数用于设置 [Translation](#Q7) 属性的第二个元素。  
  
**<a id="Q4"></a> translMat — 二维正向平移变换**  
3 × 3 单位矩阵 (默认) | 3 × 3 数值矩阵 | 2 × 3 数值矩阵  
  
二维正向平移变换，指定为 3 × 3 数值矩阵。创建对象时，也可以将 `translMat` 指定为 2 × 3 数值矩阵，此时对象会自动在矩阵末尾拼接行向量 [0 0 1]，形成 3 × 3 矩阵。  
一个有效的二维平移变换矩阵 `A` 格式为：  
$$
A = \begin{pmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0 & 1
\end{pmatrix}
$$  
$t_x$ 和 $t_y$ 分别为 `x` 方向和 `y` 方向的平移量，用于设置 [Translation](#Q7) 属性。  
该参数用于设置 [A](#Q6) 属性。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q5"></a> tformIn — 二维平移几何变换**  
`affinetform2d` 对象 | `rigidtform2d` 对象 | `simtform2d` 对象 | `transltform2d` 对象 | `projtform2d` 对象  
  
二维平移几何变换，指定为 <a href="../affinetform2d/affinetform2d.html">affinetform2d</a>  </a> 、 <a href="../rigidtform2d/rigidtform2d.html">rigidtform2d</a>  </a> 、 <a href="../simtform2d/simtform2d.html">simtform2d</a>  </a> 、 `transltform2d` 或 <a href="../projtform2d/projtform2d.html">projtform2d</a>  </a> 对象。  
  
### 输出参数  
**<a id="P1"></a> tform — 二维平移几何变换**   
`transltform2d` 对象  

二维平移几何变换，指定为 `transltform2d` 对象。  
  
## 属性           

**<a id="Q6"></a> A — 二维正向平移变换**  
3 × 3 单位矩阵 | 3 × 3 数值矩阵  
  
二维正向平移变换，指定为 3×3 数值矩阵。 `A` 的默认值为单位矩阵。  
矩阵 `A` 遵循以下约定，将输入坐标空间中的点 (u, v) 变换为输出坐标空间中的点 (x, y)： 
$$  
\begin{pmatrix} x \\ y \\ 1 \end{pmatrix} = A \times \begin{pmatrix} u \\ v \\ 1 \end{pmatrix}  
$$  
对于平移变换，`A` 的形式为： 
$$
A = \begin{pmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0 & 1
\end{pmatrix}
$$  
其中 $t_x$ 和 $t_y$ 分别为 `x` 方向和 `y` 方向的平移量，用于设置 [Translation](#Q7) 属性。  
  
**数据类型：** `double` | `single`  
  
**<a id="Q7"></a> Translation — 平移量**  
[0 0] (默认) | 2 元素数值向量  
  
平移量指定为 $(t_x\ t_y)$ 格式的 2 元素数值向量。
  
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
href="../rigidtform2d/rigidtform2d.html">rigidtform2d</a> | <a 
href="../simtform2d/simtform2d.html">simtform2d</a> | <a 
href="../projtform2d/projtform2d.html">projtform2d</a> | <a 
href="../imwarp/imwarp.html">imwarp</a> 
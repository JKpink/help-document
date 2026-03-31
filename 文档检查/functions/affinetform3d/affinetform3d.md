## affinetform3d
三维仿射几何变换  

## 简介
[`tform = affinetform3d`](#function1)  
[`tform = affinetform3d(affineMat)`](#function2)  
[`tform = affinetform3d(tformIn)`](#function3)

## 用法  
<a id="function1"></a> [tform](#P1) = affinetform3d 创建一个用于执行恒等变换的 `affinetform3d` 对象。  
<a id="function2"></a> [tform](#P1) = affinetform3d([affineMat](#P2)) 从指定的三维仿射变换矩阵 `affineMat` 创建 `affinetform3d` 对象。  
<a id="function3"></a> [tform](#P1) = affinetform3d([tformIn](#P3)) 从另一个代表有效仿射几何变换对象 `tformIn` 创建一个 `affinetform3d` 对象。

## 参数说明
### 输入参数  
**<a id="P2"></a> affineMat — 三维正向仿射变换**   
4 × 4 单位矩阵（默认） | 4 × 4 数值矩阵 | 3 × 4 数值矩阵  
  
三维正向仿射变换，指定为 4 × 4 数值矩阵；创建对象时，也可以将 `affineMat` 指定为 3 × 4 数值矩阵，此时对象会自动在矩阵末尾拼接行向量 [0 0 0 1]，形成 4 × 4 数值矩阵。
有效的三维仿射变换 `A` 形式如下： 

$$
    A = 
    \begin{pmatrix}
    a_{11} & a_{12} & a_{13} & a_{14} \\
    a_{21} & a_{22} & a_{23} & a_{24} \\
    a_{31} & a_{32} & a_{33} & a_{34} \\
    0 & 0 & 0 & 1
    \end{pmatrix}.
$$  
此参数用于设置 [A](#Q1) 的属性。  
  
**数据类型：** `double`| `single`  
  
**<a id="P3"></a> tformIn — 三维仿射几何变换**  
`affinetform3d` 对象 | `rigidtform3d` 对象 | `simtform3d` 对象 | `transltform3d` 对象 
  
三维仿射几何变换，指定为 `affinetform3d` 对象、<a href="../rigidtform3d/rigidtform3d.html">rigidtform3d</a>  </a> 对象、<a href="../simtform3d/simtform3d.html">simtform3d</a>  </a> 对象或 <a href="../transltform3d/transltform3d.html">transltform3d</a>  </a> 对象。 


### 输出参数
**<a id="P1"></a> tform — 三维仿射几何变换**  
`affinetform3d` 对象

三维仿射几何变换，指定为 `affinetform3d` 对象。  
  
## 属性  
**<a id="Q1"></a> A — 三维正向仿射变换**  
4 × 4 单位矩阵 (默认) | 4 × 4 数值矩阵  
  
三维正向仿射变换，指定为 4 × 4 数值矩阵。`A` 的默认值为单位矩阵。  
矩阵 `A` 使用以下约定将输入坐标空间中的点 $(u, v, w)$ 转换为输出坐标空间中的点 $(x, y, z)$：  
$$
\begin{pmatrix}
x \\
y \\
z \\
1
\end{pmatrix}
=
A \times
\begin{pmatrix}
u \\
v \\
w \\
1
\end{pmatrix}
$$  
对于仿射变换，`A` 的形式为：  
$$
    A = 
    \begin{pmatrix}
    a_{11} & a_{12} & a_{13} & a_{14} \\
    a_{21} & a_{22} & a_{23} & a_{24} \\
    a_{31} & a_{32} & a_{33} & a_{34} \\
    0 & 0 & 0 & 1
    \end{pmatrix}.
$$    
  
**数据类型：** `double`| `single`   
 
**Dimensionality — 几何变换的维度**  
只读：3（默认）

此属性为只读。 
输入点和输出点的几何变换维度，这里始终为3。  
**数据类型：** `double` 
  

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../simform3d/simform3d.html">simform3d</a> | <a 
href="../rigidtform3d/rigidtform3d.html">rigidtform3d</a> | <a 
href="../transltform3d/transltform3d.html">transltform3d</a> | <a 
href="../imwarp/imwarp.html">imwarp</a>
## affinetform2d
二维仿射几何变换  

## 简介
[`tform = affinetform2d`](#function1)  
[`tform = affinetform2d(affineMat)`](#function2)  
[`tform = affinetform2d(tformIn)`](#function3)

## 用法 
<a id="function1"></a> [tform](#P1) = affinetform2d 创建一个用于执行恒等变换的 `affinetform2d` 对象。  
<a id="function2"></a> [tform](#P1) = affinetform2d([affineMat](#P2)) 从指定的二维仿射变换矩阵 `affineMat` 创建 `affinetform2d` 对象。  
<a id="function3"></a> [tform](#P1) = affinetform2d([tformIn](#P3)) 从另一个代表二维有效仿射几何变换对象 `tformIn` 创建一个 `affinetform2d` 对象。

## 参数说明
### 输入参数
**<a id="P2"></a> affineMat — 二维正向仿射变换**  
3 × 3 单位矩阵（默认） | 3 × 3 数值矩阵 | 2 × 3 数值矩阵   

二维正向仿射变换，指定为 3×3 数值矩阵；创建对象时，也可以将 `affineMat` 指定为 2 × 3 数值矩阵，此时对象会自动在矩阵末尾拼接行向量 [0 0 1]，形成 3 × 3 数值矩阵。  
有效的二维仿射变换 `A` 形式如下：  
   
$$
    A = 
    \begin{pmatrix}
    a_{11} & a_{12} & a_{13} \\
    a_{21} & a_{22} & a_{23} \\
    0 & 0 & 1
    \end{pmatrix}.
$$  
此参数用于设置 [A](#Q1) 的属性。
  
**数据类型：** `double` | `single` 
  
**<a id="P3"></a> tformIn — 二维仿射几何变换**  
`affinetform2d` 对象 | `rigidtform2d` 对象 | `simtform2d` 对象 | `transltform2d` 对象 | `projtform2d` 对象  
  
仿射二维几何变换，指定为 `affinetform2d` 对象、<a href="../rigidtform2d/rigidtform2d.html">rigidtform2d</a>  </a> 对象、<a href="../simtform2d/simtform2d.html">simtform2d</a>  </a> 对象、<a href="../transltform2d/transltform2d.html">transltform2d</a>  </a> 对象或 <a href="../projtform2d/projtform2d.html">projtform2d</a>  </a> 对象。  

### 输出参数
**<a id="P1"></a> tform — 二维仿射几何变换**  
`affinetform2d` 对象

二维仿射几何变换，指定为 `affinetform2d` 对象。  
   
## 属性  
**<a id="Q1"></a> A — 二维正向仿射变换**  
3 × 3 单位矩阵 (默认) | 3 × 3 数值矩阵  
  
二维正向仿射变换，指定为 3 × 3 数值矩阵。`A` 的默认值为单位矩阵。  
矩阵 `A` 使用以下约定将输入坐标空间中的点 (u, v) 转换为输出坐标空间中的点 (x, y)：
$$
\begin{pmatrix}
x \\
y \\
1
\end{pmatrix}
=
A \times
\begin{pmatrix}
u \\
v \\
1
\end{pmatrix}
$$  
对于仿射变换，`A` 的形式为：  
$$
    A = 
    \begin{pmatrix}
    a_{11} & a_{12} & a_{13} \\
    a_{21} & a_{22} & a_{23} \\
    0 & 0 & 1
    \end{pmatrix}.
$$  
  
**数据类型：** `double` | `single`   
  
**Dimensionality — 几何变换的维度**  
只读：2（默认）

此属性为只读。 
输入点和输出点的几何变换维度，这里始终为2。  
  
**数据类型：** `double`
  

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../simform2d/simform2d.html">simform2d</a> | <a 
href="../rigidtform2d/rigidtform2d.html">rigidtform2d</a> | <a 
href="../fitgeotform2d/fitgeotform2d.html">fitgeotform2d</a> | <a 
href="../transltform2d/transltform2d.html">transltform2d</a> | <a 
href="../projtform2d/projtform2d.html">projtform2d</a> | <a 
href="../imwarp/imwarp.html">imwarp</a>
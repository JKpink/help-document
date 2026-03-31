## projtform2d
二维投影几何变换

## 简介
[`tform = projtform2d`](#function1)  
[`tform = projtform2d(projMat)`](#function2)  
 
## 用法 
<a id="function1"></a> [tform](#P1) = projtform2d 创建一个执行恒等变换的 `projtform2d` 对象。  
<a id="function2"></a> [tform](#P1) = projtform2d([projMat](#Q1)) 从有效的二维投影变换矩阵 `projMat` 创建一个 `projtform2d` 对象。

## 参数说明
### 输入参数  
**<a id="Q1"></a> projMat — 二维正向投影变换**  
3 × 3 单位矩阵 (默认) | 3 × 3 数值矩阵  
  
二维正向投影变换矩阵，指定为 3 × 3 数值矩阵。  
此参数用于设置 [A](#Q2) 属性。

**数据类型：** `double` | `single`  
  
### 输出参数  
**<a id="P1"></a> tform — 二维投影几何变换**   
`projtform2d` 对象  

二维投影几何变换，指定为 `projtform2d` 对象。
## 属性  
**<a id="Q2"></a> A - 正向二维投影变换**  
3 × 3 单位矩阵(默认) | 3 × 3 数值矩阵  
  
正向二维投影变换，指定为 3 × 3 数值矩阵。 `A` 的默认值为单位矩阵。  

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
href="../transltform2d/transltform2d.html">transltform2d</a> | <a 
href="../imwarp/imwarp.html">imwarp</a> 
  

## transformPointsInverse
应用逆几何变换

## 简介
[`[u, v] = transformPointsInverse(tform, x, y)`](#function1)  
[`[u, v, w] = transformPointsInverse(tform, x, y, z)`](#function2)  
[`U = transformPointsInverse(tform, X)`](#function3)

## 用法 
<a id="function1"></a> [[u](#P1), [v](#P2)] = transformPointsInverse([tform](#Q1), [x](#Q2), [y](#Q3)) 将二维几何变换 `tform` 的逆变换应用于由坐标 `u` 和 `v` 指定的点。    
<a id="function2"></a> [[u](#P1), [v](#P2), [w](#P3)] = transformPointsInverse([tform](#Q1), [x](#Q2), [y](#Q3), [z](#Q4)) 将三维几何变换 `tform` 的逆变换应用于由坐标 `u`、`v` 和 `w` 指定的点。   
<a id="function3"></a> [U](#P4) = transformPointsInverse([tform](#Q1), [X](#Q5))将 `tform` 的逆变换应用于输入坐标矩阵 `X`，并返回坐标矩阵 `U`。`transformPointsForward` 将第 k 个点 X(k, :) 映射到点 U(k, :)。

## 参数说明
### 输入参数
**<a id="Q1"></a> tform — 几何变换**  
几何变换对象  

几何变换，指定为下表所列的几何变换对象之一：

|几何变换对象|描述|
|:---|:---|
|二维线性几何变换|
|<a href="../transltform2d/transltform2d.html">transltform2d</a>  </a>|平移变换|
|<a href="../rigidtform2d/rigidtform2d.html">rigidtform2d</a>  </a>|刚性变换：平移和旋转|
|<a href="../simtform2d/simtform2d.html">simtform2d</a>  </a>|相似变换：平移、旋转和各向同性缩放|
|<a href="../affinetform2d/affinetform2d.html">affinetform2d</a>  </a>|仿射变换：平移、旋转、各向异性缩放、反射和剪切|
|<a href="../projtform2d/projtform2d.html">projtform2d</a>  </a>|投影变换|
|三维线性几何变换|
|<a href="../transltform3d/transltform3d.html">transltform3d</a>  </a>|平移变换|
|<a href="../rigidtform3d/rigidtform3d.html">rigidtform3d</a>  </a>|刚性变换：平移和旋转|
|<a href="../simtform3d/simtform3d.html">simtform3d</a>  </a>|相似变换：平移、旋转和各向同性缩放|
|<a href="../affinetform3d/affinetform2、3d.html">affinetform3d</a>  </a>|仿射变换：平移、旋转、各向异性缩放、反射和剪切|
|非线性几何变换|
|<a href="../geometricTransform2d/geometricTransform2d.html">geometricTransform2d</a>  </a>|使用逐点映射函数的自定义二维几何变换|
|<a href="../geometricTransform3d/geometricTransform3d.html">geometricTransform3d</a>  </a>|使用逐点映射函数的自定义三维几何变换|

**<a id="Q2"></a> x — 要变换点的 x 坐标**  
m × n 或 m × n × p 的数值数组  

要变换点的 `x` 坐标，指定为 m × n 或 m × n × p 数值数组。`x` 的维度数与 [tform](#Q1) 的维数相同。

**数据类型：** `single` | `double`

**<a id="Q3"></a> y — 要变换点的 y 坐标**  
m × n 或 m × n × p 的数值数组  

要变换点的 `y` 坐标，指定为 m × n 或 m × n × p 数值数组。`y` 的大小必须与 [x](#Q2) 的大小相同。

**数据类型：** `single` | `double`

**<a id="Q4"></a> z — 要变换点的 z 坐标**  
m × n × p 数值数组  

要变换点的 `z` 坐标，指定为 m × n × p 数值数组。当 [tform](#Q1) 为三维几何变换时，才会使用 `z`。`z` 的大小必须与 [x](#Q2) 的大小相同。

**数据类型：** `single` | `double`

**<a id="Q5"></a> X — 要变换点坐标**  
1 × 2 或 1 × 3 数值数组  
  
要变换点的坐标，指定为 1 × 2 或 1 × 3 数值数组。`X` 的列数与 [tform](#Q1) 的维数相同。  
第一列存储每个要变换点的 `x` 坐标，第二列存储要变换点的 `y` 坐标。若 `tform` 为三维几何变换，则 `X` 为 1 × 3 数组，且第三列存储要变换点的 `z` 坐标。  
  
**数据类型：** `single` | `double`

### 输出参数
**<a id="P1"></a> u — 变换后点的 x 坐标**  
m × n 或 m × n × p 的数值数组  

变换后点的 `x` 坐标，指定为 m × n 或 m × n × p 数值数组。`u` 的维度数与 [tform](#Q1) 的维数相同。

**数据类型：** `single` | `double`

**<a id="P2"></a> v — 变换后点的 y 坐标**  
m × n 或 m × n × p 的数值数组  

变换后点的 `y` 坐标，指定为 m × n 或 m × n × p 数值数组。`v` 的大小必须与 [u](#P1) 的大小相同。

**数据类型：** `single` | `double`

**<a id="P3"></a> w — 变换后点的 z 坐标**  
m × n × p 数值数组  

变换后点的 `z` 坐标，指定为 m × n × p 数值数组。`w` 的大小必须与 [u](#P1) 的大小相同。 

**数据类型：** `single` | `double`

**<a id="P4"></a> U — 变换后点的坐标**  
数值数组  
  
变换后点的坐标，指定为数值数组。`U` 的尺寸必须与 [X](#Q2) 的大小相同。  
第一列存储每个变换后点的 `x` 坐标，第二列存储变换后点的 `y` 坐标。若 [tform](#Q1) 为三维几何变换，则数组包含第三列，存储变换后点的 `z` 坐标。


**数据类型：** `single` | `double`

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../transformPointsForward/transformPointsForward.html">transformPointsForward</a> | <a
href="../imwarp/imwarp.html">imwarp </a>
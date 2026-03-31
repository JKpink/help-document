## transformPointsForward
应用正向几何变换

## 简介
[`[x, y] = transformPointsForward(tform, u, v)`](#function1)  
[`[x, y, z] = transformPointsForward(tform, u, v, w)`](#function2)   
[`X = transformPointsForward(tform, U)`](#function3)

## 用法 
<a id="function1"></a> [[x](#P1), [y](#P2)] = transformPointsForward([tform](#Q1), [u](#Q2), [v](#Q3)) 将二维几何变换 `tform` 的正向变换应用于由坐标 `u` 和 `v` 指定的点。  
<a id="function2"></a> [[x](#P1), [y](#P2), [z](#P3)] = transformPointsForward([tform](#Q1), [u](#Q2), [v](#Q3), [w](#Q4)) 将三维几何变换 `tform` 的正向变换应用于由坐标 `u`、`v` 和 `w` 指定的点。  
<a id="function3"></a> [X](#P4) = transformPointsForward([tform](#Q1), [U](#Q5)) 将 `tform` 的正向变换应用于输入坐标矩阵 `U`，并返回坐标矩阵 `X`。`transformPointsForward` 将第 k 个点 U(k, :) 映射到点 X(k, :)。
## 参数说明
### 输入参数
**<a id="Q1"></a> tform — 几何变换**   
几何变换对象 
 
几何变换，指定为下表所列的几何变换对象之一：
  
|几何变换对象|描述|
|:-------|:-------|
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

**<a id="Q2"></a> u — 要变换点的 x 坐标**  
m × n 或 m × n × p 的数值数组

要变换点的 `x` 坐标，指定为 m × n 或 m × n × p 的数值数组。`u` 的维数与 [tform](#Q1) 的维数相同。

**数据类型：** `single` | `double`  

**<a id="Q3"></a> v — 要变换点的 y 坐标**  
m × n 或 m × n × p 数值数组  

要变换点的 `y` 坐标，指定为 m × n 或 m × n × p 数值数组。`v` 的大小必须与 [u](#Q2) 的大小相同。

**数据类型：** `single` | `double`  

**<a id="Q4"></a> w — 要变换点的 z 坐标**  
m × n × p 的数值数组  

要变换点的 `z` 坐标，指定为 m × n × p 的数值数组。当 [tform](#Q1) 为三维几何变换时，才会使用 `w`。`w` 的大小必须与 [u](#Q2) 的大小相同。

**数据类型：** `single` | `double`

**<a id="Q5"></a> U — 要变换点的坐标**  
1 × 2 或 1 × 3 的数值数组   

要变换点的坐标，指定为 1 × 2 或 1 × 3 的数值数组。`U` 的列数与 [tform](#Q1) 的维数相同。  
第一列存储每个要变换点的 `x` 坐标，第二列存储要变换点的 `y` 坐标。若 `tform` 为三维几何变换，则 `U` 为 1 × 3 数组，且第三列存储要变换点的 `z` 坐标。

**数据类型：** `single` | `double`

### 输出参数
**<a id="P1"></a> x — 变换后点的 x 坐标**  
m × n 或 m × n × p 数值数组  

变换后点的 `x` 坐标，指定为 m × n 或 m × n × p 数值数组。`x` 的维数与 [tform](#Q1) 的维数相同。

**数据类型：** `single` | `double`

**<a id="P2"></a> y — 变换后点的 y 坐标**  
m × n 或 m × n × p 数值数组  

变换后点的 `y` 坐标，指定为 m × n 或 m × n × p 数值数组。`y` 的大小必须与 [x](#P1) 的大小相同。

**数据类型：** `single` | `double`  

**<a id="P3"></a> z — 变换后点的 z 坐标**  
m × n × p 数值数组  
变换后点的 `z` 坐标，指定为 m × n × p 数值数组。`z` 的大小必须与 [x](#P1) 的大小相同。

**数据类型：** `single` | `double`

**<a id="P4"></a> X — 变换后点的坐标**  
数值数组

变换后点的坐标，指定为数值数组。`X` 的大小与 [U](#Q5) 的大小相同。  
第一列存储每个变换后点的 `x` 坐标，第二列存储变换后点的 `y` 坐标。若 [tform](#Q1) 为三维几何变换，则数组包含第三列，存储变换后点的 `z` 坐标。

**数据类型：** `single` | `double`

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../transformPointsInverse/transformPointsInverse.html">transformPointsInverse</a> | <a
href="../imwarp/imwarp.html">imwarp</a>  </a>
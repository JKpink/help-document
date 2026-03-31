## geometricTransform2d
二维几何变换对象

## 简介
[ `tform = geometricTransform2d(inverseFcn)`](#function1)  
[ `tform = geometricTransform2d(inverseFcn, forwardFcn)`](#function2)  
## 用法
<a id="function1"></a>
tform = geometricTransform2d([inverseFcn](#Q1)) 创建一个 `geometricTransform2d` 对象并设置逆映射 `inverseFcn` 属性。  
tform = geometricTransform2d([inverseFcn](#Q1), [forwardFcn](#Q2)) 添加了正向映射 `forwardFcn` 属性。  

## 参数说明
### 输入参数
**<a id="Q1"></a> inverseFcn — 逆映射函数**  
函数句柄

逆映射函数，指定为函数句柄。该函数的输入与输出必须遵循统一的数据结构：以 n×2 矩阵表示 n 个二维点的坐标集合，其中第一列为 `x` 坐标，第二列为 `y` 坐标。  
**示例：** ifcn = @(xy) [xy(:,1).^2, sqrt(xy(:,2))];

**<a id="Q2"></a> inverseFcn — 正映射函数**  
函数句柄

正映射函数，指定为函数句柄。该函数的输入与输出必须遵循统一的数据结构：以 n×2 矩阵表示 n 个二维点的坐标集合，其中第一列为 `x` 坐标，第二列为 `y` 坐标。 
**示例：** ffcn = @(xy) [sqrt(xy(:,1)),(xy(:,2).^2)];

### 输出参数
**<a id="P1"></a> tform — 二维几何变换对象**  
`geometricTransform2d` 对象

二维几何变换对象，返回 `geometricTransform2d` 对象。`geometricTransform2d` 对象使用逐点映射函数定义自定义的二维几何转换。

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../imwarp/imwarp.html">imwarp</a> | <a
href="../affinetform2d/affinetform2d.html">affinetform2d</a> | <a 
href="../simtform2d/simtform2d.html">simtform2d</a> | <a 
href="../rigidtform2d/rigidtform2d.html">rigidtform2d</a> | <a 
href="../transltform2d/transltform2d.html">transltform2d </a> | <a 
href="../pojtform2d/pojtform2d.html">pojtform2d</a> | <a 
href="../geometricTransform3d/geometricTransform3d.html">geometricTransform3d </a>
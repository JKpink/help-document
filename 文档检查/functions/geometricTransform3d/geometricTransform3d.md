## geometricTransform3d
三维几何变换对象

## 简介
[ `tform = geometricTransform3d(inverseFcn)`](#function1)  
[ `tform = geometricTransform3d(inverseFcn, forwardFcn)`](#function2)  
## 用法
<a id="function1"></a>
[tform](#P1) = geometricTransform3d([inverseFcn](#Q1)) 创建一个 `geometricTransform3d` 对象并设置逆映射 `inverseFcn` 属性。  
[tform](#P1) = geometricTransform3d([inverseFcn](#Q1), [forwardFcn](#Q2)) 添加了正向映射 `forwardFcn` 属性。  

## 参数说明
### 输入参数
**<a id="Q1"></a> inverseFcn — 逆映射函数**  
函数句柄

逆映射函数，指定为函数句柄。该函数的输入与输出必须遵循统一的数据结构：以 n×3 矩阵表示 n 个三维点的坐标集合，其中第一列为 `x` 坐标，第二列为 `y` 坐标，第三列为 `z` 坐标。  
**示例：** ifcn = @(xyz) [xyz(:,1).^2,xyz(:,2).^2,xyz(:,3).^2];

**<a id="Q2"></a> inverseFcn — 正映射函数**  
函数句柄

正映射函数，指定为函数句柄。该函数的输入与输出必须遵循统一的数据结构：以 n×3 矩阵表示 n 个三维点的坐标集合，其中第一列为 `x` 坐标，第二列为 `y` 坐标，第三列为 `z` 坐标。  
**示例：** ffcn = @(xyz) [sqrt(xyz(:,1)),sqrt(xyz(:,2)),sqrt(xyz(:,3))];

### 输出参数
**<a id="P1"></a> tform — 三维几何变换对象**  
`geometricTransform3d` 对象

三维几何变换对象，返回 `geometricTransform3d` 对象。`geometricTransform3d` 对象使用逐点映射函数定义自定义的三维几何转换。

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../imwarp/imwarp.html">imwarp</a> | <a
href="../affinetform3d/affinetform3d.html">affinetform3d</a> | <a 
href="../simtform3d/simtform3d.html">simtform3d</a> | <a 
href="../rigidtform3d/rigidtform3d.html">rigidtform3d</a> | <a 
href="../transltform3d/transltform3d.html">transltform3d</a> | <a 
href="../geometricTransform2d/geometricTransform2d.html">geometricTransform2d</a>
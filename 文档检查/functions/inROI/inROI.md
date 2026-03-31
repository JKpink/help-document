## inROI
查询点是否位于 ROI 中

## 简介
[`tf = inROI(ROI, x, y)`](#function1)

## 用法
<a id="function1"></a>
[tf](#Q4) = inROI([ROI](#Q1), [x](#Q2), [y](#Q3)) 返回一个逻辑数组 `tf`，用于指示坐标为 (x, y) 的点是否位于二维感兴趣区域的内部（或外部）。

## 参数说明
### 输入参数
**<a id="Q1"></a> ROI — 感兴趣区域**  
ROI 对象

感兴趣区域，指定为以下类型之一的 ROI 对象：  
| Circle | Polygon |
| :- | :- |
| Cuboid | Rectangle |
| Ellipse | &nbsp; |

**<a id="Q2"></a> x — 查询点的 X 坐标**  
数字标量 | 数值向量

查询点的 X 坐标，指定为数值标量或数值向量。

**<a id="Q3"></a> y — 查询点的 Y 坐标**  
数字标量 | 数值向量

查询点的 Y 坐标，指定为数值标量或数值向量。

### 输出参数
**<a id="Q4"></a> tf — 查询点的状态**  
逻辑数组

查询点的状态，以逻辑数组形式返回。该数组与输入数组 `x` 和 `y` 的长度相同。逻辑数组中设置为 true 的元素表示相应的查询点在 ROI 内部。设置为 false 的元素表示该点不在 ROI 内部。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出。

## 相关主题
<a href="../createMask /createMask .html">createMask </a> | <a 
href="../drawcircle/drawcircle.html">drawcircle</a> | <a 
href="../drawellipse/drawellipse.html">drawellipse</a> | <a 
href="../drawpolygon/drawpolygon.html">drawpolygon</a> | <a 
href="../drawrectangle/drawrectangle.html">drawrectangle</a> 
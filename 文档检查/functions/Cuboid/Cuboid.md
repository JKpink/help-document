## Cuboid
3 维长方体区域的空间范围

## 简介
[ `c = Cuboid(XLimits, YLimits, ZLimits)`](#function1)  
## 用法
<a id="function1"></a>
[c](#P1) = Cuboid([XLimits](#Q1), [YLimits](#Q2), [ZLimits](#Q3)) 创建一个 `Cuboid` 对象并设置 `XLimits`、`YLimits` 和 `ZLimits` 属性。  
 

## 参数说明
### 输入参数
**<a id="Q1"></a> XLimits — 裁剪窗口沿 x 轴的最小和最大限制**  
2 元数值向量

裁剪窗口沿 `x` 轴的最小和最大限制，指定为的 2 元数值向量，形式为 [min max]，其中 max 大于 min。   

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `uint64` | `int8` | `int16` | `int32` | `int64` 

**<a id="Q2"></a> YLimits — 裁剪窗口沿 y 轴的最小和最大限制**  
2 元数值向量

裁剪窗口沿 `y` 轴的最小和最大限制，指定为的 2 元数值向量，形式为 [min max]，其中 max 大于 min。   

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `uint64` | `int8` | `int16` | `int32` | `int64`

**<a id="Q3"></a> ZLimits — 裁剪窗口沿 z 轴的最小和最大限制**  
2 元数值向量

裁剪窗口沿 `z` 轴的最小和最大限制，指定为的 2 元数值向量，形式为 [min max]，其中 max 大于 min。 

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `uint64` | `int8` | `int16` | `int32` | `int64`


## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../imcrop3/imcrop3.html">imcrop3</a> | <a
href="../centerCropWindow3d/centerCropWindow3d.html">centerCropWindow3d</a> | <a
href="../randomCropWindow3d/randomCropWindow3d.html">randomCropWindow3d</a> | <a
href="../Rectangle/Rectangle.html">Rectangle</a>
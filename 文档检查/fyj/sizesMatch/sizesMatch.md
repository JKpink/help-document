## sizesMatch
确定空间参考对象和图像是否大小兼容

## 简介
[`tf = sizesMatch(R, A)`](#function1)

## 用法 
<a id="function1"></a> [tf](#P1) = sizesMatch([R](#Q1), [A](#Q2)) 如果图像 `A` 的大小与空间参考对象 `R` 的 `ImageSize` 属性一致，则返回 `true` 。

## 参数说明
### 输入参数
**<a id="Q1"></a> R — 空间参考对象**  
`imref2d` 或 `imref3d` 对象  
  
空间参考对象，指定为 <a href="../imref2d/imref2d.html">imref2d</a>  </a> 或 <a href="../imref3d/imref3d.html">imref3d</a>  </a> 对象。

**<a id="Q2"></a> A — 输入图像**  
数值 m × n 或 m × n × p 数组  
  
输入图像，指定为 m × n 或 m × n × p 数组。  
  
**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数
**<a id="P1"></a> tf — 大小兼容性标志**  
逻辑标量  

大小兼容性标志，指定为逻辑标量。若图像 [A](#Q2) 的大小与空间参考对象 [R](#Q1) 一致，则 `tf` 为 `true`。  
当 `R` 为 :  
  
- <a href="../imref2d/imref2d.html">imref2d</a>  </a> 空间参考对象 : 当 ImageSize == [size(A, 1) size(A, 2)] 时，`tf` 返回 `true`。  
  注意：`A` 的维度无需与 `imref2d`  空间参考对象的维度匹配。例如，RGB图像可与 `imref2d` 对象兼容，此时 `sizesMatch` 会忽略图像的第三维度。  
- <a href="../imref3d/imref3d.html">imref3d</a>  </a> 空间参考对象 : 当 ImageSize == size(A) 时， `tf` 返回 `true` ，且 `A` 必须为三维数组。  

**数据类型：** `logical`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出


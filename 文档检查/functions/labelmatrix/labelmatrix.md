## labelmatrix  
由 bwconncomp 结构创建 label 矩阵

## 简介  
[ `L = labelmatrix(CC)`](#function1)

## 用法  
标签矩阵为二值图像中的对象或连通分量分配唯一的整数值，使用标签矩阵来可视化不同的对象或连通分量。  
<a id="function1"></a>
[L](#Q1) = labelmatrix([CC](#Q2)) 从连通组件结构 [`CC`](#Q2) 创建标签矩阵 [`L`](#Q1)。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>CC — 连通分量**  
结构

连通分量，您可以使用 <a href="../bwconncomp/bwconncomp.html">`bwconncomp`</a> 函数获取连通分量结构，指定为具有四个字段的结构：

| **字段** | **描述** |
|:-|:-|
| Connectivity | 连通分量（对象）的连通性 |
| ImageSize | 二值图像的大小 |
| NumObjects |  二值图像中连通分量（对象）的数量 |
| PixelIdxList |  1xNumObjects 的单元数组，其中单元数组中的第 k 个元素是一个向量，包含第 k 个对象中像素的线性索引。 |

### 输出参数  
**<a id="Q1"></a>L — 标签矩阵**  
非负整数矩阵

连通区域的标签矩阵，返回为非负整数的矩阵。标记为 0 的像素是背景；标记为 1 的像素组成一个对象；标记为 2 的像素组成第二个对象；依此类推。
`L` 的大小由 CC.ImageSize 字段的值决定，`L` 的类取决于连续区域的数量，`labelmatrix` 使用可以表示对象数量 (CC.NumObjects) 的最小数据类型，如表中所示：

| **数据类型** | **范围** |
|:-|:-|
| uint8 | CC.NumObjects ≤ 255 |
| uint16 | 256 ≤ CC.NumObjects ≤ 65535 |
| uint32 |  65536 ≤ CC.NumObjects ≤ 2^32 – 1 |
| double |  CC.NumObjects ≥ 2^32 |

**数据类型：** `double` | `uint8` | `uint16` | `uint32` 

## 版本历史  
在北太天元图像处理工具箱 V1.1 推出

## 相关主题  
<a href="../bwconncomp/bwconncomp.html">bwconncomp</a> | <a 
href="../label2rgb/label2rgb.html">label2rgb</a> | <a 
href="../regionprops/regionprops.html">regionprops</a> 


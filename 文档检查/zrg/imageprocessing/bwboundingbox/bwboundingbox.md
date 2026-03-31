## bwboundingbox 
包含二值图像区域的最小外接框的位置和大小

## 简介
[ `Stats = bwboundingbox(BW)`](#function1)

## 用法
<a id="function1"></a>
[Stats](#Q1) = bwboundingbox([BW](#Q2)) 返回 `n×(2×m)` 矩阵，其中 `n` 为图像中前景目标的数量，`m` 为输入图像的维度数；每行对应一个目标的全维度外接框坐标信息，每2列对应一个图像维度的最小（min）和最大（max）坐标，2D图像下固定为 `n×4` 矩阵，列顺序为 `[minX, maxX, minY, maxY]`。

## 参数说明
### 输入参数
**<a id="Q2"></a>BW — 二值图像**  
逻辑数组

二值图像，指定为任意维度的逻辑数组

**数据类型：** `logical`

### 输出参数
**<a id="Q1"></a>Stats — 外接框坐标**  
n×(2×m) 矩阵 

测量值，返回一个 n×(2×m) 矩阵。每行对应一个前景目标的全维度外接框参数，列顺序：  
- 第1列：x维度（横向）最小坐标（minX）
- 第2列：x维度（横向）最大坐标（maxX）
- 第3列：y维度（纵向）最小坐标（minY）
- 第4列：y维度（纵向）最大坐标（maxY） 

**数据类型：** `int32`


## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../bwconncomp/bwconncomp.html">bwconncomp</a> | <a href="../bwconvhull/bwconvhull.html">bwconvhull</a> | <a href="../regionprops/regionprops.html">regionprops</a>
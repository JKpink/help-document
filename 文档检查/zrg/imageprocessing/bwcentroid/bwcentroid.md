## bwcentroid 
二值图像区域的质心

## 简介
[ `Stats = bwcentroid(BW)`](#function1)

## 用法
<a id="function1"></a>
[Stats](#Q1) = bwcentroid([BW](#Q2)) 返回 n×1 向量，每行对应一个目标的 x 方向质心坐标，n 为图像中目标的数量；元素值即为该目标在 x 轴上的质心位置。

## 参数说明
### 输入参数
**<a id="Q2"></a>BW — 二值图像**  
逻辑数组

二值图像，指定为任意维度的逻辑数组

**数据类型：** `logical`

### 输出参数
**<a id="Q1"></a>Stats — 外接框坐标**  
n×1 向量 

测量值，返回一个 n×1 向量。元素为各目标在 x 方向的质心坐标。

**数据类型**:`double`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../bwconncomp/bwconncomp.html">bwconncomp</a> | <a href="../bwconvhull/bwconvhull.html">bwconvhull</a> | <a href="../regionprops/regionprops.html">regionprops</a>
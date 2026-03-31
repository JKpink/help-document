## qtblk

可视化四叉树分解

## 简介

[`mask = qtblk(qt, size)`](#function1)

## 用法
<a id="function1"></a>
[mask](#Q3) = qtblk([qt](#Q1), [size](#Q2)) 将 `qtgetblk` 得到的块列表 `qt`（n×3 矩阵，每行 `[col row L]`）绘制成二值图像 `mask`：

- 对每个块固定列 `col`，在行区间 `[row, row+L-1]` 画垂直线；
- 固定行 `row`，在列区间 `[col, col+L-1]` 画水平线；
- 返回与原始图像同尺寸的 `logical` 矩阵，十字线位置为 `true`。

&gt; 注：若块超出图像边界，越界部分被静默截断。

## 参数说明

### 输入参数

**<a id="Q1"></a>qt — 块列表**
n×3 矩阵

每行 `[col row L]` 给出左上角列、行坐标及边长。

**数据类型：** `int32`

**<a id="Q2"></a>size — 输出图像尺寸**
二元向量

二元向量 `[H W]`，指定生成图的高和宽。

### 输出参数

**<a id="Q3"></a>mask — 十字线掩膜** 
逻辑矩阵

返回 `H×W` 矩阵，十字线像素为 `true`，其余为 `false`。

**数据类型：** `logical` 

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../qtdecomp/qtdecomp.html">qtdecomp</a> | <a href="../qtgetblk/qtgetblk.html">qtgetblk</a>
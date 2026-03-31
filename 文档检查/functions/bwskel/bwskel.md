## bwskel 
提取骨架

## 简介
[`B = bwskel(A)`](#function1)  
[`B = bwskel(V)`](#function2)

## 用法
<a id="function1"></a>
[B](#Q3) = bwskel([A](#Q1))  将二维二值图像 `A` 中的所有对象缩减为 1 像素宽的曲线，同时保持图像的基本结构不变。这一过程称为骨架化，它提取对象的中心线，同时保留其拓扑结构和欧拉数。`bwskel` 使用中轴变换[[1]](#R1)。
<a id="function2"></a>
[B](#Q3)  = bwskel([V](#Q2))  返回三维二值体积 `V` 的骨架。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 二进制映像**  
二维逻辑矩阵

二进制图像，指定为二维逻辑矩阵。

**数据类型:** `logical`

**<a id="Q2"></a> V — 3-D 二进制卷**  
3-D 逻辑阵列

3-D 二进制卷，指定为 3-D 逻辑数组。

**数据类型:** `logical`

### 输出参数
**<a id="Q3"></a> B — 骨架化图像或体积** 
二维逻辑矩阵 | 三维逻辑数组

骨架化图像或体积，作为与输入图像或卷大小相同的二维逻辑矩阵或三维逻辑数组返回。

## 参考文献
<a id="R1"></a>   

[1] Lee T. C, Kashyap R L,  Chu C N. Building skeleton models via 3-D medial surface axis thinning algorithms. CVGIP: Graphical Models and Image Processing, 56(6), 462–478,  1994. 

## 版本历史 
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../bwmorph/bwmorph.html">bwmorph</a> 




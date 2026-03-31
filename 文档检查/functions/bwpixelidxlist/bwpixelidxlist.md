## bwpixelidxlist  
二值图像区域中像素的线性索引

## 简介  
[ `PixelIdxList = bwpixelidxlist(BW)`](#function1)

## 用法  
<a id="function1"></a>
[PixelIdxList](#Q1) = bwpixelidxlist([BW](#Q2)) 

对输入的任意维度二值图像 [`BW`](#Q2) ，先按 “n 维全连通规则” 识别所有独立连通区域（2 维为 8 邻域、3 维为 26 邻域、n 维同理）；再按 “从最高维到最低维” 的顺序计算每个连通区域内像素的线性索引（索引从 0 开始）；最终返回多个一维向量，每个向量对应一个连通区域，向量内存储该区域所有像素的线性索引。

有如下核心规则：

- 连通性判断：2 维图像采用 8 邻域（上下左右 + 对角线）识别连通区域，3 维图像采用 26 邻域（三维空间全邻域），n 维图像沿用 “n 维全连通” 逻辑；
- 线性索引计数顺序：对 n 维数组 I(dim1, dim2, ..., dimn)，先从第 n 维（最高维）计数，再依次向低维度递减；
- 索引起始值：所有线性索引从 0 开始。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 二值图像**  
数值数组 | 逻辑数组

- 支持任意维度的逻辑数组或数值数组；
- 若为逻辑数组，true 表示目标像素，false 表示背景像素；
- 若为数值数组，非零元素视为目标像素，零元素视为背景像素。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数  
**<a id="Q1"></a>PixelIdxList — 连通区域的线性索引集合**  
一维向量组

二值图像区域中像素的线性索引，每个向量对应一个连通区域，向量内存储该区域所有像素的线性索引。

**数据类型：** `cell`（元胞数组），内部向量为 `int32`

##版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../bwconncomp/bwconncomp.html">bwconncomp</a> | <a 
href="../bwpixellist/bwpixellist.html">bwpixellist</a> | <a 
href="../bwsolidity/bwsolidity.html">bwsolidity</a> | <a 
href="../regionprops/regionprops.html">regionprops</a>
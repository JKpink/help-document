## cmap2gray
将 RGB 颜色表转换为灰度颜色表

## 简介
[`newmap = cmap2gray(map)`](#function1)

## 用法
<a id="function1"></a>
[newmap](#P1) = cmap2gray([map](#Q1)) 将 RGB 颜色表 `map` 转换为等效的灰度颜色表 `newmap`。

## 参数说明
### 输入参数
**<a id="Q1"></a> map — RGB 颜色表**  
c×3 数值矩阵

RGB 颜色表，指定为由范围 [0, 1] 内的值组成的 c×3 数值矩阵。`map` 的每行都是一个三元素 RGB，指定颜色表的单种颜色的红、绿和蓝分量。

**数据类型：** `double`

### 输出参数
**<a id="P1"></a> newmap — 灰度颜色表**  
c×3 数值矩阵

灰度颜色表，返回为由范围 [0, 1] 内的值组成的 c×3 数值矩阵。`newmap` 的三列是相同的，因此每行都指定一个灰度值。

**数据类型：** `double`

## 算法
`cmap2gray` 通过计算 R、G 和 B 分量的加权和，将 RGB 值转换为灰度值：  
0.298936021293775 \* R + 0.587043074451121 \* G + 0.114020904255103 \* B 

在舍入到小数点后 3 位之后，`cmap2gray` 函数中用来计算灰度值的系数与 Rec.ITU-R BT.601-7 中用来计算亮度 (E'y) 的系数相同。Rec.ITU-R BT.601-7 使用以下公式计算 E'y：  
0.299 \* R + 0.587 \* G + 0.114 \* B

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../im2gray/im2gray.html">im2gray</a> | <a
href="../rgb2gray/rgb2gray.html">rgb2gray</a> | <a 
href="../rgb2ind/rgb2ind.html">rgb2ind</a> | <a 
href="../rgb2lightness/rgb2lightness.html">rgb2lightness </a>

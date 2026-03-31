## ind2gray
将索引图像转换为灰度图像

## 简介
[`I = ind2gray(X, cmap)`](#function1)

## 用法
<a id="function1"></a>
[I](#P1) = ind2gray([X](#Q1), [cmap](#Q3)) 将关联颜色映射表 `cmap` 的索引图像 `X` 转换为灰度图像 `I`。`ind2gray` 函数从输入图像中删除色调及饱和度信息，同时保持亮度。

## 参数说明
### 输入参数
**<a id="Q1"></a> X — 索引图像**  
数值数组

索引图像，指定为任意大小和维度的数值数组。

**数据类型：** `single` | `double` | `uint8` | `uint16`

**<a id="Q2"></a> cmap — 颜色映射表**  
c×3 数值矩阵

与索引图像 [X](#Q1) 相关联的颜色映射表，指定为在 [0, 1] 区间内取值组成的 c×3 数值矩阵形式返回。cmap 每一行对应一组 RGB 三元色值，用于指定该颜色映射表中一种颜色的红、绿、蓝分量。

**数据类型：** `double`

### 输出参数
**<a id="P1"></a> I — 灰度图像**  
数值数组

灰度图像，指定为数值数组。`I` 与 [X](#Q1) 具有相同的大小、维度。

**数据类型：** `double`

## 算法
ind2gray 使用 <a href="../rgb2ntsc/rgb2ntsc.html">rgb2ntsc</a> 将颜色映射表转换为 NTSC 坐标，并将色调及饱和度分量（I 和 Q）设置为零，从而创建一个灰度颜色映射表。然后，`ind2gray` 将图像 `X` 中的索引替换为灰度颜色映射表中对应的灰度值。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../gray2ind/gray2ind.html">gray2ind</a> | <a
href="../imshow/imshow.html">imshow</a> | <a 
href="../mat2gray/mat2gray.html">mat2gray</a> | <a 
href="../im2gray/im2gray.html">im2gray</a> | <a 
href="../rgb2ntsc/rgb2ntsc.html">rgb2ntsc </a>

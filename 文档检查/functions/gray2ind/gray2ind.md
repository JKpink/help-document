## gray2ind
将灰度或二值图像转换为索引图像

## 简介
[`[X, cmap] = gray2ind(I, c)`](#function1)  
[`[X, cmap] = gray2ind(BW, c)`](#function2)  

## 用法
<a id="function1"></a>
[[X](#P1), [cmap](#P2)] = gray2ind([I](#Q1), [c](#Q3)) 将灰度图像 `I` 转换为索引图像 `X`，并生成包含 c 个灰度级的灰度颜色映射表 `cmap`；若未指定 c，默认使用 64 个灰度级。  
<a id="function2"></a>
[[X](#P1), [cmap](#P2)] = gray2ind([BW](#Q2), [c](#Q3)) 将二值图像 `BW` 转换为索引图像 `X`，生成的颜色映射表 `cmap` 包含 c 个灰度级。  

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 灰度图像**  
数值数组

灰度图像，指定为任意维度的数值数组。`gray2ind` 需要数据类型为 `double` 和 `single` 的图像的值在 [0, 1] 的范围内。如果 I 的值超出范围 [0, 1]，则可以使用 <a href="../rescale/rescale.html">rescale</a> 函数将值重新缩放到需要的范围。

**数据类型：** `single` | `double` | `int16` | `uint8` | `uint16`

**<a id="Q2"></a> BW — 二值图像**  
逻辑数组

二值图像，指定为任意维度的逻辑数组。

**数据类型：** `logical`

**<a id="Q3"></a> c — 颜色映射表的灰度级数量**  
c×3 数值矩阵

颜色表的颜色数量，指定为 1 到 65536 之间的正整数。

### 输出参数
**<a id="P1"></a> X — 索引图像**  
数值数组

索引图像，以与输入灰度或二值图像维度相同的数值数组形式返回。

**数据类型：** `uint16`

**<a id="P2"></a> cmap — 灰度颜色映射表**  
c×3 数值矩阵

与索引图像 [X](#P1) 相关联的颜色映射表，以范围 [0, 1] 内的值组成的 c×3 数值矩阵形式返回。每行是一个三元素 RGB 三元组，指定颜色表的单个颜色的红、绿和蓝分量。等效于调用 <a href="../gray/gray.html">gray</a>([c](#Q3)) 生成的灰度颜色映射表。

**数据类型：** `double`

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../grayslice/grayslice.html">grayslice</a> | <a
href="../ind2gray/ind2gray.html">ind2gray</a> | <a 
href="../mat2gray/mat2gray.html">mat2gray </a>

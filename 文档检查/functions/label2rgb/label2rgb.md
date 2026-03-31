## label2rgb
将 label 矩阵转换为 RGB 图像

## 简介
[`RGB = label2rgb(L)`](#function1)  
[`RGB = label2rgb(L, cmap)`](#function2)  
[`RGB = label2rgb(L, cmap, zerocolor)`](#function3)  

## 用法
<a id="function1"></a>
[RGB](#P1) = label2rgb([L](#Q1)) 将标签图像转换为 RGB 图像，以便可视化标记区域。`label2rgb` 函数根据标签矩阵中的对象数量来确定分配给每个对象的颜色。`label2rgb` 函数从整个颜色映射范围中选取颜色。  
<a id="function2"></a>
[RGB](#P1) = label2rgb([L](#Q1), [cmap](#Q2)) 指定在 RGB 图像中使用的颜色映射表 `cmap`。  
<a id="function3"></a>
[RGB](#P1) = label2rgb([L](#Q1), [cmap](#Q2), [zerocolor](#Q3)) 指定背景元素（标记为0的像素）的 RGB 颜色。  

## 参数说明
### 输入参数
**<a id="Q1"></a> L — 非负整数的标签图像**  
非负整数矩阵 | 逻辑矩阵

连续区域的标签图像，指定为以下选项之一。  

- 非负整数的矩阵。标记为 0 的像素是背景。标记为 1 的像素代表一个对象；标记为 2 的像素代表第二个对象，以此类推。可以从 <a href="../Watershed/Watershed.html">Watershed</a> 或 <a href="../LabelMatrix/LabelMatrix.html">LabelMatrix</a> 等标记函数中获取数值标签图像。  
- 分类矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q2"></a> cmap — 颜色映射表**  
"jet"（默认） | c×3 矩阵 | 颜色映射函数  

生成 RGB 图像时使用的颜色映射表，支持以下输入形式：  

- c×3 数值矩阵（double 类型）：矩阵每行对应一组 RGB 三元色值（取值归一化至 [0, 1] 区间），定义一种颜色；要求矩阵行数 c ≥ numlabels（numlabels = max(L(:))，即非零标签数量），若 c > numlabels，函数仅使用前 numlabels 行；  
- 颜色映射函数如 "jet"， "parula"：自动生成适配标签数量的颜色映射表；  
- 默认值："jet" 颜色映射表。

**<a id="Q3"></a> zerocolor — 填充颜色**  
[1, 1, 1]（默认白色） | 三元素向量 | "b" | "c" | "g"

填充颜色，指定为一个 3 阶向量，表示一个 RGB 三元组，或者是以下数值标签图像的颜色缩写之一。`label2rgb` 将填充颜色应用于数值标签图像的标签 0，或者应用于分类标签图像的标签 <undefined>。

| 值 | 颜色 |
| :----------------------- | :--------------------------- |
| "b" | Blue |
| "c" | Cyan |
| "g" | Green |
| "k" | Black |
| "m" | Magenta |
| "r" | Red |
| "w" | White |
| "y" | Yellow |

### 输出参数
**<a id="P1"></a> RGB — RGB 数据**  
数值矩阵

RGB 数据，以数值矩阵的形式返回。

**数据类型：** `double`

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../bwconncomp/bwconncomp.html">bwconncomp</a> | <a
href="../bwlabel/bwlabel.html">bwlabel</a> | <a 
href="../bwlabeln/bwlabeln.html">bwlabeln</a> | <a 
href="../colormap/colormap.html">colormap</a> | <a 
href="../ismember/ismember.html">ismember</a> | <a 
href="../labelmatrix/labelmatrix.html">labelmatrix</a> | <a 
href="../watershed/watershed.html">watershed </a>

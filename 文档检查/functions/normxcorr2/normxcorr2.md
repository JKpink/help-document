## normxcorr2
归一化二维互关性

## 语法
[`C = normxcorr2(template, A)`](#function1)

## 用法
<a id="function1"></a>[C](#P1) = normxcorr2([template](#Q1), [A](#Q2)) 核心作用是在待搜索图像 `A` 中寻找与模板图像 `template` 最相似的区域，通过计算两者的归一化互相关矩阵 `C` ，以峰值位置指示模板在 `A` 中的匹配位置。

## 参数说明
### 输入参数
**<a id=Q1></a>template — 输入模板**  
模板图像（待匹配的局部特征区域）。指定为数值矩阵。template 的值不能都相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`

**<a id=Q1></a>A — 输入图像**  
输入图像，指定为数值图像。A 必须大于矩阵`template`，归一化才有意义。
对于 A 中在模板的整个范围内对应方差为零的区域，归一化互相关性为未定义的运算。在这些区域中，`normxcorr2` 为输出 `C` 赋予零相关系数。
### 输出参数
**<a id=Q1></a>C — 相关系数**  
相关系数，以数值矩阵形式返回，值在 [-1, 1] 范围内。

**数据类型：**`double` 
## 参考文献
[1] Lewis, J. P. "Fast Normalized Cross-Correlation." Industrial Light & Magic, 1995. https://scribblethink.org/Work/nvisionInterface/nip.pdf.  
[2] Haralick, Robert M., and Linda G. Shapiro, Computer and Robot Vision, Volume II, Addison-Wesley, 1992, pp. 316-317.
## 版本历史
在北太天元图像处理工具箱 V1.0 推出
## 相关主题
<a href="../corrcoef /corrcoef .html">corrcoef </a> | <a
href="../corr2/corr2.html">corr2</a>
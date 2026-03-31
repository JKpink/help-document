## imhist  
图像直方图

## 简介  
[ `[counts, binLocations] = imhist(I)`](#function1)  
[ `[counts, binLocations] = imhist(I, n)`](#function2)  
[ `imhist(__)`](#function3)

## 用法  
<a id="function1"></a>
[[counts](#Q1), [binLocations](#Q4)] = imhist([I](#Q2)) 计算灰度图像 [`I`](#Q2) 的直方图。imhist 函数在 [`counts`](#Q1) 中返回直方图计数，在 binLocations 中返回 bin 位置。
<a id="function2"></a>  
[[counts](#Q1), [binLocations](#Q4)] = imhist([I](#Q2), [n](#Q3)) 指定用于计算直方图的 bin 的数量 [`n`](#Q3)。
<a id="function3"></a>  
`imhist(__)`显示绘制的直方图，在“__”内，输入参数同上。


## 参数说明  
### 输入参数  

**<a id="Q2"></a>I — 灰度图像**  
数值数组 | 逻辑数组

灰度图像，指定为任意维度的数值数组或逻辑数组。

**数据类型：**  `uint8` | `logical`

**<a id="Q3"></a>n — bin 的个数**  
正整数

bin的个数，指定为正整数，建议至少为2。默认值规则：

- 若输入I为逻辑型二值图像，默认使用n=2个 bin，分别对应false（0）和true（1）。
- 若输入I为灰度图像（非逻辑型数值数组），默认使用n=256个 bin。
- 补充说明：若数值数组I仅包含0和1两个值（如uint8类型[0,1]），但非逻辑型，仍按灰度图像处理，默认使用n=256个 bin。

**示例：** 50

### 输出参数  
**<a id="Q1"></a>counts — 直方图计数**  
数值数组

直方图计数，以数值数组形式返回。该数组中的每个元素，对应直方图中一个 bin 内包含的输入图像 I 的像素总个数（即该 bin 对应的像素出现次数），所有元素的值均为非负整数。

**数据类型：** `int32`

**<a id="Q4"></a>binLocations — bin位置**  
数值数组

bin 位置，以数值数组形式返回。核心说明如下：

- 与 counts 关联：数组长度与 counts 完全一致，元素一一对应，每个 binLocations 元素对应 counts 中同一位置 bin 的像素值参考位置。
- 数值特征：取值范围与输入图像 I 的像素值范围保持一致，用于标识对应 bin 所覆盖的像素值区间。

**数据类型：** `double`

## 版本历史  
在北太天元图像处理工具箱 V1.1 推出

##相关主题
<a href="../histeq/histeq.html">histeq</a>
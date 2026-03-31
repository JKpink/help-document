## offsetstrel
形态学偏移结构元素

## 描述
`offsetstrel` 对象表示非平坦形态学结构元素，是形态学膨胀和腐蚀运算的重要组成部分。

非平坦结构元素是一个矩阵，用于标识图像中正在处理的像素，并定义处理该像素时使用的邻域。非平坦结构元素包含有限值，作为形态学计算中的加性偏移。矩阵的中心像素称为原点，标识图像中正在处理的像素。邻域中值为 `-Inf` 的像素不参与计算。

`offsetstrel` 对象仅可用于灰度图像的形态学运算。

若要创建平坦结构元素，请使用 `strel`。

## 创建方式
### 语法
[`SE = offsetstrel(offset)`](#function1)  
[`SE = offsetstrel("ball",r,h)`](#function2)  
[`SE = offsetstrel("ball",r,h,n)`](#function3)

### 说明
<a id="function1"></a>
[SE](#P1) = offsetstrel([offset](#Q1)) 创建非平坦结构元素，其中矩阵 `offset` 指定加性偏移量。

### 输入参数
**<a id="Q1"></a> offset — 邻域中每个像素位置的加性偏移量**  
数值矩阵

执行形态学运算时邻域中每个像素位置的加性偏移量，指定为数值矩阵。值为 `-Inf` 的位置不参与计算。

**数据类型：** `double`

## 对象函数

| 函数                                                  | 描述                     |
| ----------------------------------------------------- | ------------------------ |
| <a href="../imdilate/imdilate.html">`imdilate`</a>    | 对图像进行膨胀           |
| <a href="../imerode/imerode.html">`imerode`</a>       | 对图像进行腐蚀           |
| <a href="../imclose/imclose.html">`imclose`</a>       | 对图像进行形态学闭运算   |
| <a href="../imopen/imopen.html">`imopen`</a>          | 对图像进行形态学开运算   |
| <a href="../imbothat/imbothat.html">`imbothat`</a>    | 进行底帽滤波             |
| <a href="../imtophat/imtophat.html">`imtophat`</a>    | 进行顶帽滤波             |
| <a href="../decompose/decompose.html">`decompose`</a> | 返回分解后的结构元素序列 |
| <a href="../reflect/reflect.html">`reflect`</a>       | 反射结构元素             |
| <a href="../translate/translate.html">`translate`</a> | 平移结构元素             |

## 提示
- 非平坦结构元素的 `Offset` 矩阵中，值为 `-Inf` 的位置表示不在邻域中，不参与形态学计算。

## 版本历史
在北太天元图像处理工具箱 V3.0 推出  

## 相关主题
<a href="../strel/strel.html">strel</a> | <a href="../imdilate/imdilate.html">imdilate</a> | <a href="../imerode/imerode.html">imerode</a> | <a href="../imclose/imclose.html">imclose</a> | <a href="../imopen/imopen.html">imopen</a> | <a href="../imbothat/imbothat.html">imbothat</a> | <a href="../imtophat/imtophat.html">imtophat</a>
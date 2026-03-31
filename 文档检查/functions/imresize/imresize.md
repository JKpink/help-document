## imresize
调整图像大小

## 简介
[`B = imresize(A, scale)`](#function1)  
[`B = imresize(A, [numrows numcols])`](#function2)  
[`___ = imresize(___, method)`](#function3)

## 用法 
<a id="function1"></a> [B](#P1) = imresize([A](#Q1), [scale](#Q2)) 返回图像 `B`，其大小为将 `A` 的长宽缩放 `scale` 倍。输入图像 `A` 可以是灰度图像、RGB 图像、二值图像。  
如果 `A` 有两个以上维度，则 `imresize` 只调整前两个维度的大小。如果 `scale` 介于 0 和 1 之间，则 `B` 的大小小于 `A` 的大小,如果 scale 大于 1，则 `B` 的大小大于 `A` 的大小。默认情况下，`imresize` 使用双三次插值。  
<a id="function2"></a> [B](#P1) = imresize([A](#Q1), [[numrows numcols]](#Q3)) 返回图像 `B`，其行数和列数由二元素向量 (numrows numcols) 指定。  
<a id="function3"></a>  \_\_\_ = imresize(\_\_\_, [method](#Q4)) 指定使用的插值方法。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 要调整大小的图像**  
数值数组 | 逻辑数组

要调整大小的图像，指定为任意维度的数值数组或逻辑数组。输入必须为非稀疏的，且数值输入必须为实数。

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`


**<a id="Q2"></a> scale — 大小调整因子**  
正数

大小调整因子，指定为正数。`imresize` 对行和列维度应用相同的缩放因子。
如果指定的大小调整因子不会产生整数长度的图像维度，则 `imresize` 会在调整大小操作后调用 <a href="../ceil/ceil.html">ceil</a>  </a> 函数。换句话说，输出图像有 ceil(scale * size(A,1)) 行和 ceil(scale * size(A,2)) 列。

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q3"></a> [numrows numcols] — 输出图像的行和列维度**  
2 元素正整数向量

输出图像的行和列维度，指定为 2 元素正整数向量。暂不支持为 `numrows` 或 `numcols` 指定 `NaN` 值。

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q4"></a> method — 插值方法**  
字符向量 | 字符串标量 

插值方法，指定为字符向量或字符串标量。数值图像和逻辑图像的默认值为 `"bilinear"`。

| **方法**   | **描述**                                                                                                        |
| :--------- | :-------------------------------------------------------------------------------------------------------------- |
| `"nearest"`  | 最近邻插值；赋给输出像素的值就是其输入点所在像素的值。不考虑其他像素。                                          |
| `"bilinear"` | 双线性插值；输出像素值是最近 2 × 2 邻域中的像素的加权平均值。                                                     |
| `"bicubic"`  | 双三次插值；输出像素值是最近 4 × 4 邻域中的像素的加权平均值。（注意：双三次插值可能生成在原始范围之外的像素值。） |
  
**数据类型：**`char` | `string` 
### 输出参数

**<a id="P1"></a> B — 调整大小后的图像**  
数值数组 | 逻辑数组

调整大小后的图像，指定为与输入图像 [A](#Q1) 的数据类型相同的数值或逻辑数组。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imresize3/imresize3.html">imresize3</a> | <a 
href="../interp2/interp2.html">interp2</a> 
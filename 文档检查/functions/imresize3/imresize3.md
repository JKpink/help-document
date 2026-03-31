## imresize3
调整 3 维图像大小

## 简介
[`B = imresize3(V, scale)`](#function1)  
[`B = imresize3(V, [numrows numcols numframes]) `](#function2)

## 用法 
<a id="function1"></a> [B](#P1) = imresize3([V](#Q1), [scale](#Q2)) 返回图像 `B`，其大小为将三位数值图像 `V` 的长宽缩放 `scale` 倍。  
<a id="function2"></a> [B](#P1) = imresize3([V](#Q1), [[numrows numcols numframes]](#Q3)) 返回图像 `B`，其行数、列数和帧数由三元素向量 `(numrows numcols numframes)` 指定。

## 参数说明
### 输入参数
**<a id="Q1"></a> V — 要调整大小的图像**  
三维数值数组

要调整大小的图像，指定为三维数值数组。

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | 

**<a id="Q2"></a> scale — 缩放因子**  
数值标量

缩放因子，指定为数值标量。

- 如果 `scale` 小于 1，则输出图像小于输入图像。

- 如果 `scale` 大于 1，则输出图像大于输入图像。  
  
`imresize3` 将缩放因子应用于图像的每个维度。  

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q3"></a> [numrows numcols numplanes] — 输出图像的大小**  
3 元素正整数向量

输出图像的大小，指定为3 元素正整数向量 [rows columns planes]。暂不支持指定一个数值，并将其他两个值指定为 `NaN`。

**数据类型：**`single` | `double`

### 输出参数

**<a id="P1"></a> B — 调整大小后的图像**  
数组

调整大小后的图像，指定为与输入图像 [V](#Q1) 数据类型相同的数组。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../imresize/imresize.html">imresize</a> | <a 
href="../imrotate/imrotate.html">imrotate</a> | <a 
href="../imrotate3/imrotate3.html">imrotate3</a> | <a 
href="../imwarp/imwarp.html">imwarp</a> 
## bwextent  
二值图像区域中的像素数与边界框中总像素数的比率

## 简介  
[ `Stats = bwextent(BW)`](#function1)
 
## 用法  
<a id="function1"></a>
[Stats](#Q1) = bwextent([BW](#Q2))
对输入的二维二值图像 [`BW`](#Q2)，计算所有目标像素的总数量，以及能包围所有目标像素的最小矩形边界框的总像素数量，返回二者的比率 [`Stats`](#Q1) 。该数值用于反映目标区域对其边界框的填充程度，最小边界框是刚好覆盖所有目标像素的最小矩形区域，无冗余空间。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 二维二值图像**  
数值数组 | 逻辑数组

- 仅支持二维的逻辑数组或数值数组；
- 若为逻辑数组，true 表示目标像素，false 表示背景像素；
- 若为数值数组，非零元素视为目标像素，零元素视为背景像素。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数  
**<a id="Q1"></a>Stats — 比率**  
数值标量

区域中的像素数与边界框中总像素数的比率，以double类型数值标量形式返回，计算方法为 `bwarea` 除以边界框的面积。

**数据类型：** `double`

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../bwconncomp/bwconncomp.html">bwconncomp</a> | <a 
href="../bwsolidity/bwsolidity.html">bwsolidity</a> | <a 
href="../regionprops/regionprops.html">regionprops</a> | <a 
href="../bwarea/bwarea.html">bwarea</a>
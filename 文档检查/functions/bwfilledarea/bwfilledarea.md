## bwfilledarea  
二值图像区域填充图像的面积

## 简介  
[ `Stats = bwfilledarea(BW)`](#function1)

## 用法  
<a id="function1"></a>
[Stats](#Q1) = bwfilledarea([BW](#Q2))该函数先通过 bwfilledimage 函数对输入的任意维度二值图像 [`BW`](#Q2) 执行 “填充内部孔洞 + 剪裁至最小边界框” 操作，得到填充后二值图像 BWf；再统计 BWf 中目标像素的总数量，以标量形式返回该数值，最小边界框是指刚好覆盖所有目标像素的最小矩形 / 立方体形区域（二维 / 三维）等。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 二值图像**  
数值数组 | 逻辑数组

- 支持任意维度的逻辑数组或数值数组；
- 若为逻辑数组，true 表示目标像素，false 表示背景像素；
- 若为数值数组，非零元素视为目标像素，零元素视为背景像素。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数  
**<a id="Q1"></a>Stats — 像素的数量**  
数值标量

统计 `bwfilledimage(BW)` 输出图像中所有目标像素（true）的总数；

**数据类型：** `double`

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../bwfilledimage/bwfilledimage.html">bwfilledimage</a> | <a 
href="../regionprops/regionprops.html">regionprops</a>
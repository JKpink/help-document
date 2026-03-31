## bwperimeter  
二值图像区域的周长

## 简介  
[ `Stats = bwperimeter(BW)`](#function1)

## 用法  
<a id="function1"></a>
[Stats](#Q1) = bwperimeter([BW](#Q2))计算 [`BW`](#Q2) 中目标区域的边界周长（单位：像素），以标量形式返回。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 二值图像**  
数值数组 | 逻辑数组

- 仅支持二维的逻辑数组或数值数组；
- 若为逻辑数组，true 表示目标像素，false 表示背景像素；
- 若为数值数组，非零元素视为目标像素，零元素视为背景像素。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数  

**<a id="Q1"></a>Stats — 周长**  
数值标量

计算二维二值图像中目标区域的边界周长，以标量形式返回。通过计算围绕区域边界的相邻像素对之间的距离来计算周长。

**数据类型：** `double` 

##版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../bwarea/bwarea.html">bwarea</a> | <a 
href="../bwfilledarea/bwfilledarea.html">bwfilledarea</a> | <a 
href="../regionprops/regionprops.html">regionprops</a>
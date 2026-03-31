## bwextrema  
二值图像区域中的极值点

## 简介  
[ `Stats = bwextrema(BW)`](#function1) 

## 用法  
<a id="function1"></a>
[Stats](#Q1) = bwextrema([BW](#Q2))  
对输入的二维二值图像 [`BW`](#Q2) ，提取目标区域在 8 个标准方位的极值点坐标，以 8×2 矩阵形式返回。极值点为目标区域在对应方位上的最外侧像素，可用于快速量化目标区域的边界特征与轮廓范围。  

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 二值图像**  
数值数组 | 逻辑数组

- 仅支持二维的逻辑数组或数值数组；
- 若为逻辑数组，true 表示目标像素，false 表示背景像素；
- 若为数值数组，非零元素视为目标像素，零元素视为背景像素。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数  
**<a id="Q1"></a>Stats — 极值点**  
极值点

区域中的极值点，以 8×2 矩阵形式返回。  
矩阵的每一行都包含其中一个点的 x 和 y 坐标，向量的形式为 [ top-left, top-right, right-top, right-bottom, bottom-right, bottom-left, left-bottom, left-top ]，  
关于以上元素的意义，  
例如 “ top-left ” 的意义是，最顶行的最左侧元素，“ right-bottom ”的意义是，最右列的最底部元素，其他同理，  
对于某些形状，多个极值点可以具有相同的坐标。

**数据类型：** `int32` 

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../regionprops/regionprops.html">regionprops</a> | <a 
href="../bwarea/bwarea.html">bwarea</a> | <a 
href="../bwpixellist/bwpixellist.html">bwpixellist</a> 

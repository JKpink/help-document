## bwminoraxislength  
二值图像中与区域具有相同归一化二阶中心矩的椭圆短轴长度

## 简介  
[ `Stats = bwminoraxislength(BW)`](#function1)

## 用法  
<a id="function1"></a>
[Stats](#Q1) = bwmajoraxislength([BW](#Q2))对输入的二维二值图像 [`BW`](#Q2) ，求解与该区域具有相同归一化二阶中心矩的等效椭圆，最终以标量形式返回该等效椭圆短轴的长度。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 二值图像**  
数值数组 | 逻辑数组

- 仅支持二维的逻辑数组或数值数组；
- 若为逻辑数组，true 表示目标像素，false 表示背景像素；
- 若为数值数组，非零元素视为目标像素，零元素视为背景像素。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数  
**<a id="Q1"></a>Stats — 长度**  
数值标量

计算与区域具有相同归一化二阶中心矩的椭圆短轴的长度（以像素为单位），以标量形式返回。

**数据类型：** `double` 

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../bwmajoraxislength/bwmajoraxislength.html">bwmajoraxislength</a> | <a href="../regionprops/regionprops.html">regionprops</a>
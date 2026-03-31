## bworientation  
x 轴与椭圆长轴（该椭圆与区域具有相同二阶矩）之间的角度

## 简介  
[ `Stats = bworientation(BW)`](#function1)

## 用法  
<a id="function1"></a>
[Stats](#Q1) = bwmajoraxislength([BW](#Q2))对输入的二维二值图像 [`BW`](#Q2)，求解与该区域具有相同归一化二阶中心矩的等效椭圆，最终以标量形式返回该等效椭圆长轴与x轴之间的角度，该值以度为单位，范围从 -90 度到 90 度。  

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 二值图像**  
数值数组 | 逻辑数组

- 仅支持二维的逻辑数组或数值数组；
- 若为逻辑数组，true 表示目标像素，false 表示背景像素；
- 若为数值数组，非零元素视为目标像素，零元素视为背景像素。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数  
**<a id="Q1"></a>Stats — 角度**  
数值标量

求解与该区域具有相同归一化二阶中心矩的等效椭圆，最终以标量形式返回该等效椭圆长轴与x轴之间的角度，该值以度为单位，范围从 -90 度到 90 度。

**数据类型：** `double` 



##版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../bweccentricity/bweccentricity.html">bweccentricity</a> | <a 
href="../regionprops/regionprops.html">regionprops</a>

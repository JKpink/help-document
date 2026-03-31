## bwhitmiss 
二值击中击不中

## 简介
[ `BW2 = bwhitmiss(BW, SE1, SE2)`](#function1)  
[ `BW2 = bwhitmiss(BW, interval)`](#function2)

## 用法
<a id="function1"></a>
[BW2](#Q4) = bwhitmiss([BW](#Q1), [SE1](#Q2), [SE2](#Q2)) 执行由结构元素 `SE1` 和 `SE2` 定义的击中击不中变换。  
<a id="function2"></a>
[BW2](#Q4) = bwhitmiss([BW](#Q1), [interval](#Q3)) 使用单个数组定义击中击不中变换。该数组中的元素可以是 1、0 或 -1，其中 1 表示 `SE1` 的区域，-1 表示 `SE2` 的区域，0 表示忽略的区域。

## 参数说明
### 输入参数
**<a id="Q1"></a> BW — 二进制图像**  
数值数组 | 逻辑数组

二进制图像，指定为任意维度的数字或逻辑数组。对于数字输入，任何非零像素都被视为 1 (true)。

**<a id="Q2"></a> SE1, SE2 — 结构化元素**  
Strel 对象 | 数值数组

平面结构元素，指定为 strel 对象或值为 1 和 0 的数值矩阵。`SE1` 和 `SE2` 的邻域不应具有重叠元素。

**<a id="Q3"></a> interval — 间隔**  
数值数组

间隔，指定为值为 1、0 和 -1 的数值数组。

**数据类型**： `single` | `double` | `int8` | `int16` | `int32` | `int64`

### 输出参数
**<a id="Q4"></a> BW2 — 处理后的二进制图像**  
逻辑数组

命中后处理的二进制图像，指定为与 `BW` 大小相同的逻辑数组。

**数据类型**: `logical` 

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imdilate/imdilate.html">imdilate</a> | <a 
href="../imerode/imerode.html">imerode</a> | <a 
href="../strel/strel.html">strel</a> 



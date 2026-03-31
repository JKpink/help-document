## bwselect3  
选择二进制卷中的对象

## 简介  
[`J = bwselect3(V, c, r, p)`](#function1)

## 用法  
<a id="function1"></a>
[J](#Q1) = bwselect3([V](#Q2), [c](#Q3), [r](#Q4), [p](#Q5)) 返回包含与体素 ([`c`](#Q3), [`r`](#Q4), [`p`](#Q5)) 重叠对象的二值体积 [`J`](#Q1)。对象是由值为 1 的体素组成的连通集合。

## 参数说明  
### 输入参数  
**<a id="Q2"></a> V — 二值体积**  
三维数值数组 | 三维逻辑数组

二值体积，指定为三维数值数组或三维逻辑数组。

**<a id="Q3"></a> r — 体素行索引**  
数值标量 | 数值向量

目标对象中体素的行索引，指定为数值标量或数值向量。若指定为向量，则 `r` 必须与 `c` 和 `p` 长度相同。输出二值体积 `J` 包含与任意体素 (r(k), c(k), p(k))重叠的对象集合，其中 `k` 为向量索引。

**<a id="Q4"></a> c — 体素列索引**  
数值标量 | 数值向量

目标对象中体素的列索引，指定为数值标量或数值向量。若指定为向量，则 `c` 必须与 `r` 和 `p` 长度相同。输出二值体积J包含与任意体素 (r(k), c(k), p(k)) 重叠的对象集合，其中 `k` 为向量索引。

**<a id="Q5"></a> p — 体素平面索引**  
数值标量 | 数值向量

目标对象中体素的平面索引，指定为数值标量或数值向量。若指定为向量，则 `p` 必须与 `r` 和 `c` 长度相同。输出二值体积 `J` 包含与任意体素 (r(k), c(k), p(k)) 重叠的对象集合，其中 `k` 为向量索引。

### 输出参量  
**<a id="Q1"></a> J — 包含与指定体素重叠对象的二值体积**  
三维逻辑数组

包含与指定体素重叠对象的二值体积，以三维逻辑数组形式返回。`J` 包含与 `r`, `c`, `p` 指定的任意体素存在重叠的对象集合。

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
 <a href="../bwlabel/bwlabel.html">bwlabel</a> | <a 
href="../imfill/imfill.html">imfill</a> | <a 
href="../roipoly/roipoly.html">roipoly</a> | <a 
href="../regionfill/regionfill.html">regionfill</a> | <a 
href="../bwselect/bwselect.html">bwselect</a> 

### 主题  
 <a href="../Image Coordinate Systems/Image Coordinate Systems.html">Image Coordinate Systems</a> | <a 
href="../Shift X- and Y-Coordinate Range of Displayed Image/Shift X- and Y-Coordinate Range of Displayed Image.html">Shift X- and Y-Coordinate Range of Displayed Image</a> 
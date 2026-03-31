## bwpack  
将二值图像打包为 uint32 类型矩阵

## 简介  
[ `BWP = bwpack(BW)`](#function1)

## 用法  
<a id="function1"></a>
[BWP](#Q1) = bwpack([BW](#Q2))将输入的二维二值图像 [`BW`](#Q2) 打包为 uint32 类型的数值矩阵 [`BWP`](#Q1) （称为打包二进制图像）。打包逻辑为利用二值像素仅含 0/1 的特性，将每个像素映射为输出矩阵中 uint32 值的单个比特位，按列处理每 32 个像素合并为一个 uint32 元素。

## 参数说明  
### 输入参数  
**<a id="Q2"></a>BW — 二维二值图像**  
数值数组 | 逻辑数组

- 仅支持二维的逻辑数组或数值数组；
- 若为逻辑数组，true 表示目标像素，false 表示背景像素；
- 若为数值数组，非零元素视为目标像素（值为 1），零元素视为背景像素（值为 0）。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数  
**<a id="Q1"></a>BWP — 打包后的二值图像**  
数值矩阵

打包后的二进制图像，以 uint32 类型数值矩阵形式返回。若输入图像为 M 行 N 列，输出矩阵尺寸为 ceil(M/32) 行 N 列；矩阵中每个 uint32 元素的比特位按列映射输入图像的 32 个像素（首行像素对应最低有效位，第 32 行像素对应最高有效位）。

**数据类型：**  `uint32`

## 版本历史  
在北太天元图像处理工具箱 V3.0 推出

## 相关主题  
<a href="../bwunpack/bwunpack.html">bwunpack</a> | <a
href="../imdilate/imdilate.html">imdilate</a> | <a
href="../imerode/imerode.html">imerode</a> | <a
href="../bwarea/bwarea.html">bwarea</a>
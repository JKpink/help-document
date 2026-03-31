# bwunpack

解包二值图像

## 简介
[`BW = bwunpack(BWP, m)`](#section1)

## 用法
<a id="section1"></a>

[BW]() = bwunpack([BWP](), [m]())：将打包后的二值图像 `BWP` 解包为具有 `m` 行的二值图像 `BW` 。

## 参数说明
### 输入参数
**<a id="Q2"></a> BWP — 打包后的二值图像**  
二维数值矩阵

打包后的二值图像，指定为 uint32 数据类型的二维数值数组。

**数据类型：**  `uint32`  

**<a id="Q3"></a> m —  图像行数**  
正整数

图像行数，指定为一个正整数。`m` 的默认值为 32*size (BWP,1)。

**数据类型：**  `uint32`  

### 输出参数
**<a id="Q5"></a> BW — 解包后的二值图像**  
m 行 n 列的逻辑矩阵

解包后的二值图像，以 m 行的逻辑矩阵形式返回。

**数据类型**：`logical`

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
 <a href="../bwpack/bwpack.html">bwpack</a> | <a 
href="../imerode/imerode.html">imerode</a> | <a 
href="../imdilate/imdilate.html">imdilate</a> 


## dicomread
读取 DICOM 图像

## 简介
[`X = dicomread(filename)`](#function1)  

## 用法
<a id="function1"></a>
[X](#P1) = dicomread([filename](#Q1)) 从符合医学数字成像和通信 (DICOM) 标准的文件 `filename` 中读取图像数据。  

## 参数说明
### 输入参数
**<a id="Q1"></a> filename — DICOM 文件的名称**  
字符串标量 | 字符向量

DICOM 文件的名称，指定为字符向量或字符串标量。 

**数据类型：** `char` | `string`

### 输出参数
**<a id="P1"></a> X — DICOM 图像**  
m×n 矩阵 | m×n×3 数组 | 四维数组

DICOM 图像，返回为下列选项之一：

- 表示单帧灰度图像或索引图像的 m×n 矩阵。
- 表示单帧真彩色 (RGB) 图像的 m×n×3 数组。
- 表示多帧图像的四维数组。

**数据类型：** `int8` | `int16` | `uint8` | `uint16`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../dicomanon/dicomanon.html">dicomanon</a> | <a
href="../dicomreadVolume/dicomreadVolume.html">dicomreadVolume</a> | <a 
href="../dicomdict/dicomdict.html">dicomdict</a> | <a 
href="../dicomdisp/dicomdisp.html">dicomdisp</a> | <a 
href="../dicominfo/dicominfo.html">dicominfo</a> | <a 
href="../dicomlookup/dicomlookup.html">dicomlookup</a> | <a 
href="../dicomwrite/dicomwrite.html">dicomwrite</a> | <a 
href="../dicomuid/dicomuid.html">dicomuid</a> | <a 
href="../../MedicalImaging/dicomFile/dicomFile.html">dicomFile</a> | <a 
href="../../MedicalImaging/getPixelData/getPixelData.html">getPixelData</a>

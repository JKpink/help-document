## dicominfo
从 DICOM 文件中读取元数据

## 简介
[`info = dicominfo(filename)`](#function1)

## 用法
<a id="function1"></a>
[info](#P1) = dicominfo([filename](#Q1)) 从符合医学数字成像和通信 (DICOM) 标准或安全数字成像和通信 (DICOS) 规范的文件 `filename` 中读取元数据。

## 参数说明
### 输入参数
**<a id="Q1"></a> filename — DICOM 文件的名称**  
字符串标量 | 字符向量

DICOM 文件的名称，指定为字符向量或字符串标量。  

**数据类型：** `char` | `string`

### 输出参数
**<a id="P1"></a> info — DICOM 元数据**  
结构体  

DICOM 元数据，以结构体形式返回。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../dicomanon/dicomanon.html">dicomanon</a> | <a
href="../dicomdict/dicomdict.html">dicomdict</a> | <a 
href="../dicomdisp/dicomdisp.html">dicomdisp</a> | <a 
href="../dicomwrite/dicomwrite.html">dicomwrite</a> | <a 
href="../dicomlookup/dicomlookup.html">dicomlookup</a> | <a 
href="../dicomread/dicomread.html">dicomread</a> | <a 
href="../dicomuid/dicomuid.html">dicomuid</a> | <a 
href="../../MedicalImaging/dicomFile/dicomFile.html">dicomFile</a> | <a 
href="../../MedicalImaging/getAttribute/getAttribute.html">getAttribute</a> | <a 
href="../../MedicalImaging/findAttribute/findAttribute.html">findAttribute</a>

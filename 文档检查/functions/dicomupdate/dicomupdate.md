## dicomupdate
更新 DICOM 元数据中目标属性的值

## 简介 
[`newinfo = dicomupdate(info, attributeInfo)`](#function1)  
[`newinfo = dicomupdate(info, attribute, value)`](#function2)  

## 用法
<a id="function1"></a>
[newinfo](#Q1)  = dicomupdate([info](#P1), [attributeInfo](#P4))
更新 DICOM 元数据结构 info 中目标属性的值，并返回更新后的元数据结构 newinfo。参数 attributeInfo 用于指定目标属性的位置及其新值。  
<a id="function2"></a>
[newinfo](#Q1) = dicomupdate([info](#P1), [attribute](#P2), [value](#P3)) 通过指定目标属性的名称和新值，更新 DICOM 元数据结构中该目标属性的值。

## 参数说明
### 输入参数

**<a id="P1"></a> info — DICOM 元数据**  
结构体  

DICOM 元数据，指定为一个结构体。可以使用 dicominfo 函数从 DICOM 文件中提取 DICOM 元数据结构体。  

**数据类型：** `struct`  

**<a id="P4"></a> attributeInfo — 目标属性的位置和新值**  
表  

目标属性的位置和新值，指定为一个表。

**<a id="P2"></a> attribute — 目标 DICOM 元数据字段的名称**  
字符向量 | 字符串标量  

目标 DICOM 元数据字段的名称，指定为字符串标量或字符向量。  

**示例：** "BitsAllocated"  
**数据类型：** `char` | `string`

**<a id="P3"></a> value — DICOM 元数据属性的新值**  
数值数组 | 字符向量 | 字符串标量  

DICOM 元数据属性的新值，指定为数值数组、字符串标量或字符向量。  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `char` | `string`  

### 输出参数
**<a id="Q1"></a> newinfo — 更新后的 DICOM 元数据**  
结构体  

更新后的 DICOM 元数据，以结构体形式返回。  

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../dicomanon/dicomanon.html"> dicomanon</a> | <a
href="../dicomdict/dicomdict.html"> dicomdict</a> | <a 
href="../dicomdisp/ dicomdisp.html"> dicomdisp</a> | <a 
href="../dicominfo/dicominfo.html"> dicominfo </a> | <a 
href="../dicomwrite/dicomwrite.html"> dicomwrite</a> | <a 
href="../dicomread/dicomread.html"> dicomread</a> | <a 
href="../dicomuid/dicomuid.html"> dicomuid</a> | <a 
href="../dicomfind/dicomfind.html"> dicomfind</a> | <a 
href="../dicomreadVolume/ dicomreadVolume.html"> dicomreadVolume</a> | <a 
href="../dicomlookup/dicomlookup.html"> dicomlookup</a> 
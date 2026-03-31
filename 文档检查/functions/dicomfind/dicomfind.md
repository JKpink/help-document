## dicomfind
在 DICOM 元数据中查找目标属性的位置与取值

## 简介
[`attributeinfo = dicomfind(info, attribute)`](#function1)  
[`attributeinfo = dicomfind(filename, attribute)`](#function2)  
## 用法
<a id="function1"></a>
[attributeinfo](#Q1) = dicomfind([info](#P1), [attribute](#P2))用于查找 DICOM 元数据结构 `info` 中，元数据字段 `attribute` 的位置和值。要从 DICOM 文件中提取元数据结构，可以使用 `dicominfo`。可以使用 `dicomfind` 来帮助查找那些在 `info` 结构中深层嵌套的元数据项的值。  
<a id="function2"></a>
[attributeinfo](#Q1) = dicomfind([filename](#P3), [attribute](#P2))在指定的 DICOM 文件中，查询并返回由 `attribute` 参数所标识的特定元数据元素的值。  
## 参数说明
### 输入参数

**<a id="P1"></a> info — DICOM 元数据**  
结构体  

DICOM 元数据，指定为一个结构体。可以使用 `dicominfo` 函数从 DICOM 文件中提取 DICOM 元数据结构体。  

**数据类型:** `struct`  

**<a id="P2"></a> attribute — DICOM 元数据字段名称**  
字符串标量 | 字符向量DICOM  

元数据字段的名称，指定为字符串标量或字符向量。attribute 的拼写和大小写必须与输入的 DICOM 元数据结构体 info 中的某个元数据字段的完整名称完全匹配。  

**数据类型:** `string` | `char`  

**<a id="P3"></a> filename — DICOM 文件名**  
字符串标量 | 字符向量  

指定为字符串标量或字符向量的 DICOM 文件名。  

**示例：** "rtstruct.dcm"  
**数据类型：** `string` | `char`

### 输出参数
**<a id="Q1"></a> attributeinfo — 指定 DICOM 属性的位置和值**  
表  

指定 DICOM 属性的位置和值，以一个包含两列的表形式返回：Location（位置）和 Value（值）。Location 列使用点表示法列出属性名称，指明它在嵌套的 DICOM 元数据结构中的位置。Value 列列出 DICOM 元数据结构中该属性的每个实例所分配的值。  

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../dicomanon/dicomanon.html"> dicomanon</a> | <a
href="../dicomdict/dicomdict.html"> dicomdict</a> | <a 
href="../dicomdisp/ dicomdisp.html"> dicomdisp</a> | <a 
href="../dicominfo/dicominfo.html"> dicominfo </a> | <a 
href="../dicomupdate/dicomupdate.html"> dicomupdate</a> | <a 
href="../dicomread/dicomread.html"> dicomread</a> | <a 
href="../dicomuid/dicomuid.html"> dicomuid</a> | <a 
href="../dicomreadVolume/dicomreadVolume.html"> dicomreadVolume</a> | <a 
href="../dicomlookup/dicomlookup.html"> dicomlookup</a>
## dicomlookup
DICOM 数据字典属性检索

## 简介
[`nameOut = dicomlookup(group, element)`](#function1)  
[`[groupOut, elementOut] = dicomlookup(name)`](#function2)

## 用法
<a id="function1"></a>
[nameOut](#P3) = dicomlookup([group](#Q2), [element](#Q3)) 在当前 DICOM 数据字典中，检索与指定组标签 group 和元素标签 element 对应的属性，返回该属性的标准名称。  
<a id="function2"></a>
[[groupOut](#P1), [elementOut](#p2)] = dicomlookup([name](#Q1)) 在当前 DICOM 数据字典中检索由参数 `name` 指定的属性，并返回与该属性关联的组标签和元素标签。

## 参数说明
### 输入参数

**<a id="Q2"></a> group — DICOM组标签**  
正整数（十进制） | 字符向量 | 字符串标量  

DICOM 组标签，指定为一个正整数（十进制），或者一个包含十六进制值的字符向量或字符串标量。element 和 group 必须使用相同类型的值：  

- 如果 group 是一个正整数（十进制），则 element 也必须是一个正整数。  
- 如果 group 是一个包含十六进制值的字符向量或字符串标量，则 element 必须是一个包含十六进制值的字符向量或字符串标量。  

**示例：** 40  
**示例：** '7FE0' 或 "7FE0"  
**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `char` | `string`

**<a id="Q3"></a> element — DICOM 元素标签**  
正整数（十进制） | 字符向量 | 字符串标量  

DICOM 元素标签，指定为一个正整数，或者一个包含十六进制值的字符向量或字符串标量。element 和 group 必须使用相同类型的值：  

- 如果 group 是一个正整数，则 element 也必须是一个正整数。  
- 如果 group 是一个包含十六进制值的字符向量或字符串标量，则 element 必须是一个包含十六进制值的字符向量或字符串标量。  

**示例：** 4  
**示例：** '0010' 或 "0010"  
**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `char` | `string`

**<a id="Q1"></a> name — DICOM 属性名称**  
字符向量 | 字符串标量  

DICOM 属性名称，指定为字符向量或字符串标量。  

**示例：**'PhotometricInterpretation' 或 "PhotometricInterpretation"  
**数据类型：** `char` | `string`  

### 输出参数
**<a id="P1"></a> groupOut — 返回的 DICOM 组标签**  
正整数（十进制）  

返回的 DICOM 组标签，以正十进制整数形式返回。  

**数据类型：** `double`  

**<a id="P2"></a> elementOut — 返回的 DICOM 元素标签**  
正整数（十进制）  

返回的 DICOM 元素标签，以正十进制整数形式返回。

**数据类型：** `double`  

**<a id="P3"></a> nameOut — 返回的 DICOM 属性名称**  
字符向量  

返回的 DICOM 属性名称，以字符向量形式返回。  

**数据类型：** `char`

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../dicomanon/dicomanon.html"> dicomanon</a> | <a
href="../dicomdict/dicomdict.html"> dicomdict</a> | <a 
href="../dicomdisp/ dicomdisp.html"> dicomdisp</a> | <a 
href="../dicominfo/dicominfo.html"> dicominfo </a> | <a 
href="../dicomread/dicomread.html"> dicomread</a> | <a 
href="../dicomuid/dicomuid.html"> dicomuid</a>

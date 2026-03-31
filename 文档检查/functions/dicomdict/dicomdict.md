## dicomdict
获取或设置当前有效的 DICOM 数据字典

## 简介
[`dictionaryOut = dicomdict("get")`](#function1)  
[`dicomdict("set", dictionaryIn)`](#function2)  
[`dicomdict("factory")`](#function3)

## 用法
<a id="function1"></a>[dictionaryOut](#Q1) = dicomdict("get")返回当前有效的 DICOM（数字成像与通信医学） 数据字典文件的名称。  
<a id="function2"></a>
dicomdict("set", [dictionaryIn](#Q1)) 将由输入参数 `dictionaryIn` 指定的文件设置为当前有效的 DICOM 数据字典。  
<a id="function3"></a> 
dicomdict("factory")
将当前有效的 DICOM 数据字典恢复为其默认值。
## 参数说明
### 输入参数
**<a id="Q1"></a> dictionaryIn — DICOM 数据字典文件**  
字符向量 | 字符串标量  

指定 DICOM 数据字典文件，其值可以是字符向量或字符串标量。数据字典文件必须为 .txt 类型。除非在函数调用时显式指定其他字典，否则所有与 DICOM 相关的函数都将使用此字典。

**数据类型：** `char` | `string`  

### 输出参数
**<a id="Q2"></a> dictionaryOut — 当前有效的 DICOM 数据字典文件**  
字符向量 | 字符串标量  

当前有效的 DICOM 数据字典文件，以字符向量或字符串标量的形式返回。数据字典文件的格式必须为 .txt 类型。  

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../dicomanon/dicomanon.html"> dicomanon</a> | <a
href="../dicomdisp/dicomdisp.html"> dicomdisp</a> | <a 
href="../dicominfo/dicominfo.html"> dicominfo </a> | <a 
href="../dicomlookup/dicomlookup.html"> dicomlookup</a> | <a 
href="../dicomread/dicomread.html"> dicomread</a> | <a 
href="../dicomuid/dicomuid.html"> dicomuid</a>

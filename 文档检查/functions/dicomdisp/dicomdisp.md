## dicomdisp
显示 DICOM 文件结构

## 简介
[`dicomdisp(filename)`](#function1)  
[`dicomdisp(filename, Name, Value)`](#function2)

## 用法
<a id="function1"></a>
dicomdisp([filename](#Q1)) 从符合标准的 DICOM 文件 filename 中读取元数据，并在命令行中显示这些元数据。  
<a id="function2"></a>
dicomdisp([filename](#Q1), [Name, Value](#Q2))通过名称 - 值参数读取元数据，以控制操作的各个方面。
## 参数说明
### 输入参数
**<a id="Q1"></a> filename — DICOM 文件名**  
字符向量 | 字符串标量  

DICOM 文件名，指定为字符串标量或字符向量。  

**数据类型：**  `char` | `string`  

### <a id="Q2"></a> 名称 - 值参数  
将可选参数指定为 Name1, Value1 ,..., NameN, ValueN 的成对形式，其中 Name 是参数名，Value 是对应的值。名称 - 值参数必须位于其他参数之后，但其配对顺序无关紧要。  

**示例：**dicomdisp("CT-MONO2-16-ankle.dcm", "UseVRHeuristic", 0) 从 DICOM 文件中读取元数据，不使用启发式算法。  

**dictionary — DICOM 数据字典的名称**  
"dicom-dict.txt" (默认值) | 字符串标量 | 字符向量  

指定 DICOM 数据字典的名称，其值可以是字符串标量或字符向量。当指定此参数时，`dicomdisp` 会使用该数据字典来读取 DICOM 文件。 

**数据类型:** `char` | `string`  

**UseVRHeuristic — 读取 VR 模式切换错误的非标准 DICOM 文件**  
 1 (默认值) | 0  

指定是否读取那些 VR（Value Representation，值表示）模式切换错误的非标准 DICOM 文件，其值为逻辑值 1 或 0。
当设置为 1 时，`dicomdisp` 会使用一种启发式算法来帮助读取某些 VR 模式切换错误的非标准 DICOM 文件。对于标准文件，将 `UseVRHeuristic` 设置为 0 以确保正确读取。  

**数据类型:** `logical`


## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../dicomanon/dicomanon.html"> dicomanon</a> | <a
href="../dicomdict/dicomdict.html"> dicomdict</a> | <a 
href="../dicominfo/dicominfo.html"> dicominfo </a> | <a 
href="../dicomlookup/dicomlookup.html"> dicomlookup</a> | <a 
href="../dicomread/dicomread.html"> dicomread</a> | <a 
href="../dicomuid/dicomuid.html"> dicomuid</a>

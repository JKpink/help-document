## dicomCollection
采集相关 DICOM 序列的详细信息

## 简介
[`collection = dicomCollection(directory)`](#function1)

## 用法
<a id="function1"></a>
[collection](#P1) = dicomCollection([directory](#Q1)) 采集指定目录 directory 下所有 DICOM 文件的相关信息，并将文件信息以表格形式返回至变量 `collection` 中。`dicomCollection` 函数依据 DICOM 序列对信息进行聚合，以每个文件元数据字段中SeriesInstanceUID（序列实例唯一标识符）的取值作为判定序列归属的依据。DICOM 序列指的是一次成像操作中所获取的、具有逻辑关联性的一整套影像数据集合。

## 参数说明
### 输入参数
**<a id="Q1"></a> directory — 包含 DICOM 文件的文件夹**  
字符向量 | 字符串标量  

指定为字符串标量或字符向量的、包含 DICOM 文件的文件夹名称。  
 
**数据类型：** `char` | `string`
### 输出参数
**<a id="P1"></a> collection — 来自 DICOM 文件的元数据**  
表格  

来自 DICOM 文件的元数据以表格形式返回。dicomCollection 函数会按 DICOM 序列对这些信息进行聚合。

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../dicominfo/dicominfo.html">dicominfo</a> | <a
href="../dicomread/ dicomread.html"> dicomread</a> | <a 
href="../dicomreadVolume/ dicomreadVolume.html"> dicomreadVolume</a> | <a 
href="../DICOM Browser/DICOM Browser.html">DICOM Browser </a>

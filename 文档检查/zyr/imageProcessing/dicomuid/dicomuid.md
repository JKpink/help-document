## dicomuid
生成 DICOM 全局唯一标识符

## 简介
[`uid = dicomuid`](#function1)  

## 用法
<a id="function1"></a>
[uid](#P1) = dicomuid 返回新的 DICOM 全局唯一标识符 uid。该函数每次调用都会生成一个新的唯一值，因此连续多次调用将返回不同的 uid。

## 参数说明
### 输出参数
**<a id="P1"></a> uid — DICOM 全局唯一标识符**  
字符向量

DICOM 全局唯一标识符，以字符向量形式返回。

**数据类型：** `char`

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../dicomanon/dicomanon.html">dicomanon</a> | <a
href="../dicomdisp/dicomdisp.html">dicomdisp</a> | <a
href="../dicominfo/dicominfo.html">dicominfo</a> | <a
href="../dicomread/dicomread.html">dicomread</a> | <a
href="../dicomwrite/dicomwrite.html">dicomwrite</a> | <a
href="../images.dicom.decodeUID/images.dicom.decodeUID.html">images.dicom.decodeUID</a>

## imfinfo
图像文件的信息

## 简介
[`info = imfinfo(filename)`](#function1)  

## 用法
<a id="function1"></a>
[info](#P1) = imfinfo[(filename)](#Q1) 返回一个结构体，其字段包含有关指定图形文件中图像的信息。此文件的格式从其内容推知。  

## 参数说明
### 输入参数
**<a id="Q1"></a> filename — 图形文件名**  
字符串标量 | 字符向量

图形文件的名称，指定为字符串标量或字符向量。
根据文件的位置，`filename` 可以采用下列形式之一。

| 位置 | 形式 |
| :----------------------- | :----------------------- |
| 当前文件夹或北太天元路径上的文件夹 | 指定 `filename` 中文件的名称。 <br> **例如：**"myImage.jpg" |
| 文件夹中的文件 | 如果该文件不在当前文件夹或北太天元路径下的文件夹中，则指定完整或相对路径名。 <br> **例如：**"C:\myFolder\myImage.png" <br> **例如：**"\imgDir\myImage.bmp"|

**数据类型：** `char` | `string`

### 输出参数
**<a id="P1"></a> info — 有关图形文件的信息**  
有关图形文件的信息，以结构体数组形式返回。`info` 中的字段集取决于文件和文件格式。下表描述了始终包含的字段。

| 字段名称 | 描述 | 值 |
| :----------------------- | :----------------------- | :----------------------- |
| Filename | 文件的名称。如果文件不在当前文件夹中，Filename 包含文件的完整路径。 | 字符向量 |
| FileModDate | 上次修改文件的日期。 | 字符向量 |
| FileSize | 文件大小。| 整数 |
| Format | 文件格式，以文件扩展名形式表示。 | 字符向量 |
| Width | 图像宽度（以像素为单位）。 | 整数 |
| Height | 图像高度（以像素为单位）。 | 整数 |

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imformats/imformats.html">imformats</a> | <a
href="../imread/imread.html">imread</a> | <a 
href="../imwrite/imwrite.html">imwrite</a> | <a 
href="../rawinfo/rawinfo.html">rawinfo</a>

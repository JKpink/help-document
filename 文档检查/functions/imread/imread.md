## imread
从图像文件读取图像

## 简介
[`A = imread(filename)`](#function1)  
 
## 用法
<a id="function1"></a>
[A](#P1) = imread[(filename)](#Q1) 从 `filename` 指定的文件读取图像，并从文件内容推断出其格式。如果 `filename` 为多图像文件，则 `imread` 读取该文件中的第一个图像。  

## 参数说明
### 输入参数
**<a id="Q1"></a> filename — 图像文件名**  
字符串标量 | 字符向量

图形文件的名称，指定为字符串标量或字符向量。
根据文件的位置，`filename` 可以采用下列形式之一。

| 位置 | 形式 |
| :----------------------- | :--------------------------- |
| 当前文件夹或北太天元路径上的文件夹 | 指定 `filename` 中文件的名称。 <br>  **例如：**"myImage.jpg" |
| 文件夹中的文件 | 如果该文件不在当前文件夹或北太天元路径下的文件夹中，则指定完整或相对路径名。 <br> **例如：**"C:\myFolder\myImage.png" <br> **例如：**"\imgDir\myImage.bmp"|

### 输出参数
**<a id="P1"></a> A — 图像数据**  
数组

图像数据，以数组的形式返回。如果图像数据有 m 行和 n 列，则：  

- 如果文件包含灰度图像，则 `A` 是一个 m×n 数组，其中包含的值表示图像中像素的强度。  
- 如果文件包含索引图像，则 `A` 是一个 m×n 数组，其中包含引用 map 的行的索引值。  
- 如果文件包含真彩色图像，则 `A` 是一个 m×n×3 数组。  
- 如果文件是一个包含使用 CMYK 颜色空间的彩色图像的 TIFF 文件，则 `A` 为 m×n×4 数组。

A 的类取决于图像数据的图像格式和位深。有关详细信息，请参阅[算法](#R1)。

## 详细信息
**位深**   
位深是指用于表示每个图像像素的位数。  
位深是通过将每样本位数与每像素样本数相乘而得。因此，使用每个颜色分量（或样本）8 位和每像素三个样本的格式的位深为 24。有时，与位深关联的样本大小可能不确定。例如，48 位的位深可以表示 6 个 8 位样本、4 个 12 位样本，或 3 个 16 位样本。请参阅[算法](#R1)了解样本大小信息以避免这种多义性。

## <a id="R1"></a> 算法
对于大多数图像文件格式，`imread` 对每个颜色平面使用 8 位或更少位来存储图像像素。此表列出了返回的图像数组 [A](#P1) 与文件格式使用的位深对应的数据类型。

| 文件中的位深 | imread 返回的数组的类 |
| :----------- | :----------- |
| 每像素 1 位 | logical |
| 每颜色平面 2 到 8 位 | uint8 |
| 每像素 9 位到 16 位 | uint16（BMP、JPEG、PNG 和 TIFF）<br> 对于 16 位的 BMP 压缩格式（5-6-5），北太天元返回 `uint8`。 |

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../fread/fread.html">fread</a> | <a
href="../image/image.html">image</a> | <a 
href="../imfinfo/imfinfo.html">imfinfo</a> | <a 
href="../imformats/imformats.html">imformats</a> | <a 
href="../imwrite/imwrite.html">imwrite</a> | <a 
href="../ind2rgb/ind2rgb.html">ind2rgb</a> | <a 
href="../tiffreadVolume/tiffreadVolume.html">tiffreadVolume </a>

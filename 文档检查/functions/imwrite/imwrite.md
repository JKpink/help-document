## imwrite
将图像写入图像文件

## 简介
[`imwrite(A, filename)`](#function1)  
[`imwrite(A, map, filename)`](#function2)   

## 用法
<a id="function1"></a>
imwrite([A](#Q1), [filename](#Q2)) 将图像数据 `A` 写入 `filename` 指定的文件，并从扩展名推断出文件格式。`imwrite` 在当前文件夹中创建新文件。输出图像的位深取决于 `A` 的数据类型和文件格式。对于大多数格式来说：

- 如果 `A` 的数据类型为 `uint8`，则 `imwrite` 输出 8 位值。  
- 如果 `A` 的数据类型为 `uint16` 且输出文件格式支持 16 位数据（JPEG、PNG、TIFF），则 `imwrite` 将输出 16 位的值。如果输出文件格式不支持 16 位数据，则 `imwrite` 返回错误。  
- 如果 `A` 是灰度图像或者属于数据类型 `double` 或 `single` 的 RGB 彩色图像，则 `imwrite` 假设动态范围是 [0, 1]，并在将其作为 8 位值写入文件之前自动按 255 缩放数据。如果 `A` 中的数据是 `single`，则在将其写入 GIF 或 TIFF 文件之前将 `A` 转换为 `double`。  
- 如果 `A` 的数据类型为 `logical`，则 `imwrite` 会假定数据为二值图像并将数据写入位深为 1 的文件（如果格式允许）。BMP、PNG 或 TIFF 格式以输入数组形式接受二值图像。  

如果 `A` 包含索引图像数据，则应另外指定 [map](#Q3) 输入参量。  
<a id="function2"></a>
imwrite([A](#Q1), [map](#Q3), [filename](#Q2))将 A 中的索引图像及其关联的颜色映射表 `map` 写入由 `filename` 指定的文件。  

- 如果 `A` 是属于数据类型 `double` 或 `single` 的索引图像，则 `imwrite` 通过从每个元素中减去 1 来将索引转换为从 0 开始的索引，然后以 `uint8` 形式写入数据。  
- 如果 `A` 中的数据是 `single`，则在将其写入 GIF 或 TIFF 文件之前将 `A` 转换为 `double`。  

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 图像数据**  
矩阵

图像数据，指定为满（非稀疏）矩阵。

- 对灰度图像而言，`A` 可以是 m×n。
- 对索引图像而言，`A` 可以是 m×n。指定 [map](#Q3) 输入参量中的相关颜色表。
- 对真彩色图像而言，`A` 必须是 m×n×3 的矩阵。`imwrite` 不支持将 RGB 图像写入 GIF 文件。

对于 TIFF 文件而言，`A` 可以是 m×n×4 数组，其中包含使用 CMYK 颜色空间的颜色数据。  
对于多帧 GIF 文件而言，`A` 可以是包含灰度图像或索引图像的 m×n×1×p 数组，其中 p 是写入帧的数量。这种情况不支持 RGB 图像。

**数据类型：** `double` | `single` | `uint8` | `uint16` | `logical`

**<a id="Q2"></a> filename — 输出文件名**  
字符串标量 | 字符向量

输出文件的名称，指定为字符串标量或字符向量。  
根据您写入的位置，`filename` 可以采用以下形式之一。

| 位置 | 形式 |
| :----------------------- | :----------------------- |
| 当前文件夹或北太天元路径上的文件夹 | 指定 `filename` 中文件的名称。 <br>  **例如：**"myImage.jpg" |
| 文件夹中的文件 | 如果该文件不在当前文件夹或北太天元路径下的文件夹中，则指定完整或相对路径名。 <br> **例如：**"C:\myFolder\myImage.png" <br> **例如：**"\imgDir\myImage.bmp"|

**数据类型：** `char` | `string`

**<a id="Q3"></a> map — 索引图像的颜色映射表**  
m×3 数组

[A](#Q1) 中与索引图像数据相关联的颜色映射表，指定为 m×3 数组。`map` 必须是有效的北太天元颜色映射表。大多数图像文件格式都不支持条目数超过 256 个的颜色映射表。  

**示例：** [0,0,0; 0.5,0.5,0.5; 1,1,1]  
**示例：** jet(60)  
**数据类型：** `double`

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../fread/fread.html">fread</a> | <a
href="../getframe/getframe.html">getframe</a> | <a 
href="../imfinfo/imfinfo.html">imfinfo</a> | <a 
href="../imformats/imformats.html">imformats</a> | <a 
href="../imread/imread.html">imread</a> | <a 
href="../Tiff/Tiff.html">Tiff</a>

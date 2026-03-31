## centerCropWindow2d
创建矩形中心裁剪窗口

## 简介
[ `win = centerCropWindow2d(inputSize, targetSize)`](#function1)  
## 用法
<a id="function1"></a>
[win](#P1) = centerCropWindow2d([inputSize](#Q1), [targetSize](#Q2)) 根据输入二维图像的尺寸 `inputSize` 和目标尺寸 `targetSize`，计算居中裁剪窗口的坐标范围。计算出的窗口位于输入图像的中心区域，确保裁剪后图像尺寸精确匹配目标尺寸。  
 

## 参数说明
### 输入参数
**<a id="Q1"></a> inputSize — 输入图像大小**  
2 元正整数向量 | 3 元正整数向量

输入图像大小，指定为以下之一。  

| 输入图像类型 | 	输入图像格式 |
| :----------- | :----------- |
| 二维灰度或二值图像 | 2 元正整数向量的格式为 [height width] | 
| 二维 RGB 或多光谱图像 | 3 元正整数向量的格式为 [height width channels] | 

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q2"></a> targetSize — 目标图像大小**  
2 元正整数向量 | 3 元正整数向量

目标图像大小，指定为以下之一。  

| 输入图像类型 | 	输入图像格式 |
| :----------- | :----------- |
| 二维灰度或二值图像 | 2 元正整数向量的格式为 [height width] | 
| 二维 RGB 或多光谱图像 | 3 元正整数向量的格式为 [height width channels] | 

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` 


### 输出参数
**<a id="P1"></a> win — 裁剪窗口**  
Rectangle 对象

裁剪窗口，返回 Rectangle 对象。

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../centerCropWindow3d/centerCropWindow3d.html">centerCropWindow3d</a> | <a
href="../randomWindow2d/randomWindow2d.html">randomWindow2d</a> | <a
href="../imcrop/imcrop.html">imcrop</a>
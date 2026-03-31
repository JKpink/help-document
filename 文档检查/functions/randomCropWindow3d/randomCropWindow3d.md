## randomCropWindow3d  
创建随机立方体裁剪窗口  
  
## 简介  
[`win = randomCropWindow3d(inputSize, targetSize)`](#function1)  
  
## 用法  
<a id="function1"></a> [win](#P1) = randomCropWindow3d([inputSize](#P2), [targetSize](#P3)) 该函数用于确定从大小为`inputSize`的三维输入图像中裁剪的窗口，使得裁剪后图像的大小为`targetSize`。其中，窗口的坐标是从输入图像内的随机位置中选取的。  
  
## 参数说明
### 输入参数  
**<a id="P2"></a> inputSize — 输入图像大小**   
3 元素正整数向量 | 4 元素正整数向量  
  
输入图像大小，指定为以下形式之一：  
  
| **输入图像类型** | **`inputSize` 格式** |
| --- | ---|
| 三维灰度或二值图像 | 3 元素正整数向量，格式为 `[height width depth]` |
| 三维 RGB 或多光谱图像 | 4 元素正整数向量，格式为 `[height width depth channels]` |
  
**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` `  
  
**<a id="P3"></a> targetSize — 目标图像大小**  
  
目标图像大小，指定为以下形式之一 :   
  
| **目标图像类型** | **`targetSize` 格式** |
| --- | --- |
| 三维灰度或二值图像 | 3 元素正整数向量，格式为 `[height width depth]` |
| 三维 RGB 或多光谱图像 | 4 元素正整数向量，格式为 `[height width depth channels]` |
  
**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` `   
### 输出参数  
**<a id="P1"></a> win — 裁剪窗口**  
`Cuboid` 对象  
  
裁剪窗口，指定为 <a href="../Cuboid/Cuboid.html">Cuboid</a>  </a>对象。  
  
## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../centerCropWindow3d/centerCropWindow3d.html">centerCropWindow3d</a> | <a 
href="../randomWindow2d/randomWindow2d.html">randomWindow2d</a> | <a 
href="../imcrop3/imcrop3.html">imcrop3</a>  
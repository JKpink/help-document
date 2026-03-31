## bwconveximage 
二值图像区域凸包图像

## 简介
[ `Stats = bwconveximage(BW)`](#function1) 

## 用法
<a id="function1"></a>
[Stats](#Q1) = bwconveximage([BW](#Q2)) 指定凸包的图像，凸包内的所有像素均被填充（设置为 on），以 n×1 元胞数组形式返回。

## 参数说明
### 输入参数

**<a id="Q2"></a>BW — 二值图像**  
逻辑数组

二值图像，指定为二维的逻辑数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数
**<a id="Q1"></a>Stats —  凸包掩膜**  
逻辑数组

以 n×1 元胞数组形式返回，图像大小与区域边界框的大小相同。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../bwconvexarea/bwconvexarea.html">bwconvexarea</a> | <a 
href="../bwconvhull/bwconvhull.html">bwconvhull</a> | <a 
href="../regionprops/regionprops.html">regionprops</a>
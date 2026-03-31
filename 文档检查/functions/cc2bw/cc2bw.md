## cc2bw  
将连通分量转换为二值图像

## 简介  
[`BW = cc2bw(CC)`](#function1)  
[`BW = cc2bw(CC, objectsToKeep)`](#function2)

## 用法  
<a id="function1"></a>
[BW](#Q1) = cc2bw([CC](#Q2)) 根据连通分量（对象）[`CC`](#Q2) 创建二值图像  
<a id="function2"></a>
[BW](#Q1) = cc2bw([CC](#Q2), [objectsToKeep](#Q3)) 根据指定的需保留对象子集 [`objectsToKeep`](#Q3)，从连通分量创建二值图像

## 参数说明  
### 输入参数  
**<a id="Q2"></a> CC — 连通分量**  
结构体

连通分量（对象），指定为包含四个字段的结构体。

| **字段** | **说明** |
|:-|:-|
Connectivity | 连通分量的连通性
ImageSize | 二值图像的尺寸
NumObjects | 二值图像中的连通分量数量
PixelIdxList | 1 × NumObjects 的元胞数组，其中第 `k` 个元胞元素是包含第 `k` 个对象像素线性索引的向量

**<a id="Q3"></a> objectsToKeep — 需保留对象**  
正整数 | 正整数向量 | 逻辑向量

需保留对象，指定为以下值之一：

- 正整数或正整数向量——保留索引包含在 `objectsToKeep` 中的对象。`objectsToKeep` 的长度需小于或等于 `CC.NumObjects`.

- 逻辑向量——保留 `objectsToKeep` 中对应元素为 `true` 的对象。`objectsToKeep` 的长度必须等于 `CC.NumObjects`.

### 输出参量  
**<a id="Q1"></a> BW — 二值图像**  
逻辑数组

二值图像，以逻辑数组形式返回，其尺寸与 `CC.ImageSize` 相同。

**数据类型：** `logical`

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
 <a href="../bwconncomp/bwconncomp.html">bwconncomp</a> | <a 
href="../bwpropfilt/bwpropfilt.html">bwpropfilt</a> | <a 
href="../regionprops/regionprops.html">regionprops</a> 

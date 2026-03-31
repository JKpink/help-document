## bwsolidity  
二值图像区域凸包中区域内像素所占比例

## 简介  
[ `Stats = bwsolidity(BW)`](#function1) 
## 用法  
<a id="function1"></a>
[Stats](#Q1) = bwsolidity([BW](#Q2))   
计算二值图像中连通目标区域的实度（Solidity），即目标区域实际像素面积与其凸包包围区域面积的比值，用于量化目标区域的紧凑程度与凸性特征。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>BW — 二值图像**  
逻辑数组

二值图像，要求为二维的逻辑数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`
### 输出参数
**<a id="Q1"></a>Stats — 比例**  
数值标量

凸包中区域内像素所占的比例，以标量形式返回。  
实度计算为$bwarea/bwconvexArea$，其中分子为目标区域实际像素面积，分母为该区域最小凸包的包围面积。  
实度越接近 1，说明目标区域形状越接近凸多边形，凹陷、缺口越少；实度越小，说明区域存在明显凹陷、镂空或不规则缺口。

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../bwpixellist/bwpixellist.html">bwpixellist</a> | <a 
href="../bwpixelidxlist/bwpixelidxlist.html">bwpixelidxlist</a> | <a 
href="../bwarea/bwarea.html">bwarea</a> | <a 
href="../bwconvexArea/bwconvexArea.html">bwconvexArea</a> | <a 
href="../regionprops/regionprops.html">regionprops</a>
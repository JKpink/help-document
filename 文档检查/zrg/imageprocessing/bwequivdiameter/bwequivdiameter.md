## bwequivdiameter 
与二值图像区域面积相同的圆的直径

## 简介
[ `Stats = bwequivdiameter(BW)`](#function1) 

## 用法
<a id="function1"></a>
[Stats](#Q1) = bwequivdiameter([BW](#Q2)) 与区域面积相同的圆的直径，以1×n 向量形式返回。

## 参数说明
### 输入参数

**<a id="Q2"></a>BW — 二值图像**  
逻辑数组

二值图像，指定为二维逻辑数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数
**<a id="Q1"></a>Stats — 直径**  
1×n 向量

与区域面积相同的圆的直径，以1×n 向量形式返回。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../bwarea/bwarea.html">bwarea</a> | <a 
href="../regionprops/regionprops.html">regionprops</a>
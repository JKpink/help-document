## bweccentricity
与二值图像区域具有相同二阶矩的椭圆的偏心率

## 简介
[ `Stats = bweccentricity(BW)`](#function1) 

## 用法
<a id="function1"></a>
[Stats](#Q1) = bweccentricity([BW](#Q2)) 与区域具有相同二阶矩的椭圆的偏心率，以 1×n 向量形式返回。

## 参数说明
### 输入参数

**<a id="Q2"></a>BW — 二值图像**  
逻辑数组

二值图像，指定为二维逻辑数组

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

### 输出参数
**<a id="Q1"></a>Stats — 偏心率**  
1×n 向量

偏心率是椭圆焦距与其长轴的比值，该值介于 0 和 1 之间。（0 和 1 是特例，偏心率为 0 的椭圆其实是圆，偏心率为 1 的椭圆是线段。）

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../bworientation/bworientation.html">bworientation</a> | <a 
href="../regionprops/regionprops.html">regionprops</a>
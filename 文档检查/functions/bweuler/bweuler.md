## bweuler 
二值图像的欧拉数

## 简介
[ `eul = bweuler(BW, conn)`](#function1)

## 用法
<a id="function1"></a>
[eul](#Q1) = bweuler([BW](#Q2), [conn](#Q3)) 返回二值图像 `BW` 的欧拉数。欧拉数（也称为欧拉特性）是图像中对象的总数减去这些对象中的孔总数。conn 指定连通方式。目标是值为 1 的像素的连通集合。

## 参数说明
### 输入参数

**<a id="Q2"></a>BW — 二值图像**  
二维数值矩阵 | 二维逻辑矩阵

二值图像，指定为二维数值矩阵或二维逻辑矩阵。对于数值输入，任何非零像素均被视为 1 (true)。
**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `logical`

**<a id="Q3"></a>conn — 连通性**  
8（默认）| 4

连通性，指定为 4 连通对象的值为 4 或 8 连通对象的值为 8。

**数据类型：** `double`

### 输出参数
**<a id="Q1"></a>eul — 欧拉数**  
数值标量

欧拉数，以数值标量形式返回。

**数据类型：** `double`


## 参考文献
[1] Horn B P K. Robot Vision. New York: McGraw-Hill, 1986: 73-77.
Pratt W K. Digital Image Processing. New York: John Wiley & Sons, Inc., 1991: 633.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../bwperim/bwperim.html">bwperim</a> | <a
href="../bwmorph/bwmorph.html">bwmorph</a>
## imhistmatchn
N维图像直方图匹配

## 简介
[ `J = imhistmatchn(I, ref)`](#function1)  
[ `J = imhistmatchn(I, ref, nbins)`](#function2)  

## 用法
<a id="function1"></a>
[J](#Q4) = imhistmatchn([I](#Q1), [ref](#Q2)) 对N 维灰度图像 I 进行变换，返回一幅直方图与参考图像ref的直方图近似匹配的图像。输入图像 I 和参考图像ref都必须是灰度图像，但二者的数据类型、尺寸和维度数量可以不同。  
<a id="function2"></a>
[J](#Q4) = imhistmatchn([I](#Q1), [ref](#Q2),[nbins](#Q3)) 在相应的数值范围内采用 nbins 个等距区间划分直方图，输出图像J的离散灰度级数量不超过 nbins 个。  
不同数据类型图像对应的直方图数值范围如下：    
- 若图像数据类型为 single 或 double，直方图数值范围为 [0, 1]  
- 若图像数据类型为 uint8，直方图数值范围为 [0, 255]  
- 若图像数据类型为 uint16，直方图数值范围为 [0, 65535]  
- 若图像数据类型为 int16，直方图数值范围为 [-32768, 32767]

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
N 维灰度图像

待进行直方图变换的输入图像，指定为一幅 N 维灰度图像。对于数据类型为double和single的图像，`imhistmatchn` 函数要求其数值范围必须在 [0, 1] 内。若图像I的数值超出该范围，可使用 `rescale` 函数将其缩放到要求的数值区间。

**数据类型**：`single` | `double` | `int16` |  `uint8` | `uint16` 

**<a id="Q2"></a> ref — 参考图像**  
灰度图像

提供参考直方图的参考图像，指定为一幅灰度图像。该图像的直方图会被划分为 [nbins](#Q3) 个等距区间，作为输出图像 [J](#Q5) 的直方图匹配目标。  
对于数据类型为double和single的参考图像，`imhistmatchn` 函数要求其数值范围必须在 [0, 1] 内。

**数据类型**： `single` | `double` | `int16` |  `uint8` | `uint16`

**<a id="Q3"></a> nbins — 参考直方图的等距区间数量**   
64（默认值）| 正整数

参考直方图划分的等距区间数量，指定为一个正整数。该参数同时也是输出图像 [J](#Q5) 中离散灰度级数量的上限值。

**数据类型**： `double`

### 输出参数
**<a id="Q5"></a> J — 输出图像**    
N 维灰度图像

直方图匹配后的输出图像，返回为一幅 N 维灰度图像。该图像由输入图像 [I](#Q1) 变换得到，其直方图与参考图像 [ref](#Q2) 的直方图（划分为nbins个等距区间）近似匹配。输出图像 J 与输入图像 I 的尺寸和数据类型完全相同，其离散灰度级数量不超过参数 [nbins](#Q4) 的取值。

**数据类型**： `single` | `double` | `int16` |  `uint8` | `uint16`

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../imhistmatch/imhistmatch.html">imhistmatch</a> | <a href="../histeq/histeq.html">histeq</a> | <a href="../imadjust/imadjust.html">imadjust</a> | <a href="../imhist/imhist.html">imhist</a>
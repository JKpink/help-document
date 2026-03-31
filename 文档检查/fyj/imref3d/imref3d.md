## imref3d
将三维图像参考到世界坐标

## 简介  
[`R = imref3d`](#function1)  
[`R = imref3d(imageSize)`](#function2)  
[` R = imref3d(imageSize, pixExtentWorldX, pixExtentWorldY, pixExtentWorldZ`)](#function3)  
[`R = imref3d(imageSize, xWorldLim, yWorldLim, zWorldLim)`](#function4)

## 用法  
<a id="function1"></a> [R](#P1) = imref3d 创建一个带有默认属性设置的 `imref3d` 对象。   
<a id="function2"></a> [R](#P1) = imref3d([imageSize](#Q1)) 指定图像在各空间维度的大小。  
<a id="function3"></a> [R](#P1) = imref3d([imageSize](#Q1), [pixExtentWorldX](#Q2), [pixExtentWorldY](#Q3), [pixExtentWorldZ](#Q4)) 在指定图像大小的基础上，进一步定义单个像素在世界坐标系下 `x` 方向、 `y` 方向和 `z` 方向的空间范围。  
<a id="function4"></a> R = imref3d([imageSize](#Q1), [xWorldLim](#Q5), [yWorldLim](#Q6), [zWorldLim](#Q7)) 在指定图像大小的基础上，进一步定义图像在世界坐标系下 `x` 方向、 `y` 方向和 `z` 方向的空间范围。  
## 参数说明
### 输入参数  
**<a id="Q1"></a> imageSize — 各空间维度的元素数量**  
3 元素正整数行向量  

各空间维度的元素数量，指定为 3 元素正整数行向量。`imageSize` 的格式与 <a href="../size/size.html">size</a>  </a> 函数返回值相同。  
该参数用于设置 [ImageSize](#Q8) 属性。

**数据类型：** `double`  
  
**<a id="Q2"></a> pixExtentWorldX — 单个像素在 x 方向的大小**  
正数  

单个像素在世界坐标系下 `x` 方向的大小，指定为正数。  
该参数用于设置 [PixelExtentInWorldX](#Q9) 属性。

**数据类型：** `double`  
  
**<a id="Q3"></a> pixExtentWorldY — 单个像素在 y 方向的大小**  
正数  

单个像素在世界坐标系下 `y` 方向的大小，指定为正数。  
该参数用于设置 [PixelExtentInWorldY](#Q10) 属性。

**数据类型：** `double`  
  
**<a id="Q4"></a> pixExtentWorldZ — 单个像素在 z 方向的大小**  
正数  

单个像素在世界坐标系下 `z` 方向的大小，指定为正数。  
该参数用于设置 [PixelExtentInWorldZ](#Q11) 属性。

**数据类型：** `double`


**<a id="Q5"></a> xWorldLim — 图像在世界坐标系 x 方向的空间范围**  
2 元素数值行向量
  
图像在世界坐标系 `x` 方向的空间范围，指定为 2 元数值行向量 [xMin xMax]。  
该参数用于设置 [XWorldLimits](#Q12) 属性。

**数据类型：** `double`  
  
**<a id="Q6"></a> yWorldLim — 图像在世界坐标系 y 方向的空间范围**  
2 元素数值行向量
  
图像在世界坐标系 `y` 方向的空间范围，指定为 2 元数值行向量 [yMin yMax]。  
该参数用于设置 [YWorldLimits](#Q13) 属性。  
  
**数据类型：** `double`  
  
**<a id="Q7"></a> zWorldLim — 图像在世界坐标系 z 方向的空间范围**  
2 元素数值行向量
  
图像在世界坐标系 `z` 方向的空间范围，指定为 2 元数值行向量 [zMin zMax]。  
该参数用于设置 [ZWorldLimits](#Q14) 属性。  
  
**数据类型：** `double`     

###  输出参数
**<a id="P1"></a> R — 三维空间参考对象**  
`imref3d` 对象  
  
三维空间参考对象，指定为一个 `imref3d` 对象。

## 属性  
**ImageExtentInWorldX — 图像在世界坐标系 x 方向的跨度**  
数值标量  
  
图像在世界坐标系 `x` 方向的跨度，指定为一个数值标量。`imref3d` 对象将此值设为 `PixelExtentInx` * `ImageSize(2)`。  

**数据类型：** `double`
  
**ImageExtentInWorldY — 图像在世界坐标系 y 方向的跨度**  
数值标量  
  
图像在世界坐标系 `y` 方向的跨度，指定为一个数值标量。`imref3d` 对象将此值设为 `PixelExtentInY` * `ImageSize(1)`。  

**数据类型：** `double`  
  
**ImageExtentInWorldZ — 图像在世界坐标系 z 方向的跨度**  
数值标量  
  
图像在世界坐标系 `z` 方向的跨度，指定为一个数值标量。`imref3d` 对象将此值设为 `PixelExtentInZ` * `ImageSize(3)`。  

**数据类型：** `double`  
  
**<a id="Q8"></a> ImageSize — 各空间维度的元素数量**  
3 元素正整数行向量  
  
各空间维度的元素数量，指定为 3 元素正整数行向量。`imageSize` 的格式与 <a href="../size/size.html">size</a>  </a> 函数返回值相同。  
  
**数据类型：** `double`  

**<a id="Q9"></a> PixelExtentInWorldX — 单个像素在世界坐标系 x 方向的大小**  
正数  
  
单个像素在世界坐标系 `x` 方向的大小，指定为正数。  
  
**数据类型：** `double`  
  
**<a id="Q10"></a> PixelExtentInWorldY — 单个像素在世界坐标系 y 方向的大小**  
正数  
  
单个像素在世界坐标系 `y` 方向的大小，指定为正数。  
  
**数据类型：** `double`  
  
**<a id="Q11"></a> PixelExtentInWorldZ — 单个像素在世界坐标系 z 方向的大小**  
正数  
  
单个像素在世界坐标系 `z` 方向的大小，指定为正数。  
  
**数据类型：** `double`  
  
**<a id="Q12"></a> XWorldLimits — 图像在世界坐标系 x 方向的空间范围**  
2 元素数值行向量  
  
图像在世界坐标系 `x` 方向的空间范围，指定为 2 元素数值行向量 [xMin xMax]。 
  
**数据类型：** `double`  
  
**<a id="Q13"></a> YWorldLimits — 图像在世界坐标系 y 方向的空间范围**  
2 元素数值行向量  
  
图像在世界坐标系 `y` 方向的空间范围，指定为 2 元素数值行向量 [yMin yMax]。 
  
**数据类型：** `double`  
  
**<a id="Q14"></a> ZWorldLimits — 图像在世界坐标系 z 方向的空间范围**  
2 元素数值行向量  
  
图像在世界坐标系 `z` 方向的空间范围，指定为 2 元素数值行向量 [zMin zMax]。 
  
**数据类型：** `double`  
  
**XIntrinsicLimits — 图像在固有坐标系 x 方向的空间范围**  
2 元素行向量  
  
图像在固有坐标系 `x` 方向的空间范围，指定为 2 元素行向量 [xMin xMax]。对于 m × n × p 图像，`XIntrinsicLimits`固定为 [0.5, n+0.5]。  
  
**数据类型：** `double`  
  
**YIntrinsicLimits — 图像在固有坐标系 y 方向的空间范围**  
2 元素行向量  
  
图像在固有坐标系 `y` 方向的空间范围，指定为 2 元素行向量 [yMin yMax]。对于 m × n × p 图像，`YIntrinsicLimits`固定为 [0.5, m+0.5]。 
 
**数据类型：** `double`  
  
**ZIntrinsicLimits — 图像在固有坐标系 z 方向的空间范围**  
2 元素行向量  
  
图像在固有坐标系 `z` 方向的空间范围，指定为 2 元素行向量 [zMin zMax]。对于 m × n × p 图像，`ZIntrinsicLimits`固定为 [0.5, p+0.5]。 
 
**数据类型：** `double`      


## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../imref2d/imref2d.html">imref2d</a> | <a
href="../imregister/imregister.html">imregister</a> 
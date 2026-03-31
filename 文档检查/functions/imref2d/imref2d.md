## imref2d
将二维图像参考到世界坐标

## 简介  
[`R = imref2d`](#function1)   
[`R = imref2d(imageSize)`](#function2)  
[`R = imref2d(imageSize, pixExtentWorldX, pixExtentWorldY)`](#function3)  
[`R = imref2d(imageSize, xWorldLim, yWorldLim)`](#function4)

## 用法  
<a id="function1"></a> [R](#P1) = imref2d 创建一个带有默认属性设置的 `imref2d` 对象。  
<a id="function2"></a> [R](#P1) = imref2d([imageSize](#Q1)) 指定图像在各空间维度的大小。  
<a id="function3"></a> [R](#P1) = imref2d([imageSize](#Q1), [pixExtentWorldX](#Q2), [pixExtentWorldY](#Q3)) 在指定图像大小的基础上，进一步定义单个像素在世界坐标系下 `x` 方向和 `y` 方向的空间范围。  
<a id="function4"></a> [R](#P1) = imref2d([imageSize](#Q1), [xWorldLim](#Q4), [yWorldLim](#Q5)) 在指定图像大小的基础上，进一步定义图像在世界坐标系下 `x` 方向和 `y` 方向的空间范围。 

## 参数  
### 输入参数  
**<a id="Q1"></a> imageSize — 各空间维度的元素数量**  
2 元素正整数行向量  

各空间维度的元素数量，指定为 2 元素正整数行向量。`imageSize` 的格式与 <a href="../size/size.html">size</a>  </a> 函数返回值相同。  
该参数用于设置 [ImageSize](#Q6) 属性。

**数据类型：** `double`  

**<a id="Q2"></a> pixExtentWorldX — 单个像素在 x 方向的大小**  
正数  
  
单个像素在世界坐标系下 `x` 方向的大小，指定为正数。  
该参数用于设置 [PixelExtentInWorldX](#Q7) 属性。

**数据类型：** `double`

**<a id="Q3"></a> pixExtentWorldY — 单个像素在 y 方向的尺寸**  
正数  

单个像素在世界坐标系下 `y` 方向的大小，指定为正数。  
该参数用于设置 [PixelExtentInWorldY](#Q8) 属性。

**数据类型：** `double`

**<a id="Q4"></a> xWorldLim — 图像在世界坐标系 x 方向的空间范围**  
2 元素数值行向量  

图像在世界坐标系 `x` 方向的空间范围，指定为 2 元素数值行向量 [xMin xMax]。  
该参数用于设置 [XWorldLimits](#Q9) 属性。

**数据类型：** `double`

**<a id="Q5"></a> yWorldLim — 图像在世界坐标系 y 方向的空间范围**  
2 元素数值行向量  

图像在世界坐标系 `y` 方向的空间范围，指定为 2 元数数值行向量 [yMin yMax]。  
该参数用于设置 [YWorldLimits](#Q10) 属性。  
  
**数据类型：** `double`  
  
## 输出参数  
**<a id="P1"></a> R — 二维空间参考对象**  
`imref2d` 对象  
  
二维空间参考对象，指定为一个 `imref2d` 对象。  
  
## 属性  
**ImageExtentInWorldX — 图像在世界坐标系 x 方向的跨度**  
数值标量  
  
图像在世界坐标系 `x` 方向的跨度，指定为一个数值标量。`imref2d` 对象将此值设为 `PixelExtentInx` * `ImageSize(2)`。  

**数据类型：** `double`  
  
**ImageExtentInWorldY — 图像在世界坐标系 y 方向的跨度**  
数值标量  
  
图像在世界坐标系 `y` 方向的跨度，指定为一个数值标量。`imref2d` 对象将此值设为 `PixelExtentInY` * `ImageSize(1)`。  

**数据类型：** `double`  
  
**<a id="Q6"></a> ImageSize — 各空间维度的元素数量**  
2 元素正整数行向量  
  
各空间维度的元素数量，指定为 2 元素正整数行向量。`imageSize` 的格式与 <a href="../size/size.html">size</a>  </a> 函数返回值相同。  
  
**数据类型：** `double`  
  
**<a id="Q7"></a> PixelExtentInWorldX — 单个像素在世界坐标系 x 方向的大小**  
正数  
  
单个像素在世界坐标系 `x` 方向的大小，指定为正数。  
  
**数据类型：** `double`   
  
**<a id="Q8"></a> PixelExtentInWorldY — 单个像素在世界坐标系 y 方向的大小**  
正数  
  
单个像素在世界坐标系 `y` 方向的大小，指定为正数。  
  
**数据类型：** `double`  
  
**<a id="Q9"></a> XWorldLimits — 图像在世界坐标系 x 方向的空间范围**  
2 元素数值行向量  
  
图像在世界坐标系 `x` 方向的空间范围，指定为 2 元素数值行向量 [xMin xMax]。 
  
**数据类型：** `double`  
  
**<a id="Q10"></a> YWorldLimits — 图像在世界坐标系 y 方向的空间范围**  
2 元素数值行向量  
  
图像在世界坐标系 `y` 方向的空间范围，指定为 2 元素数值行向量 [yMin yMax]。 
  
**数据类型：** `double`  
  
**XIntrinsicLimits — 图像在固有坐标系 x 方向的空间范围**  
2 元素行向量  
  
图像在固有坐标系 `x` 方向的空间范围，指定为 2 元素行向量 [xMin xMax]。对于 m × n（或 m × n × p）图像，`XIntrinsicLimits` 固定为 [0.5, n+0.5]。  
  
**数据类型：** `double`   
  
**YIntrinsicLimits — 图像在固有坐标系 y 方向的空间范围**  
2 元素行向量  
  
图像在固有坐标系 `y` 方向的空间范围，指定为 2 元素行向量 [yMin yMax]。对于 m × n（或 m × n × p）图像，`YIntrinsicLimits` 固定为 [0.5, m+0.5]。 
 

**数据类型：** `double`                 


## 提示
- 你可以为 RGB 图像创建一个 `imref2d` 对象。如果在创建对象时将 `ImageSize` 属性指定为一个三元素向量（例如 <a href="../size/size.html">size</a>  </a> 函数返回的向量)，则只有前两个元素会被用于设置 `ImageSize`。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imref3d/imref3d.html">imref3d</a> | <a
href="../imwarp/imwarp.html">imwarp</a> | <a 
href="../imshow/imshow.html">imshow</a> 
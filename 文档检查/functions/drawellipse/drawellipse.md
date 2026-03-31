## drawellipse 
创建椭圆形 ROI

## 描述
函数创建一个 ellipse 对象，用于指定椭圆形感兴趣区域 (ROI) 的大小和位置。可通过使用名称 — 值参数指定 ROI 的初始外观和行为。

## 简介
[`J = drawellipse(I, center, s, rot)`](#function1)  
[`J = drawellipse(I, center, s)`](#function2)  
[`J = drawellipse(_, Name, Value)`](#function3)

## 用法
<a id="function1"></a>
[J](#Q6) = drawellipse([I](#Q1), [center](#Q2), [s](#Q3), [rot](#Q4)) 创建一个 ellipse 对象。需要指定椭圆形的中心 `'Center'`，椭圆半轴的长度`'Semiaxes'`以及围绕 ROI 中心的角度`'RotationAngle'`。     
<a id="function2"></a>
[J](#Q6) = drawellipse([I](#Q1), [center](#Q2), [s](#Q3))   创建一个 ellipse 对象。需要指定椭圆形的中心 `'Center'`以及椭圆半轴的长度 `'Semiaxes'`。  
<a id="function3"></a>
[J](#Q6) = drawellipse(_, [Name, Value](#Q5))  使用一个或多个名称 — 值参数自定义 ROI 的外观和行为。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
灰度图像 | RGB 图像

指定为灰度或 RGB 图像。

**数据类型**： `uint8`

**<a id="Q2"></a> center — ROI的中心**  
1×2 数值向量

ROI 的中心，指定为 1×2 形式的数字向量 [x y]。

**<a id="Q3"></a> s — 椭圆的半轴长度** 
1×2 数值向量

指定为 `[semiaxis1 semiaxis2]` 形式的 1×2 数值向量。ellipse 对象将最接近 x 方向的半轴长度分配给 `semiaxis1`。

**<a id="Q4"></a>rot — 围绕 ROI中心的角度**  
0（默认）| 非负数值标量  

围绕 ROI 中心的角度 `RotationAngle`，指定为非负数值标量。该角度以顺时针方向的度数为单位进行测量。`RotationAngle` 的值不会影响 `Position` 的值。`Position` 属性表示旋转前 ROI 的初始位置。

**<a id="Q5"></a> 名称 — 值参数**  
将可选的参量对组指定为 Name1, Value1, ..., NameN, ValueN，其中 Name 是参量名称，Value 是对应的值。名称 — 值参量必须出现在其他参量之后，但参量对组的顺序无关紧要。

**Color — 线条颜色**  
颜色名称 | 短名称 | 十六进制颜色代码 

线条颜色，指定为颜色名称或短名称或十六进制颜色代码。
可以按名称指定一些常见的颜色。下表列出了命名颜色选项。

| **颜色名称** | **短名称** | **十六进制颜色代码**|
|:-|:-|:-|
|"red"|"r"|"#FF0000"|
|"green"|"g"|"#00FF00"|	
|"blue"|"b"|"#0000FF"|
|"cyan"|"c"|"#00FFFF"|
|"magenta"|"m"	|"#FF00FF"|
|"yellow"|"y"|"#FFFF00"|
|"black"|"k"|"#000000"|
|"white"|"w"|"#FFFFFF"|    
**示例**： "Color","r"  
**示例**： "Color","green"

**LineWidth — ROI 边框**  
正数

ROI 边框的宽度，指定为以磅为单位的正数。默认值是每个屏幕像素点数的三倍，使得 border 为 3 像素宽。

**MarkerSize — 标记大小**   
正数

标记大小，指定为以磅为单位的正数。默认值为 8 乘以每个屏幕像素的点数，使得标记为 8 个像素大小。

### 输出参数
**<a id="Q6"></a> J — 输出图像**  
灰度图像 | RGB 图像

与输入图像 `I` 的大小和数据类型相同。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../Ellipse/Ellipse.html">Ellipse</a> | <a 
href="../drawcircle/drawcircle.html">drawcircle</a> 
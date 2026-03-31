## dip::figure
创建图形窗口

## 简介
[`dip::figure`](#function1)  
<!-- [`figure(Name, Value)`](#function2)   
[`f = figure(___)`](#function3)   
[`figure(f)`](#function4)   
[`figure(n)`](#function5)    -->

## 用法 
<a id="function1"></a> dip::figure 创建符合默认属性配置的新图窗窗口。  
<!-- <a id="function2"></a> figure([Name, Value](#Q1)) 通过名称-值参数对定制图窗属性。例如 figure('Color', 'white') 将窗口背景色设为白色。  
<a id="function3"></a> [f](#P1) = figure(___) 返回 Figure 对象。在创建图窗后可使用 `f` 查询或修改其属性。  
<a id="function4"></a> figure([f](#P1)) 将 `f` 指定的图窗作为当前图窗，并将其显示在其他所有图窗的上面。  
<a id="function5"></a> figure([n](#Q2)) 查找 Number 属性等于 `n` 的图窗，并将其作为当前图窗。若不存在具有该属性值的图窗，则创建一个新图窗并将其 Number 属性设置为 `n`。   -->

<!-- ## 参数说明
### 输入参数
**<a id="P1"></a> f — 目标图窗**  
Figure 对象

目标图窗，指定为 Figure 对象。

**<a id="Q2"></a> n — 目标图窗编号**  
整数标量值

目标图窗编号，指定为整数标量值。  
当指定此参数时，北太天元将检索现有图窗集合中 Number 属性等于 `n` 的对象。若不存在对应图窗，则创建新图窗并初始化其 Number 属性为 `n`。该属性值默认显示于图窗标题栏。  

**数据类型：** `double`  -->

<!-- ### <a id="Q1"></a> 名称-值参数
指定可选的参数对，格式为 Name1, Value1, ... , NameN, ValueN，其中 Name 是参数名称，Value 是对应的值。名称-值参数必须出现在其他参数之后，但各参数对的顺序可以任意。  
示例：figure("Color", "white") 创建具有白色背景的图窗。  

**Name — 图窗名称**  
' '（默认）| 字符向量 | 字符串标量  

图窗名称，指定为字符向量或字符串标量。   
默认情况下，名称为 'Figure n'，其中 n 是整数。如果指定 Name 属性，图窗的标题将变为 'Figure n: name'。若只显示 Name 值，需要将 NumberTitle 设置为 'off'。   
示例：figure('Name', 'Measured Data', 'NumberTitle', 'off');

**Color  — 背景颜色**  
RGB 三元组 | 十六进制颜色代码 | 'r' | 'g' | 'b' | ...

背景颜色，指定为 RGB 三元组、十六进制颜色代码、颜色名称或短名称。  
对于自定义颜色，请指定 RGB 三元组或十六进制颜色代码。

- RGB 三元组是包含三个元素的行向量，其元素分别指定颜色中红、绿、蓝分量的强度。强度值必须位于 [0, 1] 范围内，例如 [0.2 0.4 0.6]。
- 十六进制颜色代码是字符串标量或字符向量，以 # 开头，后跟三个或六个十六进制数字，范围是 0 到 F。这些值不区分大小写。因此，颜色代码 "#FF8800" 与 "#ff8800"、"#F80" 与 "#f80" 是等效的。

此外，还可以按名称指定一些常见的颜色。下表列出了一些命名颜色选项、其等效 RGB 三元组及十六进制颜色代码。

| **颜色名称** | **短名称** | **RGB 三元组** | **十六进制颜色代码** | **外观** |
| :----------- | :----------- | :----------- | :----------- | :----------- |
|"red" | 	"r"|[1 0 0]|	"#FF0000"|<img src="red.png" style="width:50%;" >|
| "green" | 	"g" | [0 1 0]|	"#00FF00"|<img src="green.png" style="width:50%;">|
| "blue" | "b" |[0 0 1]|"#0000FF"|<img src="blue.png" style="width:50%;">|
| "cyan" | 	"c" | [0 1 1]|	"#00FFFF"|<img src="cyan.png" style="width:50%;">|
|"magenta" | 	"m"|	[1 0 1]|	"#FF00FF"|<img src="magenta.png" style="width:50%;">|
| "yellow" | 	"y" | [1 1 0]|	"#FFFF00"|<img src="yellow.png" style="width:50%;">|
| "black" | "k" |	[0 0 0]|"#000000"|<img src="black.png" style="width:50%;">|
| "white" | 	"w" | [1 1 1]|	"#FFFFFF"|<img src="white.png" style="width:50%;">|

**数据类型：** `double` | `char`

**Position  — 图窗的位置和大小，不包括边框、图窗工具和标题栏**  
[left bottom width height]

图窗的位置和大小，不包括边框、图窗工具和标题栏，指定为 [left bottom width height] 形式的四元素向量。下表介绍该向量中的每个元素。

| **元素** | **描述** |
| :----------- | :----------- | 
|left |该属性定义为从主显示屏画面左边界到窗口内容区域左边界的垂直距离（以像素为单位）。在多显示器配置中，该值可能为负。当窗口处于停靠状态时，此距离的参考基准将切换为其父容器。|
| bottom | 该属性定义为从主显示屏画面下边界到窗口内容区域下边界的垂直距离（以像素为单位）。在多显示器配置中，该值可能为负。当窗口处于停靠状态时，此距离的参考基准将切换为其父容器。|
| width | 窗口的左右内部边缘之间的距离。 |
| height | 	窗口的上下内部边缘之间的距离。 | 

**Units  — 测量单位**  
'pixels'（默认）| 'normalized' | 'inches' | 'centimeters' | 'points' | 'characters'

测量单位，指定为下表中的值之一。

| **单位值** | **描述** |
| :----------- | :----------- | 
|'pixels' |像素。|
|  'normalized' | 该单位依据父容器进行归一化。容器的左下角映射到 (0, 0)，右上角映射到 (1, 1)。|
| 'inches' | 英寸。 |
| 'centimeters' | 		厘米。 | 
| 'points' | 	磅。1 磅等于 1/72 英寸。 | 
| 'characters' | 	单位基于图形根对象的默认 uicontrol 字体：<br>字符宽度 = 字母 x 的宽度。<br>字符高度 = 两个文本行的基线之间的距离。 |  -->


## 版本历史
在北太天元图像处理工具箱 V1.0 推出

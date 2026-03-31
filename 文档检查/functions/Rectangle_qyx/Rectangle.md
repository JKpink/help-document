## Rectangle
矩形 ROI 

## 简介
[`roi = Rectangle(p)`](#function1)  
[`roi = Rectangle(p, rot)`](#function2)

## 用法
<a id="function1"></a>
[roi](#Q3) = Rectangle([p](#Q1)) 创建一个 `Rectangle` 对象，并可以指定矩形的位置 `Position`。  
<a id="function2"></a>
[roi](#Q3) = Rectangle([p](#Q1), [rot](#Q2)) 创建一个 `Rectangle` 对象，并可以指定矩形的位置 `Position` 以及围绕 ROI 中心旋转的角度 `RotationAngle`。


## 参数说明
### 输入参数
**<a id="Q1"></a> p — ROI 的位置**  
1×4 数值向量

其中 ROI 的位置，指定为 [xmin, ymin, width, height] 形式的 1×4 数字向量。xmin 和 ymin 指定矩形左上角的位置。width 和 height 指定矩形在二维中的范围。

**<a id="Q2"></a> rot — 围绕 ROI中心的角度**  
0 (默认) | 非负数值标量

围绕 ROI 中心的角度 `RotationAngle`，指定为非负数值标量。该角度以顺时针方向的度数为单位进行测量。`RotationAngle` 的值不会影响 `Position` 的值。`Position` 属性表示旋转前 ROI 的初始位置。
### 输出参数
**<a id="Q3"></a>roi — 感兴趣区域**   
ROI 对象

矩形感兴趣区域。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../drawrectangle/drawrectangle.html">drawrectangle</a> | <a 
href="../Polygon/Polygon.html">Polygon</a> | 

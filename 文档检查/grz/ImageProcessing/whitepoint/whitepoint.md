## whitepoint
标准光源的 XYZ 颜色值

## 简介
[ `xyz = whitepoint`](#function1)  
[ `xyz = whitepoint(illuminant)`](#function2)

## 用法
<a id="function1"></a>
[xyz](#P1) = whitepoint 返回默认的 "d65" 白色参考光源对应的 `XYZ` 值，并按比例缩放，使得 Y=1。  
<a id="function2"></a>
[xyz](#P1) = whitepoint([illuminant](#Q1)) 返回指定的白色参考光源 `illuminant` 对应的 `XYZ` 值，并按比例缩放，使得 Y=1。

## 参数说明
### 输入参数
**<a id="Q1"></a> illuminant — 白色参考光源**  
"d65"（默认）| "a" | "c" | "e" | "d50" | "d55"  

白色参考光源，指定为这些值之一。

| **Value** | **White Point** |
| :----------- | :----------- |
| "a" | CIE 标准光源 A，[1.0985, 1.0000, 0.3558]。模拟典型的家用白炽灯照明，相关色温为 2856K。 |
| "c" | CIE 标准光源 C，[0.9807, 1.0000, 1.1822]。模拟平均或北方天空日光，相关色温为 6774K。已被 CIE 弃用。 |
| "e" | 等能量辐射体，[1.000, 1.000, 1.000]。作为理论参考很有用。 |
| "d50" | CIE 标准光源 D50，[0.9642, 1.0000, 0.8251]。模拟日出或日落时的温暖日光，相关色温为 5003K。也称为地平线光。 |
| "d55" | CIE 标准光源 D55，[0.9568, 1.0000, 0.9214]。模拟上午或下午的中等日光，相关色温为 5500K。 |
| "d65" | CIE 标准光源 D65，[0.9504, 1.0000, 1.0888]。模拟正午日光，相关色温为 6504K。 |
<!-- | "icc" | ICC配置文件中使用的 Profile Connection Space (PCS) 光源。使用定点、有符号的 32 位数字，其中 16 位为小数部分，对 [0.9642, 1.000, 0.8249] 进行近似。实际值为：[31595, 32768, 27030]/32768。 | -->

**数据类型：**`string` | `char`

### 输出参数
**<a id="P1"></a> xyz — XYZ 值**   
3 元数值行向量

对应光源的 `XYZ` 值，以 3 元数值行向量形式返回。这些值经过缩放，使得 Y=1。  

**数据类型：** `double` 

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<!-- <a href="../applycform/applycform.html">applycform</a> | <a 
href="../makecform/makecform.html">makecform</a> |  -->
<a 
href="../xyz2double/xyz2double.html">xyz2double</a> | <a 
href="../xyz2uint16/xyz2uint16.html">xyz2uint16</a> | <a 
href="../xyz2lab/xyz2lab.html">xyz2lab</a> | <a 
href="../xyz2rgb/xyz2rgb.html">xyz2rgb</a>
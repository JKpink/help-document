## fsamp2
基于频率采样的二维 FIR 滤波器设计
## 简介
[ `h = fsamp2(Hd)`](#function1)  
[ `h = fsamp2(f1, f2, Hd, [m n])`](#function2)  
## 用法
<a id="function1"></a>
[h](#Q1) = fsamp2([Hd](#Q2))设计频率响应为[Hd](#Q2)的二维 FIR 滤波器，返回滤波器系数矩阵h。该滤波器的频率响应会经过Hd中指定的采样点，是基于笛卡尔平面上的期望二维频率响应采样点来实现设计的。  
<a id="function2"></a>
[h](#Q1) = fsamp2([f1](#Q4), [f2](#Q5), [Hd](#Q2), [[m n]](#Q3))生成 `m×n` 尺寸的二维 FIR 滤波器，通过匹配频率向量`f1`、`f2`对应点处的响应完成设计。

## 参数说明
### 输入参数
**<a id="Q1"></a> Hd — 频率响应**   
数值矩阵  

指定为包含期望频率响应的数值矩阵，其采样点在 x、y 频率轴上以等间隔分布于-1.0到1.0之间。  

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint64`  

**<a id="Q2"></a> f1 — 频率向量**  
数值向量  

指定的 x 维度频率向量。  

**数据类型：**  `double`   

**<a id="Q3"></a> f2 — 频率向量**  
数值向量  

指定的 y 维度频率向量。  

**数据类型：**  `double`   

**<a id="Q4"></a> [m n] — 输出 FIR 滤波器的尺寸**  
2元素正整数向量  

指定输出 FIR 滤波器`h`的尺寸，其中`m`对应滤波器的行数，`n`对应列数。  

**数据类型：**  `double`  

## 输出参量
**<a id="P1"></a> h — 二维 FIR 滤波器**  
数值数组  

以数值数组形式返回的二维 FIR 滤波器，fsamp2会将其封装为相关核形式，适配filter2函数进行二维信号（如图像）的滤波操作。  

**数据类型：**  `single` | `double`  

## 参考文献
[1] Lim, Jae S., Two-Dimensional Signal and Image Processing, Englewood Cliffs, NJ, Prentice Hall, 1990, pp. 213-217.
## 版本历史
在北太天元图像处理工具箱 V3.0 推出
## 相关主题
<a href="../conv2/conv2.html">conv2</a>|<a href="../filter2/filter2.html">filter2|</a><a href="../freqspace/freqspace.html">freqspace</a>|</a><a href="../ ftrans2/ ftrans2.html"> ftrans2</a>|</a><a href="../fwind1/fwind1.html">fwind1</a>|</a><a href="../fwind2/fwind2.html">fwind2</a>
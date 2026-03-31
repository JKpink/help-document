## ftrans2  
使用频率变换的2维FIR滤波器
## 简介
[ `h = ftrans2(b, t)`](#function1)  
[ `h = ftrans2(b)`](#function1)  
## 用法
<a id="function1"></a>
[h](#Q1) = ftrans2([b](#Q2), [t](#Q3))利用变换矩阵t，将一维 FIR 滤波器b转换为对应的二维 FIR 滤波器h。其中变换矩阵t包含定义所用频率变换的系数。  
<a id="function2"></a>
[h](#Q1) = ftrans2([b](#Q2))使用变换矩阵t完成转换其默认矩阵为：
$\begin{bmatrix}
0&1&1\\
1&1&0\\
1&0&1\\
\end{bmatrix}$
## 参数说明
### 输入参数
**<a id="Q1"></a> b — FIR 滤波器**   
数值矩阵  

需指定为一维TypeI(偶对称、奇数长度的FIR滤波器)  

**数据类型：** `double`  

**<a id="Q2"></a> t — 变换矩阵**  
数值矩阵  

包含定义频率变换系数的数值矩阵，默认使用 McClellan 变换矩阵。  

**数据类型：**  `double` 

## 输出参量
**<a id="P1"></a> h — 二维 FIR 滤波器**  
数值数组  

以数值数组形式返回的二维 FIR 滤波器，fsamp2会将其封装为相关核形式，适配filter2函数进行二维信号（如图像）的滤波操作。  
## 参考文献
[1] Lim, Jae S., Two-Dimensional Signal and Image Processing, Englewood Cliffs, NJ, Prentice Hall, 1990, pp. 218-237.
## 版本历史
在北太天元图像处理工具箱 V3.0 推出
## 相关主题
<a href="../conv2/conv2.html">conv2</a>|<a href="../filter2/filter2.html">filter2|</a><a href="../fsamp2/fsamp2.html">fsamp2</a>|</a><a href="../fwind1/fwind1.html">fwind1</a>|</a><a href="../fwind2/fwind2.html">fwind2</a>
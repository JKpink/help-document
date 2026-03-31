## fwind2
采用2维窗口方法的2维FIR滤波器

## 简介
[ `h = fwind2(Hd, win)`](#function1)

## 用法
<a id="function1"></a>
[h](#Q3)= fwind2([Hd](#Q1), [win](#Q2)) 对期望频率响应矩阵 `Hd` 执行二维傅里叶逆变换，再与二维窗函数 `win` 进行加权运算，最终得到2维 FIR 滤波器系数矩阵 `h`。

## 参数说明
### 输入参数
**<a id="Q1"></a> Hd — 期望频率响应矩阵**  
数值矩阵

在直角坐标系的均匀间隔频率点上采样得到的期望频率响应，以数值矩阵形式输入。

**数据类型**：`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q2"></a> win — 二维窗函数**  
数值矩阵

输入的二维窗函数，以数值矩阵形式输入。

**数据类型**：`single` | `double` 

### 输出参数
**<a id="Q3"></a> h — 2维FIR滤波器系数**    
数值矩阵

设计得到的2维 FIR 滤波器系数，以数值矩阵形式输出。滤波器的尺寸与输入的二维窗函数 [win](#Q2) 一致。

**数据类型**： `double`

## 算法
`fwind2` 函数通过二维逆傅里叶变换和二维窗函数加权两个步骤计算滤波器系数，具体公式如下：

$$
h_d(n_1, n_2) = \frac{1}{(2\pi)^2} \int_{-\pi}^{\pi} \int_{-\pi}^{\pi} H_d(\omega_1, \omega_2) e^{j\omega_1 n_1} e^{j\omega_2 n_2} d\omega_1 d\omega_2
$$

$$
h(n_1, n_2) = h_d(n_1, n_2)w(n_1, n_2)
$$

## 参考文献
[1] Lim, Jae S., Two-Dimensional Signal and Image Processing, Englewood Cliffs, NJ, Prentice Hall, 1990, pp. 202-213.

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../fwind1/fwind1.html">fwind1</a> 
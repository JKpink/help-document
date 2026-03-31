## fwind1
采用1维窗口方法的2维FIR滤波器

## 简介
[ `h = fwind1(Hd, win)`](#function1)  
[ `h = fwind1(Hd, win1, win2)`](#function2)

## 用法
<a id="function1"></a>
[h](#Q5) = fwind1([Hd](#Q1), [win](#Q2)) 根据期望频率响应矩阵`Hd`，生成2维 FIR 滤波器系数矩阵 `h`。函数采用黄氏方法，将输入的一维窗函数 `win` 转换为近似圆对称的二维窗函数。    
<a id="function2"></a>
[h](#Q5) = fwind1([Hd](#Q1), [win1](#Q3), [win2](#Q4)) 使用两个1维窗函数 `win1` 和 `win2`，构造可分离的2维窗函数，进而生成2维 FIR 滤波器系数矩阵 `h`。

## 参数说明
### 输入参数
**<a id="Q1"></a> Hd — 期望频率响应矩阵**  
数值矩阵

期望的滤波器频率响应，以数值矩阵形式输入。在归一化频率域（取值范围为 [-1.0, 1.0]，其中 1.0 对应采样频率的一半，即π弧度）内，Hd在 x 轴和 y 轴方向的频率点上均匀采样。

**数据类型**：`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q2"></a> win — 一维窗函数**  
数值矩阵

输入的一维窗函数，以数值矩阵形式输入。

**数据类型**：`single` | `double` 

**<a id="Q3"></a> win1 — 一维窗函数**  
数值矩阵  

第一个输入的一维窗函数，以数值矩阵形式输入。

**数据类型**：`single` | `double`

**<a id="Q4"></a> win2 — 一维窗函数**  
数值矩阵

第二个输入的一维窗函数，以数值矩阵形式输入。

**数据类型**：`single` | `double`

### 输出参数
**<a id="Q5"></a> h — 2维FIR滤波器系数**    
数值矩阵

设计得到的2维 FIR 滤波器系数，以数值矩阵形式输出。滤波器的尺寸由输入窗函数的长度决定：
- 若输入单个长度为 n 的窗函数 [win](#Q2) ，则输出滤波器尺寸为 n×n；
- 若输入两个长度分别为 n 和 m 的窗函数 [win1](#Q3) 和 [win2](#Q4) ，则输出滤波器尺寸为 m×n。
若输入的 [Hd](#Q1) 为 single 类型，则输出 `h` 为 single 类型；否则，输出 `h` 为 double 类型。

**数据类型**： `single` | `double`

## 算法
`fwind1` 函数采用黄氏方法，将一维窗函数转换为近似圆对称的二维窗函数，转换公式如下：

$w(n_1, n_2) = \left. w(t) \right|_{t=\sqrt{n_1^2+n_2^2}}$
式中，w(t)为输入的一维窗函数，w(n1,n2)为转换得到的二维窗函数。
若输入两个一维窗函数，函数可构造分离二维窗函数，公式如下：
$w(n_1, n_2) = w_1(n_1)w_2(n_2)$
本质上，`fwind1` 函数会调用 `fwind2` 函数，将期望频率响应 Hd 和构造好的二维窗函数传入，最终通过二维逆傅里叶变换和二维窗函数加权得到滤波器系数，计算过程如下：

$$
h_d(n_1, n_2) = \frac{1}{(2\pi)^2} \int_{-\pi}^{\pi} \int_{-\pi}^{\pi} H_d(\omega_1, \omega_2) e^{j\omega_1 n_1} e^{j\omega_2 n_2} d\omega_1 d\omega_2
$$

$$
h(n_1, n_2) = h_d(n_1, n_2)w(n_1, n_2)
$$

## 参考文献
[1] Lim, Jae S., Two-Dimensional Signal and Image Processing, Englewood Cliffs, NJ, Prentice Hall, 1990.

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../fwind2/fwind2.html">fwind2</a> 
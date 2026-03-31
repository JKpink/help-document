## fspecial3
创建预定义的3维滤波器

## 简介
[ `h = fspecial3(type)`](#function1)  
[ `h = fspecial3('average', hsize)`](#function2)  
[ `h = fspecial3('gaussian', hsize, sigma)`](#function3)   
[ `h = fspecial3('gaussian', hsize, sigma)`](#function4)  
[ `h = fspecial3('laplacian', gamma1, gamma2)`](#function5)  
[ `h = fspecial3('log', hsize, sigma)`](#function6)  

## 用法
<a id="function1"></a>
[h](#Q7) = fspecial3([type](#Q1))   创建指定类型的三维滤波器h，部分类型支持额外可选参数；返回的h是相关核，适配imfilter使用  
<a id="function2"></a>
[h](#Q7) = fspecial3('average', [hsize](#Q2)) 创建尺寸为hsize的三维平均滤波器  
<a id="function2"></a>
[h](#Q7) = fspecial3('ellipsoid', [semiaxes](#Q2)) 创建主轴半轴长度由semiaxes指定的椭球形平均滤波器  
<a id="function3"></a>
[h](#Q7) = fspecial3('gaussian', [hsize](#Q2), [sigma](#Q3))  创建尺寸为hsize、标准差为sigma的三维高斯低通滤波器  
<a id="function4"></a>
[h](#Q7)  = fspecial3('laplacian', [gamma1, gamma2](#Q4))创建 3×3×3 的三维拉普拉斯算子近似滤波器，gamma1与gamma2控制算子形状     
<a id="function5"></a>
[h](#Q7)  = fspecial3('log', [hsize](#Q2), [sigma](#Q3))创建尺寸为hsize、标准差为sigma的三维高斯拉普拉斯（LoG）滤波器   
<a id="function6"></a>


## 参数说明
### 输入参数
**<a id="Q1"></a> type — 滤波器的类型**  
"average" | "ellipsoid" | "gaussian" | "laplacian" | "log"  | "prewitt" | "sobel"

滤波器的类型，指定为下列值之一：

|值|描述|
|:-|:-|
|"average"|平均值滤波器|
|"ellipsoid"|椭球形平均滤波器|
|"gaussian"|高斯低通滤波器。不推荐。请改用 `imgaussfilt` 或 `imgaussfilt3`。|
|"laplacian"|逼近二维拉普拉斯算子|
|"log"|高斯拉普拉斯滤波器|
|"prewitt"|普瑞维特水平边缘强调滤波器|
|"sobel"|索贝尔水平边缘强调滤波器|

**数据类型：**  `char` | `string`

**<a id="Q2"></a> hsize — 滤波器的大小**  
正整数 | 由正整数组成的三元素向量

滤波器的大小，指定为正整数或由正整数组成的三元素向量。使用向量指定 h 中的行数和列数。如果您指定标量，则 h 是方阵。

**数据类型：**  `double`

**<a id="Q3"></a> sigma — 标准差**  
1 (默认) | 正数

标准差，指定为正数。

**数据类型：**  `double`

**<a id="Q4"></a> gamma1, gamma2 — 拉普拉斯算子的形状**  
0(默认) | [0, 1] 范围内的数值

控制三维拉普拉斯算子的形状，且gamma1 + gamma2的和不得超过 1。通过调整这两个参数，可改变拉普拉斯算子对不同方向边缘的响应权重。

**数据类型：**  `double`




### 输出参数
**<a id="Q7"></a> h — 相关性核**  
矩阵

相关性核，以矩阵形式返回。

**数据类型：**  `double`
## 参考文献
[1] Lindeberg, T., Scale-Space Theory in Computer Vision. Boston, MA: Kluwer Academic Publishers, 1994.  
[2] Geometry-Driven Diffusion in Computer Vision. Edited by B. M. ter Haar Romeny. Boston, MA: Kluwer Academic Publishers, 1994.  
[3] Engel, K., M. Hadwiger, J. M. Kniss, C. Rezk-Salama, and D. Weiskopf. Real-Time Volume Graphics. Wellesley, MA: A K Peters, Ltd., 2006, pp. 112–114.
## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../imfilter/imfilter.html">imfilter</a>|<a href="../fspecial/fspecial.html">fspecial</a>|<a href="../imboxfilt3/imboxfilt3.html">imboxfilt3</a>|<a href="../imgaussfilt3/imgaussfilt3.html">imgaussfilt3</a>|<a href="../edge3/edge3.html">edge3</a>
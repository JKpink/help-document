## imdilate 
膨胀

## 简介
[ `J = imdilate(I, SE)`](#function1)  
[ `J = imdilate(I, nhood)`](#function2)  
[ `J = imdilate(___, packopt)`](#function3)  
[ `J = imdilate(___, shape)`](#function4) 

## 用法
<a id="function1"></a>
[J](#Q7) = imdilate([I](#Q1), [SE](#Q2)) 使用结构元素 `SE` 膨胀灰度、二值或压缩二值图像 `I`。  
<a id="function2"></a>
[J](#Q7)  = imdilate([I](#Q1), [nhood](#Q3)) 膨胀图像 `I`，其中 `nhood` 是由指定结构元素邻域的 0 和 1 组成的矩阵。此语法等效于 imdilate(I, strel(nhood))。  
<a id="function3"></a>
[J](#Q7)  = imdilate(\_, [packopt](#Q4)) 指定输入图像 `I` 是否为压缩二值图像。  
<a id="function4"></a>
[J](#Q7)  = imdilate(\_, [shape](#Q6)) 指定输出图像的大小。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
灰度图像 | 二值图像 | 压缩二值图像

输入图像，指定为灰度图像、二值图像或任意维度的压缩二值图像。

**数据类型**： `single` | `double` | `uint8` | `uint16` | `int8` | `int16` | `logical`

**<a id="Q2"></a> SE — 结构元素**  
strel 对象 | offsetstrel 对象 | strel 对象的数组 | offsetstrel 对象的数组

结构元素，指定为标量 strel 对象或 offsetstrel 对象。`SE` 也可以是 strel 对象或 offsetstrel 对象的数组，在这种情况下，`imerode` 连续使用每个结构元素对输入图像执行多次腐蚀。`imerode` 对除数据类型为 `logical` 的图像之外的所有图像执行灰度腐蚀。在这种情况下，结构元素必须为平面结构，并且 `imerode` 执行二值腐蚀。

**<a id="Q3"></a> nhood — 结构元素邻域**  
0 和 1 组成的矩阵

结构元素邻域，指定为 0 和 1 组成的矩阵。

**示例**：[0 1 0; 1 1 1; 0 1 0]

**<a id="Q4"></a> packopt — 压缩二值图像的指示符**  
'notpacked' (默认) | 'packed'

压缩二值图像的指示符，指定为下列值之一。

 | **值** | **描述** |
|:-|:-|:-|
| 'notpacked' | [I](#Q1) 被视为普通数组。 |
| 'ispacked' | I 被视为由 bwpack 生成的压缩二值图像。I 必须为二维 uint32 数组，SE 必须为平面二维结构元素。 [shape](#Q6) 的值必须为 'same'。 |

**数据类型**： `char` | `string` 

**<a id="Q5"></a> m — 原始未压缩图像的行维度**  
正整数

原始未压缩图像的行维度，指定为正整数。

**数据类型**： `double` 

**<a id="Q6"></a> shape — 输出图像的大小**  
'same' (默认) | 'full'

输出图像的大小，指定为下列值之一。

| **值** | **描述** |
| :- | :- |
| 'same' | 输出图像与输入图像大小相同。如果 [packopt](#Q4) 的值为 'ispacked'，则 shape 必须为 'same'。 |
| 'full' | 计算完全膨胀。 |

**数据类型**： `char` | `string` 

### 输出参数
**<a id="Q6"></a> J — 膨胀的图像**  
灰度图像 | 二值图像 | 压缩二值图像

膨胀的图像，以灰度图像、二值图像或压缩二值图像形式返回。如果输入图像 `I` 是压缩二值图像，则 `J` 也是压缩二值图像。`J` 与 `I` 具有相同的数据类型。

## 详细信息
二值膨胀
用 B 对 A 执行二值膨胀（记为 A⊕B）的过程定义为如下集合运算：
A⊕B={z|(ˆB)<sub>z</sub>∩A≠∅},
其中 ˆB是结构元素 B 的反射。换句话说，它是满足以下条件的像素位置 z 的集合：当反射的结构元素平移至位置 z 时与 A 中的前景像素存在重叠。注意，一些应用使用的膨胀定义不会反射结构元素。
有关二值膨胀的详细信息，请参阅 [[1]](#R1)。

灰度膨胀
在一般形式的灰度膨胀中，结构元素有高度。用 B(x, y) 对 A(x, y) 执行灰度膨胀的过程定义为：
(A⊕B)(x, y)=max{A(x − x′, y − y′)+B(x′, y′)∣(x′, y′)∈D<sub>B</sub>},
其中 D<sub>B</sub> 是结构元素 B 的域，A(x, y) 假定为图像域外的 –∞。请注意，一些应用程序使用公式 A(x + x′, y + y′) 而不是 A(x – x′, y – y′) 来定义灰度膨胀。
要创建具有非零高度值的结构元素，请使用语法 strel(nhood, height)，其中 height 给出高度值，nhood 对应于结构元素域 D<sub>B</sub>。
灰度膨胀最常使用平面结构元素 (B(x,y) = 0)。使用这种结构元素的灰度膨胀等效于使用局部最大值运算符：
(A⊕B)(x, y)=max{A(x − x′, y − y′)∣(x′, y′)∈D<sub>B</sub>}.
除了 strel(nhood, height)、strel('arbitrary', nhood, height) 和 strel('ball', ___) 之外，所有 strel 语法都生成平面结构元素。

## 提示
- 如果图像 `I` 的维度大于结构元素的维度，则 `imdilate` 函数会将相同的形态学膨胀应用于较高维度上的所有平面。
您可以使用此行为对 RGB 图像执行形态学膨胀。为 RGB 图像指定二维结构元素，以便对每个颜色通道分别执行运算。
- 当指定结构元素邻域时，`imdilate` 通过 floor((size(nhood) + 1) / 2) 确定 `nhood` 的中心元素。
- `imdilate` 自动利用结构元素对象的分解（如果存在分解）。此外，当使用具有分解的结构元素对象执行二值膨胀时，`imdilate` 会自动使用二值图像压缩来加速膨胀[[3]](#R1)。

## <a id="R1"></a> 参考文献
[1] Gonzalez Rafael C, Richard E Woods, Steven L Eddins. Digital Image Processing Using MATLAB. Third edition. Knoxville: Gatesmark Publishing, 2020.  
[2] Haralick Robert M, and Linda G Shapiro. Computer and Robot Vision. 1st ed. USA: Addison-Wesley Longman Publishing, 1992.  
[3] Boomgaard, Rein van den, Richard van Balen. Methods for Fast Morphological Image Transforms Using Bitmapped Binary Images.CVGIP: Graphical Models and Image Processing, 54(3): 252–58, May 1, 1992.

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imclose/imclose.html">imclose</a> | <a 
href="../imerode/imerode.html">imerode</a> | <a 
href="../imopen/imopen.html">imopen</a> 



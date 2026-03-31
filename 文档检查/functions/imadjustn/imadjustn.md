## imadjustn
调整N维图像强度值

## 简介
[ `J = imadjustn(V) `](#function1)  
[ `J = imadjustn(V, [low_in high_in])`](#function2)  
[ `J = imadjustn(V, [low_in high_in], [low_out high_out]) `](#function3)  
[ `J = imadjustn(V, [low_in high_in], [low_out high_out], gamma`)](#function4)

## 用法
<a id="function1"></a>
[J](#Q5) = imadjustn([V](#Q1)) 将 N 维体强度图像 `V` 中的像素值映射为输出图像 `J` 中的新值，以此提升输出体数据图像的对比度。  
默认情况下，`imadjustn` 会对所有像素值的底部 1% 和顶部 1% 进行饱和处理。该语法等价于 imadjustn(V,stretchlim(V(:)))。        
<a id="function2"></a>
[J](#Q5) = imadjustn([V](#Q1), [[`low_in` `high_in`]](#Q2) 将 V 中的像素值映射到区间 [0, 1] 内。低于 `low_in` 的值映射为 0，高于 `high_in` 的值映射为 1。    
<a id="function3"></a>
[J](#Q5) = imadjustn([V](#Q1), [[`low_in` `high_in`]](#Q2), [[`low_out` `high_out`]](#Q3)) 将 V 中的像素值映射到输出图像 J 中，使区间 [low_in, high_in] 内的输入值对应映射到 [low_out, high_out] 区间内的输出值。低于 `low_in` 的值被截断为 `low_out`，高于 `high_in` 的值被截断为 `high_out`。  
<a id="function4"></a> 
[J](#Q5) = imadjustn([V](#Q1), [[`low_in` `high_in`]](#Q2), [[`low_out` `high_out`]](#Q3),  [gamma](#Q4)) 则通过非线性伽马曲线，完成输入图像 V 到输出图像 J 的像素值映射。  

## 参数说明
### 输入参数
**<a id="Q1"></a> V — 待处理的体强度图像**  
N 维数值数组  

待处理的体强度图像，指定为一个 N 维数值数组。

**数据类型**：`single` | `double` | `int16` |  `uint8` | `uint16` 

**<a id="Q2"></a> [`low_in` `high_in`] — 输入图像的取值范围**  
[0 1]（默认值） | 二元向量

输入图像的目标取值范围，指定为 [`low_in` `high_in`] 形式的二元向量，向量内数值需在 [0, 1] 区间内。在调整强度值之前，`imadjustn` 会先通过 `im2double` 函数将输入图像转换为 double 类型，并将像素值缩放到 [0, 1] 区间。`low_in` 和 `high_in` 对应的是图像转换为 double 类型后的输入范围。  
可以使用空矩阵 [] 来指定该参数的默认值 [0 1]。

**数据类型**：`double` 

**<a id="Q3"></a> [low_out high_out] — 输出图像的取值范围**  
[0 1]（默认值） | 二元向量  

输出图像的目标取值范围，指定为 [`low_out` `high_out`] 形式的二元向量，向量内数值需在 [0, 1] 区间内。在调整强度值之前，`imadjustn` 会先通过 `im2double` 函数将输入图像转换为 double 类型，并将像素值缩放到 [0, 1] 区间。`low_out` 和 `high_out` 对应的是图像转换为 double 类型后的输出范围。完成强度值调整后，`imadjustn` 会将图像转换回输入图像的数据类型。
可以使用空矩阵 [] 来指定该参数的默认值 [0 1]。

**数据类型**： `double`

**<a id="Q4"></a> gamma — 伽马曲线的形状参数**  
1（默认值） | 数值标量

用于描述输入图像 V 和输出图像 J 像素值映射关系的伽马曲线形状参数，指定为一个数值标量。  
若省略该参数，gamma 默认为 1，此时执行的是线性映射。  
- 当 gamma 小于 1 时，imadjustn 会让映射关系偏向更高（更亮）的输出值。  
- 当 gamma 大于 1 时，imadjustn 会让映射关系偏向更低（更暗）的输出值。  

**数据类型**： `double`

### 输出参数
**<a id="Q5"></a> J — 强度值调整后的图像**    
N 维强度图像

强度值调整后的输出数据图像，返回为一个 N 维强度图像，其数据类型与输入图像完全一致。

**数据类型**：  `double`

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../decorrstretch/decorrstretch.html">decorrstretch</a> | <a href="../histeq /histeq .html">histeq </a> 
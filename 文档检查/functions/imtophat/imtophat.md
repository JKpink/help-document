## imtophat 
顶帽滤波

## 简介
[`J = imtophat(I, SE)`](#function1)  
[`J = imtophat(I, nhood)`](#function2)

## 用法
<a id="function1"></a>
[J](#Q4) = imtophat([I](#Q1), [SE](#Q2)) 使用结构元素 `SE` 对灰度或二值图像 `I` 执行顶帽滤波。  
<a id="function2"></a>
[J](#Q4) = imtophat([I](#Q1), [nhood](#Q3)) 对图像I执行顶帽滤波，其中 `nhood` 是由指定结构元素邻域的 0 和 1 组成的矩阵。此语法等效于 imtophat(I, strel(nhood))。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
灰度图像 | 二值图像 

输入图像，指定为灰度图像或二值图像。

**数据类型**： `single` | `double` | `uint8` | `uint16` |  `logical`

**<a id="Q2"></a> SE — 结构元素**   
strel 对象 | offsetstrel 对象

结构元素，指定为 strel 对象或 offsetstrel 对象。如果图像 `I` 的数据类型为 `logical`，则结构元素必须为平面。

**<a id="Q3"></a> nhood — 结构元素邻域**  
0 和 1 组成的矩阵

结构元素邻域，指定为 0 和 1 组成的矩阵。

**示例**:[0 1 0; 1 1 1; 0 1 0]

### 输出参数
**<a id="Q4"></a> J — 顶帽滤波后的图像**  
灰度图像 | 二值图像

经过顶帽滤波的图像，以灰度图像或二值图像形式返回。`J` 与输入图像 `I` 具有相同的数据类型。

## 提示
- 如果图像 `I` 的维度大于结构元素的维度，则 `imtophat` 函数会将相同的形态学开运算应用于较高维度上的所有平面。
您可以使用此行为对 RGB 图像执行顶帽滤波。为 RGB 图像指定二维结构元素，以便对每个颜色通道分别执行运算。
- 当指定结构元素邻域时，`imtophat` 通过 floor((size(nhood) + 1) / 2) 确定 `nhood` 的中心元素。
 
## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imopen/imopen.html">imopen</a> | <a 
href="../imclose/imclose.html">imclose</a> | <a 
href="../imerode/imerode.html">imerode</a> | <a 
href="../imdilate/imdilate.html">imdilate</a> | <a 
href="../imbothat/imbothat.html">imbothat</a> 
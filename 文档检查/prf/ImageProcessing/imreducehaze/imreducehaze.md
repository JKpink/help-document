## imreducehaze
去雾

## 简介
[`J = imreducehaze(I) `](#function1)

## 用法
<a id="function1"></a>
[J](#Q2) = imreducehaze([I](#Q1))  减少彩色图像 `I` 中的大气雾霾。该函数返回去雾图像 `J`。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 有雾图像**  
RGB 图像  

有雾图像，指定为 RGB 图像。

**数据类型:** `uint8`

### 输出参数
**<a id="Q2"></a> J — 去雾图像**  
数字数组  

去雾后的图像，与输入图像 `I` 的大小和数据类型相同。

## 算法
描述模糊图像 `I` 的模型是  
I(x) = J(x)T(x) + L(1-T(x))  
`I` 是观测到的强度，`J` 是场景辐射度，`L` 是大气光，`T` 是描述到达相机的光线部分的传输图。  
去雾算法根据对传输图和大气光的估计，恢复场景辐射度（去雾图像）`J`：  
J(x) = (I(x)-A)/(max(t(x),t<sub>0</sub>)) + A  
`imreducehaze` 使用两种不同的去雾算法：`simpledcp` 和 `approxdcp`。这些方法都依赖于暗通道先验，其基础在于观察到户外场景的无雾图像通常包含一些在一个或多个颜色通道中信号强度较低的像素。这两种方法的不同之处在于它们估算暗通道先验和大气光的方式。

`imreducehaze` 中的去雾算法包括以下五个步骤：

1. 使用暗通道先验估算大气光 `L`。
2. 估算传输图 `T`。
3. 优化估算的传输图。
4. 恢复图像。
5. 执行可选的对比度增强。

## 参考文献
[1] Kaiming He, Jian Sun and Xiaoou Tang. Single image haze removal using dark channel prior. IEEE Conference on Computer Vision and Pattern Recognition. IEEE, 2009: 1956-1963.  
[2] D. Park, H. Park, D. K. Han and H. Ko. Single image dehazing with image entropy and information fidelity. 2014 IEEE International Conference on Image Processing. IEEE, 2014: 4037-4041.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../imadjust/imadjust.html">imadjust</a> | <a
href="../stretchlim/stretchlim.html">stretchlim</a>
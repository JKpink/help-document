## integralImage3 
3维积分图

## 简介
[ `J = integralImage3(I)`](#function1)

## 用法
<a id="function1"></a>
[J](#Q2) = integralImage3([I](#Q1)) 根据灰度体积图像 `I` 计算积分图像 `J`。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 灰度体积**  
3-D 数值数组

灰度体积，指定为 3-D 数值数组。

**数据类型：** `uint8`

### 输出参数
**<a id="Q2"></a> J — 积分图像**  
数值数组

积分图像以数值数组的形式返回。该函数对顶部、左侧以及第一个平面进行了零填充，导致积分图像的大小为 size(J) = size(I) + 1。输出的类为双精度数。输出积分图像的最终大小为：size(J) = size(I) + 1。这种大小设置便于在所有图像边界上进行像素和的简便计算。积分图像 J 本质上是值 cumsum(cumsum(cumsum(I), 2), 3) 的一个填充版本。

**数据类型：** `double`



## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../integralImage/integralImage.html">integralImage</a> | <a
href="../integralBoxFilter3/integralBoxFilter3.html">integralBoxFilter3</a>


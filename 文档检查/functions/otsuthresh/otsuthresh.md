## otsuthresh
使用 Otsu 方法的全局直方图阈值

## 简介
[`T = otsuthresh(counts)`](#function1) 

[[T,EM] = otsuthresh(counts)](#function2) 

## 用法
<a id="function1"></a>
[T](#Q1) = otsuthresh([counts](#Q2))根据输入的直方图计数向量 `counts`，采用大津法计算一个全局阈值 `T`。该阈值的核心目标是最小化阈值分割后两类像素的类内方差，返回的阈值 `T` 归一化到 `[0, 1]` 区间，可直接作为 `imbinarize` 函数的输入，将灰度图像转换为二值图像。

<a id="function2"></a>

[[T](#Q1) , [EM](#Q2)] = otsuthresh([counts](#Q2)) 额外返回有效性度量 `EM`，用于评估阈值的分割效果，取值范围同样为 `[0, 1]`。

## 参数说明
### 输入参数
**<a id="Q2"></a> counts — 直方图计数**  
非负数值向量

图像的直方图计数向量，每个元素表示对应灰度级的像素数量，需满足非负性。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` 

### 输出参量
**<a id="Q1"></a> T — 全局阈值**  
数值标量

大津法计算得到的全局阈值，归一化到 `[0,1]` 区间。

- 与 `imbinarize` 配合使用时，大于 `T` 的像素会被设为 `1`（前景），小于等于 `T` 的像素设为 `0`（背景）；
- 阈值的物理意义：分割后前景和背景的类内方差之和最小。

**数据类型：** `double` 

**<a id="Q2"></a> T — 全局阈值**  
数值标量

阈值分割效果的评估指标，取值范围 `[0,1]`，核心特性如下：

- **值越接近 1**：分割效果越好，理想情况为直方图仅有两个非零 bin（完全分离的两类像素），此时 `EM=1`；
- **值越接近 0**：分割效果越差，最差情况为直方图所有计数集中在一个 bin（无有效分割阈值），此时 `EM=0`。

**数据类型：** `double` 

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imbinarize/imbinarize.html">imbinarize</a> | <a 
href="../adaptthresh/adaptthresh.html">adaptthresh</a> | <a 
href="../graythresh/graythresh.html">graythresh</a> 

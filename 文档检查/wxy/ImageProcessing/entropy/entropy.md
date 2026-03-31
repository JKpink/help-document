## entropy  
灰度图像的熵

## 简介  
[ `e = entropy(I)`](#function1)

## 用法  
<a id="function1"></a>
[e](#Q1) = entropy([I](#Q2)) 返回灰度图像的熵 [`I`](#Q2) 。熵是随机性的统计测度，可用于表征输入图像的纹理。

## 参数说明  
### 输入参数  

**<a id="Q2"></a>I — 灰度图像**  
数值数组 | 逻辑数组

灰度图像，指定为任意维度的数值数组或逻辑数组。`entropy` 需要数据类型为 `double` 和 `single` 的图像的值在 [0, 1] 的范围内。

**数据类型：** `double` | `single` | `uint8` | `uint16` | `logical`
### 输出参数  
**<a id="Q1"></a>e — 熵**  
数值标量

图像 [`I`](#Q2) 的熵，以数值标量形式返回，无论输入何种维数的图像，均计算全局熵。

- 若输入数组元素全部相同，则熵的输出为0;
- 若输入为逻辑数组，熵的取值为[0,1];
- 若输入为数值数组，熵的取值为[0,8]。

**数据类型：** `double`

## 详细信息  
### 熵  
- 熵定义为 -sum(p.*log2(p))，其中 p 包含从 <a href="../imhist/imhist.html">imhist</a> 返回的归一化直方图计数；
- 默认情况下，`entropy` 对逻辑数组使用两个 bin，对 `uint8`、`uint16` 或 `double` 数组使用 256 个 bin；
- 为计算直方图计数，`entropy` 将除 `logical` 以外的任何数据类型转换为 `uint8`，以使像素值离散并直接对应于 bin 值；

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## 相关主题  
<a href="../imhist/imhist.html">imhist</a> | <a 
href="../entropyfilt/entropyfilt.html">entropyfilt</a>
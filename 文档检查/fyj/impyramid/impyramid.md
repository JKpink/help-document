## impyramid
图像金字塔缩放图像

## 简介
[`B = impyramid(A, direction)`](#function1)

## 用法 
<a id="function1"></a> [B](#P1) = impyramid([A](#Q1), [direction](#Q2)) 对图像 `A` 进行图像金字塔缩放，`direction` 决定 `impyramid` 执行的是缩小还是放大操作。

## 参数说明
### 输入参数
**<a id="Q1"></a> A — 需要缩小或放大的图像**  
数值数组 | 逻辑数组

需要缩小或放大的图像，指定为数值数组或逻辑数组。

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `logical`

**<a id="Q2"></a> direction — 缩小或放大**  
`"reduce"` | `"expand"`

缩小或放大，指定为以下值之一：

| **值** | **描述** |
| :----------- | :----------- |
| `"reduce"` | 返回比原始图像小的图像。 |
| `"expand"` | 返回比原始图像大的图像。 |

**数据类型：**`char` | `string`

### 输出参数
**<a id="P1"></a> B — 缩小或放大后的图像**  
数值数组 | 逻辑数组

缩小或放大后的图像，指定为数值数组或逻辑数组，其类型与 [A](#Q1) 相同。

## 算法
如果 `A` 是 m × n，方向为 “reduce”，则 `B` 的大小是 ceil(M/2) × ceil(N/2)。如果方向为 “expand”，则 `B` 的大小为 (2* M-1)×(2*N-1)。  
  
缩减和膨胀仅发生在前两个维度。例如，如果 `A` 是 100 x 100 x 3，方向是 “reduce”，那么 `B` 是 50 × 50 × 3。   
`impyramid` 使用了 Burt 和 Adelson[[1]](#Ref1)[[2]](#Ref2)第 533 页指定的核:  
w = [ 1/4 - a/2 , 1/4 , a , 1/4 , 1/4 - a/2 ]
将参数 `a` 设置为 0.375，以便等效加权函数接近高斯形状。此外，可以很容易地使用定点算法来应用权重。

## 参考文献  
<a id="Ref1"></a> [1] Burt and Adelson. The Laplacian Pyramid as a Compact Image Code. IEEE Transactions on Communications, 1983, COM-31(4): 532-540.  
<a id="Ref2"></a> [2] Burt. Fast Filter Transforms for Image Processing. Computer Graphics and Image Processing, 1981, 16: 20-51.

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../imresize/imresize.html">imresize</a>
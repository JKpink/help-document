## imhistmatch 
直方图匹配

## 简介
[ `J = imhistmatch(I, ref)`](#function1)  
[ `J = imhistmatch(I, ref, nbins)`](#function2)  
[ `[J, hgram] = imhistmatch(___)`](#function3)

## 用法
<a id="function1"></a>
[J](#Q5) = imhistmatch([I](#Q1), [ref](#Q2)) 调整 2-D 灰度或真彩色图像 `I` 的直方图，使直方图与参考图像 `ref` 的直方图大致匹配。
- 如果 `I` 和 `ref` 都是 RGB 图像，则 `imhistmatch` 将 `I` 的每个颜色通道与 `ref` 的相应颜色通道独立匹配。
- 如果 `I` 是 RGB 图像，而 `ref` 是灰度图像，则 `imhistmatch` 会将 `I` 的每个通道与从 `ref` 派生的单个直方图进行匹配。
- 如果 `I` 是灰度图像，则 `ref` 也必须是灰度图像。
图像 `I` 和 `ref` 的大小不必相等。  
<a id="function2"></a>
[J](#Q5) = imhistmatch([I](#Q1), [ref](#Q2), [nbins](#Q3)) 在给定图像数据类型的适当范围内使用 `nbin` 等距分箱。返回的图像 `J` 不超过 `nbins` 离散级别。如果图片的数据类型为 `uint8`，则直方图范围为 [0, 255]。  
<a id="function3"></a>
[[J](#Q5), [hgram](#Q6)] = imhistmatch(___) 返回用于在 `hgram` 中匹配的参考图像 `ref` 的直方图。

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**   
2-D RGB 图像 | 2-D 灰度图像 
 
输入要变换的图像，指定为 2-D RGB 或 2-D 灰度图像。imhistmatch 函数要求数据类型为 `double` 和 `single` 的图像具有 [0, 1] 范围内的值。如果我的值超出 [0, 1] 范围，则可以使用 `rescale` 函数将值重新缩放到预期范围。

**数据类型：** `uint8`

**<a id="Q2"></a> ref — 参考图像**  
2-D RGB 图像 | 2-D 灰度图像   

其直方图为参考直方图的参考图像，指定为 2-D RGB 或 2-D 灰度图像。参考图像提供等间距的 `nbins` bin 参考直方图，输出图像 `J` 尝试匹配该直方图。`imhistmatch` 函数要求数据类型为 `double` 和 `single` 的图像具有 [0, 1] 范围内的值。

**数据类型：** `uint8`

**<a id="Q3"></a> nbins — 等距 bin 的数量**  
64（默认）| 正整数  

参考直方图中等距的 bin 数，指定为正整数。除了指定图像 `ref` 的直方图中等距 bin 的数量外，`nbins` 还表示输出图像 `J` 中存在的离散数据水平数的上限。

### 输出参数
**<a id="Q5"></a> J — 输出图像**  
2D RGB 图像 | 2D 灰度图像  

输出图像，以 2-D RGB 或 2-D 灰度图像形式返回。输出图像来自图像 I，其直方图与使用 `nbins` 等距分箱构建的输入图像 `ref` 的直方图近似匹配。图像 `J` 的大小和数据类型与输入图像 `I` 相同。输入参数 `nbins` 表示图像 `J` 中包含的离散级别数的上限。

**数据类型：** `uint8`

## 算法
`imhistmatch` 的目标是转换图像 `I`，使图像 `J` 的直方图与从图像 ref 派生的直方图匹配。它由等距 bins 组成，这些 bin 跨越了 image 数据类型的整个范围。以这种方式匹配直方图的结果是 nbins 也表示图像 `J` 中存在的离散数据级别数的上限。  
需要注意的该算法的一个重要行为方面是，随着 `nbins` 值的增加，图像 `J` 直方图中相邻填充峰之间的快速波动程度趋于增加。 
`nbins` 的最佳值表示在更多输出水平（较大的 nbins 值）与最小化直方图中的峰值波动（较小的 nbins 值）之间进行权衡。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../histeq/histeq.html">histeq</a> | <a
href="../imadjust/imadjust.html">imadjust</a> | <a 
href="../imhist/imhist.html">imhist</a> | <a 
href="../imhistmatchn/imhistmatchn.html">imhistmatchn</a> 
## imcrop3
裁剪三维图像

## 简介
[`Vout = imcrop3(V, cuboid)`](#function1)

## 用法 
<a id="function1"></a> [Vout](#P1) = imcrop3([V](#Q1), [cuboid](#Q2)) 根据 `cuboid` 指定的裁剪窗口的大小和位置，在空间坐标系中对三维图像 `V` 进行裁剪。

## 参数说明
### 输入参数
**<a id="Q1"></a> V — 需要裁剪的体积**  
数值数组 | 逻辑数组 

需要裁剪的体积，指定为数值数组或逻辑数组。`V` 可以是一个表示单通道三维体积的三维数组，也可以是一个表示多通道三维体积的四维数组。如果 `V` 表示多通道体积，则 `imcrop3` 仅裁剪前三个维度。

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `logical`

**<a id="Q2"></a> cuboid — 裁剪体积的大小和位置**  
6 元素数值向量

裁剪体积的大小和位置，指定为 [xmin ymin zmin width height depth] 格式的 6 元素数值向量。

**数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出参数
**<a id="P1"></a> Vout — 裁剪后的体积**  
逻辑数组 | 数值数组

裁剪后的体积，指定为逻辑数组或数值数组，其类型与输入体积 [V](#Q1) 相同。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../imcrop/imcrop.html">imcrop</a> 
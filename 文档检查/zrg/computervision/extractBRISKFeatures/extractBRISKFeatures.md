## extractBRISKFeatures  
提取 BRISK 特征

## 简介  
[ `[binaryFeatures, briskPointsOut] = extractBRISKFeatures(image, briskPointsIn)`](#function1)  

## 用法  
<a id="function1"></a>  
[[binaryFeatures](#Q1), [ briskPointsOut](#Q2)] = extractBRISKFeatures([ image](#Q3), [ briskPointsIn](#Q4))  
根据输入关键点 `briskPointsIn` 计算 BRISK 特征描述子，返回 512 位二进制描述子矩阵及对应关键点对象。


## 参数说明  
### 输入参数  
**<a id="Q3"></a>image — 输入图像**  
二维或三维数值矩阵  

灰度或彩色图像，指定为二维或三维数值矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `logical`

**<a id="Q4"></a>briskPointsIn — 输入 BRISK 关键点**  
`BRISKPoints` 外部对象  

由 `detectBRISKFeatures` 或 `BRISKPoints()` 生成，允许 0 点。

### 输出参数  
**<a id="Q1"></a>binaryFeatures — BRISK 描述子容器**  
binaryFeatures 外部对象  

属性 `Descriptors` 为 `N×64 uint8` 矩阵，每行 512 位描述子。

**数据类型：** 外部对象 `binaryFeatures`

**<a id="Q2"></a>briskPointsOut — 输出关键点**  
`BRISKPoints` 外部对象  

与输入同类型，可能 0 点；常用属性 `N`、 `Location`、 `Scale`、 `Orientation`。

**数据类型：** 外部对象 `BRISKPoints`


## 版本历史  
在北太天元图像处理工具箱 V3.0 推出。

## 相关主题  
<a href="../detectBRISKFeatures/detectBRISKFeatures.html">detectBRISKFeatures</a>
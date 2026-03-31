## detectCheckerboardPoints  
检测图像中的棋盘格模式

## 简介  
[ `[pts, boardSize] = detectCheckerboardPoints(I)`](#function1)

## 用法  
<a id="function1"></a>  
[[pts](#Q1), [boardSize](#Q2)] = detectCheckerboardPoints([I](#Q3))  
在灰度图像 `I` 中检测黑白棋盘格角点，返回角点坐标 `pts` 和棋盘尺寸 `boardSize`；若未检测到，则 `pts` 为空，`boardSize` 为 `[0 0]`。

## 参数说明  
### 输入参数  
**<a id="Q3"></a>I — 输入图像**  
二维数值矩阵  

灰度图像，指定为二维数值矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `logical`

### 输出参数  
**<a id="Q1"></a>pts — 角点坐标**  
N×2 矩阵  

角点坐标，返回 `N×2` 矩阵 。每行 `[x y]`；未检测到时返回空矩阵。

**数据类型：** `double`

**<a id="Q2"></a>boardSize — 棋盘尺寸**  
1×2 矩阵  

棋盘尺寸，返回`[rows cols]` 矩阵。未检测到时为 `[0 0]`。

**数据类型：** `double`
## 版本历史  
在北太天元图像处理工具箱 V3.0 推出。

## 相关主题  
<a href="../detectBRISKFeatures/detectBRISKFeatures.html">detectBRISKFeatures</a>
## worldToIntrinsic
从世界坐标转换为固有坐标

## 简介
[`[xIntrinsic, yIntrinsic] = worldToIntrinsic(R, xWorld, yWorld)`](#function1)

## 用法 
<a id="function1"></a> [[xIntrinsic](#P1), [yIntrinsic](#P2)] = worldToIntrinsic([R](#Q1), [xWorld](#Q2), [yWorld](#Q3)) 将地图栅格 `R` 中的世界坐标 (xWorld, yWorld) 转换为固有坐标 (xIntrinsic, yIntrinsic)。如果点位于栅格 `R` 的范围之外，`worldToIntrinsic` 会对坐标进行外插计算，返回对应的 `xIntrinsic` 和 `yIntrinsic` 。 

## 参数说明
### 输入参数
**<a id="Q1"></a> R — 地图栅格**  
`MapCellsReference` 或 `MapPostingsReference` 对象。  

地图栅格，指定为 <a href="../MapCellsReference/MapCellsReference.html">MapCellsReference</a>  </a> 或 <a href="../MapPostingsReference/MapPostingsReference.html">MapPostingsReference</a>  </a> 对象。

**<a id="Q2"></a> xWorld — 世界坐标系 x 坐标**  
数值数组  

世界坐标系 `x` 坐标，指定为数值数组。`xWorld` 坐标可超出栅格 [R](#Q1) 的边界范围。

**数据类型：** `single` | `double`

**<a id="Q3"></a> yWorld — 世界坐标系 y 坐标**  
数值数组  

世界坐标系 `y` 坐标，指定为数值数组。`yWorld` 的大小与 [xWorld](#Q2) 的大小相同，且 `yWorld` 坐标可超出栅格 [R](#Q1) 的边界范围。

**数据类型：** `single` | `double`

### 输出参数
**<a id="P1"></a> xIntrinsic — 固有坐标系 x 坐标**  
数值数组  

固有坐标系 `x` 坐标，指定为数值数组。`xIntrinsic` 的大小与 [xWorld](#Q2) 的大小相同。

当 `xWorld(k)` 超出栅格 [R](#Q1) 的边界时，`xIntrinsic(k)` 会在固有坐标系下进行外插计算。

**数据类型：** `double`

**<a id="P2"></a> yIntrinsic — 固有坐标系 y 坐标**  
数值数组  

固有坐标系 `y` 坐标，指定为数值数组。`yIntrinsic` 的大小与 [xWorld](#Q2) 的大小相同。

当 [yWorld](#Q3)(k) 超出栅格 [R](#Q1) 的边界时，`yIntrinsic(k)` 会在固有坐标系下进行外插计算。

**数据类型：** `double``

## 版本历史
在北太天元图像处理工具箱 V2.0 推出
## 相关主题
<a href="../intrinsicToWorld/intrinsicToWorld.html">intrinsicToWorld</a> | <a
href="../worldToDiscrete/worldToDiscrete.html">worldToDiscrete</a> | <a
href="../geographicToIntrinsic/geographicToIntrinsic.html">geographicToIntrinsic</a> 

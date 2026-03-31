## intrinsicToWorld
从固有坐标转换为世界坐标

## 简介
[`[xWorld, yWorld] = intrinsicToWorld(R, xIntrinsic, yIntrinsic)`](#function1)  
[`[xWorld, yWorld, zWorld] = intrinsicToWorld(R, xIntrinsic, yIntrinsic, zIntrinsic)`](#function2)

## 用法 
<a id="function1"></a> [[xWorld](#P1), [yWorld](#P2)] = intrinsicToWorld([R](#Q1), [xIntrinsic](#Q2), [yIntrinsic](#Q3)) 将二维空间参考对象 `R` 中的点的固有坐标系 (xIntrinsic, yIntrinsic) 映射到世界坐标系 (xWorld, yWorld)。  
若第 k 组输入坐标 (xIntrinsic(k), yIntrinsic(k)) 落在固有坐标系的图像边界之外，`intrinsicToWorld` 会对世界坐标系下的 `xWorld(k)` 和 `yWorld(k)` 进行外推计算。  
<a id="function2"></a> [[xWorld](#P1), [yWorld](#P2), [zWorld](#P3)] = intrinsicToWorld([R](#Q1), [xIntrinsic](#Q2), [yIntrinsic](#Q3), [zIntrinsic](#Q4)) 将三维空间参考对象 `R` 中的点从固有坐标系映射到世界坐标系。
## 参数说明
### 输入参数
**<a id="Q1"></a> R — 空间参考对象**   
`imref2d` 或 `imref3d` 对象   

空间参考对象，指定为 <a href="../imref2d/imref2d.html">imref2d</a>  </a> 或 <a href="../imref3d/imref3d.html">imref3d</a>  </a> 对象。

**<a id="Q2"></a> xIntrinsic — 固有坐标系 x 坐标**    
数值标量或向量  
  
固有坐标系中的 `x` 坐标，指定为数值标量或向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="Q3"></a> yIntrinsic — 固有坐标系 y 坐标**  
数值标量或向量  

固有坐标系中的 `y` 坐标，指定为数值标量或向量。`yIntrinsic` 的长度需与 [xIntrinsic](#Q2) 保持一致。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`  
  
**<a id="Q4"></a> zIntrinsic — 固有坐标系 z 坐标**  
数值标量或向量  

固有坐标系中的 `z` 坐标，指定为数值标量或向量。`zIntrinsic` 的长度需与 [xIntrinsic](#Q2) 保持一致。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出参数

**<a id="P1"></a> xWorld — 世界坐标系 x 坐标**  
数值标量或向量  

世界坐标系中的 `x` 坐标，指定为数值标量或向量。`xWorld` 的长度需与 [xIntrinsic](#Q2) 保持一致。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `uint64`

**<a id="P2"></a> yWorld — 世界坐标系 y 坐标**  
数值标量或向量  

世界坐标系中的 y 坐标，指定为数值标量或向量。`yWorld` 的长度需与 [xIntrinsic](#Q2) 保持一致。   
  
**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `uint64` 
  
**<a id="P3"></a> zWorld — 世界坐标系 z 坐标**  
数值标量或向量  

世界坐标系中的 z 坐标，指定为数值标量或向量。`zWorld` 的长度需与 [xIntrinsic](#Q2) 保持一致。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `uint64`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../imref2d/imref2d.html">imref2d</a> | <a
href="../imref3d/imref3d.html">imref3d</a> | <a 
href="../worldToIntrinsic/worldToIntrinsic.html">worldToIntrinsic</a> 
## findbounds  
计算几何变换的输出范围  

## 简介  
[`outbounds = findbounds(tform, inbounds)`](#function1)  

## 用法  
<a id="function1"></a> [outbounds](#P1) = findbounds([tform](#Q1), [inbounds](#Q2)) 估算对应于特定空间变换和一组输入边界条件的输出边界范围。`tform` 是表示空间几何变换的结构体。`inbounds` 是一个 2 × num_dims 矩阵，用于指定输入空间矩形区域的上下边界。`outbounds` 是对能完整包裹输入边界经变换后所得图形的最小矩形区域的近似估计。正因为它只是一个近似值，所以可能无法完全覆盖变换后的输入图形。
## 参数说明  
### 输入参数  
**<a id="Q1"></a> tform — 空间变换**  
结构体  
  
空间变换，指定为 `TFORM` 结构体。可以用一个 [maketform](#Q3) 获取一个结构体。  

**数据类型：** `struct`  

**<a id="Q2"></a> inbounds — 输入图像各维度的边界**  
2 × num_dims 矩阵  
  
输入图像各维度的边界，指定为一个 2×num_dims 矩阵。`inbounds` 的第一行指定为各维度的下界，第二行指定各维度的上界。`num_dims` 必须与 `tform` 的 `ndims_in` 字段保持一致。  
  
示例：[0 0; 256 256]，其中输入图像像素为 256×256。  
  
**数据类型：** `double`  
  
### 输出参数  
**<a id="P1"></a> outbounds — 输出图像各维度的边界**  
2 × num_dims 矩阵  
  
输出图像各维度的边界，指定为一个 2×num_dims 矩阵。  
  
**数据类型：** `double`    
  
## 版本历史  
在北太天元图像处理工具箱 V2.0 推出  
  
## 相关主题  
<a href="../tformarry/tformarry.html">tformarry</a> | <a
href="../tformfwd/tformfwd.html">tformfwd</a> | <a 
href="../tforminv/tforminv.html">tforminv</a>   

       
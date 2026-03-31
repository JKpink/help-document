## blockproc  
图像的非重复块处理 

## 简介  
[ `B = blockproc(A, [m n], fun)`](#function1)
 
## 用法  
<a id="function1"></a>
[B](#Q1) = blockproc([A](#Q2), [[m n]](#Q3), [fun](#Q4))  通过对大小为 [[m n]](#Q3) 的每个非重叠图像块应用 [fun](#Q4) 函数并将结果串联到输出图像 [B](#Q1) 中，来处理输入图像 [A](#Q2)。  

## 参数说明  
### 输入参数  

**<a id="Q2"></a>A — 要处理的图像**    
数值数组  

要处理的图像，指定为数值数组。  

**<a id="Q3"></a>[m n] — 图像块大小**   
二元素向量  

图像块大小，指定为二元素向量。m 是图像块中的行数，n 是列数。  

**<a id="Q4"></a>fun — 函数句柄**   
句柄  

函数句柄，指定为句柄。返回数组、向量或标量。如果 fun 返回空值，则 blockproc 不会生成任何输出，并且在处理完所有图像块后返回空值。  

### 输出参数  
**<a id="Q1"></a>B — 已处理图像**    
数值数组  

已处理的图像，以数值数组形式返回。  

## 版本历史  
在北太天元图像处理工具箱 V3.0 推出  

## 相关主题  
<a href="../blockedImage/blockedImage.html">blockedImage</a> | <a 
href="../colfilt/colfilt.html">colfilt</a> | <a 
href="../ImageAdapter/ImageAdapter.html">ImageAdapter</a> | <a 
href="../nlfilter/nlfilter.html">nlfilter</a>
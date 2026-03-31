## affineOutputView  
为形变图像创建输出视图  
  
## 简介  
[`Rout = affineOutputView(sizeA, tform)`](#function1)  
[`Rout = affineOutputView(sizeA, tform, BoundsStyle=style)`](#function2)  
  
## 用法  
<a id="function1"></a> [Rout](#P1) = affineOutputView([sizeA](#P2), [tform](#P3)) 接收输入图像的大小 `sizeA` 和一个仿射几何变换 `tform`，返回一个空间参考对象 `Rout`。可以将该对象传入 <a href="../imwarp/imwarp.html">imwarp</a>  </a> 函数，来控制变换后图像的输出范围和网格间距。  
<a id="function2"></a> [Rout](#P1) = affineOutputView([sizeA](#P2), [tform](#P3), BoundsStyle=[style](#P4)) 除上述参数外，还可以指定 `BoundsStyle` 参数，对输出视图空间范围施加约束，例如：输出视图是应完全包含变换后的图像，还是应与输入图像的范围保持一致。  
  
## 参数说明
### 输入参数  
**<a id="P2"></a> sizeA — 输入图像大小**  
2 元素数值向量 | 3 元素数值向量  
  
输入图像大小，对于二维图像输入，指定为 2 元素数值向量；对于三维图像输入，指定为 3 元素数值向量。  
  
**<a id="P3"></a> tform — 几何变换**  
几何变换对象  
  
几何变换，指定为下表中列出的几何变换对象：  
  
| 几何变换对象 | 说明 |
| --- | --- |
| **二维几何变换** | |
| <a href="../transltform2d/transltform2d.html">transltform2d</a>  </a> | 平移变换 |
| <a href="../rigidtform2d/rigidtform2d.html">rigidtform2d</a>  </a> | 刚性变换：平移和旋转 |
| <a href="../simtform2d/simtform2d.html">simtform2d</a>  </a> | 相似变换：平移、旋转和各向同性缩放 |
| <a href="../affinetform2d/affinetform2d.html">affinetform2d</a>  </a> | 仿射变换：平移旋转、各向异性缩放、反射和剪切 |
| **三维几何变换** | |
| <a href="../transltform3d/transltform3d.html">transltform3d</a>  </a> | 平移变换 |
| <a href="../rigidtform3d/rigidtform3d.html">rigidtform3d</a>  </a> | 刚性变换：平移和旋转 |
| <a href="../simtform3d/simtform3d.html">simtform3d</a>  </a> | 相似变换：平移、旋转和各向同性缩放 |
| <a href="../affinetform3d/affinetform3d.html">affinetform3d</a>  </a> | 仿射变换：平移、旋转、各向异性缩放、反射和剪切 |
  
**<a id="P4"></a> style — 边界样式**  
`"CenterOutput"` （默认）| `"FollowOutput"` | `"SameAsInput"`  
  
边界样式，指定为以下值之一：  
  
| 样式 | 说明 |
| --- | --- |
| `"CenterOutput"` | 将视图居中于输出空间的图像中心，同时允许平移操作使输出图像移出视图范围。 |
| `"FollowOutput"` | 设置输出视图的范围，使其完全包含变换后的输出图像。 |
| `"SameAsInput"` | 将输出范围设置为与输入范围保持一致。 |
 
### 输出参数  
**<a id="P1"></a> Rout — 空间参考信息**  
`imref2d` 对象 | `imref3d` 对象  
  
空间参考信息，指定为 <a href="../imref2d/imref2d.html">imref2d</a>  </a> 或 <a href="../imref3d/imref3d.html">imref3d</a>  </a> 对象。将 `Rout` 传入 <a href="../imwarp/imwarp.html">imwarp</a>  </a> 函数的 `OutputView`，可用于指定变换后输出图像的空间参考信息。  
  
## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../imwarp/imwarp.html">imwarp</a> | <a   
href="../randomAffine2d/randomAffine2d.html">randomAffine2d</a> | <a
href="../randomAffine3d/randomAffine3d.html">randomAffine3d</a>   
  
  
  

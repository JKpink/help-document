## imcontrast  
调整灰度图像对比度工具

## 说明  

imcontrast 函数用于打开调整对比度工具，使您能够以交互方式调整已显示灰度图像的对比度和亮度。使用该工具，您可以：

- 可视化图像像素值直方图，查看图像数据范围与显示范围；
- 通过拖动直方图红色窗口、输入数值或吸管取点调整图像显示范围；
- 自动缩放显示范围（匹配数据范围 / 消除异常值）；
- 可选调整图像实际像素数据（需先修改对比度后启用）。

注意：该工具默认仅修改图像的显示效果（通过调整坐标区 CLim 属性），不改变图像原始数据；若需修改图像数据，可使用 imadjust 函数，或在工具中选择 “调整数据” 选项。

## 打开图像查看器App  
- 使用 imcontrast 函数，打开与当前图窗中灰度图像关联的对比度调整工具；

## 编程用途  
**<a id="Q1"></a> imageViewer**  
mcontrast 以空状态打开调整对比度工具
- 要从文件加载图像，请选择从文件导入图像。
- 要加载以变量形式存储在工作区中的图像，请选择从工作区导入图像。

## 版本历史  
在北太天元图像处理工具箱 V2.0 推出

## App  
<a href="../imageViewer/imageViewer.html">imageViewer</a> 

## 函数  
<a href="../imadjust/imadjust.html">imadjust</a> | <a 
href="../stretchlim/stretchlim.html">stretchlim</a> | <a 
href="../imshow/imshow.html">imshow</a> 
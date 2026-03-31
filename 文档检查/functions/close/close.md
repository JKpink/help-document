## dip::close
关闭图形窗口

## 简介
[`dip::close`](#function1)  
[`dip::close(fig)`](#function2)  
[`dip::close("all")`](#function4)  
<!-- [ `close all hidden`](#function5)   
[ `close all force`](#function6)    -->

## 用法 
<a id="function1"></a> dip::close 关闭当前图窗。  
<a id="function2"></a> dip::close([fig](#Q1)) 关闭 `fig` 指定的图窗。  
<a id="function4"></a> dip::close("all") 关闭其句柄可见的所有图窗。 

## 参数说明
### 输入参数
**<a id="Q1"></a> fig — 要关闭的图窗**  
一个或多个 `Figure` 对象、图窗编号或图窗名称

要关闭的图窗，指定为一个或多个 `Figure` 对象、图窗编号或图窗名称。  

**示例：** dip::close(f) 关闭具有句柄 f 的图窗。  
**示例：** dip::close([1 2]) 关闭具有编号 1 和 2 的图窗。  
**示例：** dip::close('First Figure', 'Second Figure') 关闭具有名称 'First Figure' 和 'Second Figure' 的图窗。



## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../figure/figure.html">figure</a> 
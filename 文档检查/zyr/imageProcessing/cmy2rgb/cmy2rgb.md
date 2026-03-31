## cmy2rgb
将 CMY 图像转换为 RGB 图像

## 简介
[`RGB = cmy2rgb(CMY)`](#function1)

## 用法
<a id="function1"></a>
[RGB](#P1) = cmy2rgb[(CMY)](#Q1) 将 CMY 图像的青色、品红和黄色值转换为 RGB 图像的红色、绿色和蓝色值。

## 参数说明
### 输入参数
**<a id="Q1"></a> CMY — CMY 图像**  
数值数组

要转换的 CMY 颜色表，指定为数值数组，采用下列格式之一。
- c×3 颜色表，每行指定一个 CMY 三元组。
- m×n×3 图像。

**数据类型：** `single` | `double` | `uint8` | `uint16` 

### 输出参数
**<a id="P1"></a>  RGB — RGB 图像**  
数值数组

转换后的 RGB 颜色表，以与输入大小相同的数值数组形式返回。

**数据类型：** `double` 

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../rgb2cmy/rgb2cmy.html">rgb2cmy</a>

## rgb2cmy
将 RGB 图像转换为 CMY 图像

## 简介
[`CMY = rgb2cmy(RGB)`](#function1)

## 用法
<a id="function1"></a>
[CMY](#P1) = rgb2cmy[(RGB)](#Q1) 将 RGB 图像的红色、绿色和蓝色值转换为 CMY 图像的青色、品红和黄色值。

## 参数说明
### 输入参数
**<a id="Q1"></a> RGB — RGB 图像**  
数值数组

要转换的 RGB 颜色值，指定为数值数组，采用下列格式之一。

- c×3 颜色图。每行指定一个 RGB 三元组。
- m×n×3 RGB 图像。

**数据类型：** `single` | `double` | `uint8` | `uint16` 

### 输出参数
**<a id="P1"></a> CMY — CMY 图像**  
数值数组

转换后的 CMY 颜色值，以与输入大小相同的数值数组形式返回。

**数据类型：** `double` 

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../cmy2rgb/cmy2rgb.html">cmy2rgb</a>

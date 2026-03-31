## getrangefromclass
基于图像类型获取其默认显示范围

## 简介
[ `range = getrangefromclass(I)`](#function1)  

## 用法
<a id="function1"></a>
[range](#P1) = getrangefromclass([I](#Q1)) 根据输入图像 `I` 的数据类型返回该图像的默认显示范围。  

## 参数说明
### 输入参数
**<a id="Q1"></a> I — 输入图像**  
数值数组 | 逻辑数组

输入图像，指定为数值数组或逻辑数组。

### 输出参数
**<a id="P1"></a> range — 显示范围**  
2 元数值向量

显示范围，以 [min max] 形式的 2 元数值向量形式返回。

**数据类型：**`double`

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

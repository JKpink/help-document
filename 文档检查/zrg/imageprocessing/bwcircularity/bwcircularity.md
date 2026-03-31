## bwcircularity 
二值图像区域的圆度

## 简介
[ `Stats = bwcircularity(BW)`](#function1)

## 用法
<a id="function1"></a>
[Stats](#Q1) = bwcircularity([BW](#Q2)) 返回 1×n 向量，元素值为各连通域的圆度，范围 0–1，1 表示完美圆形。

## 参数说明
### 输入参数
**<a id="Q2"></a>BW — 二值图像**  
逻辑数组

二值图像，指定为二维逻辑数组。

**数据类型：** `logical`

### 输出参数
**<a id="Q1"></a>Stats — 圆度**  
1×n 向量 

圆度，返回一个 1×n 向量。圆度是区域与圆相似程度的度量。

**数据类型**:`double`

## 版本历史
在北太天元图像处理工具箱 V3.0 推出

## 相关主题

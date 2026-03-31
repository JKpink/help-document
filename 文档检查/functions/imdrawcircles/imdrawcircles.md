## imdrawcircles
在图像上画圆

## 简介
[`B = imdrawcircles(I, center, radius)`](#function1)  
[`B = imdrawcircles(I, center, radius, color)`](#function2)

## 用法 
<a id="function1"></a> B = imdrawcircles([I](#Q4), [center](#Q1), [radius](#Q2)) 在图像 `I` 上绘制具有以 `centers` 为圆心和 `radius` 为半径的圆。  
<a id="function2"></a> B = imdrawcircles([I](#Q4), [center](#Q1), [radius](#Q2), [color](#Q3)) 使用 `color` 来指定圆的颜色。

## 参数说明
### 输入参数
**<a id="Q4"></a> I — 需要画圆的图像**  


需要画圆的图像，可指定为灰度、真彩色或二值图像。

**<a id="Q1"></a> centers — 圆心坐标**  

圆心坐标，指定为两列数值矩阵。圆心的 `x` 坐标在第一列，`y` 坐标在第二列。

**<a id="Q2"></a> radius — 圆半径**  

圆半径，指定为正数或由正数组成的列向量，长度与 `centers` 相同。当 `radius` 是一个正数时，`imdrawcircles` 以相同半径绘制所有圆。当 `radius` 是一个列向量时，`imdrawcircles` 按圆心 centers(j,:) 及其对应的半径 radius(j) 绘制每个圆。

**<a id="Q3"></a> color — 圆的颜色**  


圆的颜色，现仅支持指定为 RGB 三元组。

RGB 三元组是包含三个元素的行向量，其元素分别指定颜色中红、绿、蓝分量的强度。强度值必须位于 [0, 255] 范围内，例如 [100 200 30]。

### 输出参数
**<a id="P1"></a> B — 画上圆后的图像**  


画上圆后的图像，返回为 RGB 图像。

## 版本历史
在北太天元图像处理工具箱 V1.1 推出

## bwulterode 
二值图像终极腐蚀

## 简介
[`BW2 = bwulterode(BW)`](#function1)  
[`BW2 = bwulterode(BW, method)`](#function2)  
[`BW2 = bwulterode(__, conn)`](#function3)

## 用法
<a id="function1"></a>
[BW2](#Q4) = bwulterode([BW](#Q1)) 计算二值图像 `BW` 的终极腐蚀。`BW` 的终极腐蚀由 `BW` 的补集的欧几里得距离变换的区域最大值组成。  
<a id="function2"></a>
[BW2](#Q4)  = bwulterode([BW](#Q1), [method](#Q2)) 指定距离变换的计算方法，其中 `method` 可以为chessboard，cityblock，euclidean，quasi-euclidean之一。  
<a id="function3"></a>
[BW2](#Q4)  = bwulterode(__, [conn](#Q3)) 指定像素连通性。


## 参数说明
### 输入参数
**<a id="Q1"></a> BW — 二进制图像**  
数值数组 | 逻辑数组

二进制图像，指定为任意维度的数字或逻辑数组。对于数字输入，任何非零像素都被视为 1 (true)。

**数据类型: ** `logical`

**<a id="Q2"></a> method — 距离变换方法**  
'euclidean'  (默认) | 'quasi-euclidean' | 'cityblock' | 'chessboard'

距离变换方法，指定为此表中的值之一。

|方法|描述| 
|:-|:-|
|'euclidean' |在二维中，(x<sub>1</sub>, y<sub>1</sub>)  和 (x<sub>2</sub>, y<sub>2</sub>) 之间的棋盘距离为最大值 (│x<sub>1</sub> – x<sub>2</sub>│,│y<sub>1</sub> – y<sub>2</sub>│)。|
| 'cityblock' |在二维中，(x<sub>1</sub>, y<sub>1</sub>) 和 (x<sub>2</sub>, y<sub>2</sub>) 之间的城市街区距离为│x<sub>1</sub> – x<sub>2</sub>│+│y<sub>1</sub> – y<sub>2</sub>│
|'quasi-euclidean'|在二维中，(x<sub>1</sub>, y<sub>1</sub>) 和 (x<sub>2</sub>, y<sub>2</sub>) 之间的准欧几里得距离为√(x<sub>1</sub> − x<sub>2</sub>)<sup>2</sup> + (y<sub>1</sub> − y<sub>2</sub>)<sup>2|
| 'chessboard'|在二维中，(x<sub>1</sub>, y<sub>1</sub>) 和  (x<sub>2</sub>, y<sub>2</sub>) 之间的欧几里得距离为│x<sub>1</sub> − x<sub>2</sub>│+ (√2−1)│y<sub>1</sub> − y<sub>2</sub>│, │x<sub>1</sub> − x<sub>2</sub>│>│y<sub>1</sub> − y<sub>2</sub>│<br> (√2−1)│x<sub>1</sub> − x<sub>2</sub>│+│y<sub>1</sub> − y<sub>2</sub>│,否则|

**<a id="Q3"></a> conn — 像素连通性**  
4 | 8 

像素连通性，指定为下表中的值之一。对于二维图像，默认连通性是 4。

<table>
  <tr>
    <td>值</td>
    <td>意义</td>
  </tr>
  <tr>
    <td colspan="2">二维连通</td>
  </tr>
  <tr>
    <td>4</td>
    <td>如果像素的边缘相互接触，则这些像素具有连通性。像素的邻域是水平或垂直方向上的相邻像素。</td>
  </tr>
  <tr>
    <td>8</td>
    <td>如果像素的边缘或角相互接触，则这些像素具有连通性。像素的邻域是水平、垂直或对角线方向上的相邻像素。</td>
  </tr>
</table>
**数据类型: ** `double` | `logical`

### 输出参数
**<a id="Q4"></a> BW2 — 腐蚀图像**  
逻辑数组

腐蚀图像，作为与 `BW` 大小相同的逻辑数组返回。

**数据类型: ** `logical`

## 版本历史
在北太天元图像处理工具箱 V1.1 推出

## 相关主题
<a href="../bwdist/bwdist.html">bwdist</a> | <a 
href="../conndef/conndef.html">conndef</a> | <a 
href="../imregionalmax/imregionalmax.html">imregionalmax</a> 


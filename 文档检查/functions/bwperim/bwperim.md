## bwperim 
确定二值图像中目标的边界

## 简介
[`BW2 = bwperim(BW)`](#function1)  
[`BW2 = bwperim(BW, conn)`](#function2)   

## 用法
<a id="function1"></a>  
[BW2](#Q3) = bwperim([BW](#Q1)) 返回一个二值图像，该图像仅包含输入图像 `BW` 中对象的边界像素。如果某像素非零并且与至少一个零值像素连通，则该像素是边界的一部分。  
<a id="function2"></a>  
[BW2](#Q3)  = bwperim([BW](#Q1), [conn](#Q2)) 还指定连通性 `conn` 。  

## 参数说明
### 输入参数
**<a id="Q1"></a> BW — 输入二值图像**  
数值数组 | 逻辑数组

输入二值图像，指定为任意维度的数值或逻辑数组。对于数值输入，任何非零像素都被视为真。

**数据类型：** `logical`

**<a id="Q2"></a> conn — 像素连通性**  
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

**数据类型：** `double` | `logical`

### 输出参数
**<a id="Q3"></a> BW2 — 仅包含对象的边界像素的输出二值图像**  
逻辑数组

仅包含对象的边界像素的输出图像，以逻辑数组形式返回。  

**数据类型：** `logical`

## 版本历史 
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../bwarea/bwarea.html">bwarea</a> | <a 
href="../imfill/imfill.html">imfill</a> | <a 
href="../conndef/conndef.html">conndef</a> | <a 
href="../bweuler/bweuler.html">bweuler</a> | <a 
href="../bwboundaries/bwboundaries.html">bwboundaries</a> | <a 
href="../bwtraceboundary/bwtraceboundary.html">bwtraceboundary</a> 


## bwmorph3 
二值3维图像形态学运算

## 简介
[ `J = bwmorph3(BW, operation)`](#function1)

## 用法
<a id="function1"></a>
[J](#Q3) = bwmorph3([BW](#Q1), [operation](#Q2)) 对二值3维图像 `BW` 应用特定的形态学运算，其中 `operation` 可以为branchpoints，clean，endpoints，fill，majority，remove其中之一。

## 参数说明
### 输入参数
**<a id="Q1"></a> BW — 二值3维图像**  
三维数值矩阵 | 三维逻辑矩阵

二值3维图像，指定为三维数值矩阵或三维逻辑矩阵。对于数值输入，任何非零像素都被视为 1 (true)。如需对2维图像进行操作，需改用 `bwmorph`。

**<a id="Q2"></a> operation — 要执行的形态学运算**  
字符向量 | 字符串标量

要执行的形态学运算，指定为下列项之一。  
|操作|描述| 
|:-|:-|
|branchpoints|提取骨架的分支点。分支点指的是多个骨架分支交汇的体素。
注意：提取分支点前，必须先对图像进行骨架化处理，可使用 `bwskel` 函数实现。|  
|clean|移除孤立体素并将其置为 0。孤立体素的定义为：取值为 1、按 26 连通规则判断无相邻的 1 值体素、且被 0 值体素完全包围的单个体素。|  
|endpoints|提取骨架的端点。端点指的是骨架分支末端的体素。
注意：提取端点前，必须先对图像进行骨架化处理，可使用 `bwskel` 函数实现。|  
|fill|填充孤立的内部体素（即孔洞）并将其置为 1。孤立内部体素的定义为：取值为 0、且被 6 连通的 1 值体素完全包围的单个体素。|  
|majority|针对目标体素的3×3×3,26连通邻域，若邻域内有 14 个及以上的 1 值体素（即占多数），则保留该目标体素的 1 值；否则将其置为 0。|  
|remove|移除内部体素并将其置为 0。内部体素的定义为：取值为 1、且被 6 连通的 1 值体素完全包围的单个体素。|  

**数据类型**： `char` | `string	`

### 输出参数
**<a id="Q3"></a> J — 执行形态学运算后的图像**  
逻辑数组

执行形态学运算后的图像，以逻辑数组形式返回，其大小与输入图像 [BW](#Q1) 相同。

### 提示
- 要对3维图像执行行形态学膨胀或腐蚀操作，请使用 <a href="../imdilate/imdilate.html">imdilate</a> 或 <a 
href="../imerode/imerode.html">imerode</a>  函数，并指定结构元素 ones(3,3,3)。
- 要对3维图像执行形态学闭运算、开运算、底帽滤波或顶帽滤波，请分别使用 <a 
href="../imclose/imclose.html">imclose</a> 、 <a 
href="../imopen/imopen.html">imopen</a> 、 <a href="../imbothat/imbothat.html">imbothat</a> 或 <a 
href="../imtophat/imtophat.html">imtophat</a>  函数，并指定结构元素 ones(3,3,3)。

## 版本历史 
在北太天元图像处理工具箱 V3.0 推出

## 相关主题
<a href="../imdilate/imdilate.html">imdilate</a> | <a 
href="../imerode/imerode.html">imerode</a> | <a 
href="../imclose/imclose.html">imclose</a> | <a 
href="../imopen/imopen.html">imopen</a> | <a href="../imbothat/imbothat.html">imbothat</a> | <a 
href="../imtophat/imtophat.html">imtophat</a> | <a 
href="../bwmorph/bwmorph.html">bwmorph</a> | <a 
href="../bwskel/bwskel.html">bwskel</a> 

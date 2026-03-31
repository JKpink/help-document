## jaccard
Jaccard指标

## 简介
[`similarity = jaccard(BW1, BW2)`](#function1)  
[`similarity = jaccard(L1, L2)`](#function2)  
[`similarity = jaccard(C1, C2)`](#function3)

## 用法
<a id="function1"></a>
[similarity](#Q1) = jaccard([BW1](#Q2), [BW2](#Q3)) 计算二值图像 `BW1` 和 `BW2` 的交集与 `BW1` 和 `BW2` 的并集的比值，也称为 `Jaccard` 指数，图像是二值图像。

<a id="function2"></a>[similarity](#Q1) = jaccard([L1](#Q4), [L2](#Q5)) 对标签图像 `L1` 与 `L2` 中的每一个标签类别分别计算 `Jaccard` 系数。

<a id="function3"></a>[similarity](#Q1) = jaccard([C1](#Q6), [C2](#Q7)) 对类别型图像 `C1` 与 `C2` 中的每一个类别分别计算 `Jaccard` 系数。

## 参数说明
### 输入参数
**<a id="Q2"></a> BW1 — 第一个二值图像**  
逻辑数组

第一个二值图像，指定为任何维度的逻辑数组。

**数据类型：** `logical`

**<a id="Q3"></a> BW2 — 第二个二值图像**  
逻辑数组

第二个二值图像，指定为任何维度的逻辑数组。

**数据类型：** `logical`

**<a id="Q4"></a> L1 —— 第一个标签图像**
非负整数数组

第一个标签图像，指定为一个由非负整数构成的数组，维度不限。

**数据类型：** `double`

**<a id="Q5"></a> L2 —— 第二个标签图像**
非负整数数组

第二个标签图像，指定为一个由非负整数构成的数组，维度不限。

**数据类型：** `double`
**<a id="Q6"></a> C1 —— 第一个标签图像**
类别数组

第一个类别图像，指定为一个维度不限的 `categorical` 数组。

**数据类型：** `category`

**<a id="Q7"></a> C2 —— 第二个标签图像**
类别数组

第二个类别图像，指定为一个维度不限的 `categorical` 数组。

**数据类型：** `category`

### 输出参量
**<a id="Q1"></a> similarity — Jaccard相似系数**  
数值标量 | 数值向量

相似系数，以数值标量或数值向量的形式返回，其值在 [0,1] 范围内。相似性为1表示两个图像的分割完全匹配，如果输入数组是：
- 二值图像，相似性是一个标量。

**数据类型：** `double`


## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../dice/dice.html">dice</a> | <a 
href="../bfscore/bfscore.html">bfscore</a> 


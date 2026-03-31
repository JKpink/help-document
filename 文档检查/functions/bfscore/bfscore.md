## bfscore
图像分割的轮廓匹配分数

## 简介
[`score = bfscore(prediction, groundTruth)`](#function1)  
[`[score, precision, recall] = bfscore(prediction, groundTruth)`](#function2)  
[`[___]=bfscore(prediction,groundTruth,threshold)`](#function3)

## 用法
<a id="function1"></a>
[score](#Q1) = bfscore([prediction](#Q4), [groundTruth](#Q5))  计算预测分割结果 (prediction) 与真实分割结果 (groundTruth) 之间的 BF(Boundary F1) 轮廓匹配得分。prediction 和 groundTruth 可以是一对用于二值分割的逻辑数组，也可以是一对用于多类分割的标签数组或分类数组。

<a id="function2"></a>
[[score](#Q1), [precision](#Q2), [recall](#Q3)] = bfscore([prediction](#Q4), [groundTruth](#Q5))  并返回预测图像相较于真实图像的精确率与召回率数值。

<a id="function3"></a>
[ ___ ]=bfscore([precesion](#Q2),[groundTruth](#Q5),[threshold](#Q6))  以指定阈值作为距离误差容限，判定边界点是否匹配，并据此计算BF分数。

## 参数说明
### 输入参数
**<a id="Q4"></a> prediction — 预测分割结果**  
二维或三维逻辑数组、数值数组或分类数组

预测分割结果，指定为二维或三维的逻辑数组、数值数组或分类数组。若 `prediction` 为数值数组，则表示标签数组，必须包含数据类型为 double 的非负整数。

**数据类型：** `logical` | `double` | `categorical`

**<a id="Q5"></a> groundTruth — 真实分割标注**  
二维或三维逻辑数组、数值数组或分类数组

真实分割标注，指定为与预测尺寸和数据类型相同的二维或三维逻辑数组、数值数组或分类数组。若 `groundTruth` 为数值数组，则表示标签数组，必须包含数据类型为 double 的非负整数。

**数据类型：** `logical` | `double` | `categorical`

**<a id="Q6"></a> threshold - 距离误差阈值**
正标量

以像素为单位的距离误差容限阈值，须指定为正标量。该阈值用于判定边界点是否匹配。若没有指定此阈值，则默认取值为图像对角线长度的0.75%。

**数据类型：** `double`

### 输出参量
**<a id="Q1"></a> score — BF 分数**  
数值标量 | 数值向量

BF 分数，以数值标量或向量形式返回，其值范围在 [0, 1] 之间。分数为 1 表示 `prediction` 和 `groundTruth` 中对应类别的物体轮廓完全匹配。若输入数组为：

- 逻辑数组，`score` 为标量，表示前景的 `BF` 分数。

- 标签数组或分类数组，`score` 为向量。`score` 中的第一个系数是第一个前景类别的 `BF` 分数，第二个系数是第二个前景类别的分数，依此类推。

**<a id="Q2"></a> precision — 精确率**  
数值标量 | 数值向量

精确率，以数值标量或向量形式返回，其值范围在 [0, 1] 之间。每个元素表示对应前景类别中物体轮廓的精确率。

精确率是指预测分割边界上足够接近真实分割边界的点数量与预测边界总长度的比值。换言之，精确率反映的是真正例检测所占的比例，而非假正例。

**<a id="Q3"></a> recall — 召回率**  
数值标量 | 数值向量

召回率，以数值标量或向量形式返回，其值范围在 [0, 1] 之间。每个元素表示对应前景类别中物体轮廓的召回率。

召回率是指真实分割边界上足够接近预测分割边界的点数量与真实边界总长度的比值。换言之，召回率反映的是被正确检测到的真正例所占的比例，而非漏检的正例。

​
## 参考
[1] Csurka G, Larlus D, Perronnin F. What is a good evaluation measure for semantic segmentation? Proceedings of the British Machine Vision Conference. 2013: 32.1-32.11.

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
 <a href="../jaccard/jaccard.html">jaccard</a> | <a 
href="../dice/dice.html">dice</a> 
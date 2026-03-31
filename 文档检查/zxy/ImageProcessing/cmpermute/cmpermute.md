## cmpermute
重新排列颜色图中的颜色

## 简介
[`[Y, newmap] = cmunique(X, map)`](#function1)  
[`[Y, newmap] = cmunique(X, map, index)`](#function2)  

## 用法
<a id="function1"></a>
[[Y](#P1), [newmap](#P2)] = cmunique([X](#Q1), [map](#Q2)) 随机对颜色图 `map` 中的颜色重新排序以生成一个新的颜色图 `newmap`。cmpermute 函数还修改索引图像 X 中的值以保持索引与颜色图之间的对应，并在 `Y` 中返回结果。图像 `Y` 和关联的颜色图 `newmap` 生成与 `X` 和 `map` 相同的图像。  
<a id="function2"></a>
[[Y](#P1), [newmap](#P2)] = cmunique([X](#Q1), [map](#Q2), [index](#Q3)) 使用排序矩阵（例如 sort 的第二个输出）来在新颜色图中定义颜色的顺序。  

## 参数说明
### 输入参数
**<a id="Q1"></a> X — 索引图像**  
m×n 整数矩阵

索引图像，指定为 m×n 整数矩阵。

**数据类型：** `double` | `uint8`

**<a id="Q2"></a> map — 颜色图**  
c×3 矩阵

与索引图像 [X](#Q1) 相关联的颜色图，指定为由范围 [0, 1] 内的值组成的 c×3 矩阵。`map` 的每行都是一个三元素 RGB，指定颜色图的单种颜色的红、绿和蓝分量。

**数据类型：** `double`

**<a id="Q3"></a> index — 排序索引**  
由正整数组成的 c 元素向量

排序索引，指定为由正整数组成的 c 元素向量。

**数据类型：** `double`

### 输出参数
**<a id="P1"></a> Y — 索引图像**  
m×n 整数矩阵

索引图像，以 m×n 整数矩阵形式返回。Y 与输入索引图像 [X](#Q1) 具有相同的数据类型。  

**数据类型：** `double` | `uint8`

**<a id="P2"></a> newmap — 减少了颜色的颜色图**  
c×3 矩阵

与输出索引图像 [Y](#P1) 相关联的减少了颜色的颜色图，返回为由范围 [0, 1] 内的值组成的 c×3 矩阵。newmap 的每行都是一个三元素 RGB，指定颜色图的单种颜色的红、绿和蓝分量。  

**数据类型：** `double`

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
<a href="../randperm/randperm.html">randperm</a> | <a
href="../sort/sort.html">sort</a>

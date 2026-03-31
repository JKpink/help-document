## conndef
创建连通性矩阵

## 简介
[`conn = conndef(num_dims, type)`](#function1)

## 用法
<a id="function1"></a>
[conn](#P1) = conndef([num_dims](#Q1), [type](#Q2)) 返回针对 `num_dims` 维、由 `type` 定义的像素连通性矩阵。

## 参数说明
### 输入参数
**<a id="Q1"></a> num_dims — 维度数**  
正整数

维度数：指定为正整数。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16`

**<a id="Q2"></a> type — 邻域连通性类型**   
`minimal` | `maximal`

邻域连通性类型：指定为 `"minimal"` 或 `"maximal"`。

| 值 | 说明 |
| :----------- | :----------- |
| `minimal` | 定义一种邻域：对于 N 维场景，其邻域像素仅在 (N-1) 维表面上与中心像素接触。 |
| `maximal` | 定义一种包含所有以任意方式接触中心像素的邻域像素的邻域；等价于 `ones(repmat(3,1,NUM_DIMS))`。 |

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` 

### 输出参数
**<a id="P1"></a> conn — 像素连通性**   
`3×3×…×3` 逻辑矩阵

像素连通性矩阵：返回为 `3×3×…×3` 的逻辑矩阵。`conn` 关于其中心元素对称。

## 版本历史
在北太天元图像处理工具箱 V1.0 推出
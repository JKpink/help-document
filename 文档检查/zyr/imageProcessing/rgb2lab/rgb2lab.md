## rgb2lab
将 RGB 转换为 CIE 1976 L\*a\*b\*

## 简介
[`lab = rgb2lab(RGB)`](#function1)  
[`lab = rgb2lab(RGB, Name, Value)`](#function2)

## 用法
<a id="function1"></a>
[lab](#P1) = rgb2lab[(RGB)](#Q1) 将 sRGB 值转换为 CIE 1976 L\*a\*b\* 值。

<a id="function2"></a>
[lab](#P1) = rgb2lab[(RGB, Name, Value)](#Q2) 通使用名称-值参数指定额外选项，例如 RGB 图像的颜色空间。

## 参数说明
### 输入参数
**<a id="Q1"></a> RGB — RGB 颜色值**  
数值数组

要转换的 RGB 颜色值，指定为数值数组，采用下列格式之一。

- c×3 颜色图。每行指定一个 RGB 颜色值。
- m×n×3 图像。
- m×n×3×p 图像堆叠。

**数据类型：** `single` | `double` | `uint8` | `uint16`

### 名称-值参数
将可选参数对按 `Name1, Value1, ..., NameN, ValueN` 的形式指定，其中 Name 为参数名称，Value 为对应的取值。名称-值参数必须放在其他输入参数之后，但各名称-值对之间的顺序不影响结果。

**示例** lab = rgb2lab([0.25 0.40 0.10], "WhitePoint", "d50") 将 WhitePoint 指定为 "d50"。

**<a id="Q2"></a> ColorSpace — 输入 RGB 数值的颜色空间**  
"srgb" | "adobe-rgb-1998" | "prophoto-rgb" | "linear-rgb"

输入 RGB 数值的颜色空间，指定为 "srgb"、"adobe-rgb-1998"、"prophoto-rgb" 或 "linear-rgb"。如果指定为 "linear-rgb"，则 rgb2lab 假设输入 RGB 是线性 sRGB 数值。

**数据类型：** `string` | `char`

**<a id="Q2"></a> WhitePoint — 参考白点**  
"d65" | "a" | "c" | "e" | "d50" | "d55"

参考白点，指定为 1×3 向量，或表中列出的某一种 CIE 标准光源。

| **取值**  | **白点（White Point）**                                                                                                  |
| ------- | -------------------------------------------------------------------------------------------------------------------- |
| `"a"`   | CIE 标准 A，[1.0985, 1.0000, 0.3558]。模拟典型的家用钨丝灯照明，相关色温为 2856 K。                                                |
| `"c"`   | CIE 标准 C，[0.9807, 1.0000, 1.1822]。模拟平均或北方天空日光，相关色温为 6774 K。该标准已被 CIE 弃用。                       |
| `"e"`   | 等能量辐射体，[1.000, 1.000, 1.000]。常用作理论参考白点。                                                     |
| `"d50"` | CIE 标准 D50，[0.9642, 1.0000, 0.8251]。模拟日出或日落时较暖的日光，相关色温为 5003 K。也称为地平线光。                      |
| `"d55"` | CIE 标准 D55，[0.9568, 1.0000, 0.9214]。模拟上午中段或下午中段日光，相关色温为 5500 K。                                             |
| `"d65"` | CIE 标准 D65，[0.9504, 1.0000, 1.0888]。模拟正午日光，相关色温为 6504 K。                                                    |

**数据类型：** `single` | `double` | `string` | `char`

### 输出参数
**<a id="P1"></a> lab — 转换后的 L\*a\*b\* 颜色值**  
m×n×3 数值数组

转换后的 L\*a\*b\* 颜色值，返回与输入大小相同的数值数组。

| 属性 | 描述 |
| :----------------------- | :----------------------- |
| L\* | 图像的亮度。值在 [0, 100] 范围内，其中 0 指定黑色，100 指定白色。随着 L\* 的增加，颜色变得更亮。 |
| a\* | 图像中红色或绿色色调的量。大的正 a\* 值对应于红色/品红色。大的负 a\* 值对应于绿色。虽然 a\* 没有单一范围，但值通常在 [-100, 100] 或 [-128, 127) 范围内。 |
| b\* | 图像中黄色或蓝色色调的量。大的正 b\* 值对应于黄色。大的负 b\* 值对应于蓝色。虽然 b\* 没有单一范围，但值通常在 [-100, 100] 或 [-128, 127) 范围内。 |

## 提示
- 如果将输入 RGB 颜色空间指定为 "linear-rgb"，那么 rgb2lab 假设输入是线性 sRGB 数值。相反，如果输入为 Adobe RGB (1998)，则可以使用 <a href="../lin2rgb/lin2rgb.html">lin2rgb</a> 函数将其转换为非线性编码的 Adobe RGB。
例如，要将线性化 Adobe RGB (1998) 图像 RGBlinadobe 转换为 CIE 1976 L\*a\*b\* 颜色空间，可以分两步进行转换:

```
    RGBadobe = lin2rgb(RGBlinadobe, "ColorSpace", "adobe-rgb-1998");
    LAB = rgb2lab(RGBadobe, "ColorSpace", "adobe-rgb-1998");
```

## 版本历史
在北太天元图像处理工具箱 V1.0 推出

## 相关主题
<a href="../rgb2xyz/rgb2xyz.html">rgb2xyz</a> | <a
href="../lab2rgb/lab2rgb.html">lab2rgb</a> | <a 
href="../xyz2lab/xyz2lab.html">xyz2lab </a>

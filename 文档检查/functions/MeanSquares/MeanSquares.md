## MeanSquares
基于均方误差（Mean Squared Error, MSE）的图像相似性度量工具

## 用法 
`MeanSquares` 创建用于配置均方误差度量的对象（用于配准优化），可以将其传递给 `imregister` 函数以解决图像配准问题。

## 算法
均方图像相似度度量是通过计算每张图像中相应像素的差值的平方，并对这些平方差取平均值得到的。

## 版本历史
在北太天元图像处理工具箱 V2.0 推出

## 相关主题
### 函数
<a href="../imregister/imregister.html">imregister</a> | <a
href="../imregconfig/imregconfig.html">imregconfig</a> 
### 对象
<a 
href="../MattesMutualInformation/MattesMutualInformation.html">MattesMutualInformation</a> | <a 
href="../OnePlusOneEvolutionary/OnePlusOneEvolutionary.html">OnePlusOneEvolutionary</a> | <a 
href="../RegularStepGradientDescent/RegularStepGradientDescent.html">RegularStepGradientDescent</a>
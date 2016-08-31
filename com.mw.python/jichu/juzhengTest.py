# encoding:utf-8
# 列表
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
# 当a和b为array时， a * b 计算了a和b的数量积（对应Matlab的 a .* b ），。
print 'a * b = \n', a * b
# dot(a, b) 计算了a和b的矢量积（对应Matlab的 a * b ）
# dot函数用于矩阵乘法，对于二维数组，它计算的是矩阵乘积，对于一维数组，它计算的是内积
print 'dot(a,b) = \n', np.dot(a, b)

a = np.mat('1 2; 3 4')
b = np.mat('5 6; 7 8')
# 使用matrix时，运算符 * 用于计算矢量积
print 'a * b = \n', a * b
# 函数 multiply() 用于计算数量积
print 'multiply(a, b) = \n', np.multiply(a, b)

# 创建单位矩阵
I = np.eye(3)
print I

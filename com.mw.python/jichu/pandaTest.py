# coding: utf-8

from pandas import Series, DataFrame

# Series 可以看做一个定长的有序字典。基本任意的一维数据都可以用来构造 Series 对象
s = Series([1, 2, 3.0, 'abc'])
print s

# Series 对象包含两个主要的属性：index 和 values，index 的值是从 0 起递增的整数,

d = Series(data=[1, 3, 5, 7], index=['a', 'b', 'x', 'y'])
print d

# DataFrame
# DataFrame 是一个表格型的数据结构，它含有一组有序的列（类似于 index），每列可以是不同的值类型（不像 ndarray 只能有一个 dtype）。
data = {'state': ['Ohino', 'Ohino', 'Ohino', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

df = DataFrame(data)
print df

# 较完整的 DataFrame 构造器参数为：DataFrame(data=None,index=None,coloumns=None),同样缺失值由 NaN 补上
# DataFrame 面向行和面向列的操作基本是平衡的，任意抽出一列都是 Series。
df = DataFrame(data, index=['one', 'two', 'three', 'four', 'five'],
               columns=['year', 'state', 'pop', 'debt'])
print df

print df.index
print df.columns
print type(df['debt'])

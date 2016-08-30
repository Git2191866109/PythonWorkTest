# -*- coding:utf-8 -*-

import numpy as np
import xlrd

# model save
# 打开Excel文件读取数据
data = xlrd.open_workbook('raw-model-v5.xlsx')
table = data.sheets()[0]
model = []
#  获取行数和列数
nrows = table.nrows
print nrows
ncols = table.ncols
print ncols

for i in xrange(1, table.nrows):
    model.append(table.row_values(i)[2:27])
    # 获取整行和整列的值（数组）
    # table.row_values(i)
    # table.col_values(i)

model = np.array(model)
print model
print model.shape

# save the model
np.save('model_v5.npy', model)

# tags save
tag_list = []
for i in xrange(1, table.nrows):
    tag_list.append(int(table.col_values(0)[i]))
print tag_list
# tag_list = np.array(tag_list)
print tag_list[84]
np.save('tag_list_v5.npy', tag_list)

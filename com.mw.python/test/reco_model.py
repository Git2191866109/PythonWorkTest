# -*- coding:utf-8 -*-

import numpy as np
import xlrd

##model save
data = xlrd.open_workbook('./raw-model-v6.xlsx')
table = data.sheets()[0]
model = []

for i in xrange(1,table.nrows):
    model.append(table.row_values(i)[2:27])


model = np.array(model)
print model
print model.shape[0]

#save the model
np.save('model_v6.npy', model)

##tags save
tag_list = []
for i in xrange(1, table.nrows):
    tag_list.append(int(table.col_values(0)[i]))

#tag_list = np.array(tag_list)
print tag_list[84]
np.save('tag_list_v6.npy',tag_list)






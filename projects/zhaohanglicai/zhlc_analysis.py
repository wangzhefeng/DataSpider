#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


# data
cmb = pd.read_excel("/home/wangzhefeng/project/python/projects/zhaohanglicai/CMB_Finance.xlsx")
print(cmb.head())
print(cmb.shape)
print(cmb.dtypes)

# 数据类型转换
# 将FinDate(期限)字段转换为数值型
cmb.FinDate = cmb.FinDate.str[:-1]#.astype('int')
# 将NetValue(收益率)字段转换为数值型
cmb.NetValue = cmb.NetValue.str[:-1]#.astype('float') / 100
print(cmb.head())

# 预期收益率最高的3各产品
NetValue_sort_desc = cmb[['PrdCode', 'NetValue']].sort_values(by = 'NetValue', ascending = False)
NetValue_duplicate_top = NetValue_sort_desc.drop_duplicates(subset = 'NetValue').head(3)
print(NetValue_duplicate_top)
# 预期收益率最低的3个产品

NetValue_sort_asc = cmb[['PrdCode', 'NetValue']].sort_values(by = 'NetValue', ascending = True)
NetValue_duplicate_last = NetValue_sort_asc.drop_duplicates(subset = 'NetValue').head(3)
print(NetValue_duplicate_last)

# 对各类风险类型的样本量做统计
stats = cmb.Risk.value_counts()
print(stats)

# 理财产品期限的描述性统计
print(cmb.FinDate.describe())

# 
FinDate = []
Risks = cmb.Risk.unique()
print(Risks.sort())
for Risk in Risks:
	FinDate.append(cmb.loc[cmb.Risk == Risk, 'FinDate'])

print(FinDate)

import pandas as pd 
import numpy as np
import matplotlib as plt
from matplotlib import pyplot


# Read file excel
data_xls_Cost = pd.read_excel('CostofbizstartupprocedureinpercentofGNIpercapita.xlsx', index_col=None)
data_xls_Disclosure = pd.read_excel('bizextentdisclosureindex.xlsx', index_col=None)
data_xls_Ease = pd.read_excel('easeofdoingbusiness.xlsx', index_col=None)


# Convert TO CSV
data_xls_Cost.to_csv('Cost.csv', encoding='utf-8', index=False)
data_xls_Disclosure.to_csv('Disclosure.csv', encoding='utf-8', index=False)
data_xls_Ease.to_csv('Ease.csv', encoding='utf-8', index=False)

df1 = pd.read_csv("Cost.csv")
df2 = pd.read_csv("Disclosure.csv")
df3 = pd.read_csv("Ease.csv")

# df1.shape
# df2.shape
# df3.shape
# (df1.isnull().sum())
# (df2.isnull().sum())
# (df3.isnull().sum())

# (df1.iloc[:,-3:].describe())
# (df2.iloc[:,-3:].describe())
# (df3.iloc[:,:].describe())

# df1.info()
# df2.info()
# df3.info()

# #### Top ten countries finding it easiest to do businesses: (index=1 means the most friendly)
Ease_most_friendly_2017 = df3[["country","2017"]].nsmallest(10,"2017")
# Ease_most_friendly_2017.plot(kind="bar",x="country",y="2017",label="index2017", alpha=0.4)
# plt.pyplot.legend(loc='upper right')
# plt.pyplot.title('Top ten countries finding it easiest to do businesses')
# # plt.pyplot.show()


##### Top ten countries finding it hardest to do businesses: (index=1 means the most friendly)
Ease_least_friendly_2017 = df3[["country","2017"]].nlargest(10,"2017")
# Ease_least_friendly_2017.plot(kind="bar",x="country",y="2017",label="index2017", alpha=0.4)
# plt.pyplot.legend(loc='upper right')
# plt.pyplot.title('Top ten countries finding it hardest to do businesses')
# plt.pyplot.show()


##### Top ten countries with minimum expense of setting up business:
Cost_minimum_2017 = df1[["country","2017"]].nsmallest(10,"2017")

##### Top ten countries with maximum expense of setting up business:
Cost_maximum_2017 = df1[["country","2017"]].nlargest(10,"2017")





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

# # print(df1["2017"])
# df1.hist(color='b', label='costbiz2017')
# plt.pyplot.legend(loc='upper right')
# plt.pyplot.title('BusinessSetup2017')
# plt.pyplot.xlabel('country')
# plt.pyplot.ylabel('Cost')
# plt.pyplot.show()

# print (df1["2017"].nlargest(20))
# print (df1[(df1["2003"].nlargest(20))])

# print(df1.nlargest(20, ["2003"]))
# print(df1.nsmallest(20, ["2017"]))
# print (df1["2003"])
# print (df1[["2003","country"]].nlargest(20, "2003"))

a = (df1[["2003","country"]].nlargest(20, "2003"))
a.plot(kind='bar',x='country',y='2003', color='y', label='Cost2003')
plt.pyplot.legend(loc='upper right')
plt.pyplot.title('Hardcore')
plt.pyplot.show()
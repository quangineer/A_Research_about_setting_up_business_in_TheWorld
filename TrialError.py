import pandas as pd 
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

# basic command for df1:
# print (df1.shape)
# print (df1.info())
# print (df1.describe())
# print (df1.dtypes)
# print (df1.isnull().sum())
# print (df1[df1.isnull()])
# print (df1[df1['2017'].notnull()])
# print (df1.isnull())
# print(df1[["2013","2014","2015","2016","2017"]].isnull().sum())
# print (df1.loc[:,"country"])
# print (df1[df1["2010"].isnull()])
# print (df1["2013"].isnull().sum())

# # print(df1["2017"])
# df1.hist(color='b', label='costbiz2017')
# plt.pyplot.legend(loc='upper right')
# plt.pyplot.title('BusinessSetup2017')
# plt.pyplot.xlabel('country')
# plt.pyplot.ylabel('Cost')
# plt.pyplot.show()


s = pd.DataFrame({"A":["Mi","Do","Re","Fa","Son","La","Xi","DoDo"], "B":[1,1,0,1,0,0,0,1]})
# s.where(s>0)
# s.where(s["B"]>0, inplace=True)
# a = s.where(s["B"]>0,10)
# s.mask(s["B"]>0, inplace=True)
# print (s)
# print (a)

survived = s.B == True
died = s.B == False
print (survived)
Rubbish
# # Before the merge, we have to change the name of all columns in df_08 to distinguish from 2018 columns. 
# Cost_minimum_2015.rename(lambda x: x[:] + "_15", axis=1, inplace=True)
# Cost_minimum_2016.rename(lambda x: x[:] + "_16", axis=1, inplace=True)
# Cost_minimum_2017.rename(lambda x: x[:] + "_17", axis=1, inplace=True)
# print (Cost_minimum_2015)
# print (Cost_minimum_2016)
# print (Cost_minimum_2017)
# # Merge 2 datasets:
# df_combined = Cost_minimum_2015.merge(Cost_minimum_2016, left_on='country_15', right_on='country_16', how='outer')
# print (df_combined)
# # M = Cost_minimum_2015.append(Cost_minimum_2016, sort=False)
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

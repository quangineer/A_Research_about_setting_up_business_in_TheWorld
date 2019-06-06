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

# #### Top ten countries finding it easiest to do businesses in 2017: (index=1 means the most friendly)
Ease_most_friendly_2017 = df3[["country","2017"]].nsmallest(10,"2017")
# Ease_most_friendly_2017.plot(kind="bar",x="country",y="2017",label="index2017", alpha=0.4)
# plt.pyplot.legend(loc='upper right')
# plt.pyplot.title('Top ten countries finding it easiest to do businesses')
# # plt.pyplot.show()


##### Top ten countries finding it hardest to do businesses in 2017: (index=1 means the most friendly)
Ease_least_friendly_2017 = df3[["country","2017"]].nlargest(10,"2017")
# Ease_least_friendly_2017.plot(kind="bar",x="country",y="2017",label="index2017", alpha=0.4)
# plt.pyplot.legend(loc='upper right')
# plt.pyplot.title('Top ten countries finding it hardest to do businesses')
# plt.pyplot.show()


##### Top ten countries with minimum expense of setting up business in 2017:
Cost_minimum_2017 = df1[["country","2017"]].nsmallest(10,"2017")
# Cost_minimum_2017.plot(kind="bar",x="country",y="2017",label="price = % over GNI per capita", alpha=0.4)
# plt.pyplot.legend(loc='upper right')
# plt.pyplot.title('Top ten countries with minimum expense of setting up business')
# plt.pyplot.show()

##### Top ten countries with maximum expense of setting up business in 2017:
Cost_maximum_2017 = df1[["country","2017"]].nlargest(10,"2017")
# Cost_maximum_2017.plot(kind="bar",x="country",y="2017",label="price = % over GNI per capita", alpha=0.4)
# plt.pyplot.legend(loc='upper right')
# plt.pyplot.title('Top ten countries with maximum expense of setting up business')
# plt.pyplot.show()

# ##### List all countries that have minimum cost of set-up business AND in the list of easiest countries:
# List_A = []
# for i in Cost_minimum_2017.country:
#     if i in Ease_most_friendly_2017.country.tolist():
#         List_A.append(i)

# ##### Get the values of cost of set-up business in each country in List_A:
# for i in List_A:
#     print (df1[["country","2017"]][df1[["country","2017"]].country == str(i)])

# ##### List all countries that are in the list of easiest countries BUT do NOT have the minimum cost of set-up business:
# List_B = list(set(Ease_most_friendly_2017.country.tolist()) - set(List_A))

# ##### Get the values of cost of set-up business in each country in List_B:
# for i in List_B:
#     print (df1[["country","2017"]][df1[["country","2017"]].country == str(i)])



##### List all countries that have maximum cost of set-up business AND in the list of hardest countries:
List_C = []
for i in Cost_maximum_2017.country:
    if i in Ease_least_friendly_2017.country.tolist():
        List_C.append(i)
# print (List_C)
##### Get the values of cost of set-up business in each country in List_C:
for i in List_C:
    # print (df1[["country","2017"]][df1.country == str(i)])

##### List all countries that are in the list of hardest countries BUT do Not appear in the maximum cost of set-up business:
List_D = list(set(Ease_least_friendly_2017.country.tolist()) - set(List_C))
# print (List_D)
##### Get the values of cost of set-up business in each country in List_D:
for i in List_D:
    print (df1[["country","2017"]][df1.country == str(i)])
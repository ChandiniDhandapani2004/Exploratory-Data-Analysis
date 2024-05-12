import numpy as np import pandas as pd import seaborn as sns
import matplotlib.pyplot as plt
path="/content/drive/MyDrive/Colab Notebooks/Flipkart_laptops.csv" df=pd.read_csv(path)
print(df) 

#To print first 5 rows
df.head()

#To print the number of rows and number of columns or simply the dimension of the dataset
df.shape

#To display summary of statistics
df.describe()
#To display the unique columns of a row
df.Rating.unique()

# Heatmap: 
plt.figure(figsize=(2,3))
sns.heatmap(id.corr(method="pearson")) 
plt.show()

#SCATTER PLOT

sns.scatterplot(x='Name',y='Price',hue='Name',data=Top)
plt.legend(bbox_to_anchor=(1,1),loc=2)
plt.show()


#LINE PLOT

plt.plot(df.Name,df.Price) 
plt.xlabel("Name")
plt.ylabel("Price")

# BAR CHART

plt.bar(Top.Name,Top.Price, color="green") 
plt.xlabel('NAME')
plt.ylabel('PRICE')


#HISTOGRAM

plt.hist(Top.Price , color="pink") 
plt.xlabel('Price')

#Polar Plot 

plt.polar(Top.Price)
plt.xlabel('Price')







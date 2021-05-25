import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('data_for_dose_regression.csv')
data.head()
data2= data[data['r2'] == 3] #CHANGE HERE FOR DIFF BRAIN REGION

plt.scatter(x=data2['Dose'],
y=data2['estimate'],
s=data2['variance'] ** -1 * 10 ,
alpha=0.3,
c='black',
edgecolors='black', zorder=2)

# chart axis labels
plt.xlabel('THC dose/mg', fontsize=14)
plt.ylabel("Hedge's g effect-size estimate", fontsize=14)
plt.grid(color='grey', linestyle='-', linewidth=0.25)


#Trendline
x = data2['Dose']
y = data2['estimate']

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

plt.plot(x,p(x), color="black")


plt.tight_layout()
#plt.show()
plt.savefig ('SMA_fig.png')


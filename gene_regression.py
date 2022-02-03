import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm


#Model
data = pd.read_csv('atlas-desikankilliany_w_cnr1_7.4.21.csv')
data.head()
data = data.dropna()


x = data[['CNR1', 'CNR2']] #.values
y = data['Estimate'] #.values
x, y = np.array(x), np.array(y)


x = sm.add_constant(x)
model = sm.OLS(y, x).fit()
predictions= model.predict(x)

print_model = model.summary()
print (print_model)

#%%
#Figure
sns.set(style='whitegrid', context='talk', rc={"grid.linewidth": 0.7})
sns.set_context("paper", font_scale=2)
plt.figure(figsize=(9, 5))

ax = sns.regplot(data=data, x="CNR1", y="Estimate", ci=95, color='black', scatter_kws={'s':50})
ax.set_xlabel("CNR1 gene density",fontsize=30)
ax.set_ylabel("Hedge's g effect-size estimate",fontsize=30)

plt.tight_layout()
plt.show()







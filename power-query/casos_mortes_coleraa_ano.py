import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df_casos_globais = pd.DataFrame(dataset)

ax = sns.lineplot(data=df_casos_globais)

plt.xlabel('Anos', fontsize=12)
plt.show()
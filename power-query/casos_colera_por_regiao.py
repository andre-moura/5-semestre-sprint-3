import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df_casos_regiao = pd.DataFrame(dataset)

df_casos_regiao = df_casos_regiao.pivot(index = 'Anos', columns = 'REGIAO', values = 'CASOS').fillna(0.0)

df_casos_regiao.plot.area()

plt.show()
import matplotlib.pyplot as plt
import pandas as pd

df_populacao_ago_defecando_aberto = pd.DataFrame(dataset)
df_populacao_ago_defecando_aberto.sort_values(by=['ANOS'], inplace=True)

ax = df_populacao_ago_defecando_aberto.plot.bar(x='ANOS',figsize=(10,8))
ax.legend(["População urbana defecando em aberto %", "População rural defecando em aberto %"]);

plt.title('População angolana com acesso ao sistema de esgoto')
plt.xlabel("Anos")
plt.ylabel("População")
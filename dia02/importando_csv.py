# %%
import pandas as pd

df_customers = pd.read_csv("../data/customers.csv", sep=";")# ".." anda um diretório para trás
df_customers
# %%
df_customers.shape
# %%
df_customers.info(memory_usage='deep')
# %%
df_customers["Points"]
# %%
df_customers["Points"].astype(int)
# %%
df_customers["Points"].describe()
#%%
df_customers
# %%
# como descobrir quem tem mais pontos nesse exemplo

# %%
notas = [4.5, 6, 7, 3.5]
for i in notas:
    if i > 5:
        print(i)
# %%
# para somar 1 ponto em todas as notas
notas_novas=[]
for i in notas:
    notas_novas.append(i+1)

notas_novas
# %%
#parei em 35 minutos do video 2
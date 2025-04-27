# %%
import pandas as pd
# %%

idades = [30, 42, 90,34]
idades

# %%
media = sum(idades) / len(idades)
print(media)
total = 0
for i in idades:
    total += (media - i)**2
    
variancia= total / (len(idades) - 1)
print(variancia)
# %%
series_idades = pd.Series(idades)
series_idades
# %%
#media
series_idades.mean()
# %%
#variancia
series_idades.var()
print(series_idades.var())
#desvio padrão
series_idades.std()
print(series_idades.std())
# %%
#mediana
series_idades.median()
# %%
# 3 quartil
series_idades.quantile(0.75)
# %%
#sumarização
series_idades.describe()
# %%
#dimensão da série
#shape é auma tupla que me diz quantas linhas minha série tem
series_idades.shape

# %%
#navegando na lista
idades[0]
# %%
#navegando na série
series_idades
# %%
#modificando os indices das series
series_idades.index = ['t', 'e', 'o', 'c']
series_idades
# %%
#navegando nos índices novos
series_idades['e']
# %%
series_idades.iloc[0]
# %%

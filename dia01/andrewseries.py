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
# você está garantindo que está pegando pela posição
series_idades.iloc[0:2]
# %%
# com o .loc voce está garantindo que está pegando pelo índice
series_idades.loc['t']
print(series_idades.loc['t'])
series_idades['t']
print(series_idades['t'])
# %%
series_idades.name = 'idades'
series_idades
# %%
# é como se fosse igual nomear uma coluna no excel
series_idades = pd.Series(idades, name="idades")
series_idades
# %%

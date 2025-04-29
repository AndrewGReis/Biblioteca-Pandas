# %%
import pandas as pd

# %%

data = {
    "nome":["teo", "nah", "lara", "maria"],
    "sobrenome":["calvo", "ataíde", "calvo", "calvo"],
    "idade":[31, 32, 31, 2]
}
data
# %%
data["idade"][0]
# %%
print(data["idade"][0])
# %%

df = pd.DataFrame(data)
df
# %%
df.iloc[0]
# %%

df["idade"].iloc[0]
# %%
df["sobrenome"].iloc[0]
# %%
type(df.iloc[0])
# %%
df["idade"]
# %%
df.index=[0, 1, 2, 3]
df
# %%
df.index
# %%
df.columns
# %%
df.info(memory_usage='deep')
# %%
df.dtypes
# %%
#aplica todas essas estatísticas para as colunas numéricas
df.describe()
# %%
# mostrando na prática
df['peso'] = [80, 53, 65, 14]

df.describe()
# %%
#mostra as 5 primeiras linhas do dataframe ou você passa um número
df.head()
# %%
df.head(2)
# %%
#mostra as 5 ultimas linhas do dataframe ou voce informa um numero
df.tail()
# %%
df.tail(2)
# %%

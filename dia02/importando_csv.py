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
# como realizar operações com toda a tabela de 1x
# alguns exemplos
df_customers["Points"]
print(df_customers["Points"])
df_customers["Points"] + 1000 # soma + 1000 para cada VALOR
print(df_customers["Points"] + 1000)
df_customers["Points"] * 50 #multiplica * 50 cada valor
# %%
# verificando os números acima de 1000 e retornando uma série booleana
# pois está aplicando uma condição lógica booleana a todos os valores da série
df_customers["Points"] > 1000
# %%
# vai retornar apenas as linhas na qual a condição é verdadeira
condicao = df_customers["Points"] > 1000
df_customers[condicao]
# %%
# como descobrir quem tem mais pontos nesse exemplo
maximo = df_customers["Points"].max()
maximo
# %%
# vai mostrar de forma mais detalhada
#pois estamos pegando a linha inteira da serie
maximo = df_customers["Points"].max()
condicao = df_customers["Points"] == maximo
df_customers[condicao]
# %%
# como é comumente utilizado
df_customers[df_customers["Points"] == df_customers["Points"].max()]
# %%
#caso eu queira saber apenas o nome e travar ele
df_customers[df_customers["Points"] == df_customers["Points"].max()]["Name"].iloc[0]
# %%
# melhorando a legibilidade para facilitar o entendimento
condicao = df_customers["Points"] == df_customers["Points"].max()
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0]
# %%
#finalidade de exemplo com valores pequenos e de forma concisa
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
# entre 1000 e 2000 pontos
condicao_entre = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)
print(df_customers[condicao_entre])
# %%
# parei em 52 minutos no video 2
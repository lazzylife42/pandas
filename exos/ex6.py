# Tâches :

#     Faire une jointure interne (inner join) sur ID.
#     Faire une jointure externe (outer join) sur ID.

import pandas as pd

# Charger les deux DataFrames
df1 = pd.read_csv('dataframe1.csv')
df2 = pd.read_csv('dataframe2.csv')

# Inner Join : lignes communes aux deux DataFrames (par défaut, sur les colonnes ayant le même nom)
inner = pd.merge(df1, df2, on='ID', how='inner')
print(f"Inner Join :\n{inner}\n")

# Outer Join : toutes les lignes des deux DataFrames (avec valeurs NaN pour les colonnes non correspondantes)
outer = pd.merge(df1, df2, on='ID', how='outer')
print(f"Outer Join :\n{outer}")

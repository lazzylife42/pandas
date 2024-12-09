# Tâches :

#     Identifier les valeurs manquantes et les remplir ou les supprimer.
#     Corriger les âges négatifs en les remplaçant par une valeur acceptable (ex. moyenne).
#     Remplacer les salaires manquants par la médiane des salaires.
#     Vérifier que toutes les colonnes sont propres et prêtes à être utilisées.

import pandas as pd

# Charger les données brutes
df = pd.read_csv('dirty_data.csv')
print("Données brutes :\n")
print(df)

# Remplir les salaires manquants avec la moyenne
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Corriger les âges négatifs en les remplaçant par la moyenne des âges valides
mean_age = df[df['Age'] > 0]['Age'].mean()
df['Age'] = df['Age'].apply(lambda x: mean_age if x < 0 else x)

# Supprimer les lignes où le nom est manquant
df = df.dropna(subset=['Name'])

print("\nDonnées finales nettoyées :\n")
print(df)

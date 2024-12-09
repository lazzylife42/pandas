# Tâches :

#     Lire un fichier CSV et créer un DataFrame.
#     Filtrer les données pour obtenir uniquement les ventes de "Apple".
#     Calculer le chiffre d'affaires pour chaque produit (Price × Quantity).
#     Ajouter une nouvelle colonne "Revenue" au DataFrame avec le chiffre d'affaires.
#     Grouper les données par produit et obtenir le chiffre d'affaires total pour chaque produit.

import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("sales_data.csv")

# 1. Filtrer les lignes où le produit est "Apple"
apple_data = df[df['Product'] == 'Apple']
print("Données pour 'Apple':")
print(apple_data)

# 2. Calculer le chiffre d'affaires pour "Apple" (Price × Quantity)
apple_ca = sum(apple_data['Price'] * apple_data['Quantity'])
print("\nChiffre d'affaires pour 'Apple':")
print(apple_ca)

# 3. Ajouter une nouvelle colonne "Revenue" au DataFrame avec le chiffre d'affaires
df['Revenue'] = df['Price'] * df['Quantity']
print("\nDataFrame avec la colonne 'Revenue':")
print(df)

# 4. Grouper les données par produit et obtenir le chiffre d'affaires total pour chaque produit
revenue_by_product = df.groupby('Product')['Revenue'].sum()
print("\nChiffre d'affaires total par produit :")
print(revenue_by_product)

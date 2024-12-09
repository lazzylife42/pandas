import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv('sales_data.csv')

# Ajouter une colonne Revenue (Chiffre d'affaires)
df['Revenue'] = df['Price'] * df['Quantity']

# Regrouper les revenus par produit
revenue_by_product = df.groupby('Product')['Revenue'].sum()

# Créer un graphique à barres
plt.figure(figsize=(8, 5))
plt.bar(revenue_by_product.index, revenue_by_product.values)
plt.title("Chiffre d'affaires par produit")
plt.xlabel("Produit")
plt.ylabel("Revenu total")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Afficher le graphique
plt.show()

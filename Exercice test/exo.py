import pandas as pd
import matplotlib.pyplot as plt

# Charger les fichiers de commandes
files = [
    'orders_1_2024.csv', 'orders_2_2024.csv', 'orders_3_2024.csv',
    'orders_4_2024.csv', 'orders_5_2024.csv', 'orders_6_2024.csv',
    'orders_7_2024.csv', 'orders_8_2024.csv', 'orders_9_2024.csv',
    'orders_10_2024.csv', 'orders_11_2024.csv', 'orders_12_2024.csv'
]

dataframes = []
for i, file in enumerate(files, start=1):
    df = pd.read_csv(file)
    df['month'] = i
    dataframes.append(df)

merged_df = pd.concat(dataframes, ignore_index=True)
products_df = pd.read_csv('products.csv')

# Fusion des données et nettoyage
consolidated_df = merged_df.merge(products_df, on='product_id', how='left')
cleaned_orders = consolidated_df.dropna(subset=['quantity', 'price_per_unit']).drop_duplicates()
print("--------------------")
print(cleaned_orders)
print("--------------------")

cleaned_orders['total_price'] = cleaned_orders['quantity'] * cleaned_orders['price_per_unit']

# Nettoyage des produits
cleaned_products = products_df.drop_duplicates()

# Sauvegarde des fichiers nettoyés
cleaned_orders.to_csv('cleaned_orders.csv', index=False)
cleaned_products.to_csv('cleaned_products.csv', index=False)

# Résumé des données
category_month_summary = cleaned_orders.groupby(['category', 'month']).agg(
    total_quantity=('quantity', 'sum'),
    total_revenue=('total_price', 'sum')
).reset_index()

# Calcul des totaux annuels pour chaque catégorie
annual_summary = cleaned_orders.groupby('category').agg(
    total_quantity=('quantity', 'sum'),
    total_revenue=('total_price', 'sum'),
    total_orders=('order_id', 'count')
).reset_index()

# Création des graphiques
fig, axes = plt.subplots(3, 1, figsize=(16, 9))

# Graphique 1 : Nombre d'articles par catégorie et mois
pivot_quantity = category_month_summary.pivot(index='month', columns='category', values='total_quantity')
pivot_quantity.plot(kind='bar', stacked=True, ax=axes[0])
axes[0].set_title("Nombre d'articles par catégorie et mois")
axes[0].set_xlabel("Mois")
axes[0].set_ylabel("Quantité totale")
axes[0].legend(title="Catégorie", bbox_to_anchor=(1.05, 1), loc='upper left')
axes[0].tick_params(axis='x', rotation=45)

# Graphique 2 : Revenu total par catégorie et mois
pivot_revenue = category_month_summary.pivot(index='month', columns='category', values='total_revenue')
pivot_revenue.plot(kind='bar', stacked=True, ax=axes[1])
axes[1].set_title("Revenu total par catégorie et mois (CHF)")
axes[1].set_xlabel("Mois")
axes[1].set_ylabel("Revenu total (CHF)")
axes[1].legend(title="Catégorie", bbox_to_anchor=(1.05, 1), loc='upper left')
axes[1].tick_params(axis='x', rotation=45)

# Ajouter "CHF" aux valeurs des barres pour le graphique 2
for container in axes[1].containers:
    axes[1].bar_label(container, labels=[f"{v.get_height():.2f} CHF" if v.get_height() > 0 else '' for v in container], fontsize=8, label_type="edge")

# Graphique 3 : Résumé annuel des catégories
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
bars = annual_summary.plot(
    x='category',
    kind='bar',
    ax=axes[2],
    stacked=False,
    title="Résumé annuel des catégories"
)
axes[2].set_title("Résumé annuel des catégories (CHF)")
axes[2].set_xlabel("Catégorie")
axes[2].set_ylabel("Valeurs")
axes[2].tick_params(axis='x', rotation=45)
axes[2].legend(title="Catégorie", bbox_to_anchor=(1.05, 1), loc='upper left')

# Ajouter les valeurs au-dessus des barres pour le graphique 3
for i, bar_container in enumerate(axes[2].containers):
    for bar in bar_container:
        height = bar.get_height()
        if height > 0:
            if i == 1:  # Pour les revenus (colonne 1)
                axes[2].text(
                    bar.get_x() + bar.get_width() / 2,
                    height,
                    f"{height:.2f} CHF",
                    ha="center",
                    va="bottom",
                    fontsize=9,
                    color=colors[i]
                )
            else:  # Pour les autres colonnes
                axes[2].text(
                    bar.get_x() + bar.get_width() / 2,
                    height,
                    f"{height:.0f}",
                    ha="center",
                    va="bottom",
                    fontsize=9,
                    color=colors[i]
                )

# Ajustement et affichage
plt.tight_layout()
plt.show()

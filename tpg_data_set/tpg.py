import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Charger les données
file_path = 'montees-par-arret-par-ligne.csv'
df = pd.read_csv(file_path, delimiter=';', ) #  nrow=<int> pour aller plus vite
pd.options.display.float_format = '{:,.2f}'.format
sns.set_palette('Set2') 

# 2. Analyse exploratoire
print("Colonnes disponibles :", df.columns) #   display les columns dispos
print("\nAperçu des données :")
print(df.head())

# Statistiques descriptives pour `Nombre de Montées`
print("\nStatistiques descriptives pour 'Nombre de Montées' :")
print(df['Nombre de Montées'].describe()) #     donnes des infos sur la columns

# Arrêt avec le plus et le moins de montées
print("\nArrêt avec le maximum de montées :")
print(df.loc[df['Nombre de Montées'].idxmax()]) #   renvoie les infos sur líndex max 
print("\nArrêt avec le minimum de montées :")
print(df.loc[df['Nombre de Montées'].idxmin()])

# 3. Nettoyage des données
df_cleaned = df.dropna(subset=['Nombre de Montées', 'Ligne', 'Arrêt']).copy()
median_montees = df_cleaned['Nombre de Montées'].median()
df_cleaned['Nombre de Montées'] = df_cleaned['Nombre de Montées'].apply(
    lambda x: median_montees if x < 0 or x > 10000 else x
)

# 4. Analyse par ligne et par jour
total_by_line = df_cleaned.groupby('Ligne')['Nombre de Montées'].sum()
mean_by_day = df_cleaned.groupby('Jour Semaine')['Nombre de Montées'].mean()

# **Personnalisation globale des graphiques**
plt.rcParams.update({
    'figure.titlesize': 14,
    'axes.titlesize': 12,
    'axes.labelsize': 8,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 10,
    'figure.figsize': (16, 9)  # Ratio 16:9
})

# 5. Visualisation avec subplots
fig, axes = plt.subplots(3, 1, figsize=(16, 9), gridspec_kw={'height_ratios': [2, 2, 3]})

# Graphique 1 : Montées totales par ligne
total_by_line.sort_values().plot(kind='bar', ax=axes[0], title="Montées totales par ligne")
axes[0].set_xlabel("Ligne")
axes[0].set_ylabel("Montées totales")
axes[0].tick_params(axis='x', rotation=45)
axes[0].ticklabel_format(style='plain', axis='y')  # Désactiver l'écriture scientifique

# Graphique 2 : Moyenne des montées par jour de la semaine
mean_by_day.plot(kind='bar', color='skyblue', ax=axes[1], title="Moyenne des montées par jour de la semaine")
axes[1].set_xlabel("Jour")
axes[1].set_ylabel("Montées moyennes")
axes[1].tick_params(axis='x', rotation=45)
axes[1].ticklabel_format(style='plain', axis='y')  # Désactiver l'écriture scientifique

# Ajouter les moyennes sur les barres
for i, v in enumerate(mean_by_day):
    axes[1].text(i, v, f"{v:,.2f}", ha='center', va='bottom', fontsize=8)

# Graphique 3 : Montées par jour pour la ligne avec le plus de montées
top_line = total_by_line.idxmax()
df_top_line = df_cleaned[df_cleaned['Ligne'] == top_line]
montées_par_jour_top_ligne = df_top_line.groupby('Jour Semaine')['Nombre de Montées'].sum()
montées_par_jour_top_ligne.plot(kind='line', marker='o', ax=axes[2], title=f"Montées par jour pour la ligne {top_line}")
axes[2].set_xlabel("Jour")
axes[2].set_ylabel("Montées totales")
axes[2].tick_params(axis='x', rotation=45)
axes[2].ticklabel_format(style='plain', axis='y')  # Désactiver l'écriture scientifique

# Ajouter les valeurs sur les points
for i, v in enumerate(montées_par_jour_top_ligne):
    axes[2].text(i, v, f"{int(v):,}", ha='center', va='bottom', fontsize=8)

# Ajuster l'espacement entre les graphiques
plt.tight_layout()

# Afficher tous les graphiques
plt.show()

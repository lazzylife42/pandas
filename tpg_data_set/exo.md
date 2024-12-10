### **Exercice : Analyse des données de montée des passagers par arrêt et par ligne**

#### **Objectif**
Analyser et visualiser les données de montée des passagers fournies dans le dataset. Cet exercice dure environ **1h30** et utilise les notions vues aujourd'hui, tout en introduisant des concepts supplémentaires comme les agrégations multiples et la visualisation avancée.

---

### **Étapes de l'exercice**

#### **1. Charger et préparer les données**
- Télécharge le fichier CSV depuis [le lien du dataset](https://opendata.tpg.ch/explore/dataset/montees-par-arret-par-ligne/information/).
- Charge les données dans un DataFrame Pandas.
- Affiche les colonnes disponibles et identifie les colonnes utiles pour l'analyse (ex. `ligne`, `arret`, `jour_semaine`, `nb_de_montees`).

---

#### **2. Analyse exploratoire**
- Affiche les premières lignes du DataFrame.
- Calcule des statistiques descriptives (moyenne, médiane, minimum, maximum) pour le nombre de montées (`nb_de_montees`).
- Identifie les arrêts avec les montées maximales et minimales sur l'ensemble des données.

---

#### **3. Nettoyage des données**
- Supprime les lignes contenant des valeurs manquantes dans des colonnes critiques (`nb_de_montees`, `ligne`, etc.).
- Remplace les valeurs aberrantes dans `nb_de_montees` (par exemple, des montées très élevées ou négatives) par la médiane de la colonne.

---

#### **4. Analyse par ligne et par jour**
- Calcule le total des montées pour chaque ligne (`ligne`) sur l'ensemble des données.
- Calcule la moyenne des montées par jour de la semaine (`jour_semaine`).

---

#### **5. Visualisation**
- Crée un graphique à barres montrant les montées totales par ligne.
- Crée un graphique linéaire ou à barres pour visualiser la variation des montées moyennes par jour de la semaine.

---

#### **6. Questions avancées**
- Identifie les 5 arrêts les plus fréquentés (montées totales).
- Pour la ligne ayant le plus de montées totales, crée une visualisation des montées par jour de la semaine.

---

### **Code de démarrage**

Voici le code de base pour t'aider à démarrer l'exercice.

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. Charger les données
# Remplace 'file_path' par le chemin du fichier CSV téléchargé
file_path = 'montees-par-arret-par-ligne.csv'
df = pd.read_csv(file_path, delimiter=';')  # Vérifie le bon délimiteur (ici ; )

# 2. Analyse exploratoire
print("Colonnes disponibles :", df.columns)
print("\nAperçu des données :")
print(df.head())

# Statistiques descriptives pour `nb_de_montees`
print("\nStatistiques descriptives pour 'nb_de_montees' :")
print(df['nb_de_montees'].describe())

# Arrêt avec le plus et le moins de montées
print("\nArrêt avec le maximum de montées :")
print(df.loc[df['nb_de_montees'].idxmax()])
print("\nArrêt avec le minimum de montées :")
print(df.loc[df['nb_de_montees'].idxmin()])

# 3. Nettoyage des données
# Supprimer les lignes avec des valeurs manquantes
df_cleaned = df.dropna(subset=['nb_de_montees', 'ligne', 'arret'])

# Remplacer les valeurs aberrantes par la médiane
median_montees = df_cleaned['nb_de_montees'].median()
df_cleaned['nb_de_montees'] = df_cleaned['nb_de_montees'].apply(
    lambda x: median_montees if x < 0 or x > 10000 else x  # Exemple de borne supérieure
)

# 4. Analyse par ligne et par jour
# Total des montées par ligne
total_by_line = df_cleaned.groupby('ligne')['nb_de_montees'].sum()

# Moyenne des montées par jour de la semaine
mean_by_day = df_cleaned.groupby('jour_semaine')['nb_de_montees'].mean()

# 5. Visualisation
# Graphique à barres : Montées totales par ligne
plt.figure(figsize=(10, 6))
total_by_line.sort_values().plot(kind='bar', title="Montées totales par ligne", xlabel="Ligne", ylabel="Montées totales")
plt.show()

# Graphique à barres : Moyenne des montées par jour de la semaine
plt.figure(figsize=(10, 6))
mean_by_day.plot(kind='bar', color='skyblue', title="Moyenne des montées par jour de la semaine", xlabel="Jour", ylabel="Montées moyennes")
plt.show()

# 6. Questions avancées
# Les 5 arrêts les plus fréquentés
top_5_stops = df_cleaned.groupby('arret')['nb_de_montees'].sum().sort_values(ascending=False).head(5)
print("\nLes 5 arrêts les plus fréquentés :")
print(top_5_stops)

# Visualisation : Montées par jour pour la ligne avec le plus de montées
top_line = total_by_line.idxmax()
df_top_line = df_cleaned[df_cleaned['ligne'] == top_line]
montées_par_jour_top_ligne = df_top_line.groupby('jour_semaine')['nb_de_montees'].sum()

plt.figure(figsize=(10, 6))
montées_par_jour_top_ligne.plot(kind='line', marker='o', title=f"Montées par jour pour la ligne {top_line}", xlabel="Jour", ylabel="Montées totales")
plt.show()
```

---

### **Livrables attendus**
1. **Exploration des données :** Aperçu des données, statistiques descriptives.
2. **Nettoyage :** Les données nettoyées (avec justifications des choix).
3. **Analyse :** 
   - Totaux et moyennes calculées.
   - Classements (par ligne, arrêt, etc.).
4. **Visualisation :**
   - Graphique montrant les montées totales par ligne.
   - Graphique montrant les moyennes par jour.
   - Analyse détaillée pour une ligne spécifique.

---
## 🐍 Cheatsheet: Pandas, Matplotlib & Seaborn

### 📊 Data Analysis & Visualization Cheatsheet

| **Usage**                     | **Méthode/Commande**                                                                                                     | **Description**                                                                                  |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Charger les données**        | `pd.read_csv('file.csv', delimiter=';')`                                                                                  | Charger un fichier CSV dans un DataFrame.                                                       |
| **Aperçu des données**         | `df.head()`                                                                                                              | Affiche les premières lignes du DataFrame.                                                      |
|                                | `df.columns`                                                                                                             | Liste les colonnes du DataFrame.                                                                |
| **Statistiques descriptives**  | `df['col'].describe()`                                                                                                   | Statistiques de base (moyenne, médiane, min, max, etc.) pour une colonne.                       |
|                                | `df['col'].idxmax()` / `df['col'].idxmin()`                                                                              | Index de la ligne contenant la valeur max/min pour une colonne.                                 |
|                                | `pd.options.display.float_format = '{:,.2f}'.format`                                                                     | Affiche les nombres avec 2 décimales (sans écriture scientifique).                              |
| **Nettoyer les données**       | `df.dropna(subset=['col1', 'col2'])`                                                                                     | Supprime les lignes avec des valeurs manquantes dans des colonnes spécifiques.                  |
|                                | `df['col'] = df['col'].apply(lambda x: valeur_si_condition else x)`                                                      | Applique une transformation conditionnelle sur une colonne (ex : remplacer les valeurs aberrantes). |
|                                | `df.copy()`                                                                                                              | Crée une copie indépendante d’un DataFrame.                                                     |
| **Grouper et analyser**        | `df.groupby('col')['target_col'].sum()`                                                                                  | Regroupe par une colonne et calcule la somme pour chaque groupe.                                |
|                                | `df.groupby('col')['target_col'].mean()`                                                                                 | Moyenne pour chaque groupe basé sur une colonne.                                                |
| **Configurer les graphiques**  | `plt.rcParams.update({...})`                                                                                             | Personnalise les polices, tailles et styles des graphiques de manière globale.                  |
|                                | `sns.set_palette('palette_name')`                                                                                        | Définit une palette de couleurs globale avec Seaborn (ex. `Set2`, `pastel`, etc.).              |
| **Visualisation**              | `df.plot(kind='bar', ax=ax, title='...')`                                                                                | Crée un graphique (ex. barres, lignes) avec Matplotlib directement depuis un DataFrame Pandas.  |
|                                | `plt.subplots(nrows=3, ncols=1, figsize=(30, 24))`                                                                       | Crée une figure avec plusieurs graphiques.                                                      |
|                                | `ax.ticklabel_format(style='plain', axis='y')`                                                                           | Désactive l'écriture scientifique sur un axe.                                                   |
|                                | `ax.tick_params(axis='x', rotation=45)`                                                                                  | Définit la rotation des étiquettes des axes.                                                    |
| **Annoter les graphiques**     | `ax.text(x, y, 'texte', ha='center', va='bottom', fontsize=10)`                                                          | Ajoute du texte sur un graphique (ex. valeur totale au-dessus des barres).                      |
| **Afficher les graphiques**    | `plt.tight_layout()`                                                                                                     | Ajuste les marges automatiquement pour éviter le chevauchement des graphiques.                  |
|                                | `plt.show()`                                                                                                             | Affiche les graphiques créés.                                                                   |


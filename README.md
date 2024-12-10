# 🐍 **Cheatsheet : Python et Pandas** 🐼

## **Catégorie : Chargement et Aperçu des Données**

| **Action**                  | **Syntaxe**                                | **Description**                                                                 |
|-----------------------------|--------------------------------------------|---------------------------------------------------------------------------------|
| Charger un fichier CSV      | `pd.read_csv('file.csv', delimiter=';')`  | Charge un fichier CSV dans un DataFrame avec un délimiteur spécifique, facilitant la gestion de grandes quantités de données tabulaires. |
| Aperçu des premières lignes | `df.head()`                               | Affiche les premières lignes du DataFrame pour un aperçu rapide de la structure des données. |
| Colonnes disponibles        | `df.columns`                              | Liste toutes les colonnes présentes dans le DataFrame, aidant à comprendre les données disponibles. |
| Infos sur le DataFrame       | `df.info()`                               | Affiche des informations complètes, comme les types de colonnes et les valeurs manquantes, pour un diagnostic rapide. |
| Taille des données          | `df.shape`                              | Retourne le nombre de lignes et de colonnes, utile pour évaluer la volumétrie des données. |

---

## **Catégorie : Analyse Exploratoire**

| **Action**                          | **Syntaxe**                                    | **Description**                                                                    |
|-------------------------------------|-----------------------------------------------|------------------------------------------------------------------------------------|
| Statistiques descriptives           | `df['col'].describe()`                        | Calcule les stats (moyenne, médiane, min, max, etc.) pour une colonne donnée.        |
| Trouver la valeur max ou min        | `df['col'].idxmax()` / `df['col'].idxmin()`   | Trouve l’index de la ligne avec la valeur maximale ou minimale d’une colonne.         |
| Formater les nombres                | `pd.options.display.float_format = '{:,.2f}'.format` | Formate les nombres pour un affichage élégant, par exemple avec deux décimales. |
| Compter les valeurs uniques         | `df['col'].value_counts()`                    | Compte les occurrences de chaque valeur unique dans une colonne, pratique pour l’analyse. |

---

## **Catégorie : Nettoyage des Données**

| **Action**                            | **Syntaxe**                                       | **Description**                                                                      |
|---------------------------------------|--------------------------------------------------|--------------------------------------------------------------------------------------|
| Supprimer les lignes avec NaN         | `df.dropna(subset=['col1', 'col2'])`             | Supprime les lignes avec des valeurs manquantes dans des colonnes critiques.         |
| Remplacer les valeurs                 | `df['col'] = df['col'].fillna(valeur)`           | Remplace les valeurs manquantes par une valeur spécifique, stabilisant l’analyse.     |
| Condition pour remplacer les valeurs | `df['col'] = df['col'].apply(lambda x: ... )`    | Applique une logique conditionnelle pour modifier les valeurs dans une colonne.      |
| Supprimer les doublons                | `df.drop_duplicates()`                          | Élimine les lignes dupliquées pour garantir l’unicité des données.              |

---

## **Catégorie : Agrégation et Analyse**

| **Action**                          | **Syntaxe**                                      | **Description**                                                              |
|-------------------------------------|-------------------------------------------------|------------------------------------------------------------------------------|
| Groupement et somme                 | `df.groupby('col')['target_col'].sum()`         | Calcule la somme pour chaque groupe basé sur une colonne.                  |
| Groupement et moyenne               | `df.groupby('col')['target_col'].mean()`        | Calcule la moyenne pour chaque groupe.                                       |
| Compter les lignes par groupe       | `df.groupby('col').size()`                      | Retourne le nombre de lignes pour chaque groupe.                            |

---

## **Catégorie : Visualisation avec Matplotlib et Seaborn**

| **Action**                       | **Syntaxe**                                   | **Description**                                                             |
|----------------------------------|----------------------------------------------|-----------------------------------------------------------------------------|
| Importer Matplotlib              | `import matplotlib.pyplot as plt`            | Importer la bibliothèque Matplotlib pour tracer des graphiques d’analyse visuelle. |
| Configurer la taille des figures | `plt.figure(figsize=(width, height))`        | Définir la taille des graphiques pour une meilleure lisibilité.              |
| Créer un graphique à barres   | `df.plot(kind='bar', title='...', xlabel='...', ylabel='...')` | Générer un graphique à barres pour analyser des fréquences ou des comparaisons. |
| Ajouter des annotations          | `ax.text(x, y, 'texte', ha='center', va='bottom', fontsize=10)` | Annoter les graphiques avec des valeurs ou des notes explicatives.          |
| Ajuster les marges               | `plt.tight_layout()`                         | Ajuste automatiquement les marges pour éviter les chevauchements visuels. |
| Afficher les graphiques          | `plt.show()`                                 | Affiche les graphiques à l’écran ou dans un notebook interactif.            |

---

## **Catégorie : Manipulation avancée des données**

| **Action**                     | **Syntaxe**                                 | **Description**                                                                 |
|--------------------------------|---------------------------------------------|---------------------------------------------------------------------------------|
| Fusionner deux DataFrames      | `pd.merge(df1, df2, left_on='col1', right_on='col2', how='left')` | Combine les DataFrames en appliquant des jointures similaires au SQL.          |
| Filtrer les lignes             | `df[df['col'] == valeur]`                   | Filtre les lignes en appliquant des critères spécifiques.                     |
| Trier les données             | `df.sort_values(by='col', ascending=True)`  | Trie les données d’après une colonne ou plusieurs, pour une meilleure organisation. |

---

## **Catégorie : Techniques utiles pour les entretiens**

| **Action**                           | **Syntaxe**                                      | **Description**                                                                 |
|--------------------------------------|-------------------------------------------------|---------------------------------------------------------------------------------|
| Identifier les doublons              | `df[df.duplicated()]`                          | Affiche les lignes dupliquées, permettant de les corriger ou supprimer.         |
| Identifier les valeurs uniques       | `df['col'].nunique()`                           | Compte le nombre de valeurs uniques dans une colonne, une statistique utile.     |
| Comparer deux DataFrames             | `pd.concat([df1, df2]).drop_duplicates(keep=False)` | Repère les différences entre deux ensembles de données.                      |
| Pivot Table                          | `df.pivot_table(values='col', index='col1', columns='col2', aggfunc='sum')` | Résume les données dans une table pivot pour des vues croisées puissantes. |
| Appliquer des fonctions personnalisées | `df['col'].apply(ma_fonction)`                 | Exécute une fonction personnalisée sur chaque élément d’une colonne.        |

---

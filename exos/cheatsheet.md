# 🐍 Python & Pandas Cheatsheet

## **1. Manipulation de fichiers CSV**
### Lire un fichier CSV
```python
import pandas as pd

# Lire un fichier CSV et charger dans un DataFrame
df = pd.read_csv('file.csv')

# Afficher les premières lignes
print(df.head())
```

### Écrire dans un fichier CSV
```python
# Sauvegarder un DataFrame dans un fichier CSV
df.to_csv('output.csv', index=False)
```

---

## **2. Manipulations de DataFrame avec Pandas**
### Filtrer des données
```python
# Filtrer les lignes où une condition est vraie
filtered_df = df[df['ColumnName'] == 'Value']

# Filtrer avec plusieurs conditions
filtered_df = df[(df['Column1'] > 10) & (df['Column2'] == 'Something')]
```

### Ajouter une colonne
```python
# Ajouter une nouvelle colonne basée sur une opération
df['NewColumn'] = df['Column1'] * df['Column2']
```

### Grouper des données
```python
# Grouper par une colonne et appliquer une fonction
grouped = df.groupby('ColumnName')['AnotherColumn'].sum()

# Exemple : Chiffre d'affaires total par produit
revenue_by_product = df.groupby('Product')['Revenue'].sum()
```

---

## **3. Nettoyage de données**
### Identifier et gérer les valeurs manquantes
```python
# Trouver les valeurs manquantes
print(df.isna().sum())

# Remplir les valeurs manquantes
df['ColumnName'] = df['ColumnName'].fillna(value)

# Supprimer les lignes avec des valeurs manquantes
df = df.dropna()
```

### Corriger des erreurs dans les données
```python
# Remplacer les valeurs négatives par une moyenne
mean_value = df[df['ColumnName'] > 0]['ColumnName'].mean()
df['ColumnName'] = df['ColumnName'].apply(lambda x: mean_value if x < 0 else x)
```

---

## **4. Fonctions Python**
### Fonction Fibonacci
```python
# Version récursive avec mémorisation
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Version itérative
def fibonacci_iterative(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
```

### Vérifier un palindrome
```python
def is_palindrome(s):
    s = s.lower()
    s = ''.join(filter(str.isalnum, s))  # Supprimer les caractères non alphanumériques
    return s == s[::-1]
```

---

## **5. Tri et suppression des doublons**
### Trier une liste
```python
# Trier une liste de tuples par un élément spécifique
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
sorted_people = sorted(people, key=lambda x: x[1])  # Trier par âge
```

### Supprimer les doublons
```python
# Utiliser un set (ordre non garanti)
unique_numbers = list(set(numbers))

# Conserver l'ordre des éléments
unique_numbers_ordered = []
for num in numbers:
    if num not in unique_numbers_ordered:
        unique_numbers_ordered.append(num)
```

---

## **6. Jointures entre DataFrames**
### Inner Join
```python
inner_join = pd.merge(df1, df2, on='ID', how='inner')
```

### Outer Join
```python
outer_join = pd.merge(df1, df2, on='ID', how='outer')
```

---

## **7. Visualisation avec Matplotlib**
### Graphique à barres
```python
import matplotlib.pyplot as plt

# Créer un graphique à barres
plt.bar(x=revenue_by_product.index, height=revenue_by_product.values)
plt.title("Chiffre d'affaires par produit")
plt.xlabel("Produit")
plt.ylabel("Revenu total")
plt.show()
```

---

## **8. Raccourcis et fonctions utiles de Pandas**
### Fonctions utiles
- `df.head()` : Afficher les premières lignes.
- `df.describe()` : Résumé statistique.
- `df.info()` : Infos sur le DataFrame (types, valeurs manquantes).
- `df.sort_values(by='ColumnName')` : Trier par une colonne.
- `df['ColumnName'].unique()` : Obtenir les valeurs uniques d'une colonne.

---

### **1. Notions Python importantes**
#### **Compréhension des listes (List Comprehension)**
Une façon concise de créer ou de transformer des listes.
```python
# Exemple : Obtenir les carrés des nombres pairs
numbers = [1, 2, 3, 4, 5]
squared_evens = [x**2 for x in numbers if x % 2 == 0]
print(squared_evens)  # [4, 16]
```

#### **Dictionnaires**
Les dictionnaires sont omniprésents en Python. Savoir les manipuler est essentiel.
```python
# Exemple : Compter les occurrences dans une liste
words = ["apple", "banana", "apple", "orange"]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # {'apple': 2, 'banana': 1, 'orange': 1}
```

#### **Manipuler des fichiers**
Savoir lire et écrire dans des fichiers est une compétence de base.
```python
# Lire un fichier ligne par ligne
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Écrire dans un fichier
with open('output.txt', 'w') as f:
    f.write("Hello, world!")
```

#### **Gestion des erreurs**
La gestion des exceptions est souvent testée pour évaluer ta robustesse.
```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Erreur : {e}")
finally:
    print("Toujours exécuté.")
```

---

### **2. Concepts Pandas avancés**
#### **Fonctionnalités avancées de `groupby`**
Savoir utiliser des fonctions personnalisées avec `groupby`.
```python
# Appliquer des fonctions personnalisées
grouped = df.groupby('Product')['Quantity'].apply(lambda x: x.sum() * 2)
```

#### **Pivot Tables**
Créer des résumés complexes avec des tableaux croisés.
```python
# Exemple : Tableau croisé des ventes
pivot = df.pivot_table(values='Revenue', index='Product', columns='Date', aggfunc='sum')
print(pivot)
```

#### **Joindre plusieurs DataFrames**
Savoir faire des jointures plus complexes.
```python
# Exemple : Plusieurs colonnes comme clés de jointure
merged = pd.merge(df1, df2, left_on=['Product', 'Date'], right_on=['Item', 'SaleDate'], how='left')
```

---

### **3. Optimisation et performance**
#### **Comprendre la complexité temporelle**
Tu n’as pas besoin de maîtriser les algorithmes avancés, mais comprendre la complexité de tes solutions (O(n), O(n²), etc.) est un plus.

#### **Vectorisation avec NumPy**
Utiliser NumPy pour les opérations sur des tableaux, car il est beaucoup plus rapide que les boucles classiques.
```python
import numpy as np

# Exemple : Ajouter deux tableaux
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)  # [5 7 9]
```

#### **Profiling et debugging**
- Utiliser des outils comme `cProfile` ou des librairies pour mesurer les performances.
- Savoir utiliser `pdb` (debugger intégré à Python).

---

### **4. Tests et bonnes pratiques**
#### **Écrire des tests unitaires**
Tester ton code pour t'assurer qu'il fonctionne comme prévu.
```python
import unittest

class TestMyFunctions(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 3)

if __name__ == '__main__':
    unittest.main()
```

#### **Documentation**
Rendre ton code lisible et bien documenté avec des docstrings.
```python
def add(a, b):
    """
    Ajoute deux nombres.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.

    Returns:
        int: La somme de a et b.
    """
    return a + b
```

---

### **5. Visualisation avancée**
Si tu travailles sur des visualisations plus complexes :
- **Matplotlib** : Parfait pour des graphiques statiques.
- **Seaborn** : Pour des graphiques statistiques élégants.
```python
import seaborn as sns

sns.barplot(x='Product', y='Revenue', data=df)
plt.show()
```

- **Plotly** : Pour des graphiques interactifs.

---

### **6. Concepts d’algorithmes courants**
Même si ce n’est pas le focus principal, voici quelques notions courantes :
- **Tri** : Implémenter un tri simple comme Bubble Sort (ou utiliser `sorted()` en Python).
- **Recherches** : Binary Search pour chercher rapidement dans des listes triées.
- **Structures de données** : Comprendre les bases des listes, piles (`stack`), files (`queue`), et dictionnaires.

---

### **Résumé des compétences supplémentaires**
1. **Bases Python** : Listes, dictionnaires, gestion des fichiers, exceptions.
2. **Pandas avancé** : `groupby`, pivots, multi-index, jointures complexes.
3. **Performance** : Vectorisation, profiling.
4. **Tests et bonnes pratiques** : Unittest, documentation.
5. **Visualisation** : Matplotlib, Seaborn.
6. **Algorithmes courants** : Tri, recherche, structures de données.

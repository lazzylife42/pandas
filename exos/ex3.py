# Tâches :

#     Calculer la moyenne des scores pour chaque étudiant.
#     Identifier l'étudiant ayant le score moyen le plus élevé.
#     Trier les données par score de manière décroissante.

import pandas as pd

# Charger les données depuis le fichier CSV
df = pd.read_csv('students_scores.csv')
print("Données brutes :\n")
print(df)

# Calculer la moyenne des scores pour chaque étudiant
print("\nCalcul de la moyenne :\n")
moyenne = df.groupby('Student')['Score'].mean()
print(moyenne)

# Identifier l'étudiant ayant la meilleure moyenne
print("\nMeilleur étudiant :\n")
best_student = moyenne.idxmax()  # `idxmax` retourne l'index correspondant à la valeur maximale
best_score = moyenne.max()  # La valeur maximale
print(f"{best_student} avec une moyenne de {best_score}")

# Classer les étudiants par leur moyenne
print("\nClassement des étudiants :\n")
classement = moyenne.sort_values(ascending=False)  # Trier par ordre décroissant des scores
print(classement)


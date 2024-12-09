# Exercice : Tri personnalisé

# Tu as une liste de tuples contenant des noms et des âges :
	# people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]

# Tâches :

#     Trier la liste par âge de manière croissante.
#     Trier la liste par âge de manière décroissante.

# -----------------------------------------------------------

# Exercice : Trouver les doublons

# Tu as une liste de nombres :
# numbers = [1, 2, 3, 2, 4, 5, 6, 4, 7]

# Tâche : Trouve les doublons dans la liste.

# Partie 1 : Trier la liste people par âge
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
ascending_list = sorted(people, key=lambda x: x[1])
print("Liste triée par âge (ordre croissant) :")
print(ascending_list)

# Partie 2 : Supprimer les doublons de numbers
numbers = [1, 2, 3, 2, 4, 5, 6, 4, 7]

# Méthode 1 : Avec set (ordre non garanti)
unique_numbers_set = list(set(numbers))
print("\nListe sans doublons (ordre non garanti) :")
print(unique_numbers_set)

# Méthode 2 : Conserver l'ordre
unique_numbers_ordered = []
for num in numbers:
    if num not in unique_numbers_ordered:
        unique_numbers_ordered.append(num)
print("\nListe sans doublons (ordre conservé) :")
print(unique_numbers_ordered)

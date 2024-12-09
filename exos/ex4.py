def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input. n must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    

def is_palindrome(s):
    s = s.lower()  # Convertir en minuscules
    s = ''.join(filter(str.isalnum, s))  # Supprimer les caractères non alphanumériques
    return s == s[::-1]  # Comparer la chaîne avec son inverse

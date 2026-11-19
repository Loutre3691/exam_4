# Écris une fonction qui trouve l'élément maximal dans chaque fenêtre glissante de taille k dans un tableau. Renvoyez une liste des maximums pour chaque position de la fenêtre.

# La fonction doit :
# - Faire glisser une fenêtre de taille k à travers le tableau
# - Trouver l'élément maximal dans chaque position de la fenêtre
# - Renvoyer une liste des valeurs maximales
# - Gérer les cas limites (tableau vide, k <= 0, k > longueur du tableau)
# - Renvoyer une liste vide pour les entrées invalides


# EXAMPLE:

# sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
# -> [3, 3, 5, 5, 6, 7]

# sliding_window_maximum([1, 2, 3, 4, 5], 2)
# -> [2, 3, 4, 5]

# sliding_window_maximum([5, 4, 3, 2, 1], 1)
#  -> [5, 4, 3, 2, 1]

# sliding_window_maximum([1, 2, 3], 3)
# -> [3]

# sliding_window_maximum([1, 2, 3], 4) -> []

# sliding_window_maximum([], 2) -> []

# sliding_window_maximum([1, 2, 3], 0) -> []


def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    new = []
    if not nums or k == 0:
        return []

    for i in range(len(nums) - k + 1):
        new.append(max(nums[i:i+k]))
    return new


if __name__ == "__main__":
    result1 = sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
    result2 = sliding_window_maximum([1, 2, 3, 4, 5], 2)
    result3 = sliding_window_maximum([5, 4, 3, 2, 1], 1)
    result4 = sliding_window_maximum([1, 2, 3], 3)
    result5 = sliding_window_maximum([1, 2, 3], 4)
    result6 = sliding_window_maximum([], 2)
    result7 = sliding_window_maximum([1, 2, 3], 0)

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    print(result6)
    print(result7)


# Écris une fonction qui trouve l'intersection de plusieurs listes triées. Renvoyez une nouvelle liste contenant les éléments qui apparaissent dans TOUTES les listes d'entrée, dans l'ordre trié.

# La fonction doit :
# - Renvoyer les éléments qui apparaissent dans TOUTES les listes
# - Le résultat doit être trié par ordre croissant
# - Supprimer les doublons du résultat
# - Gérer proprement les entrées vides ou les listes vides
# - Si une liste est vide, l'intersection est vide

# EXAMPLES

# list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]) -> [2, 3]

# list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]) -> [4]

# list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]] -> [1, 2, 3]

# list_intersection_finder([[1, 2, 3], [4, 5, 6]]) -> []

# list_intersection_finder([]) -> []

# list_intersection_finder([[1, 2, 3], []]) -> []

# list_intersection_finder([[5]]) -> [5]


def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists:
        return ([])

    result = []
    for elem in lists[0]:
        if all(elem in lst for lst in lists[1:]):
            if not elem in result:
                result.append(elem)

    return (result)



if __name__ == "__main__":
    result1 = list_intersection_finder([[1, 1, 2, 3], [2, 3, 4], [2, 3, 5]])
    result2 = list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]])
    result3 = list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]])
    result4 = list_intersection_finder([[1, 2, 3], [4, 5, 6]])
    result5 = list_intersection_finder([])
    result6 = list_intersection_finder([[1, 2, 3], []]) 
    result7 = list_intersection_finder([[5]])

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    print(result6)
    print(result7)


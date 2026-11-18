from __future__ import annotations
# Écris une fonction qui projette une constellation d'étoiles sur une grille et renvoie 
# sa représentation visuelle sous forme de liste de chaînes.

# La fonction doit :
# - Prendre une liste de coordonnées d'étoiles sous forme de tuples (ligne, colonne) et la
#  taille de la grille sous forme d'entier
# - Renvoyer une liste de chaînes représentant la grille
# - Les étoiles sont représentées par '*' et les espaces vides par '.'
# - Les coordonnées de la grille commencent à (0, 0) en haut à gauche
# - Ignorer les coordonnées en dehors des limites de la grille
# - Gérer les doublons de coordonnées (l'étoile n'apparaît qu'une seule fois)

# EXAMPLES
# constellation_mapper([(0, 0), (1, 1), (2, 2)], 3) -> ['*..', '.*.', '..*']

# constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3) -> ['.*.', '***', '.*.']

# constellation_mapper([], 2) -> ['..', '..']

# constellation_mapper([(0, 0), (0, 0), (1, 1)], 2) -> ['*.', '.*']

# constellation_mapper([(0, 0), (5, 5)], 3) -> ['*..', '...', '...']

# constellation_mapper([(1, 0), (1, 1), (1, 2)], 3) ->  ['...', '***', '...']

def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    result = []
    for line in range(dim):
        t = ""
        for col in range(dim):
            if (line, col) in stars:
                t += "*"
            else:
                t += "."

        result.append(t)

    return (result)
    

if __name__ == "__main__":
    result1 = constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)
    result2 = constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3)
    result3 = constellation_mapper([], 2)
    result4 = constellation_mapper([(0, 0), (0, 0), (1, 1)], 2)
    result5 = constellation_mapper([(0, 0), (5, 5)], 3)
    result6 = constellation_mapper([(1, 0), (1, 1), (1, 2)], 3)

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    print(result6)

"""Advent of Code 2017, jour 22 : fourmi de Langton à deux puis quatre états.

La grille, infinie, est un defaultdict indexé par les coordonnées (y vers le
bas) ; la direction tourne dans la liste des quatre vecteurs, rangés dans le
sens horaire. Partie 1 : deux états, 10 000 pas. Partie 2 : quatre états
(propre, affaibli, infecté, marqué), 10 millions de pas. On compte les
infections.
"""
from collections import defaultdict

PROPRE, AFFAIBLI, INFECTE, MARQUE = range(4)
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # haut, droite, bas, gauche


def tourner_gauche(d):
    return DIRECTIONS[(DIRECTIONS.index(d) - 1) % 4]


def tourner_droite(d):
    return DIRECTIONS[(DIRECTIONS.index(d) + 1) % 4]


def lire_grille(donnees):
    lignes = donnees.split("\n")
    n = len(lignes)
    grille = defaultdict(int)  # PROPRE par défaut
    for x in range(n):
        for y in range(n):
            grille[x, y] = INFECTE if lignes[y][x] == "#" else PROPRE
    return grille, n // 2


def partie1(donnees):
    grille, centre = lire_grille(donnees)
    x, y = centre, centre
    d = (0, -1)
    infections = 0
    for _ in range(10000):
        if grille[x, y] == INFECTE:
            grille[x, y] = PROPRE
            d = tourner_droite(d)
        else:
            grille[x, y] = INFECTE
            infections += 1
            d = tourner_gauche(d)
        x, y = x + d[0], y + d[1]
    return infections


def partie2(donnees):
    grille, centre = lire_grille(donnees)
    x, y = centre, centre
    d = (0, -1)
    infections = 0
    for _ in range(10000000):
        etat = grille[x, y]
        if etat == PROPRE:
            grille[x, y] = AFFAIBLI
            d = tourner_gauche(d)
        elif etat == AFFAIBLI:
            grille[x, y] = INFECTE
            infections += 1
        elif etat == INFECTE:
            grille[x, y] = MARQUE
            d = tourner_droite(d)
        else:
            grille[x, y] = PROPRE
            d = (-d[0], -d[1])  # demi-tour
        x, y = x + d[0], y + d[1]
    return infections


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

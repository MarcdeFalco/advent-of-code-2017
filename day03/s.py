"""Advent of Code 2017, jour 3 : mémoire en spirale.

coord(n) donne les coordonnées de la case n de la spirale : on trouve
l'anneau k (plus petit k tel que (2k+1)^2 >= n), puis le côté et la position
sur ce côté. Partie 1 : distance de Manhattan au centre. Partie 2 : on remplit
la spirale case après case, chaque valeur étant la somme des voisins déjà
remplis, jusqu'à dépasser l'entrée.
"""
from itertools import product


def coord(n):
    k = 0
    while (2 * k + 1) ** 2 < n:
        k += 1
    # Dernière case de l'anneau précédent, puis rang d de n dans l'anneau k
    v = (2 * k - 1) ** 2
    d = n - v
    if d < 2 * k:
        x, y = k, -k + d
    elif d < 4 * k:
        x, y = k - (d - 2 * k), k
    elif d < 6 * k:
        x, y = -k, k - (d - 4 * k)
    else:
        x, y = -k + (d - 6 * k), -k
    return x, y


def somme_voisins(x, y, valeurs):
    s = 0
    for dx, dy in product(range(-1, 2), repeat=2):
        if (x + dx, y + dy) in valeurs:
            s += valeurs[x + dx, y + dy]
    return s


def partie1(donnees):
    x, y = coord(int(donnees))
    return abs(x) + abs(y)


def partie2(donnees):
    n = int(donnees)
    valeurs = {(0, 0): 1}
    k = 2
    while True:
        x, y = coord(k)
        valeurs[x, y] = somme_voisins(x, y, valeurs)
        if valeurs[x, y] > n:
            return valeurs[x, y]
        k += 1


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

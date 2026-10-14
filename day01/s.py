"""Advent of Code 2017, jour 1 : somme des chiffres égaux à leur vis-à-vis.

La suite de chiffres est vue comme circulaire : le vis-à-vis du chiffre
d'indice i est celui d'indice (i + decalage) modulo la longueur. Le décalage
vaut 1 en partie 1 (voisin immédiat) et la moitié de la longueur en partie 2.
"""


def somme_egaux(chiffres, decalage):
    n = len(chiffres)
    total = 0
    for i in range(n):
        if chiffres[i] == chiffres[(i + decalage) % n]:
            total += int(chiffres[i])
    return total


def partie1(donnees):
    return somme_egaux(donnees, 1)


def partie2(donnees):
    return somme_egaux(donnees, len(donnees) // 2)


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

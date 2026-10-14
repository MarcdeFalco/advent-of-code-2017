"""Advent of Code 2017, jour 2 : somme de contrôle d'un tableau.

Partie 1 : pour chaque ligne, écart entre le maximum et le minimum.
Partie 2 : pour chaque ligne, quotient de l'unique paire de valeurs dont
l'une divise l'autre, trouvée en testant toutes les paires.
"""


def lire_lignes(donnees):
    return [list(map(int, ligne.split())) for ligne in donnees.split("\n")]


def partie1(donnees):
    return sum(max(ligne) - min(ligne) for ligne in lire_lignes(donnees))


def partie2(donnees):
    total = 0
    for ligne in lire_lignes(donnees):
        for x in ligne:
            for y in ligne:
                # On compare des valeurs, pas des positions : deux valeurs
                # égales sur une même ligne seraient ignorées.
                if x != y and x % y == 0:
                    total += x // y
    return total


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

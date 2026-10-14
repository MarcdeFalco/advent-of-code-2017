"""Advent of Code 2017, jour 5 : sauts qui modifient leur propre décalage.

Simulation directe : on lit le décalage de la case courante, on le modifie,
puis on saute, jusqu'à sortir de la liste. Partie 1 : chaque décalage lu
augmente de 1. Partie 2 : un décalage d'au moins 3 diminue de 1.
"""


def nombre_de_pas(donnees, regle_etrange):
    decalages = list(map(int, donnees.split("\n")))
    i = 0
    pas = 1
    while True:
        o = decalages[i]
        if regle_etrange and o >= 3:
            decalages[i] -= 1
        else:
            decalages[i] += 1
        i += o
        if i < 0 or i >= len(decalages):
            return pas
        pas += 1


def partie1(donnees):
    return nombre_de_pas(donnees, False)


def partie2(donnees):
    return nombre_de_pas(donnees, True)


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

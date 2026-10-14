"""Advent of Code 2017, jour 24 : pont de pièces à deux ports.

Recherche exhaustive en largeur : un pont est la liste des ports traversés,
en partant de 0 ; on le prolonge par chaque pièce non encore utilisée dont un
port correspond au dernier. La force d'un pont est la somme des ports de ses
pièces. Partie 1 : force maximale. Partie 2 : force du pont le plus long (le
plus fort à longueur égale), en comparant les couples (longueur, force).
"""
from collections import deque


def force(pont):
    return sum(int(pont[i]) + int(pont[i + 1]) for i in range(len(pont) - 1))


def ponts(donnees):
    """Énumère tous les ponts possibles (listes de ports)."""
    pieces = [ligne.split("/") for ligne in donnees.split("\n")]
    a_traiter = deque([["0"]])
    while a_traiter:
        pont = a_traiter.popleft()
        yield pont
        for piece in pieces:
            if pont[-1] in piece:
                # Pièce déjà dans le pont (dans un sens ou l'autre) ?
                utilisee = False
                for i in range(len(pont) - 1):
                    if piece in ([pont[i], pont[i + 1]], [pont[i + 1], pont[i]]):
                        utilisee = True
                if not utilisee:
                    if pont[-1] == piece[0]:
                        a_traiter.append(pont + [piece[1]])
                    else:
                        a_traiter.append(pont + [piece[0]])


def partie1(donnees):
    return max(force(pont) for pont in ponts(donnees))


def partie2(donnees):
    return max((len(pont), force(pont)) for pont in ponts(donnees))[1]


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

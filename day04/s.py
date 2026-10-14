"""Advent of Code 2017, jour 4 : phrases de passe sans doublon.

On remplace chaque mot par une représentation, puis on cherche un doublon
dans la liste. Partie 1 : le mot lui-même. Partie 2 : ses lettres triées,
identiques pour deux anagrammes.
L'ensemble des lettres ne suffirait pas en partie 2 : il perd les
multiplicités (« aab » et « abb » seraient confondus).
"""


def nombre_valides(donnees, representation):
    nombre = 0
    for ligne in donnees.split("\n"):
        mots = [representation(mot) for mot in ligne.split()]
        valide = True
        for i, mot in enumerate(mots):
            if mot in mots[i + 1:]:
                valide = False
                break
        if valide:
            nombre += 1
    return nombre


def partie1(donnees):
    return nombre_valides(donnees, lambda mot: mot)


def partie2(donnees):
    return nombre_valides(donnees, sorted)


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

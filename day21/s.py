"""Advent of Code 2017, jour 21 : agrandir une image par règles de motifs.

Une image est une liste de chaînes. On complète les règles par les huit
transformations du carré (quatre rotations, avec ou sans retournement) des
motifs de gauche. À chaque étape, l'image est découpée en blocs 2 x 2 (taille
paire) ou 3 x 3, chaque bloc est remplacé par le membre droit de la règle
qui lui correspond, et les blocs sont recollés. Partie 1 : 5 étapes ;
partie 2 : 18 étapes. On compte les pixels allumés.
"""
DEPART = [".#.", "..#", "###"]


def retourner(p):
    return ["".join(reversed(ligne)) for ligne in p]


def tourner(p):
    n = len(p)
    q = [["."] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            q[y][x] = p[n - x - 1][y]
    return ["".join(ligne) for ligne in q]


TRANSFORMATIONS = [
    lambda p: p,
    lambda p: tourner(p),
    lambda p: tourner(tourner(p)),
    lambda p: tourner(tourner(tourner(p))),
    lambda p: retourner(p),
    lambda p: retourner(tourner(p)),
    lambda p: retourner(tourner(tourner(p))),
    lambda p: retourner(tourner(tourner(tourner(p)))),
]


def lire_regles(donnees):
    regles = []
    for ligne in donnees.split("\n"):
        gauche, droite = ligne.split(" => ")
        gauche, droite = gauche.split("/"), droite.split("/")
        regles += [(t(gauche), droite) for t in TRANSFORMATIONS]
    return regles


def decouper(image, k):
    """Matrice des blocs k x k de l'image."""
    v = len(image) // k
    blocs = []
    for j in range(v):
        ligne_de_blocs = []
        for i in range(v):
            bloc = []
            for y in range(k):
                bloc.append(image[j * k + y][i * k:(i + 1) * k])
            ligne_de_blocs.append(bloc)
        blocs.append(ligne_de_blocs)
    return blocs


def agrandir_bloc(bloc, regles):
    for gauche, droite in regles:
        if bloc == gauche:
            return droite
    raise ValueError("aucune règle pour ce bloc")


def agrandir(image, regles):
    k = 2 if len(image) % 2 == 0 else 3
    blocs = [[agrandir_bloc(b, regles) for b in ligne]
             for ligne in decouper(image, k)]
    nouvelle = []
    for ligne_de_blocs in blocs:
        for i in range(len(ligne_de_blocs[0])):
            nouvelle.append("".join(b[i] for b in ligne_de_blocs))
    return nouvelle


def pixels_apres(donnees, nb_etapes):
    regles = lire_regles(donnees)
    image = DEPART
    for _ in range(nb_etapes):
        image = agrandir(image, regles)
    return sum(ligne.count("#") for ligne in image)


def partie1(donnees):
    return pixels_apres(donnees, 5)


def partie2(donnees):
    return pixels_apres(donnees, 18)


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

"""Advent of Code 2017, jour 11 : distance sur une grille hexagonale.

Chaque pas est un vecteur dans un repère où les pas obliques valent
(±1, ±1/2). La distance est |x| (pas obliques obligatoires) plus ce qui
reste à parcourir verticalement, |y| - |x|/2, s'il en reste. Partie 1 :
distance finale ; partie 2 : distance maximale au cours du trajet.
Sans le max(0, ...), la formule sous-estimerait la distance quand
|y| < |x|/2.
"""
DEPLACEMENTS = {
    "n": (0, 1),
    "s": (0, -1),
    "nw": (-1, 0.5),
    "ne": (1, 0.5),
    "sw": (-1, -0.5),
    "se": (1, -0.5),
}


def distance(x, y):
    return abs(x) + max(0, int(abs(y) - abs(x) * 0.5))


def trajet(donnees):
    """Renvoie la liste des distances au départ après chaque pas."""
    distances = []
    x, y = 0, 0
    for pas in donnees.split(","):
        dx, dy = DEPLACEMENTS[pas]
        x += dx
        y += dy
        distances.append(distance(x, y))
    return distances


def partie1(donnees):
    return trajet(donnees)[-1]


def partie2(donnees):
    return max(trajet(donnees))


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

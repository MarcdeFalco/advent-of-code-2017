"""Advent of Code 2017, jour 20 : particules en mouvement et collisions.

Simulation pas à pas : la vitesse augmente de l'accélération, puis la
position de la vitesse. On s'arrête quand une particule dépasse une distance
seuil (critère heuristique : rien ne prouve que la situation n'évoluera plus).
Partie 1 : particule la plus proche de l'origine (distance de Manhattan) à
cet instant. Partie 2 : à chaque pas, on élimine les particules qui partagent
une position, repérées par un comptage dans un dictionnaire.
"""
import re
from collections import defaultdict

SEUIL = 10000000
MOTIF = re.compile(r"p=<(?P<p>.*)>, v=<(?P<v>.*)>, a=<(?P<a>.*)>")


def lire_particules(donnees):
    particules = []
    for ligne in donnees.split("\n"):
        groupes = MOTIF.match(ligne).groups()
        p, v, a = (list(map(int, g.split(","))) for g in groupes)
        particules.append((p, v, a))
    return particules


def distance(p):
    return sum(abs(x) for x in p)


def avancer(particules):
    """Fait un pas ; renvoie True si une particule a dépassé le seuil."""
    depasse = False
    for p, v, a in particules:
        for i in range(3):
            v[i] += a[i]
            p[i] += v[i]
        if distance(p) > SEUIL:
            depasse = True
    return depasse


def sans_collisions(particules):
    occupation = defaultdict(int)
    for p, _, _ in particules:
        occupation[tuple(p)] += 1
    return [(p, v, a) for (p, v, a) in particules if occupation[tuple(p)] == 1]


def partie1(donnees):
    particules = lire_particules(donnees)
    while not avancer(particules):
        pass
    distances = [distance(p) for p, _, _ in particules]
    return distances.index(min(distances))


def partie2(donnees):
    particules = sans_collisions(lire_particules(donnees))
    while True:
        depasse = avancer(particules)
        particules = sans_collisions(particules)
        if depasse:
            return len(particules)


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

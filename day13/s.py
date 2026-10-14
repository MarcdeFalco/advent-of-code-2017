"""Advent of Code 2017, jour 13 : traverser des scanners périodiques.

Partie 1 : simulation pas à pas des scanners (position et sens de chacun),
le paquet avançant d'une couche par instant. Partie 2 : un scanner de
profondeur p est en haut aux instants multiples de 2(p-1) ; on cherche le
plus petit délai d tel que d + t ne soit multiple de 2(p-1) pour aucune
couche t, en testant d = 0, 1, 2, ...
"""


def lire_couches(donnees):
    couches = {}
    for ligne in donnees.split("\n"):
        t, p = map(int, ligne.split(": "))
        couches[t] = p
    return couches


def partie1(donnees):
    couches = lire_couches(donnees)
    position = {t: 0 for t in couches}
    sens = {t: 1 for t in couches}
    attrape = []
    for paquet in range(max(couches) + 1):
        if paquet in position and position[paquet] == 0:
            attrape.append(paquet)
        for t in position:
            position[t] = (position[t] + sens[t]) % couches[t]
            if position[t] == couches[t] - 1:
                sens[t] = -1
            if position[t] == 0:
                sens[t] = 1
    return sum(t * couches[t] for t in attrape)


def partie2(donnees):
    couches = lire_couches(donnees)
    d = 0
    while not all((d + t) % (2 * (p - 1)) for t, p in couches.items()):
        d += 1
    return d


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

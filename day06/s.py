"""Advent of Code 2017, jour 6 : redistribution jusqu'à une répétition.

Chaque configuration (un n-uplet, donc hachable) est rangée dans un
dictionnaire avec la date de sa première apparition. À la première
répétition, la date courante donne le nombre d'étapes (partie 1) et la
différence des dates la longueur du cycle (partie 2).
"""


def detecter_cycle(donnees):
    """Renvoie (nombre d'étapes, longueur du cycle)."""
    banques = tuple(map(int, donnees.split()))
    vu_a = {}
    etape = 0
    while True:
        vu_a[banques] = etape
        etape += 1
        # Banque la plus remplie (la première en cas d'égalité)
        imax = 0
        for i in range(len(banques)):
            if banques[imax] < banques[i]:
                imax = i
        v = banques[imax]
        banques = list(banques)
        banques[imax] = 0
        for k in range(v):
            banques[(imax + k + 1) % len(banques)] += 1
        banques = tuple(banques)
        if banques in vu_a:
            return etape, etape - vu_a[banques]


def partie1(donnees):
    return detecter_cycle(donnees)[0]


def partie2(donnees):
    return detecter_cycle(donnees)[1]


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

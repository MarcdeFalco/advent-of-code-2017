"""Advent of Code 2017, jour 16 : permutations répétées d'une file de danseurs.

Une danse est une suite de rotations (s), d'échanges de positions (x) et
d'échanges de danseurs (p). Partie 1 : état après une danse. Partie 2 : une
danse est une permutation, donc les états reviennent périodiquement ; on
cherche la période en mémorisant les états successifs, puis l'état après un
milliard de danses est celui d'indice 10^9 modulo la période.
"""
NB_DANSEURS = 16


def danser(danseurs, commandes):
    for commande in commandes:
        if commande[0] == "s":
            n = int(commande[1:])
            danseurs = danseurs[-n:] + danseurs[:-n]
        elif commande[0] == "x":
            a, b = map(int, commande[1:].split("/"))
            danseurs[a], danseurs[b] = danseurs[b], danseurs[a]
        elif commande[0] == "p":
            a, b = map(lambda c: ord(c) - ord("a"), commande[1:].split("/"))
            i, j = danseurs.index(a), danseurs.index(b)
            danseurs[i], danseurs[j] = danseurs[j], danseurs[i]
    return danseurs


def trace(danseurs):
    return "".join(chr(ord("a") + n) for n in danseurs)


def etats_successifs(donnees, nb_danses):
    """Liste des états après 0, 1, ..., nb_danses danses."""
    commandes = donnees.split(",")
    danseurs = list(range(NB_DANSEURS))
    vus = [trace(danseurs)]
    for _ in range(nb_danses):
        danseurs = danser(danseurs, commandes)
        vus.append(trace(danseurs))
    return vus


def partie1(donnees):
    return etats_successifs(donnees, 1)[1]


def partie2(donnees):
    vus = etats_successifs(donnees, 200)
    # Première répétition d'un état : elle donne la période.
    periode = None
    for i in range(1, len(vus)):
        if vus[i] in vus[:i]:
            periode = i - vus.index(vus[i])
            break
    return vus[1000000000 % periode]


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

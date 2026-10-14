"""Advent of Code 2017, jour 7 : arbre déséquilibré.

L'arbre est un dictionnaire nom -> (poids, liste des fils). Partie 1 : la
racine est le seul nœud qui n'est le fils de personne. Partie 2 : parcours
postfixe ; le nœud déséquilibré le plus profond est celui dont les fils ont
deux poids totaux différents, et l'on corrige le poids propre du fils fautif
(celui dont le poids total n'apparaît qu'une fois).
"""


def lire_arbre(donnees):
    noeuds = {}
    est_fils = set()
    for ligne in donnees.split("\n"):
        mots = ligne.split()
        nom = mots[0]
        poids = int(mots[1][1:-1])  # « (66) » -> 66
        fils = []
        if len(mots) != 2:
            fils = "".join(mots[3:]).split(",")
            est_fils.update(fils)
        noeuds[nom] = (poids, fils)
    return noeuds, est_fils


def racine(noeuds, est_fils):
    for nom in noeuds:
        if nom not in est_fils:
            return nom


def partie1(donnees):
    return racine(*lire_arbre(donnees))


def partie2(donnees):
    noeuds, est_fils = lire_arbre(donnees)

    def poids_total(t):
        poids, fils = noeuds[t]
        return poids + sum(poids_total(c) for c in fils)

    def corriger(t):
        poids, fils = noeuds[t]
        # D'abord les fils : c'est le déséquilibre le plus profond qui compte.
        for c in fils:
            v = corriger(c)
            if v is not None:
                return v
        totaux = [poids_total(c) for c in fils]
        if len(set(totaux)) == 2:
            a, b = set(totaux)
            if totaux.count(a) != 1:
                a, b = b, a
            # a : poids total du fils fautif, b : celui des autres
            fautif = fils[totaux.index(a)]
            return noeuds[fautif][0] + b - a
        return None

    return corriger(racine(noeuds, est_fils))


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

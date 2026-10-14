"""Advent of Code 2017, jour 10 : hachage par retournements (knot hash).

Le cercle est une liste doublement chaînée circulaire de nœuds. Pour chaque
longueur k, on retourne les valeurs des k nœuds qui suivent la tête, puis on
avance de k + saut maillons ; rot mémorise le décalage total pour retrouver
la tête à la fin. Partie 1 : un tour, produit des deux premières valeurs.
Partie 2 : 64 tours sur les codes ASCII suivis d'un suffixe fixe, puis
compression par ou exclusif sur des blocs de 16.
"""
TAILLE = 256


class Noeud:
    def __init__(self, valeur, suivant=None, precedent=None):
        self.valeur = valeur
        self.suivant = suivant
        self.precedent = precedent


def cercle(n):
    """Liste circulaire 0, 1, ..., n-1 ; renvoie le nœud de valeur 0."""
    dernier = Noeud(n - 1)
    v = dernier
    for i in reversed(range(n - 1)):
        w = Noeud(i, suivant=v)
        v.precedent = w
        v = w
    dernier.suivant = v
    v.precedent = dernier
    return v


def retourner(tete, k):
    noeuds = []
    v = tete
    for _ in range(k):
        noeuds.append(v)
        v = v.suivant
    valeurs = [x.valeur for x in noeuds]
    valeurs.reverse()
    for i in range(k):
        noeuds[i].valeur = valeurs[i]


def melanger(longueurs, tours):
    """Renvoie le nœud de tête après les tours de retournements."""
    tete = cercle(TAILLE)
    saut = 0
    rot = 0
    for _ in range(tours):
        for k in longueurs:
            retourner(tete, k)
            for _ in range(saut + k):
                tete = tete.suivant
            rot = (rot + saut + k) % TAILLE
            saut += 1
    # Retour à la position de départ
    for _ in range(TAILLE - rot):
        tete = tete.suivant
    return tete


def partie1(donnees):
    tete = melanger(list(map(int, donnees.split(","))), 1)
    return tete.valeur * tete.suivant.valeur


def partie2(donnees):
    longueurs = list(map(ord, donnees)) + [17, 31, 73, 47, 23]
    tete = melanger(longueurs, 64)
    hache = ""
    for _ in range(16):
        v = 0
        for _ in range(16):
            v ^= tete.valeur
            tete = tete.suivant
        hache += "%02x" % v
    return hache


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

"""Advent of Code 2017, jour 14 : grille de bits issue de hachés, puis régions.

La ligne i de la grille 128 x 128 est le knot hash du jour 10 appliqué à
« entrée-i », converti en bits. Partie 1 : nombre de bits à 1. Partie 2 :
nombre de régions de 1 (voisinage à quatre), comptées par remplissage récursif.
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


def knot_hash_binaire(s):
    longueurs = list(map(ord, s)) + [17, 31, 73, 47, 23]
    tete = melanger(longueurs, 64)
    bits = ""
    for _ in range(16):
        v = 0
        for _ in range(16):
            v ^= tete.valeur
            tete = tete.suivant
        bits += format(v, "08b")  # octet -> huit bits
    return bits


def grille(donnees):
    return [knot_hash_binaire(donnees + "-%d" % i) for i in range(128)]


def partie1(donnees):
    return sum(ligne.count("1") for ligne in grille(donnees))


def partie2(donnees):
    g = grille(donnees)
    vus = set()

    def visiter(x, y):
        if (x, y) not in vus:
            vus.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < 128 and 0 <= y + dy < 128:
                    if g[y + dy][x + dx] == "1":
                        visiter(x + dx, y + dy)

    nb_regions = 0
    for x in range(128):
        for y in range(128):
            if (x, y) not in vus and g[y][x] == "1":
                nb_regions += 1
                visiter(x, y)
    return nb_regions


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

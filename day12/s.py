"""Advent of Code 2017, jour 12 : groupes de programmes reliés.

Le graphe est donné par listes d'adjacence. Un parcours en profondeur
récursif marque les sommets accessibles. Partie 1 : taille de la composante
de 0. Partie 2 : nombre de lancements depuis un sommet non marqué, c'est-à-dire
nombre de composantes connexes.
"""


def lire_graphe(donnees):
    adj = {}
    for ligne in donnees.split("\n"):
        x, voisins = ligne.split(" <-> ")
        adj[int(x)] = list(map(int, voisins.split(", ")))
    return adj


def dfs(adj, x, vus):
    if x not in vus:
        vus.add(x)
        for y in adj[x]:
            dfs(adj, y, vus)


def partie1(donnees):
    vus = set()
    dfs(lire_graphe(donnees), 0, vus)
    return len(vus)


def partie2(donnees):
    adj = lire_graphe(donnees)
    vus = set()
    nb_groupes = 0
    for x in adj:
        if x not in vus:
            dfs(adj, x, vus)
            nb_groupes += 1
    return nb_groupes


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

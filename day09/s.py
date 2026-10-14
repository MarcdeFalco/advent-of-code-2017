"""Advent of Code 2017, jour 9 : flux de groupes imbriqués.

Traitement en couches, une liste renversée servant de pile (pop lit le
caractère suivant en O(1)) : on supprime chaque « ! » et le caractère qui le
suit, puis on retire les passages ignorés <...> en comptant leurs caractères
(partie 2) et les virgules. Il ne reste que des accolades, analysées par
descente récursive en un arbre dont on calcule le score (partie 1).
"""


def nettoyer(donnees):
    """Renvoie (accolades restantes, nombre de caractères ignorés)."""
    pile = list(reversed(donnees))
    sans_echappement = []
    while pile:
        c = pile.pop()
        if c == "!":
            pile.pop()  # caractère échappé
        else:
            sans_echappement.append(c)

    pile = list(reversed(sans_echappement))
    accolades = []
    ignores = 0
    while pile:
        c = pile.pop()
        if c == "<":
            while pile.pop() != ">":
                ignores += 1
        elif c != ",":
            accolades.append(c)
    return accolades, ignores


def analyser(pile):
    """Grammaire G -> { G* } ; un groupe est la liste de ses sous-groupes."""
    assert pile.pop() == "{"
    sous_groupes = []
    while pile[-1] != "}":
        sous_groupes.append(analyser(pile))
    pile.pop()
    return sous_groupes


def score(groupe, profondeur):
    return 1 + profondeur + sum(score(g, profondeur + 1) for g in groupe)


def partie1(donnees):
    accolades, _ = nettoyer(donnees)
    accolades.reverse()  # pour lire le premier caractère par pop
    return score(analyser(accolades), 0)


def partie2(donnees):
    return nettoyer(donnees)[1]


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

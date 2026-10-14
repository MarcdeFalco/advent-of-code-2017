"""Advent of Code 2017, jour 19 : suivre un tracé dans une grille.

On part de la case « | » de la première ligne vers le bas et l'on avance tout
droit ; sur un « + », on prend la seule direction libre autre que le retour.
Le parcours s'arrête sur une case vide. Partie 1 : lettres rencontrées.
Partie 2 : nombre de pas.
"""


def parcourir(brut):
    """Renvoie (lettres rencontrées, nombre de pas)."""
    # Les espaces comptent : on ne supprime pas les blancs. On retire la
    # dernière ligne (blanche) et la chaîne vide finale, puis on ajoute une
    # ligne de blancs en bas pour pouvoir regarder sous la dernière ligne.
    grille = brut.split("\n")[:-2]
    grille.append(" " * len(grille[0]))
    y = 0
    x = grille[0].index("|")
    dx, dy = 0, 1
    lettres = []
    pas = 0
    while True:
        c = grille[y][x]
        if c == " ":
            break
        if c == "+":
            trouve = False
            for dx2, dy2 in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                libre = grille[y + dy2][x + dx2] != " "
                if libre and (dx2, dy2) != (-dx, -dy):
                    dx, dy = dx2, dy2
                    x, y = x + dx2, y + dy2
                    trouve = True
                    break
            assert trouve
            pas += 1
            continue
        if c.isalpha():
            lettres.append(c)
        x += dx
        y += dy
        pas += 1
    return "".join(lettres), pas


def partie1(brut):
    return parcourir(brut)[0]


def partie2(brut):
    return parcourir(brut)[1]


if __name__ == "__main__":
    brut = open("input.txt").read()
    print(partie1(brut))
    print(partie2(brut))

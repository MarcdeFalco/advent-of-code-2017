"""Advent of Code 2017, jour 23 : comprendre un programme assembleur trop lent.

Partie 1 : interprète du jeu d'instructions (set, sub, mul, jnz), registres
à 0 ; on compte les mul exécutés.
Partie 2 : avec a = 1, l'interprète est bien trop lent. La traduction à la
main du programme en Python montre une double boucle qui teste si d * e = b :
le programme compte les nombres composés b de la progression b0, b0 + 17,
..., b0 + 17000. On remplace la boucle intérieure (sur e) par un test de
divisibilité b % d == 0, ce qui passe de O(b^2) à O(b) par nombre.
"""


def partie1(donnees):
    instructions = [ligne.split() for ligne in donnees.split("\n")]
    registres = {r: 0 for r in "abcdefgh"}

    def valeur(v):
        return registres[v] if v.isalpha() else int(v)

    nb_mul = 0
    i = 0
    while 0 <= i < len(instructions):
        op, x, y = instructions[i]
        saut = 1
        if op == "set":
            registres[x] = valeur(y)
        elif op == "sub":
            registres[x] -= valeur(y)
        elif op == "mul":
            registres[x] *= valeur(y)
            nb_mul += 1
        elif op == "jnz":
            if valeur(x) != 0:
                saut = valeur(y)
        i += saut
    return nb_mul


def partie2(donnees):
    # Seule la constante de la première instruction (« set b 57 ») dépend
    # de l'entrée ; le reste est la traduction du programme.
    b = int(donnees.split("\n")[0].split()[2])
    b = 100 * b + 100000
    c = b + 17000
    h = 0
    while True:
        f = 1
        d = 2
        while True:
            # Programme de l'entrée : for e in 2..b-1 : if d * e == b : f = 0
            if b > d and b % d == 0:
                f = 0
            d += 1
            if d == b:
                break
        if f == 0:
            h += 1
        if b == c:
            break
        b += 17
    return h


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

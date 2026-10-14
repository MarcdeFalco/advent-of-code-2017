"""Advent of Code 2017, jour 15 : deux générateurs pseudo-aléatoires.

Chaque générateur multiplie sa valeur par une constante modulo 2^31 - 1
(générateur de Lehmer). Partie 1 : sur 40 millions de paires, on compte
celles dont les 16 bits de poids faible coïncident.
Partie 2 : pas de solution.
"""
FACTEUR_A, FACTEUR_B = 16807, 48271
MODULE = 2147483647


def suivant(valeur, facteur):
    return (valeur * facteur) % MODULE


def suivant_filtre(valeur, facteur, multiple):
    """Prochaine valeur multiple de `multiple` (partie 2, non utilisée)."""
    valeur = suivant(valeur, facteur)
    while valeur % multiple != 0:
        valeur = suivant(valeur, facteur)
    return valeur


def lire_depart(donnees):
    a, b = (int(ligne.split()[-1]) for ligne in donnees.split("\n"))
    return a, b


def partie1(donnees):
    a, b = lire_depart(donnees)
    nombre = 0
    for _ in range(40000000):
        a, b = suivant(a, FACTEUR_A), suivant(b, FACTEUR_B)
        if a % 65536 == b % 65536:  # 16 bits de poids faible
            nombre += 1
    return nombre


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))

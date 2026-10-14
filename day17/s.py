"""Advent of Code 2017, jour 17 : insertions dans un tampon circulaire.

Partie 1 : simulation avec une deque dont la tête est la position courante ;
avancer d'un pas revient à faire passer la tête en queue, et l'on insère la
nouvelle valeur en tête. Après 2017 insertions, la valeur suivante est en
deuxième position.
Partie 2 : inutile de construire le tampon de 50 millions de valeurs. 0 reste
en tête du tampon ; il suffit de suivre la position d'insertion
a <- (a + pas + 1) mod k et de retenir la dernière valeur insérée juste
après 0 (position 0 de l'insertion). Temps O(N), mémoire O(1).
"""
from collections import deque


def partie1(donnees):
    pas = int(donnees)
    tampon = deque([0])
    for t in range(2017):
        tampon.rotate(-(pas + 1))  # la tête passe pas + 1 fois en queue
        tampon.appendleft(t + 1)
    return tampon[1]


def partie2(donnees):
    pas = int(donnees)
    a = 0
    apres_zero = 0
    for k in range(1, 50000000 + 1):
        a = (a + pas + 1) % k
        if a == 0:
            apres_zero = k
    return apres_zero


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

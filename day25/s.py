"""Advent of Code 2017, jour 25 : simuler une machine de Turing.

On lit l'état initial, le nombre de pas et, pour chaque état et chaque
valeur lue, le triplet (valeur à écrire, direction, état suivant) ; les
blocs de description font 10 lignes. Le ruban infini est un defaultdict.
La réponse est le nombre de 1 sur le ruban après la simulation.
"""
from collections import defaultdict


def dernier_mot(ligne):
    return ligne.split()[-1][:-1]  # sans le point final


def lire_machine(donnees):
    lignes = donnees.split("\n")
    initial = dernier_mot(lignes[0])
    nb_pas = int(lignes[1].split()[-2])
    machine = {}
    for k in range((len(lignes) - 2) // 10):
        bloc = lignes[2 + 10 * k:2 + 10 * (k + 1)]
        etat = dernier_mot(bloc[1])
        for lu, debut in [(0, 3), (1, 7)]:
            machine[etat, lu] = (int(dernier_mot(bloc[debut])),
                                 dernier_mot(bloc[debut + 1]),
                                 dernier_mot(bloc[debut + 2]))
    return initial, nb_pas, machine


def partie1(donnees):
    etat, nb_pas, machine = lire_machine(donnees)
    ruban = defaultdict(int)
    curseur = 0
    for _ in range(nb_pas):
        valeur, direction, etat = machine[etat, ruban[curseur]]
        ruban[curseur] = valeur
        curseur += 1 if direction == "right" else -1
    return sum(ruban.values())


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))

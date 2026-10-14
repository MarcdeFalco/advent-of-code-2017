"""Advent of Code 2017, jour 8 : registres modifiés sous condition.

Les registres sont un defaultdict(int), ce qui évite de les déclarer. La
condition est évaluée par eval sur une chaîne reconstituée (valeur,
opérateur, constante). Partie 1 : plus grande valeur à la fin. Partie 2 :
plus grande valeur atteinte au cours de l'exécution.
"""
from collections import defaultdict


def executer(donnees):
    """Renvoie (maximum final, maximum atteint)."""
    registres = defaultdict(int)
    max_atteint = 0
    for ligne in donnees.split("\n"):
        reg, cmd, arg, _, reg_cond, op, valeur_cond = ligne.split()
        arg = int(arg)
        if eval(str(registres[reg_cond]) + op + valeur_cond):
            if cmd == "dec":
                arg = -arg
            registres[reg] += arg
        max_atteint = max(max_atteint, max(registres.values()))
    return max(registres.values()), max_atteint


def partie1(donnees):
    return executer(donnees)[0]


def partie2(donnees):
    return executer(donnees)[1]


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

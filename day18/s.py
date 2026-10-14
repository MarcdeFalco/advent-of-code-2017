"""Advent of Code 2017, jour 18 : interprète, puis deux programmes en duo.

Partie 1 : interprète direct ; snd mémorise un son, et l'on renvoie le
dernier son au premier rcv d'argument non nul.
Partie 2 : snd et rcv deviennent envoi et réception de messages. Chaque
programme est un objet Program (registres, compteur ordinal, état d'attente)
et deux deque servent de files. Un ordonnanceur coopératif fait tourner
chaque programme jusqu'à ce qu'il attende un message, et s'arrête quand les
deux sont bloqués (interblocage). On compte les envois du programme 1.
jgz ne saute que si la valeur testée est strictement positive (> 0) ;
avec >= 0, le programme de la partie 1 ne termine pas.
"""
from collections import defaultdict, deque


def partie1(donnees):
    instructions = donnees.split("\n")
    registres = defaultdict(int)

    def valeur(v):
        return registres[v] if v.isalpha() else int(v)

    son = 0
    i = 0
    while i < len(instructions):
        ops = instructions[i].split()
        saut = 1
        if ops[0] == "snd":
            son = valeur(ops[1])
        elif ops[0] == "set":
            registres[ops[1]] = valeur(ops[2])
        elif ops[0] == "rcv":
            if valeur(ops[1]) != 0:
                return son
        elif ops[0] == "add":
            registres[ops[1]] += valeur(ops[2])
        elif ops[0] == "mul":
            registres[ops[1]] *= valeur(ops[2])
        elif ops[0] == "mod":
            registres[ops[1]] %= valeur(ops[2])
        elif ops[0] == "jgz":
            if valeur(ops[1]) > 0:
                saut = valeur(ops[2])
        i += saut


class Program:
    def __init__(self, p, instructions):
        self.instructions = instructions
        self.regs = defaultdict(int)
        self.regs["p"] = p
        self.pc = 0
        self.waiting = None  # registre où ranger le message attendu
        self.send_count = 0

    def evalr(self, v):
        if v.isalpha():
            return self.regs[v]
        return int(v)

    def eval(self, send, recv):
        ops = self.instructions[self.pc].split()
        dec = 1
        if ops[0] == "snd":
            send.append(self.evalr(ops[1]))
            self.send_count += 1
        elif ops[0] == "rcv":
            if len(recv) == 0:
                # Blocage : on avance déjà pc, wakeup complétera la réception.
                self.pc += dec
                self.waiting = ops[1]
                return
            self.regs[ops[1]] = recv.popleft()
        elif ops[0] == "set":
            self.regs[ops[1]] = self.evalr(ops[2])
        elif ops[0] == "add":
            self.regs[ops[1]] += self.evalr(ops[2])
        elif ops[0] == "mul":
            self.regs[ops[1]] *= self.evalr(ops[2])
        elif ops[0] == "mod":
            self.regs[ops[1]] %= self.evalr(ops[2])
        elif ops[0] == "jgz":
            if self.evalr(ops[1]) > 0:
                dec = self.evalr(ops[2])
        self.pc += dec

    def execute(self, send, recv):
        while self.waiting is None and self.pc < len(self.instructions):
            self.eval(send, recv)

    def wakeup(self, recv):
        self.regs[self.waiting] = recv.popleft()
        self.waiting = None


def partie2(donnees):
    instructions = donnees.split("\n")
    programs = [Program(0, instructions), Program(1, instructions)]
    queues = [deque(), deque()]  # le programme i écrit dans queues[i]
    while True:
        locked = [False, False]
        for i in range(2):
            recv = queues[1 - i]
            if programs[i].pc >= len(instructions):
                locked[i] = True
            elif programs[i].waiting is not None:
                if len(recv) > 0:
                    programs[i].wakeup(recv)
                else:
                    locked[i] = True
            if not locked[i]:
                programs[i].execute(queues[i], recv)
        if all(locked):
            return programs[1].send_count


if __name__ == "__main__":
    donnees = open("input.txt").read().strip()
    print(partie1(donnees))
    print(partie2(donnees))

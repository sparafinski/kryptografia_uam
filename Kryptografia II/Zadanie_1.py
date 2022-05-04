#################################################################################
# Zadanie 1
#
# Funkcja która generuje losową krzywą eliptyczną nad Fp.
#################################################################################

import worker as w
import random


def generate_random_primary_number(k):
    while True:
        p = random.getrandbits(k)
        if p % 4 == 3:
            return p


def generate_random_elliptic_curve(p):
    while True:
        A = random.randint(0, p - 1)
        B = random.randint(0, p - 1)
        delta_E = (4 * w.binary(A, 3, p) + 27 * w.binary(B, 2, p)) % p
        if delta_E != 0 % p:
            return A, B, p


p = generate_random_primary_number(1000)
res = generate_random_elliptic_curve(p)
print("=================================================================================")
print("Zadanie 1 | Generowanie losowej krzywej eliptycznej nad Fp\n")
print("Y^2 = X^3\n+ " + str(res[0]) + " * X\n+ " + str(res[1]))
print("\n=================================================================================")





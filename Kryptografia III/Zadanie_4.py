#################################################################################
#
# Funkcja która oblicza odwrotność
#
#################################################################################

import Zadanie_3 as z3


def binary_inverse(x):
    b = x
    i = 13
    const = 1
    if x == '00':
        return 'nie istnieje'
    while i > 0:
        if int(bin(i),2) & int(bin(const),2) == 1:
            tmp = b
        else:
            tmp = x
        b = z3.binary_product(b, tmp)
        i = i - 1
    return b


if __name__ == '__main__':
    inverse = binary_inverse('f1')
    print("Odwrotność: ", inverse)

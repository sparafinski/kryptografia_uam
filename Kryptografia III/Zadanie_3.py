#################################################################################
#
# Funkcja która oblicza iloczyn().
#
#################################################################################

import re
import worker as w
import Zadanie_1 as z1
import Zadanie_2 as z2


def binary_product(x, y):
    solve = '00'
    x = w.hex_to_bin(x)
    x = re.sub(r'^0b', '', x)

    length = len(x)
    length2 = len(x) - 1
    for i in range(length):
        if x[i] == '1':
            tmp = y
            counter = length2
            while counter != 0:
                tmp = z2.binary_xtime(tmp)
                counter = counter - 1
            solve = z1.binary_sum(tmp, solve)
        length2 -= 1
    return solve


if __name__ == '__main__':
    product = binary_product('23', 'f1')
    print("Iloczyn: ", product)
#################################################################################
#
# Funkcja która oblicza mnożenie przez x
#
#################################################################################

import re
import worker as w
import Zadanie_1 as z1


def binary_xtime(x):
    x = str(w.hex_to_bin(x))
    x = re.sub(r'^0b', '', x)
    B = '00011011'
    B = hex(int(B, 2))

    length = len(x)
    while length < 8:
        x = '0' + x
        length = length + 1
    if x[0] == '1':
        x = x[1:8] + '0'
        x = hex(int(x, 2))
        return z1.binary_sum(x, B)
    elif x[0] == '0':
        x = x[1:8] + '0'
        return hex(int(x, 2))


if __name__ == '__main__':
    xtime = binary_xtime('bc')
    print("Xtime: ", xtime)
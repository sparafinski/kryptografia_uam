#################################################################################
#
# Funkcja która oblicza sumę dwóch liczb hex.
#
#################################################################################

import re
import worker as w


def binary_sum(x, y):
    x = str(w.hex_to_bin(x))
    # print("x to bin: ", x)
    x = re.sub(r'^0b', '', x)

    y = str(w.hex_to_bin(y))
    # print("y to bin: ", y)
    y = re.sub(r'^0b', '', y)

    sum = bin(int(x, 2) ^ int(y, 2))
    # print("binary sum: ", sum)
    sum = re.sub(r'^0b', '', sum)
    length = len(sum)
    while length < 8:
        sum = '0' + sum
        length = length + 1
    sum = hex(int(sum, 2))
    sum = re.sub(r'^0x', '', sum)
    return sum


if __name__ == '__main__':
    sum = binary_sum('AE', '11')
    print("Suma: ", sum)
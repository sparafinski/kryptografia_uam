#################################################################################
# Zadanie 5
#
# Funkcja która oblicza n-tą wielokrotność punktu P.
#################################################################################
import Zadanie_4


def n_multiple_point(n, x1, y1, A, B, p):
    x2 = x1
    y2 = y1
    x3 = float('inf')
    y3 = float('inf')

    while n > 0:
        if n % 2 == 1:
            x3, y3 = Zadanie_4.another_points(x3, y3, x2, y2, A, B, p)
            n = n - 1
        x2, y2 = Zadanie_4.same_points(x2, y2, A, p)
        n = n//2
    return x3, y3


if __name__ == '__main__':
    p = 7
    A = 2
    B = 4

    x = 3
    y = 226448623369642016063981880559768023550784441813507797884241707518308435413329534175311217
    n = 4879347923749729479274728427486284684682648644

    print(n_multiple_point(n, x, y, A, B, p))

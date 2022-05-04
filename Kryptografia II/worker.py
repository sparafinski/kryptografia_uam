import re
import random


def euclidean(N, x):
    A = N
    B = x
    U = 0
    V = 1

    while True:
        q = A // B

        new_A = B
        new_B = A - q * B
        A = new_A
        B = new_B

        new_U = V
        new_V = U - q * V
        U = new_U
        V = new_V

        if B == 0:
            d = A
            u = U
            v = (d - x * u) // N
            return (d, u, v)


def inverse(N, x):
    """
    N is modulo \n
    x is number"""
    result = 0
    e = euclidean(N, x)
    if e[0] != 1:
        print("No inverse")
        return result
    else:
        result = (e[1] % N + N) % N
        return result


def binary(x, k, n):
    k = bin(k)
    k = re.sub(r'^0b', '', k)

    y = 1
    l = len(k)
    i = 0

    while i < l:
        y = (y * y) % n
        if k[i] == '1':
            y = (y * x) % n
        i = i + 1

    return y


def primaryTest(n, k):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        generator = random.SystemRandom()
        for _ in range(0, k):
            b = generator.randint(2, n - 1)
            if binary(b, n - 1, n) != 1:
                return False
        return True


def quadratic(a, p):
    if p > 2:
        k = (p - 1) // 2
        res = binary(a, k, p)
        if res == 1 or res == 0:
            return True
        else:
            return False
    else:
        return False


def square(b, p):
    if quadratic(b, p):
        res = binary(b, (p + 1) // 4, p)
        return res
    else:
        return False


def if_point_on_curve(x, y, A, B, p):
    fx = (binary(x, 3, p) + A * x + B) % p
    if fx == binary(y, 2, p):
        return True
    else:
        return False

import timeit


def fast_exp(b, e, m):
    r = 1
    if 1 & e:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1: r = (r * b) % m
    return r


def quadratic(b, p):
    if p <= 2:
        return False
    k = (p - 1) // 2
    res = fast_exp(b, k, p)
    if res == 1 or res == 0:
        return True
    else:
        return False

b = 4
p = 7

start = timeit.default_timer()
if quadratic(b, p):
    res = fast_exp(b, (p + 1) // 4, p)
    stop = timeit.default_timer()
    print("Pierwiastek kwadratowy wynosi: {}".format(res))
else:
    print("b nie jest resztą kwadratową w p")
print("Completed in time: {}".format(stop - start))
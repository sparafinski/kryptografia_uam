import random
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


def primaryTest(n, k):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        # #Fermat test
        generator = random.SystemRandom()
        for _ in range(0, k):
            b = generator.randint(2, n - 1)
            if fast_exp(b, n - 1, n) != 1:
                return False
        return True


def generatePrimary():
    generator = random.SystemRandom()
    while True:
        p = generator.randint(2, 1000000000000000000000000000000000000000000000000000000000000000)
        if primaryTest(p, 172):
            return p


def euclidean(N, x):
    A = N
    B = x
    U = 0
    V = 1

    while True:
        q = A // B

        tempA = B
        tempB = A - q * B
        A = tempA
        B = tempB

        new_U = V
        new_V = U - q * V
        U = new_U
        V = new_V

        if B == 0:
            d = A
            u = U
            v = (d - x * u) // N
            return (d, u, v)


def inverse(number, modulo):
    result = 0
    e = euclidean(modulo, number)
    if e[0] != 1:
        print("No inverse")
        return result
    else:
        result = (e[1] % modulo + modulo) % modulo
        return result


def kluczRSA(p, q):
    n = p * q
    fin = (p - 1) * (q - 1)
    generator = random.SystemRandom()
    while True:
        e = generator.randint(max(p, q), 1000000000000000000000000000000000000000000000000000000000000000)
        if primaryTest(e, 172):
            break
    d = inverse(e, fin)

    print("Klucz prywatny: ", str(n), " ", str(d))
    print("Klucz publiczny: ", str(n), " e: ", str(e))

    return n, e, d


p = generatePrimary()
q = generatePrimary()
s = kluczRSA(p, q)

n = 3388212455467998936395235768150968114008618657999884569816166284239305900105176095446768504448339598527161691052957223294810710831340980182033
e = 3388212455467998936395235768150968114008618657999884569816166284239305900105176095446768504448339598527161691052957223294810710831340980182033
c = fast_exp(7775, s[1], s[0])
M = fast_exp(45692606477935856765015345941317934392874294012851631018127360568521530244955728482002603661257940470574756629020484698307047,
             20883136491478684318337916539451070806080788378684570292574302184407755520494592387396406110211148525839679091955353708100185,
             71095747013327687405017805261959282930620213977729935988932412598565795194144147217135329445618002709718224550797341129113231)

print(c)
print(M)

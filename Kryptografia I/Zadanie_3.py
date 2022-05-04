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
        for _ in range(0,k):
            b = generator.randint(2, n-1)
            if fast_exp(b, n-1, n) != 1:
                return False
        return True

# primary = 491
primary = 557447646341221346636192772896901610558710893835414944403480118710131817164269282839046936145176310843035027195369552947724772574976124889744487830405662539681582010111238770266408227840530530562128937575104894419356210796751265695974980542800695284666417470596597594320307059087588663353662759832753
# primary = 531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127
#primary = 2**33 - 21

start = timeit.default_timer()
result = primaryTest(primary, 30)
stop = timeit.default_timer()
if result:
    print("Liczba {}\n jest prawdopodobnie liczbą pierwszą".format(primary))
    print("Completed in time: {}".format(stop - start))
else:
    print("Not this time")



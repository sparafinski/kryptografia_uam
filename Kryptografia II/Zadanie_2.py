#################################################################################
# Zadanie 2
#
# Funkcja która znajduje losowy punkt na krzywej E : Y^2 = X^3 + AX + B nad Fp
#################################################################################
import worker as w
import random


def find_random_point_on_elliptic_curve(A, B, p):
    while True:
        x = random.randint(0, p - 1)
        f = (w.binary(x, 3, p) + A * x + B) % p
        if w.binary(f, int((p - 1) / 2), p) != -1:
            y = w.square(f, p)
            if y != False:
                return x, y


A = 230494833619330872742071433259892253887918924949625621075110348455162899582640562756609713
B = 225785530019760328737805254637561350820485164307786402015943227616074411698429350907607751
p = 523133468360889049404922330981983268743289535618129665870465316487757998439707462631766351

x, y = find_random_point_on_elliptic_curve(A, B, p)

print("Zadanie 2 | Znajdowanie losowego punktu na krzywej eliptycznej nad Fp\n")
print("P = (" + str(x) + ", " + str(y) + ")")
print("=================================================================================")

print(w.if_point_on_curve(x, y, A, B, p))
#################################################################################
# Zadanie 4
#
# Funkcja która oblicza sumę punktów na krzywej dla podanych a,b,p,x1,y1,x2,y2
#
#################################################################################
import worker as w
import Zadanie_3


def sum_of_two_points(x1, y1, x2, y2, A, B, p):
    if x1 == x2 and (y2 == -y1 % p or y1 == -y2 % p):
        return opposite_points()
    elif x1 == x2 and y1 == y2:
        return same_points(x1, y1, A, p)
    else:
        return another_points(x1, y1, x2, y2, A, B, p)


def opposite_points():
    x3 = float('inf')
    y3 = float('inf')
    return (x3, y3)


def same_points(x1, y1, A, p):
    lbd = ((3 * w.binary(x1, 2, p) + A) * w.inaqaverse(p, (2 * y1) % p)) % p
    x3 = (w.binary(lbd, 2, p) - (2 * x1) % p) % p
    y3 = (lbd * (x1 - x3) - y1) % p
    return x3, y3


def another_points(x1, y1, x2, y2, A, B, p):
    if x1 == float('inf') and y1 == float('inf'):
        x3 = x2
        y3 = y2
    elif x2 == float('inf') and y2 == float('inf'):
        x3 = x1
        y3 = y1
    else:
        lbd = ((y2 - y1) * w.inverse(p, (x2 - x1) % p)) % p
        x3 = (w.binary(lbd, 2, p) - x1 - x2) % p
        y3 = (lbd * (x1 - x3) - y1) % p
    return x3, y3


# p = 523133468360889049404922330981983268743289535618129665870465316487757998439707462631766351
# A = 230494833619330872742071433259892253887918924949625621075110348455162899582640562756609713
# B = 225785530019760328737805254637561350820485164307786402015943227616074411698429350907607751
#
# x1 = 175757722742565321624944121270945167081993085306911405305303187535900979958321560252348498
# y1 = 226448623369642016063981880559768023550784441813507797884241707518308435413329534175311217
# x2 = 304223499801180221986968767003559465876563746859119614741554413137259445936662302970066936
# y2 = 102134142598989436206400710402192938770351951638395982416611953688718767254279072458296380

p = 7
A = 2
B = 4
x1 = 3
y1 = 4
x2 = 0
y2 = 2

if __name__ == '__main__':
    print("Zadanie 4 | Obliczanie P ⊕ Q, sumę punktów krzywej eliptycznej\n")
    print("P = (" + str(x1) + ", " + str(y1) + ")")
    print("Q = (" + str(x2) + ", " + str(y2) + ")")
    x3, y3 = sum_of_two_points(x1, y1, x2, y2, A, B, p)
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    print("R = P ⊕ Q = (" + str(x3) + ", " + str(y3) + ")")
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    x3, y3 = sum_of_two_points(x1, y1, x1, y1, A, B, p)
    print("R = P ⊕ P = (" + str(x3) + ", " + str(y3) + ")")
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    x3_inv, y3_inv = Zadanie_3.find_opposite_point(x1, y1, p)
    x3, y3 = sum_of_two_points(x1, y1, x3_inv, y3_inv, A, B, p)
    print("R = P ⊕ (-P) = (" + str(x3) + ", " + str(y3) + ")")
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")


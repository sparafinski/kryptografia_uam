#################################################################################
# Zadanie 3
#
# Funkcja która oblicza punkt przeciwny do danego punktu.
#################################################################################


def find_opposite_point(x, y, p):
    if y == float('inf'):
        return x, y
    y_inversed = -y % p
    return x, y_inversed



if __name__ == '__main__':
    x = 175757722742565321624944121270945167081993085306911405305303187535900979958321560252348498
    y = 226448623369642016063981880559768023550784441813507797884241707518308435413329534175311217
    p = 523133468360889049404922330981983268743289535618129665870465316487757998439707462631766351

    x_inv, y_inv = find_opposite_point(x, y, p)

    print("Zadanie 3 | Obliczanie punktu przeciwnego do danego punktu\n")
    print(" P = (" + str(x) + ", " + str(y) + ")")
    print("-P = (" + str(x_inv) + ", " + str(y_inv) + ")")
    print("=================================================================================")
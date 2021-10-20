def citire_lista():
    """
    Citim lista cu numerele separate prin spatiu
    :return: lista citita de utilizator
    """
    lst = []
    input_string = input("Dati lista: ")
    numbers = input_string.split(" ")
    for x in numbers:
        lst.append(int(x))
    return lst


def numere_negative(lst):
    """
    Determina numerele negative nenule din lista
    :param lst:Lista de numere
    :return:Numerele negative din lst
    """
    rezultat = []
    for x in lst:
        if x < 0:
            rezultat.append(x)
    return rezultat


def test_numere_negative():
    assert numere_negative([5, 6, 10, 0]) == []
    assert numere_negative([-5, -10, 6, 7]) == [-5, -10]


def ultima_cifra(lst, cifra):
    """
    Determina cel mai mic numar care are ultima cifra egala cu un nr. dat
    :param lst: Lista de numere
    :param cifra: Numarul dat
    :return: Cel mai mic numar care are ultima cifra egala cu un nr. dat
    """
    listacresc = lst[:]
    listacresc.sort()
    for x in listacresc:
        if x % 10 == cifra:
            return x


def test_ultima_cifra():
    assert ultima_cifra([1, 6, 34, 68, 40, 48, 20], 8) == 48
    assert ultima_cifra([4, 10, 14, 28, 29, 24], 4) == 4


def main():
    lst = []
    test_numere_negative()
    test_ultima_cifra()
    while True:
        print("1. Citire lista")
        print("2. Afisarea numerelor negative din lista")
        print("3. Afisarea celui mai mic numar care are ultima cifra egala cu un nr. dat")
        print("a. Afisare lista")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "2":
            print(numere_negative(lst))
        elif optiune == "3":
            cifra = int(input("Dati un nr.: "))
            minim = ultima_cifra(lst, cifra)
            if minim is None:
                print("Nu exista")
            else:
                print(minim)
        elif optiune == "a":
            print(lst)
        elif optiune == "x":
            break
        else:
            print("Optiunea este invalida")


main()

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


def main():
    lst = []
    test_numere_negative()
    while True:
        print("1. Citire lista")
        print("2. Afisarea numerelor negative din lista")
        print("a. Afisare lista")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "2":
            print(numere_negative(lst))
        elif optiune == "a":
            print(lst)
        elif optiune == "x":
            break
        else:
            print("Optiunea este invalida")


main()

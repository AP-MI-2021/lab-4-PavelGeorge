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


def main():
    lst = []
    while True:
        print("1. Citire lista")
        print("a. Afisare lista")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "a":
            print(lst)
        elif optiune == "x":
            break
        else:
            print("Optiunea este invalida")


main()

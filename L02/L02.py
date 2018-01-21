from arrayQFile import ArrayQ
from linkedQFile import LinkedQ


def magic_trick(q, num_list):
    switch = False
    for item in num_list:
        try:
            if switch:
                q.enqueue(int(item))
            else:
                num_list.append(int(item))
            switch = not switch
        except ValueError:
            pass

    print_string = "De kommer ut i följande ordning: "
    while True:
        try:
            print_string += str(q.dequeue()) + " "
        except IndexError:
            break
    return print_string


def amagic_trick():
    print(magic_trick(ArrayQ(), input("Skriv in heltal, separerade av mellanslag ").split(" ")))


def lmagic_trick():
    print(magic_trick(LinkedQ(), input("Skriv in heltal, separerade av mellanslag ").split(" ")))


def menu():
    print("Trollkarlsprogram 1.0")
    print("Välj spelmotor:")
    print("1. Länkad lista")
    print("2. Array")
    print("3. Avsluta")
    val = input("Ange val: ")
    while True:
        if val == "1":
            lmagic_trick()
            break
        elif val == "2":
            amagic_trick()
            break
        elif val == "3":
            quit()
        else:
            val = input("Felaktig inmatning, försök igen: ")


while True:
    menu()

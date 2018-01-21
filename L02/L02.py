from arrayQFile import ArrayQ
from linkedQFile import LinkedQ


def magic_trick(q, num_list):
    ''' Uses the queue specified in q to perform a magic trick on the numbers listed in num_list'''
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
    ''' Takes input from the user for running the magick_trick function with the ArrayQ queue implementation'''
    print(magic_trick(ArrayQ(), input("Skriv in heltal, separerade av mellanslag ").split(" ")))


def lmagic_trick():
    ''' Takes input from the user for running the magick_trick function with the LinkedQ queue implementation'''
    print(magic_trick(LinkedQ(), input("Skriv in heltal, separerade av mellanslag ").split(" ")))


def menu():
    ''' A simple menu for the user to select which implementation of queue to use'''
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


menu()

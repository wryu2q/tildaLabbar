from arrayQFile import ArrayQ
from linkedQFile import LinkedQ

def magicTrick(q, numList):
    switch = True
    for item in numList:
        switch = not switch
        try:
            if switch:
                q.enqueue(int(item))
            else:
                numList.append(item)
        except ValueError:
            switch != switch
            continue
    printString = "De kommer ut i följande ordning: "
    while True:
        try:
            printString += str(q.dequeue()) + " "
        except IndexError:
            break
    print(printString)

def amagicTrick():
    magicTrick(ArrayQ(), input("Skriv in heltal, separerade av mellanslag ").split(" "))

def lmagicTrick():
    magicTrick(LinkedQ(), input("Skriv in heltal, separerade av mellanslag ").split(" "))

def menu():
    print("Trollkarlsprogram 1.0")
    print("Välj spelmotor:")
    print("1. Länkad lista")
    print("2. Array")
    print("3. Avsluta")
    val = input("Ange val: ")
    while True:
        if val == "1":
            lmagicTrick()
            break
        elif val == "2":
            amagicTrick()
            break
        elif val == "3":
            quit()
        else:
            val = input("Felaktig inmatning, försök igen: ")

while True:
    menu()
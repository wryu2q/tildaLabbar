from bfs import *

def load_svenska():
    svenska = Bintree()
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                continue 
            else:
                svenska.put(ordet)             # in i sökträdet
    return svenska
    
def makechildren(startord):
    i = 0
    for c in startord:        
        for l in "abcdefghijklmnopqrstuvwxyzåäö":
            ordet = list(startord)
            ordet[i] = l
            ordet = "".join(ordet)
            if ordet in svenska and ordet not in gamla:
                gamla.put(ordet)
        i += 1
    return

gamla = Bintree()
svenska = load_svenska()
makechildren("söt")
gamla.write()

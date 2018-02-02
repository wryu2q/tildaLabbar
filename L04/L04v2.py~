from bfs import *
from linkedQFile import *

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
    
def makechildren(startord, q):
    i = 0
    for c in startord:        
        for l in "abcdefghijklmnopqrstuvwxyzåäö":
            ordet = list(startord)
            ordet[i] = l
            ordet = "".join(ordet)
            if ordet in svenska and ordet not in gamla:
                gamla.put(ordet)
                q.enqueue(ordet)
        i += 1
    
q = LinkedQ()
gamla = Bintree()
svenska = load_svenska()
makechildren("söt", q)
slutord = "yxa"
while not q.isEmpty():
    nod = q.dequeue()
    makechildren(nod, q)
    if nod == slutord:
        print("Det finns en väg till", slutord)
        break
if nod != slutord:
    print("Det finns ingen väg till", slutord)

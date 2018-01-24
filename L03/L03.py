
from bintreeFile import *
#import bintreeFile
svenska = Bintree()

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")

engelska = Bintree()
with open("engelska.txt", "r", encoding = "utf-8") as engelskafil:
    for rad in engelskafil:
        for ordet in rad.split():
            ordet = ordet.strip("!.,\"\n")
            if ordet == "":
                continue
            if ordet in engelska :
                continue
            engelska.put(ordet)
            if ordet in svenska:
                print(ordet)
print("\n")
